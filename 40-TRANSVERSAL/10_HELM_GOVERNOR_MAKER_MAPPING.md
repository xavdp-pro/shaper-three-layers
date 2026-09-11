# Helm, Governor and Maker

| Component | Responsibility | Must not silently become |
| --- | --- | --- |
| Helm | conversational pilotage and contextual interaction | root authority or universal executor |
| Governor | routing, coordination, delegation and escalation | source of human intent |
| Maker | approved structural/infrastructure materialization | autonomous product owner |
| Runtime authority | capability, permission, mandate, policy, evidence | a UI convention |
| Steward | human governance of major scopes | manual bottleneck for all low-risk work |

```text
Steward request → Helm clarifies → declarative diff
→ Runtime authority/impact check → Governor plans
→ Maker materializes in DEV/TEST → counter-view/tests
→ authorized promotion → Workspace update → observe
→ accept or rollback
```

Helm may make shaping feel immediate; live appearance never permits bypassing authority, tests, migration or data preservation.

The deployed Governor/Maker pattern remains compatible: Governor holds delegated queues without broad host access; Maker alone materializes approved structural changes; parent/root levels repair compromised children; human plus directly controlled root-capable agents remain ultimate authority.

Separate User and Steward applications are useful defense in depth. Runtime authorization and cryptographic identity remain the real boundary.

## Fractal observation and parent-led correction

Every Shaper universe participates in the same loop, regardless of its host or
business specialization. This section describes the architectural relationship;
it does not create authority beyond the [engineering canon](https://github.com/xavdp-pro/SHAPER-OS-V1.14/blob/main/software/RULES.md)
(Rules 20, 22–25, 27, 36–37).

- **Observe locally.** The universe records operational events, failures, attempted
  corrections and evidence references through Logger. It compares observed results
  with its intent and expected state. A successful log write is not proof of the
  underlying result; verify persisted effects outside their producer.
- **Keep one meaning for state.** Logger preserves the event trail; it does not
  replace the governing ledger or the instance's `status.json`. Dated state and
  evidence freshness make silence or a stalled observer visible. Missing evidence
  is an unknown, not a healthy verdict.
- **Correct only within the granted scope.** A universe may perform authorized
  work-level corrections. It never rewrites its own active infrastructure, bridge
  or governing rules to repair itself. Structural repair comes from the parent
  level, out of band, through its authorized execution organs; root recovery
  belongs to the external guardian or human operator.
- **The parent checks the child.** It consumes permitted summaries, dated status
  and evidence references, checks outcomes and failed corrections, then arranges
  authorized repair or escalation. Parentage is not unrestricted access to raw
  child data, secrets or vector collections. Governor coordination and Maker
  materialization retain the responsibilities above.
- **Verify the correction and bound the loop.** Record the incident, mandate,
  actor, operation identity, before/after observations and verification result.
  Apply the canon's retry bounds, degraded-state and escalation rules rather than
  retrying forever. The parent is itself observed by its parent; placement across
  hosts changes connectivity, not this responsibility.
- **Reuse the existing mechanisms.** Routine observation need not invoke an LLM
  continuously. A reasoning agent can be called for scoped diagnosis or correction
  when required. This is not a second supervisory hierarchy alongside Shaper.

Integration qualification must exercise local detection, parent-visible evidence,
authorized correction and external verification, including a stale Logger/status
feed, an unreachable child, a failed repair and root escalation. These scenarios
remain to be demonstrated end to end; this documentation is not deployment proof.
