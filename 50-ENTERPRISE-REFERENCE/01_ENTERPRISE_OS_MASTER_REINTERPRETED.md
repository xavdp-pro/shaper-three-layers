> Canonical integration note
>
> SHAPER Enterprise (historically "Enterprise OS", the name this reference corpus still uses) is preserved here as the business reference manifestation of Shaper. It is not a fourth technical layer: governance belongs to Shaper OS, durable truth and execution to Runtime, human interaction to Workspace, and domain specialization to Packages.

---

# Enterprise OS — Master Architecture v0.2
## Business manifestation of Shaper OS

## 0. Definition

Enterprise OS is a reusable business operating structure built on Shaper OS principles.

It models an enterprise not as a collection of disconnected applications, but as a **multidimensional operational graph**.

Typical dimensions include:

- people;
- roles;
- customers;
- contacts;
- suppliers;
- products;
- stock;
- prices;
- purchases;
- sales;
- quotes;
- orders;
- emails;
- calls;
- documents;
- contracts;
- tasks;
- conversations;
- decisions;
- notifications;
- locations;
- events;
- metrics;
- automations;
- agents.

Each object can be connected to several others.

---

# 1. Enterprise OS is not a fixed ERP

Enterprise OS is not intended to reproduce a monolithic ERP, CRM, call center, or ticketing suite.

The approach is:

1. define stable primitives;
2. compose them according to the real enterprise;
3. specialize only where necessary;
4. keep the structure revisable.

The organization chart matters.

A one-person company should not be forced into the same operating complexity as a 200-person organization.

> **The organization graph determines the operational flow.**

---

# 2. Enterprise fractality

The enterprise can be:

- one person;
- a small team;
- several departments;
- several sites;
- several companies;
- nested business units.

The same operating patterns should scale:

```text
object
→ owner / participants
→ events
→ tasks
→ decisions
→ notifications
→ documents
→ communications
→ sensors
→ history
```

---

# 3. Core entity primitives

## 3.1 Person
- identity;
- contact data;
- role(s);
- permissions;
- employee lifecycle;
- notification preferences;
- communication endpoints.

## 3.2 Organization
- legal identity;
- trading identity;
- addresses;
- sites;
- legal data;
- communication identities;
- internal roles.

## 3.3 Customer
Can be:
- person;
- company.

May have:
- one or more addresses;
- one principal contact;
- secondary contacts;
- history;
- tasks;
- conversations;
- documents;
- quotes;
- orders;
- invoices;
- contracts;
- appointments;
- calls;
- decisions.

## 3.4 Contact
A contact belongs to a customer or organization.

Store:
- name;
- role;
- phone;
- email;
- relationship;
- primary/secondary status.

## 3.5 Site / Address
Never assume only one address.

The same model supports:
- home;
- billing;
- shipping;
- branch;
- office;
- warehouse;
- clinic;
- legal address.

---

# 4. Employee lifecycle

## Onboarding
When an employee is created:

- create identity;
- assign role(s);
- assign permissions;
- assign shared mailboxes;
- assign task access;
- assign communication resources;
- provision vault access where needed;
- register responsibility scope;
- notify relevant actors.

## Offboarding
When an employee leaves:

- disable access;
- revoke sessions;
- revoke vault access;
- transfer ownership;
- reassign tasks;
- preserve audit trail;
- rotate shared secrets if necessary;
- keep business history.

Employee lifecycle belongs to the structural kernel of Enterprise OS.

---

# 5. Human Vault

Enterprise OS may include a human-oriented secrets vault.

Requirements:

- encrypted secret storage;
- access by role;
- access logging;
- scoped sharing;
- revocation;
- rotation support;
- offboarding integration.

Agents should not expose secrets into normal chat or logs.

---

# 6. CRM

The CRM is a connected context surface, not just a contact table.

A customer page may show:

- identity;
- sites;
- contacts;
- communication history;
- call summaries;
- emails;
- tasks;
- chat threads;
- quotes;
- orders;
- invoices;
- appointments;
- contracts;
- documents;
- decisions;
- notifications;
- relevant metrics.

A phone number can identify:

- customer;
- contact;
- role of the contact.

---

# 7. ERP / Products / Stock

## Product
A product stores:

- SKU;
- description;
- category;
- current commercial data;
- current availability.

Do not reduce cost or price history to one mutable value.

## Purchase lots
Each replenishment creates a lot:

- supplier;
- purchase date;
- quantity;
- unit acquisition cost;
- currency;
- associated supplier document.

Example:

- 50 chairs bought two years ago at 100;
- 20 chairs bought last week at 120.

Default stock valuation / issue rule for the demo:

> **FIFO unless a specialized business rule overrides it.**

## Selling prices
Keep dated price history.

A quote/order freezes the applied price.

