# Enterprise Primitives Mapping

## Why this document exists

The earlier Enterprise OS documentation contained a rich business graph. Splitting the new architecture into Shaper OS / Runtime / Workspace must not accidentally erase those capabilities.

This document maps the earlier functional corpus into the new architecture without turning this repository back into a monolithic ERP specification.

## Mapping

| Earlier Enterprise primitive | Primary new home | Workspace projection |
|---|---|---|
| Person / Organization / Customer / Contact | Runtime object graph | People / customer context |
| Employee onboarding/offboarding | Runtime identity + workflow | Operator/Steward flow |
| Human Vault / confidential employee docs | Runtime vault + policy | Restricted Files/People surface |
| CRM | Runtime objects/relations/events | CRM/context app schema |
| Products / ERP / stock / purchase lots | Runtime business objects/state machines | Product/stock app surfaces |
| Purchase vs sale flows | Runtime workflows | Purchasing/Sales apps |
| Quotes / orders | Runtime objects/workflows/decisions | Quote/order surfaces |
| Email ingestion | Runtime connector/event pipeline | Mail/context surface |
| Telephony | Runtime connector/events/permissions | Softphone/call context surface |
| AI + human unified call history | Runtime event/object history | Contact/customer timeline |
| Tasks / nested tasks / lead + contributors | Runtime objects/events | Task/Kanban/attention surfaces |
| Contextual chat | Runtime conversation objects/events | Chat surface in context |
| GED + RAG | Runtime Object Space/search | Files/Search/knowledge surfaces |
| Document generation | Runtime templates/schema | Document actions/surface |
| Legal document layer | Package + Runtime policy/objects | Legal app surfaces |
| Decisions as objects | Runtime intention/decision/mandate | Decision history/approval UI |
| Notifications + ACK + deep link | Runtime event/attention | Notification to exact context |
| Quick Search | Runtime search/RAG | Global Search surface |
| Calendar/appointments | Runtime connector/object policy | Calendar surfaces |
| Prospecting queue / claim / lease | Runtime concurrency/workflow | Sales queue surface |
| Support/cases | Runtime generic case primitive/package | Support app |
| Organization-chart-driven behavior | Runtime roles/relations/policies | Navigation/workflow projection |
| Proactive optimization observer | Runtime observer/agent | “What should we improve?” |
| Common event + observer layer | Runtime | Live Workspace updates |
| Enterprise health pulse | Runtime observability | Steward/manager dashboard |
| Data ownership/system of record | Runtime policy | Human explanation/status |
| Privacy/retention/jurisdiction | Runtime policy + deployment | Steward policy UI |
| Manual → assisted → automated | Shaper OS governance + Runtime mandates | Human maturity/automation UX |
| Live shaping | Runtime app-schema change lifecycle | Workspace shaping mode |
| Idempotency/concurrency | Runtime invariant | Conflict/progress UX |
| External side effects | Runtime invariant/connector | Preview/approval/status UI |
| Schema/rule/template versioning | Runtime | Compatibility/history UI |
| Audit immutability | Runtime | History/explanation surface |
| Tenant isolation | Runtime security | Invisible to normal user |

## What changed conceptually

The old Enterprise OS corpus described both the business truth and the screens in one broad “OS.” The new model separates them:

```text
business truth + authority + events + workflows = Runtime
human projection + interaction = Workspace
adaptive rules/governance = Shaper OS
```

## What did not disappear

The following earlier invariants remain mandatory:

- object graph rather than pile of disconnected screens;
- organization structure drives behavior;
- tasks/documents/decisions/conversations attach across object types;
- notifications carry context;
- agent changes use the same event/authority paths as human changes;
- important flows have explicit state machines;
- idempotency and concurrency are first-class;
- external side effects require compensation/reconciliation thinking;
- historical rules/templates remain versioned/interpretable;
- observers themselves are monitored;
- acceptance means object + permission + event + UI + agent + trace + failure + test + recovery are coherent.

## Domain packages, not kernel hard-coding

CRM, ERP, restaurant, legal, support, accounting-adjacent and other vertical functionality should increasingly be expressed as packages over Runtime primitives and Workspace surfaces. Shaper OS does not hard-code one business model.
