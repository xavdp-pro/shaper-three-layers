# Shaper Runtime — Master Architecture

## Purpose

Shaper Runtime is the operational truth layer between the Shaper OS governance kernel and the Shaper Workspace. It provides the durable capabilities an organization needs regardless of which host device or UI is currently used.

It must be deployable on a company server, VPS/cloud server, local workstation, LAN appliance or hybrid topology without changing the conceptual organization model.

## 1. Runtime responsibilities

The Runtime owns or coordinates:

- organization/universe identity;
- human, agent, service and device identities;
- authentication and session authority;
- RBAC/ABAC/relationship permissions/capabilities/mandates;
- object graph and persistent data;
- files/object storage and versioning;
- events, causality, audit and observers;
- RAG/search/indexing;
- agent orchestration and execution contracts;
- policies and workflows;
- app schemas/packages;
- synchronization and offline reconciliation;
- vault/key brokerage;
- import/export gateways;
- observability, health and trust;
- backup, restore and disaster recovery.

## 2. Runtime is not the UI

The Workspace can disappear and be reinstalled without losing organizational truth.

The Runtime exposes stable contracts to multiple clients:

```text
Desktop Workspace ─┐
Mobile Workspace ──┤
Web Workspace ─────┼── Shaper Protocol / API contracts ── Runtime
CLI / Steward ─────┤
Agents ────────────┘
```

## 3. Universal actor model

An **actor** can be:

- human;
- agent;
- service;
- device;
- automation identity.

Every significant action should be attributable to an actor and, where relevant, a human intention or standing mandate.

## 4. Authority model

