# Shaper — Three-Layer Architecture

Private working repository for the unified Shaper architecture.

The system is organized into three distinct but connected layers:

| Layer | Role | Core question |
| --- | --- | --- |
| [Shaper OS](layers/shaper-os/README.md) | Adaptive cognitive and governance kernel | How does the system perceive, decide, act, learn, and preserve integrity? |
| [Shaper Runtime](layers/shaper-runtime/README.md) | Operational and technical substrate | How are identities, universes, objects, events, policies, agents, workflows, and evidence executed? |
| [Shaper Workspace](layers/shaper-workspace/README.md) | Human and application environment | How do humans and agents work together through role-specific interfaces and business capabilities? |

## Direction

The three layers form one stack:

```text
SHAPER WORKSPACE
Human experience, applications, role-based interaction
              ↓
SHAPER RUNTIME
Execution, objects, events, policies, agents, persistence
              ↓
SHAPER OS
Cognitive kernel, governance, integrity, learning
```

The relationships are bidirectional: higher layers express intention and context; lower layers return state, evidence, tensions, and consequences.

## Naming boundary

Earlier documents use **Enterprise OS** for the graph of reusable business primitives activated by the organization chart. That concept is preserved, but it is not treated as a fourth technical layer:

- its operational primitives belong primarily to **Shaper Runtime**;
- its human-facing capabilities belong primarily to **Shaper Workspace**;
- its governance and adaptation rules come from **Shaper OS**.

Legacy terminology must be migrated explicitly rather than silently redefined.

## Repository map

- `layers/shaper-os/` — kernel principles, governance, agent cognition, integrity, and recovery.
- `layers/shaper-runtime/` — executable substrate, contracts, event model, mandates, workflows, storage, and observability.
- `layers/shaper-workspace/` — human environment, applications, roles, interaction, and administration.
- `ARCHITECTURE.md` — boundaries and information flow across the stack.
- `AGENTS.md` — working rules for humans and AI agents contributing to this repository.

## Status

Living architecture. Stable in integrity, mobile in form, revisable in understanding.
