# Enterprise OS — Agent Implementation Guide
## Build the graph, not a pile of screens

Agents implementing Enterprise OS must treat business entities as a connected graph.

---

# 1. Universal object contract

Every important business object should support, where relevant:

```yaml
id:
type:
status:
created_at:
updated_at:
created_by:
owner:
participants:
permissions:
customer_id:
parent_id:
links:
events:
tasks:
conversations:
documents:
decisions:
notifications:
audit:
```

Not every field is mandatory for every object, but the relational pattern should stay predictable.

---

# 2. Cross-object attachment pattern

Tasks, chats, documents, decisions, and notifications should be attachable to multiple object types.

Prefer a generic relation model over hard-coding every pair.

Example:

```yaml
relation:
  source_type: task
  source_id: ...
  target_type: customer
  target_id: ...
  relation_type: concerns
```

This enables multidimensional navigation.

---

# 3. Real-time contract

For collaborative objects:

- changes publish events;
- subscribed clients receive deltas;
- UI updates without manual refresh;
- agent changes use the same event path;
- event ordering is explicit;
- conflicts are detectable.

Typical WebSocket events:

```text
task.created
task.updated
task.status_changed
task.assignee_changed
chat.message_created
document.updated
notification.created
decision.recorded
```

---

# 4. Task model

Task requirements:

- nested tasks;
- several contributors;
- one lead;
- status;
- priority;
- urgency;
- due date;
- links to arbitrary business objects;
- notifications;
- real-time state;
- collaborative Markdown;
- Kanban view;
- global attention view.

The lead/driver is distinct from participants.

---

# 5. Notification contract

Notification must include:

```yaml
event_id:
recipient:
title:
summary:
severity:
ack_required:
ack_state:
deep_link:
related_object:
created_at:
```

Deep link is mandatory whenever a direct action context exists.

---

# 6. Decision contract

```yaml
decision_id:
intent:
initiator:
validator:
date:
scope:
reason:
affected_objects:
affected_people:
expected_behavior:
execution_mode:
evidence:
review_condition:
status:
```

---

# 7. Email ingestion contract

Email processing:

```text
RECEIVE
→ IDENTIFY MAILBOX
→ PARSE
→ IDENTIFY CUSTOMER / CONTACT
→ LINK OR CREATE CONTEXT
→ EXTRACT ATTACHMENTS
→ CLASSIFY
→ CREATE EVENTS
→ OPTIONAL TASK / DECISION
→ INDEX RELEVANT DOCS
→ TRACE
```

Never overwrite historical business values because of a new email.

---

# 8. Product price history

Store dated price ranges.

Example:

```yaml
price_record:
  product_id:
  price_type: purchase|sale
  amount:
  currency:
  valid_from:
  valid_to:
  source_document:
  source_supplier:
```

Orders/quotes preserve the price actually applied.

---

# 9. Stock lots

```yaml
stock_lot:
  product_id:
  supplier_id:
  acquired_at:
  quantity_initial:
  quantity_remaining:
  unit_cost:
  source_document_id:
```

Default demo depletion strategy: FIFO.

---

# 10. Proactive optimization observer

A scheduled observer may inspect the operating graph for opportunities.

It can consider:

- repetition;
- stability;
- low exception rate;
- repeated approvals;
- predictable routing;
- user complaints;
- excessive manual effort;
- repeated searches;
- repeated corrective tasks.

Output:

```yaml
observation:
pattern:
evidence:
possible_improvement:
risk:
suggested_mode: template|assist|approval_workflow|automation
requires_human_decision: true
```

It proposes. It does not silently create policy.

---

# 11. Helm control of UI

When UI control is enabled, Helm may:

- navigate;
- filter;
- open records;
- focus specific controls;
- present contextual explanations.

The user must be able to disable UI control.

---

# 12. Live shaping mode

A separate shaping capability may modify interface structure.

Requirements:

- only authorized shaping roles;
- changes remain traceable;
- visible live updates;
- production-safe deployment path;
- rollback;
- data-preservation strategy;
- clear distinction between UI/code rollback and persistent-data rollback.

Do not run a development server in production merely to obtain hot reload.

Use production-safe event-driven or schema-driven updates.

---

# 13. Check every flow twice

