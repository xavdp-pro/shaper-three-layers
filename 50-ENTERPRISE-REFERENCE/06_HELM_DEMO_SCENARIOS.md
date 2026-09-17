> Canonical integration note
>
> SHAPER Enterprise (historically "Enterprise OS", the name this reference corpus still uses) is preserved here as the business reference manifestation of Shaper. It is not a fourth technical layer: governance belongs to Shaper OS, durable truth and execution to Runtime, human interaction to Workspace, and domain specialization to Packages.

---

# Helm — Demo Scenarios
## Simple, scripted, believable, programmable

The demo should guide the visitor through a small number of high-value experiences.

The tone is not “look at everything the AI can do.”

The tone is:

> **This is a real company. Here is how it operates. Now watch how much easier it becomes to pilot.**

---

# Scenario 1 — Guided owner tour

Helm:

1. introduces the company;
2. opens the dashboard;
3. shows current revenue;
4. shows top product;
5. shows recent customers;
6. shows stock attention items;
7. explains one historical trend.

Example questions:

- “What was our best month?”
- “Which product produced the highest margin?”
- “Why was June stronger than May?”

Purpose:
- trust;
- realism;
- natural-language analytics;
- guided navigation.

---

# Scenario 2 — Supplier price update

Preloaded email:
- known supplier;
- attached price list;
- known products.

User:
> “Helm, process this supplier price update.”

Helm:

1. reads email;
2. extracts attachment;
3. matches products;
4. detects changed purchase prices;
5. creates new dated price records;
6. preserves old history;
7. shows impact on margins;
8. asks for validation if current policy requires it;
9. records decision and evidence.

Then Helm can say:

> “This process has now occurred repeatedly. Would you like me to propose a monitored automation for future supplier price updates?”

Purpose:
- manual → assisted → possible automation;
- dated history;
- decision traceability.

---

# Scenario 3 — Restaurant receipt

User uploads or opens fictional receipt.

Helm:

1. extracts vendor, date, amount, tax;
2. categorizes expense;
3. links source document;
4. indexes in GED;
5. creates accounting-ready expense data.

Then user asks:

> “How much did we spend on client meals last month?”

Helm answers and links source documents.

Purpose:
- document ingestion;
- OCR/extraction;
- GED;
- RAG;
- business data creation.

---

# Scenario 4 — Invoice by voice

Preloaded customer email asks for a known order.

User says:

> “Prepare the invoice for this customer and this order.”

Helm:

1. resolves customer;
2. resolves order;
3. loads company legal variables;
4. generates document;
5. presents preview;
6. user validates;
7. document is archived;
8. decision/action is traced.

Purpose:
- voice;
- CRM;
- documents;
- traceability;
- rapid action.

---

# Scenario 5 — Quick Search → Call

If telephony demo is enabled:

User:
> “Find Acme Design.”

Quick Search shows customer and contact.

User:
> “Call the main contact.”

Helm:
- resolves number;
- launches click-to-call;
- links call event;
- transcription/summary appear afterward.

If telephony is not enabled, Helm explains the optional module.

Purpose:
- universal search;
- context action;
- telephony upsell.

---

# Scenario 6 — Live UI shaping

Authorized shaping role asks:

> “Add a dashboard block showing products that need replenishment.”

Helm:

1. interprets request;
2. routes implementation to Maestro;
3. generates/tests bounded change;
4. UI updates live without manual page reload;
5. block appears.

Then user says:

> “Undo that.”

System rolls back the UI/config change.

Purpose:
- live shaping;
- trust;
- reversibility;
- visible wow effect.

Important:
- do not imply that database rollback is identical to UI rollback;
- persistent-data rollback requires separate handling.

---

# Scenario 7 — Decision memory

After an automation decision:

User asks:

> “Why are supplier price emails being processed automatically?”

Helm returns:

- decision date;
- who approved;
- reason;
- workflow;
- affected mailbox;
- evidence;
- review condition.

Purpose:
- governance;
- business memory;
- trust.

---

# Scenario 8 — Observability proof

Helm says:

> “All supplier price updates were processed successfully this month.”

User asks:

> “Show me.”

Helm opens filtered logs / evidence view.

Purpose:
- trust;
- evidence;
- no black box.

---

# Scenario 9 — Optimization conversation

User asks:

> “What could we improve in the company today?”

Optimization observer has already detected patterns.

Helm may say:

- repetitive supplier price processing;
- repeated manual invoice preparation;
- stock alerts checked every morning;
- recurring customer follow-up pattern.

Helm proposes options:

```text
keep manual
→ assist
→ require approval
→ automate
```

Human decides.

Purpose:
- pilotage maturity;
- human sovereignty;
- proactive but non-autonomous optimization.

---

# Scenario 10 — Light pedagogical progression

The demo may show a subtle capability map:

- Understand connected data
- Ask Helm
- Delegate a bounded action
- Review a decision
- Use an automation
- Inspect evidence
- Shape the interface

This is not gamification.

It is a map of operational understanding.


---

# Scenario 11 — Missing supplier email investigation

Context:
- supplier claims a price update was sent;
- expected automation did not process it.

User:
> “Helm, the supplier says they sent the update. What happened?”

Helm:

1. searches relevant mailboxes;
2. checks ingestion logs;
3. checks observer/workflow execution;
4. distinguishes observed evidence from hypotheses;
5. reports whether the message was received;
6. proposes the next check if evidence is incomplete.

Purpose:
- observability;
- sensor limits;
- evidence;
- no fabricated explanation.

---

# Scenario 12 — Multi-user prospect claiming

Two sales operators view a prospecting list.

Operator A claims a prospect.

Expected behavior:

- Operator A obtains edit/work ownership;
- Operator B can still inspect context but cannot create a conflicting work result;
- the claim is visible in real time;
- stale claim recovery exists;
- result and next action release/update the claim.

Purpose:
- concurrency;
- collaborative reality;
- safe multi-user work.

---

# Scenario 13 — Standing mandate

After several successful supplier-price runs, the user approves:

> “From now on, process this supplier's standard price updates automatically, but notify me if the format changes or margin drops by more than the agreed threshold.”

The system records:

- scope;
- owner;
- normal action;
- exception condition;
- notification policy;
- review rule.

Later Helm can answer:
> “Why did this run without asking me?”

Purpose:
- low-friction automation;
- human sovereignty;
- explicit reusable mandate.