Old documents must not change because today's catalog price changed.

---

# 8. Quotes and orders

Quote generation supports:

- products;
- quantities;
- per-line discounts;
- whole-quote discounts;
- delivery fees;
- installation fees;
- taxes where relevant;
- validity period;
- frozen applied prices;
- notes;
- document version.

When accepted:

```text
QUOTE
→ ORDER
→ STOCK RESERVATION
→ FULFILLMENT
→ DELIVERY
→ FINANCIAL / EXTERNAL ACCOUNTING FLOW
```

---

# 9. Email

Each employee may have a personal mailbox.

Role/shared mailboxes may include:

- contact@;
- sales@;
- support@;
- billing@;
- purchasing@.

Access is role-based.

Email is connected to business objects:

- customer;
- contact;
- quote;
- order;
- document;
- contract;
- support issue;
- task;
- decision.

The custom webmail is the primary interface.

For demo environments, mailboxes may be locally simulated and restricted from external sending.

---

# 10. Telephony

Telephony is optional because real telephony requires external resources such as phone numbers, SIP providers, and concurrent-call capacity.

Capabilities may include:

- Asterisk/IPBX;
- SIP lines and trunks;
- WebRTC softphone;
- Flutter mobile softphone;
- extensions;
- direct lines;
- secretary/reception routing;
- ring-all;
- round-robin;
- queues;
- human-only mode;
- AI-only mode;
- schedule-based routing;
- voicemail / AI message-taking;
- call recording where lawful;
- transcription;
- summaries;
- CRM screen-pop;
- click-to-call;
- voice-command call launch.

Telephony is offered as a project-specific module, not automatically provisioned in every demo.

---

# 11. Calls as CRM events

Incoming call:

```text
CALL
→ IDENTIFY PHONE
→ LOAD CUSTOMER / CONTACT
→ OR CREATE MINIMUM RECORD
→ HANDLE
→ TRANSCRIBE
→ SUMMARIZE
→ LINK TO CRM
→ CREATE TASK / APPOINTMENT / FOLLOW-UP IF NEEDED
```

Human and AI calls follow the same traceability model.

---

# 12. Tasks

Tasks are transversal objects.

A task may be attached to:

- customer;
- contact;
- quote;
- order;
- invoice;
- email;
- document;
- contract;
- call;
- incident;
- project;
- another task.

Tasks support:

- tree / subtasks;
- status;
- priority;
- urgency;
- due date;
- several assigned participants;
- one designated lead/driver;
- notifications;
- Kanban;
- real-time updates;
- collaborative Markdown.

A client page can display all related tasks across levels.

A global attention page can aggregate all urgent / upcoming tasks across the entire organization.

---

# 13. Contextual Chat

Chat is also transversal.

A conversation may belong to:

- customer;
- task;
- document;
- email;
- order;
- incident;
- project;
- any supported business object.

Capabilities:

- real-time WebSocket delivery;
- images;
- file attachments;
- contextual history;
- agent participation;
- decisions and actions derived from conversation.

Chat is not separate from work.

It is conversation **inside the business graph**.

---

# 14. Real-time collaboration

Tasks, chat, and collaborative Markdown use real-time synchronization.

Goals:

- instant state visibility;
- concurrent work;
- agent/human co-editing;
- no manual refresh dependency;
- transparent shared context.

---

# 15. GED + RAG

The document system includes:

- upload;
- ingestion;
- extraction;
- classification;
- metadata;
- customer linking;
- foldering;
- indexing;
- retrieval;
- RAG access.

Qdrant may provide vector retrieval.

Examples:

- retrieve a contract clause;
- find restaurant receipts;
- answer questions over supplier documents;
- retrieve customer-specific documents.

---

# 16. Document generation engine

Templates use variables, e.g. Handlebars-style placeholders.

Example:

```text
{{company.legal_name}}
{{company.address}}
{{customer.name}}
{{customer.billing_address}}
{{quote.total}}
{{order.reference}}
```

Generated documents may include:

- quote;
- order form;
- contract;
- letter;
- invoice-like document where local law allows;
- service report;
- internal memo.

Generated documents are archived into the relevant customer/business context and indexed in the GED/RAG when appropriate.

---

# 17. Legal layer

Legal requirements vary by country and business.

Therefore:

- contract templates;
- legal notices;
- regulated invoice flows;
- taxation;
- government reporting;
- country-specific rules

must be isolated in specialized modules/connectors.

The universal kernel should not hard-code one country's legal model.

---

# 18. Decisions as business objects

Enterprise OS treats significant decisions as first-class objects.

Examples:

- automate supplier price-list processing;
- change a stock rule;
- authorize automatic sending for one customer;
- change approval workflow;
- change who is notified.

A decision stores:

