# Shaper Runtime (bootstrap snapshot — not canonical)

> **Redirect:** [`20-SHAPER-RUNTIME/`](../../20-SHAPER-RUNTIME/) and [`layers/README.md`](../README.md).

**Layer type:** operational and technical substrate.

Shaper Runtime implements the executable mechanisms through which Shaper OS governs real universes, cells, agents, objects, events, policies, workflows, memory, and evidence.

## Initial capability map

- identity, tenancy, universes, cells, and organization graph;
- shared object graph and schema registry;
- event bus, observers, sensors, notifications, and acknowledgements;
- roles, permissions, technical capabilities, and mandates;
- agent registry, orchestration, queues, leases, and execution;
- workflow state machines, idempotency, retries, and concurrency;
- RAG, memory, provenance, traceability, and audit;
- persistence, integrations, external side effects, and reconciliation;
- health, integrity, trust, quarantine, rebuild, and recovery.

## Boundary

Runtime is headless by design. A browser, desktop, mobile interface, CRM screen, or admin console belongs to Shaper Workspace, even when it invokes Runtime capabilities.

## Current source

- [Three-Perspective Review](reviews/12_THREE_PERSPECTIVE_REVIEW.md) records the bridges and production invariants identified in the Shaper OS / Enterprise OS coherence pass.
