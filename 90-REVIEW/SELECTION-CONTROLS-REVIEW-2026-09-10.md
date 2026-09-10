# Selection controls: three-pass closeout — 2026-09-10

Scope: record Xavier's project-wide UI requirement and link Clinic/Vox handoffs.
Observation: Clinic has CustomSelect with a six-option search threshold; some
native selects remain. No application migration or deployment is claimed here.

1. Governance: Workspace presentation only; Runtime validation and authority are
   unchanged. This does not create a new approval gate or business permission.
2. Human: preserve choice while clearing search text; growing lists searchable
   before they become long; shared branding, accessible keyboard/touch operation.
3. Runtime: require bounded remote loading, stale response protection, explicit
   errors and existing visibility constraints. Roll back regressions per component.

Independent counter-view: clinic_voice_bench read-only review found the contract
COHERENT. Incorporated its precision that visually hidden native controls must
not remove the selector's accessible semantics.

Conclusion: COHERENT for the Workspace contract and its Runtime boundaries.
Implementation checklist remains OPEN; next step is inventory and shared-component
qualification before migrating remaining screens. No executable changes this turn.