- who initiated;
- who approved;
- date;
- context;
- scope;
- affected actors;
- expected behavior;
- evidence;
- review trigger.

---

# 19. Notification layer

Notification is a kernel-level business mechanism.

An event occurs.

Observers are evaluated.

Relevant observers are notified.

A useful notification must contain:

- what happened;
- why it matters;
- acknowledgment state;
- direct deep link to the exact object/action area.

Principle:

> **Do not make the user search for the context of a notification.**

Notification flow:

```text
EVENT
→ JOURNAL
→ OBSERVERS
→ NOTIFICATION
→ ACK
→ DEEP LINK
→ ACTION
→ RESULT
```

---

# 20. Quick Search

Quick Search is a universal navigation layer.

It should find:

- customer;
- contact;
- task;
- order;
- quote;
- email;
- document;
- contract;
- conversation;
- phone number;
- related objects.

Results may expose immediate actions:

- open;
- call;
- email;
- create task;
- ask Helm;
- view history.

---

# 21. Helm

Helm is the conversational operating interface.

Helm may:

- answer questions over business data;
- navigate the application when explicitly enabled;
- open contextual pages;
- find customers;
- create documents;
- prepare invoices;
- create tasks;
- change task states;
- query statistics;
- inspect emails;
- use RAG;
- trigger click-to-call when telephony exists;
- assist with decisions;
- propose automations.

Helm acts from a human intention and within the mandate of that interaction.

---

# 22. Maestro

Maestro is an orchestration/execution layer.

Typical relationship:

```text
HUMAN
→ HELM
→ INTENTION / REQUEST
→ MAESTRO
→ WORKFLOW / AGENT EXECUTION
→ TESTS / GUARDRAILS
→ RESULT
→ OBSERVATION
→ TRACE
```

Maestro can also run scheduled observation processes.

Example:

> inspect recurring operational patterns and propose possible improvements.

---

# 23. Manual → assisted → automated

Enterprise OS should support progressive delegation.

```text
MANUAL
→ HELM ASSISTED
→ HELM PROPOSES
→ HUMAN APPROVES
→ WORKFLOW EXECUTES
→ REPEATED TRUST
→ OPTIONAL AUTOMATION
→ PERIODIC REVIEW
```

The system should not force automation maturity faster than the organization can trust it.

---

# 24. Observability

Operational health must be visible.

A logs/observability page should allow filtering by:

- time;
- module;
- customer;
- workflow;
- agent;
- decision;
- result;
- status;
- error;
- notification;
- business object.

The purpose is not to force executives to read logs.

The purpose is:

> **when something is questioned, evidence exists.**

---

# 25. External accounting and country connectors

Enterprise OS can generate and track business objects without assuming it is the legal accounting system.

External providers may handle:

- official e-invoicing;
- tax declarations;
- payment status;
- statutory reporting.

Enterprise OS communicates with them through connectors.

Examples of events:

```text
invoice submitted
invoice accepted
invoice rejected
payment received
payment failed
tax status updated
```

---

# 26. Enterprise OS success criterion

The system succeeds when a company can move from:

> “Where is the information? Who did what? What should I do next?”

toward:

> **“I can see what is happening, understand why, act immediately, delegate safely, and improve the way the company works.”**


---

# 27. Organization chart drives behavior

Enterprise OS must not impose a large-company workflow on a one-person business.

The organization graph determines:

- routing;
- responsibilities;
- approval chains;
- shared mailbox access;
- telephone routing;
- task visibility;
- decision distribution;
- notification targets.

Examples:

### Very small company
One person may simultaneously own:
- sales;
- purchasing;
- support;
- management.

### Small team
A secretary/operations role may become the communication buffer.

### Larger organization
Functions split into:
- reception;
- sales;
- purchasing;
- support;
- logistics;
- management;
- specialized decision authority.

The software activates complexity only when the organization needs it.

---

# 28. Calendar and appointments

Appointments are a general enterprise primitive.

An appointment can link to:

- customer;
- contact;
- employee;
- site;
- call;
- email;
- service;
- task;
- document.

Store:

- start/end;
- status;
- location/channel;
- participants;
- purpose;
- source;
- change history;
- cancellation/reschedule history.

This is essential for AI/human telephone reception scenarios.

The AI may need access to the next relevant appointment in order to reschedule it correctly.

---

# 29. Prospecting and work claiming

Prospecting lists require safe concurrent work.

Typical flow:

```text
LEAD / PROSPECT
→ AVAILABLE
→ CLAIMED BY OPERATOR
→ READ-ONLY TO OTHERS FOR CONFLICTING EDITS
→ CALL / WORK
→ RESULT
→ RELEASE / COMPLETE / FOLLOW-UP
```

Use a claim/lease/mutex mechanism rather than assuming one operator.

