> Canonical integration note
>
> Enterprise OS is preserved here as the business reference manifestation of Shaper. It is not a fourth technical layer: governance belongs to Shaper OS, durable truth and execution to Runtime, human interaction to Workspace, and domain specialization to Packages.

---

# Enterprise OS — Functional Graph

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
│   ├── Qdrant
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
