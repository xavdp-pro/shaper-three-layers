> Canonical integration note
>
> SHAPER Enterprise (historically "Enterprise OS", the name this reference corpus still uses) is preserved here as the business reference manifestation of Shaper. It is not a fourth technical layer: governance belongs to Shaper OS, durable truth and execution to Runtime, human interaction to Workspace, and domain specialization to Packages.

---

# Enterprise OS — Functional Graph

## State, source ownership and semantic indexes

This is a conceptual relationship graph. Durable application facts are owned in
MariaDB according to [state ownership](../40-TRANSVERSAL/17_APPLICATION_STATE_OWNERSHIP.md).
A selected Qdrant adapter is a derived retrieval index with source references and
a rebuild path. [CRM](../60-SERVICE-ROUTES/CRM.md) and
[telephony](../60-SERVICE-ROUTES/TELEPHONY.md) retain focused domain ownership.
The [glossary](https://github.com/xavdp-pro/shaper-glossary) distinguishes Maestro
the scheduling component from governance, coordination and interaction roles.

## Core graph

```text
ENTERPRISE
├── PEOPLE
│   ├── employees
│   ├── roles
│   ├── permissions
│   ├── onboarding
│   ├── offboarding
│   └── vault
│
├── CRM
│   ├── customers
│   ├── contacts
│   ├── addresses/sites
│   ├── history
│   └── relationships
│
├── ERP
│   ├── products
│   ├── suppliers
│   ├── purchase lots
│   ├── price histories
│   ├── stock
│   ├── quotes
│   └── orders
│
├── COMMUNICATION
│   ├── email
│   ├── shared mailboxes
│   ├── telephony
│   ├── chat
│   └── notifications
│
├── WORK
│   ├── tasks
│   ├── subtasks
│   ├── participants
│   ├── lead
│   ├── priorities
│   ├── urgency
│   └── Kanban
│
├── KNOWLEDGE
│   ├── GED
│   ├── OCR/extraction
│   ├── derived semantic index
│   ├── RAG
│   ├── templates
│   └── generated documents
│
├── GOVERNANCE
│   ├── intentions
│   ├── decisions
│   ├── agreements
│   ├── observers
│   ├── notifications
│   ├── ACK
│   ├── logs
│   └── review
│
├── PILOTAGE
│   ├── dashboards
│   ├── statistics
│   ├── sensors
│   ├── tensions
│   ├── pluspoints
│   ├── optimization proposals
│   └── automation maturity
│
└── AGENTS
    ├── Helm
    ├── Maestro
    ├── executors
    ├── reviewers
    ├── observers
    └── specialized workflows
```

---

## Cross-links

The power comes from cross-links, not isolated modules.

Examples:

```text
CUSTOMER
↔ EMAIL
↔ TASK
↔ DOCUMENT
↔ DECISION
↔ CHAT
↔ ORDER
↔ CALL
↔ NOTIFICATION
```

A customer view can aggregate all of them.

A global attention view can aggregate urgent items from all customers.

A search result can expose direct actions.

A notification can deep-link into the exact object.

Helm can traverse the same graph in natural language.

---

## Operational loop

```text
EVENT
→ OBJECT
→ OBSERVER
→ DECISION / TASK
→ RESPONSIBLE PEOPLE
→ ACTION
→ RESULT
→ LOG
→ NOTIFICATION
→ SENSOR
→ TENSION / PLUSPOINT
→ REVIEW
```

---

## Automation loop

```text
REPEATED HUMAN ACTION
→ PATTERN OBSERVED
→ MATURITY ANALYSIS
→ PROPOSAL
→ HUMAN DECISION
→ TEMPLATE / WORKFLOW / AUTOMATION
→ OBSERVATION
→ PERIODIC REVIEW
```
