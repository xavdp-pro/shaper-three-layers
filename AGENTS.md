# Agent Working Rules

The canonical layers are Shaper OS, Shaper Runtime and Shaper Workspace. Shaper Linux is optional. SHAPER Enterprise (historically "Enterprise OS") is the business reference manifestation across the layers and Packages.

**Routes:** start at [`00-META/06_AGENT_ROUTES.md`](00-META/06_AGENT_ROUTES.md) for layer masters, A1/A2/A3 guides, and links to the executable kit. Team credit: [`AUTHORS.md`](AUTHORS.md) here; [V1.14 `AUTHORS.md`](https://github.com/xavdp-pro/SHAPER-OS-V1.14/blob/main/AUTHORS.md) for the kit; commit trailers per Rule 2 in the executable repository.

## Before acting
1. Identify the owning layer and cross-layer contracts.
2. State intention, scope, success, STOP and recovery.
3. Separate observation, interpretation, conclusion and unknowns.
4. Resolve knowledge, responsibility, control, permission and mandate independently.
5. Inspect lineage before removing or renaming a concept.
6. Validate both human and agent/system views.
7. Before implementation, inventory all capabilities and dependencies in the
   declared perimeter using [`90-REVIEW/SCOPE-FEATURE-INVENTORY.md`](90-REVIEW/SCOPE-FEATURE-INVENTORY.md).
   Revisit the same feature IDs and acceptance checklist before delivery. Record
   source coverage gaps and separate coded, tested, deployed and human-accepted
   states. Scale the inventory to the task; do not add routine approval waits.

## Before closing a design sequence
After a coherent advance in one or more layers, complete
[`90-REVIEW/SESSION-CLOSEOUT-THREE-PASS.md`](90-REVIEW/SESSION-CLOSEOUT-THREE-PASS.md).
The three passes inspect kernel/governance, human/organizational reality, and
runtime/adversarial reality. Use an independent counter-view when one is
available; otherwise record that it was unavailable. A local conclusion is not
a cross-layer conclusion. Record handoff facts with
[`90-REVIEW/DOC-HANDOFF-CHECKLIST.md`](90-REVIEW/DOC-HANDOFF-CHECKLIST.md).

Helm is a human-facing interface, not policy, durable truth, universal orchestration or infrastructure privilege. Route execution through Runtime authority, Governor coordination and Maker materialization where required.

Files under `99-SOURCE-ARCHIVE/` are immutable evidence. Canonical corrections belong in active documents and the restoration audit.

Structural, irreversible, cross-tenant, security-sensitive or root actions require higher authority, counter-view, tests and recovery. Intelligence is not authority.