For every feature, agents should validate two views:

## Human view
- Is it understandable?
- Is the next action obvious?
- Is context one click away?
- Is responsibility visible?

## Agent/system view
- Is the data relation explicit?
- Are permissions explicit?
- Are events emitted?
- Are traces preserved?
- Are success/failure states testable?
- Is rollback defined?


---

# 14. Production invariants

## 14.1 Idempotency

Event-driven and agent-driven actions must assume retries can occur.

Important writes should have:
- stable operation/event IDs;
- deduplication strategy;
- idempotent handlers where feasible.

Examples:
- do not create two identical invoices because a job retried;
- do not import the same supplier price attachment twice;
- do not send the same notification ten times because one observer restarted.

## 14.2 Concurrency

For shared mutable objects define:
- optimistic version checks;
- claim/lease locks where appropriate;
- conflict behavior;
- stale-lock recovery.

Prospecting work is a primary example.

## 14.3 External side effects

Database rollback does not undo:
- an email already sent;
- a phone call already placed;
- an invoice already submitted externally;
- a payment already triggered.

Model side effects explicitly.

Where possible use:
- preview;
- outbox;
- staged commit;
- compensation action;
- external-state reconciliation.

## 14.4 Schema and rule versioning

Persist versions for:
- document templates;
- automations;
- decision rules;
- UI schemas;
- agent instructions;
- product price logic;
- connector mappings.

Historical operations must remain interpretable after rules change.

## 14.5 Audit immutability

Operational history should not be silently rewritten.

Corrections should normally append:
- correction event;
- superseding decision;
- new version.

Do not erase the fact that the earlier state existed unless a specific retention/privacy rule requires deletion.

## 14.6 Observer health

Observers are themselves components that can fail.

Monitor:
- last successful run;
- lag;
- error rate;
- missed-event detection;
- queue depth;
- duplicate processing;
- sensor noise.

A dead observer can create false confidence.

## 14.7 Tenant / universe isolation

If several companies share infrastructure, explicitly isolate:
- data;
- secrets;
- vector indexes;
- files;
- email;
- telephony credentials;
- logs;
- agent context;
- capabilities.

Cross-tenant graph traversal must be impossible unless explicitly designed.

---

# 15. Agent authority model

Separate:

```text
TECHNICAL CAPABILITY
≠
ROLE PERMISSION
≠
CURRENT HUMAN MANDATE
≠
STANDING MANDATE
```

Helm may technically be able to call many internal functions.

The effective authorization for an action derives from:
- current user identity;
- role;
- object permission;
- explicit current intention;
- standing decisions/mandates;
- criticality rules.

This preserves fluid interaction without turning capability into uncontrolled autonomy.

---

# 16. Shaping-mode confirmation policy

Do not require confirmation for every small UI shaping step once an authorized shaping role has explicitly entered shaping mode.

Instead:

- record the shaping mandate;
- trace changes;
- continuously test;
- show live result;
- keep rollback;
- escalate confirmation only when criticality increases.

Examples requiring stronger review may include:
- destructive persistent-data migration;
- permission changes;
- secret changes;
- irreversible external side effects;
- broad cross-tenant changes.

---

# 17. State machine discipline

Important workflows should define explicit states and valid transitions.

Examples:

```text
quote:
draft → sent → accepted | rejected | expired

task:
open → in_progress → blocked → completed | cancelled

prospect:
available → claimed → contacted → follow_up | converted | closed

decision:
proposed → approved → active → revised | revoked

automation:
draft → test → monitored → active → paused | retired
```

Agents must not invent impossible transitions.

---

# 18. Event causality

For each important event preserve:

```yaml
event_id:
event_type:
occurred_at:
actor:
origin:
correlation_id:
causation_id:
object_refs:
decision_ref:
intention_ref:
payload_summary:
```

This makes multi-step traces inspectable.

---

# 19. Acceptance rule

A feature is not complete because the screen exists.

It is complete when:

```text
OBJECT MODEL
+ PERMISSIONS
+ EVENT
+ UI
+ AGENT CAPABILITY
+ TRACE
+ OBSERVER
+ FAILURE PATH
+ TEST
+ ROLLBACK / RECOVERY
```

are coherent for the intended criticality.
