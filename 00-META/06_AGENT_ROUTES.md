# Agent and architect routes

This repository holds architecture and governance documentation. It does **not**
hold executable law, runtime proof, or per-commit agent credit. Use the table
below to pick the right entry point without duplicating authority.

| Goal | Start here | Then |
| --- | --- | --- |
| Work on architecture or cross-layer docs | [`AGENTS.md`](../AGENTS.md) | [`SCOPE-FEATURE-INVENTORY.md`](../90-REVIEW/SCOPE-FEATURE-INVENTORY.md), [`SESSION-CLOSEOUT-THREE-PASS.md`](../90-REVIEW/SESSION-CLOSEOUT-THREE-PASS.md) |
| Pick cognitive depth (A1 / A2 / A3) for a layer | Layer master below | Matching `10_AGENT_A1.md`, `11_AGENT_A2.md`, or `12_AGENT_A3.md` in that layer directory |
| Clone, build, prove, or change bricks | [SHAPER-OS-V1.14](https://github.com/xavdp-pro/SHAPER-OS-V1.14) — `docs/agent/BOOT-CONTRACT.md`, `software/RULES.md` | Universe runbook, `docs/TESTING-REPORT.md`, git `Co-Authored-By` trailers |
| Team credit (this documentation tree) | [`AUTHORS.md`](../AUTHORS.md) | Commit trailers; kit roster in [V1.14 `AUTHORS.md`](https://github.com/xavdp-pro/SHAPER-OS-V1.14/blob/main/AUTHORS.md) |
| Enterprise direction, decisions, mandates (product vision) | [`15_DIRECTION_DECISIONS_AND_MANDATES.md`](../50-ENTERPRISE-REFERENCE/15_DIRECTION_DECISIONS_AND_MANDATES.md) | Scoped current-decision retrieval when implemented in Runtime |
| Implement Enterprise graph, tasks, real-time UI | [`03_AGENT_IMPLEMENTATION_GUIDE.md`](../50-ENTERPRISE-REFERENCE/03_AGENT_IMPLEMENTATION_GUIDE.md) | Functional graph, Helm model, validation protocol |
| End a documentation session | [`DOC-HANDOFF-CHECKLIST.md`](../90-REVIEW/DOC-HANDOFF-CHECKLIST.md) | Link closeout and inventory state; do not fork a per-engine checklist |

## Layer masters and agent guides (canonical)

| Layer | Master | A1 | A2 | A3 |
| --- | --- | --- | --- | --- |
| Shaper OS | [`10-SHAPER-OS/00_MASTER.md`](../10-SHAPER-OS/00_MASTER.md) | [`10_AGENT_A1.md`](../10-SHAPER-OS/10_AGENT_A1.md) | [`11_AGENT_A2.md`](../10-SHAPER-OS/11_AGENT_A2.md) | [`12_AGENT_A3.md`](../10-SHAPER-OS/12_AGENT_A3.md) |
| Shaper Runtime | [`20-SHAPER-RUNTIME/00_MASTER.md`](../20-SHAPER-RUNTIME/00_MASTER.md) | [`10_AGENT_A1.md`](../20-SHAPER-RUNTIME/10_AGENT_A1.md) | [`11_AGENT_A2.md`](../20-SHAPER-RUNTIME/11_AGENT_A2.md) | [`12_AGENT_A3.md`](../20-SHAPER-RUNTIME/12_AGENT_A3.md) |
| Shaper Workspace | [`30-SHAPER-WORKSPACE/00_MASTER.md`](../30-SHAPER-WORKSPACE/00_MASTER.md) | [`10_AGENT_A1.md`](../30-SHAPER-WORKSPACE/10_AGENT_A1.md) | [`11_AGENT_A2.md`](../30-SHAPER-WORKSPACE/11_AGENT_A2.md) | [`12_AGENT_A3.md`](../30-SHAPER-WORKSPACE/12_AGENT_A3.md) |

Human pedagogical depth (Shaper OS layer only): [`20_HUMAN_FOUNDATIONS.md`](../10-SHAPER-OS/20_HUMAN_FOUNDATIONS.md), [`21_HUMAN_STEWARD.md`](../10-SHAPER-OS/21_HUMAN_STEWARD.md).

## Non-canonical bootstrap tree

The [`layers/`](../layers/) directory is an initial bootstrap snapshot. Do not
treat it as the active editing target. Use the numbered directories above.

## Working root (operator)

When several repositories sit under a shared operator root (for example REMOTE3),
that root's `AGENTS.md` points to canon ([SHAPER-OS-V1.14](https://github.com/xavdp-pro/SHAPER-OS-V1.14)),
this architecture repository, and mandatory inventory/closeout discipline. It
does not grant permission by itself.
