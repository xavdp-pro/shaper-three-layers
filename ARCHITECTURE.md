# Architecture

## 1. Shaper OS — governance kernel

Shaper OS defines the invariant reasoning and governance mechanisms shared by universes, cells, agents, runtimes, and applications.

It owns:

- observation, interpretation, and conclusion boundaries;
- ethics, integrity, sovereignty, and revisability;
- tensions, sensors, pluspoints, and counter-views;
- criticality and cognitive-depth selection;
- knowledge, responsibility, control, and mandate alignment;
- START, CHANGE, STOP, escalation, and recovery principles;
- fractal parent / child / grandparent governance;
- learning and meta-regulation.

It does not prescribe one database, interface, model provider, or business workflow.

## 2. Shaper Runtime — operational substrate

Shaper Runtime turns the kernel into executable system behavior.

It owns:

- identities, tenants, universes, cells, and relationships;
- object graph and schemas;
- event, observer, sensor, and notification infrastructure;
- permissions, capabilities, current mandates, and standing mandates;
- agent execution and orchestration;
- workflow state machines, retries, leases, idempotency, and concurrency;
- RAG, memory, provenance, evidence, audit history, and storage;
- external side effects, reconciliation, rollback, and recovery;
- health, integrity, and trust state.

It exposes explicit contracts upward and evidence downward.

## 3. Shaper Workspace — human operating environment

Shaper Workspace is the role-aware environment through which humans and agents perceive and operate the organization.

It owns:

- navigation, views, dashboards, search, and notifications;
- user and administrator experiences;
- human-agent collaboration surfaces;
- organization-chart-derived workspaces;
- CRM, ERP, documents, communication, projects, support, inventory, accounting, telephony, and other business capabilities;
- confirmation, explanation, evidence, undo, and escalation surfaces.

Applications are projections over the shared object and event graph, not isolated sources of truth by default.

## Cross-layer contract

Every important action should preserve this chain:

```text
INTENTION
→ AUTHORIZED MANDATE
→ RUNTIME ACTION
→ REAL RESULT
→ EVIDENCE
→ OBSERVATION
→ LEARNING
→ RULE OR INTENTION REVIEW
```

Every boundary must remain:

- human-readable;
- agent-executable;
- traceable;
- testable;
- recoverable;
- revisable.

## Dependency rule

- Workspace depends on Runtime contracts.
- Runtime implements OS invariants.
- OS remains coherent without any particular Runtime or Workspace implementation.
- Runtime and Workspace may evolve independently only while their explicit contracts remain satisfied.