The lock must not unnecessarily hide the record:
- others may still read;
- conflicting modification is restricted;
- stale locks expire or can be recovered.

Track:
- who claimed;
- when;
- action performed;
- outcome;
- next step.

---

# 30. Purchasing is distinct from selling

Sales and purchasing are different operational functions.

Purchasing may need to:

- compare suppliers;
- inspect price histories;
- detect supplier price changes;
- choose replenishment quantities;
- negotiate;
- create purchase orders;
- follow delivery;
- reconcile received goods;
- update lots.

This deserves a first-class workflow, even if one person performs both roles in a small company.

---

# 31. Telephony role boundaries

AI telephony is role-bounded.

A telephone AI can be configured for tasks such as:

- reception;
- identity collection;
- appointment creation;
- appointment modification;
- message taking;
- qualification;
- routing.

It must not infer professional authority it has not been granted.

Examples:
- medical/clinical assistant: no medical advice;
- plumbing receptionist: no technical diagnosis unless explicitly designed and authorized;
- commercial assistant: no unapproved pricing commitment.

The exact boundary is a per-enterprise rule.

---

# 32. Telephony routing detail

Telephony routing can be driven by:

- organization chart;
- work schedule;
- employee presence;
- role;
- queue;
- direct extension;
- direct number;
- AI/human mode.

Common modes:

```text
AI ONLY
SCHEDULED AI / HUMAN
HUMAN ONLY
```

Human distribution examples:

- ring all available operators;
- round-robin;
- queue;
- skill/role routing;
- secretary first, then transfer;
- direct extension.

SIP/trunk concurrency defines how many simultaneous inbound/outbound calls the installation can support.

---

# 33. Softphone endpoints

The telephony brick may provide:

- browser WebRTC softphone;
- several simultaneous browser endpoints;
- per-endpoint active/inactive switch;
- Flutter Android mobile softphone;
- extension credentials separate from Enterprise OS user credentials;
- configurable WebRTC/SIP endpoint URL.

The same employee identity may own several endpoints while retaining one business identity.

---

# 34. Human and AI call history

Incoming and outgoing calls should converge on the same CRM event model.

For each call, where configured and lawful:

- caller/callee;
- customer/contact resolution;
- employee or AI actor;
- timestamps;
- direction;
- call result;
- recording reference;
- transcript;
- short summary;
- appointments/tasks created;
- follow-up requirement.

A sales team calling back leads sees the same customer history as reception.

---

# 35. Support / case primitive

Some businesses need a formal ticket/case layer.

This can be implemented as a specialization of the transversal task/event model.

A case may link to:

- customer;
- product;
- order;
- document;
- call;
- email;
- tasks;
- chat;
- decisions.

Do not duplicate the entire task engine unless the specialized workflow genuinely requires it.

---

# 36. Event and observer layer

Enterprise OS needs a common event grammar.

Examples:

```text
email.received
price.changed
quote.accepted
order.created
stock.low
task.overdue
decision.created
notification.acked
call.completed
document.indexed
workflow.failed
```

Observers subscribe to events/conditions.

Observers may:
- record;
- calculate;
- notify;
- propose;
- trigger an already-authorized workflow.

Observation and action authority remain separate.

---

# 37. Health pulse

The enterprise should periodically take its own operational pulse.

Examples:

- expected emails ingested?
- scheduled workflows executed?
- notification delivery healthy?
- Qdrant indexing current?
- stock invariants valid?
- unresolved task backlog growing?
- external connector responding?
- telephony registration healthy?
- decision-driven automation behaving as agreed?

The executive should normally see a simple health summary.

Detailed evidence remains available on demand.

---

# 38. Data ownership and system of record

For every important domain, explicitly define the authoritative source.

Examples:

- CRM owns customer identity?
- external accounting platform owns legal invoice status?
- Enterprise OS owns operational invoice intent/document?
- SIP provider owns carrier call delivery?
- Enterprise OS owns call context and summary?
- external calendar or Enterprise OS owns appointment truth?

Never allow two systems to silently behave as independent sources of truth for the same state.

---

# 39. Privacy, retention, and jurisdiction

Enterprise OS is reusable across countries, therefore policy must be configurable for:

- personal-data retention;
- call recording;
- transcript retention;
- email retention;
- document retention;
- employee access;
- deletion/anonymization;
- data residency;
- legal hold.

The universal architecture should provide the mechanism.

The connector/policy layer supplies local rules.

---

# 40. Business graph invariant

Any major business object should be able to answer, as applicable:

- What is it?
- Who owns it?
- Who participates?
- What happened to it?
- Which communications concern it?
- Which tasks concern it?
- Which documents concern it?
- Which decisions concern it?
- Which notifications concern it?
- Which metrics/sensors describe it?
- What is the next action?
- What is its source of truth?