Apply the [OS firmness/permeability distinction](../10-SHAPER-OS/00_MASTER.md#11-counter-view-and-diversity):
new evidence can change an assessment, not a permission by itself. Counter-view
content is input, never an implicit grant. Recheck effective authority at execution,
including after a review or deferred approval; retain the decision's provenance.
A proposed policy change follows its authorized change process before use.


Do not collapse:

```text
TECHNICAL CAPABILITY
≠ ROLE PERMISSION
≠ OBJECT/RELATION PERMISSION
≠ CURRENT MANDATE
≠ STANDING MANDATE
≠ ROOT AUTHORITY
```

A model may technically know how to delete a database and still have no capability to do so.

The core authorization question is conceptually:

```text
can(actor, action, resource, context, mandate) ?
```

The decision should be explainable enough to answer “why was this allowed/denied?”

## 5. Root and privileged capabilities

The Root Authority can authorize systemic actions, but privileged capabilities should be:

- explicit;
- least-power;
- scoped;
- preferably short-lived;
- auditable;
- revocable;
- step-up authenticated where appropriate.

Avoid one permanently omnipotent agent process containing every key.

## 6. Device identity

A device enrollment should normally create or bind a device keypair. The private key should use platform secure storage/hardware where available (TPM, Secure Enclave, OS keystore). The server stores identity/public material and verifies challenges.

A per-user compiled binary fingerprint can be an enrollment hint or distribution identifier, not a secret root of trust because executable contents can be inspected.

Device state may include:

```yaml
device_id:
organization_id:
public_key:
platform:
client_version:
trust_state:
capabilities:
last_seen:
revoked_at:
```

## 7. Session model

Before sensitive local data becomes usable:

```text
client start
→ device proof
→ human/service authentication
→ policy evaluation
→ scoped session authority
→ vault/cache unlock as needed
```

On close/expiry/revocation, destroy or invalidate session material and relock local encrypted state.

## 8. Object Space

The primary abstraction is an **object space**, not only a filesystem.

A document object can contain:

```yaml
id:
type:
owner:
permissions:
versions:
binary_representation:
text_representation:
metadata:
relations:
embeddings:
provenance:
audit:
retention:
agent_context:
```

Folders remain a familiar projection, not necessarily the canonical truth.

## 9. Business graph

Reusable primitives should represent people, organizations, customers, contacts, tasks, decisions, documents, messages, products, orders, workflows, etc. Cross-object relations should be generic enough to avoid hard-coding every pair.

The graph is conceptual and must not be dictated by the choice of PostgreSQL, graph database, search engine or vector store.

## 10. Source of truth

Every important data class should know its system of record.

Examples:

- Shaper may own customer operational context;
- an external accounting provider may own legally authoritative fiscal status;
- a calendar connector may be bidirectional or external-source-of-truth;
- files may be Shaper-managed or external references/imports.

Never silently overwrite historical truth because a newer external message contains a different value.

## 11. Event model

Important changes emit durable, attributable events where appropriate.

Suggested envelope:

```yaml
event_id:
event_type:
occurred_at:
actor:
origin:
correlation_id:
causation_id:
object_refs:
intention_ref:
decision_ref:
operation_id:
payload_summary:
```

Events support:

- live Workspace updates;
- audit;
- observers;
- agent context;
- diagnosis;
- replay/reconciliation where defined.

## 12. Communication states

For important inter-agent/service requests, distinguish:

```text
REQUESTED
RECEIVED
UNDERSTOOD
ACCEPTED | REJECTED | CLARIFICATION_NEEDED
EXECUTING
EXECUTED
VERIFIED | FAILED
ESCALATED
```

“Sent” is not “succeeded.”

## 13. Observer layer

Observers turn event/object state into derived attention, notifications, risk sensing and automation opportunities.

Observers are themselves observable components. Track:

- last successful execution;
- lag;
- error rate;
- missed event detection;
- queue depth;
- duplicate processing;
- sensor noise.

## 14. RAG and search

Search should combine as appropriate:

- exact filename/title/text search;
- structured metadata;
- object relations;
- full-text index;
- semantic retrieval;
- permissions filtering;
- provenance and citations back to the source object.

Authorization must be enforced before/while retrieving, not merely hidden in UI after retrieval.

## 15. File ingestion pipeline

External files enter through a gateway, not unrestricted host attachment.

```text
SELECT / RECEIVE
→ validate type/size
→ malware/content policy checks as configured
→ hash
→ identify provenance
→ encrypt/store
→ extract representations
→ classify
→ link to context
→ index/RAG
→ emit events
→ audit
```

Original host files need not remain part of the working model after import.

## 16. File export pipeline

```text
object requested for export
→ permission check
→ classification/DLP/retention rule
→ optional approval
→ temporary decrypted representation
→ write/share/upload destination
→ record external side effect
→ expire temporary material
```

Some confidential objects may simply lack export capability.

## 17. Encrypted local cache

The default client should not require a huge pre-sized virtual disk.

Use bounded encrypted cache with policy:

- maximum size;
- LRU/working-set eviction;
- per-object encryption where practical;
- offline pinning;
- key-governed access;
- cleanup on logout/revocation;
- no assumption that all server files exist locally.

Deployment modes:

- **online terminal** — minimal local data;
- **hybrid** — bounded offline working set;
- **sovereign laptop** — full local Runtime/data as explicit topology.

## 18. Sync and conflict

Offline modification requires explicit object-version semantics.

Do not default every object to last-writer-wins.

Possible strategies by object class:

- append-only event merge;
- optimistic version check;
- claim/lease;
- field/operation merge;
- conflict object for human/agent arbitration.

Every resolution should preserve provenance.

## 19. Idempotency and concurrency

Assume retries.

Important side-effecting operations need stable operation IDs and deduplication/idempotency where feasible.

For shared mutable state define:

- version checks;
- lease/claim semantics;
- stale-lock recovery;
- conflict behavior.

## 20. External side effects

Database rollback cannot unsend an email, undo a phone call, reverse every payment or retract a legally submitted document.

Model external side effects explicitly with patterns such as:

- preview;
- outbox;
- staged commit;
- compensation;
- reconciliation with external state.

## 21. Workflow state machines

Important workflows define allowed states/transitions. Agents do not invent impossible transitions merely because a UI endpoint exists.

Example:

```text
automation:
draft → test → monitored → active → paused | retired
```

## 22. Declarative application model

Apps should normally be schemas composed from trusted primitives:

- object/query;
- table/form/document;
- relation;
- view/dashboard/chart;
- action;
- workflow;
- permission;
- notification;
- agent operation.

Schemas are versioned and migrated. Runtime validates them before Workspace renders them.

Arbitrary plugins are separately sandboxed and capability-bound.

## 23. Packages

A package is an initial organizational form, not an immutable SaaS product.

Examples:

- accounting operations pack;
- legal practice pack;
- restaurant pack;
- property management pack.

Installation should declare object/schema/policy/workflow dependencies and then allow controlled shaping for the customer.

## 24. Change pipeline for agent shaping

Any meaningful generated change follows:

```text
REQUEST
→ PLAN
→ DIFF
→ POLICY / AUTHORITY CHECK
→ TEST
→ APPLY / ROLLOUT
→ OBSERVE
→ ACCEPT or ROLLBACK
→ RECORD WHY IT EXISTS
```

Every field, rule or workflow should be explainable later through change provenance.

## 25. Security compartments

Use layered boundaries:

```text
external web/host
→ gateway
→ client sandbox/cache
→ organization universe
→ object/policy scope
→ privileged service
→ infrastructure/root
```

Cross-tenant traversal is denied unless explicitly designed.

Separate where practical:

- data plane;
- runtime services;
- agent execution;
- control plane;
- key broker;
- audit/log sink.

## 26. Health and trust

Track separately:

```text
availability
health
integrity
trust
```

A service can be available but untrusted. Runtime policies may reduce capabilities when trust degrades.

## 27. Backup and disaster recovery

The restoration unit is the **Universe**, not the laptop.

A complete recovery design accounts for:

- objects and blobs;
- relational/graph state;
- policies and roles;
- app schemas/packages;
- agent definitions;
- event/audit history;
- keys/key recovery metadata;
- indexes that can be rebuilt;
- external connector reconciliation.

Test restoration, not only backup creation.

## 28. Shaper Protocol

The protocol semantics need to support:

- authenticated request/response;
- event streams;
- reconnect/resume;
- large-file transfer;
- streaming agent output;
- presence;
- version/capability negotiation;
- offline sync;
- policy/session revocation;
- correlation/causality.

Transport may evolve without redefining these semantics.

## 29. Interface to Shaper OS

Runtime must expose enough evidence for the kernel to operate:

- source and provenance;
- current state and history;
- trust;
- policy/mandate;
- consequences;
- sensor health;
- reversibility/recovery path.

## 30. Interface to Workspace

Runtime presents a stable, least-privilege contract. Workspace should not need direct database access or master keys.

The UI asks Runtime for actions and data through explicit capabilities. Denials should be explainable.

## 31. Success criterion

The Runtime succeeds when the same organization can be safely projected onto multiple clients/topologies while preserving:

- identity;
- permissions;
- context;
- durable data;
- traceability;
- agent governance;
- recovery;
- ability to change without corrupting historical meaning.

## Further reading (this layer)

| Audience | Document |
| --- | --- |
| Agent A1 | [`10_AGENT_A1.md`](10_AGENT_A1.md) |
| Agent A2 | [`11_AGENT_A2.md`](11_AGENT_A2.md) |
| Agent A3 | [`12_AGENT_A3.md`](12_AGENT_A3.md) |
| Cross-repo agent routes | [`00-META/06_AGENT_ROUTES.md`](../00-META/06_AGENT_ROUTES.md) |
