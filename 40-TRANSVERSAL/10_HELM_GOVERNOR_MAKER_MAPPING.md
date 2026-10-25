# Helm, Governor and Maker

| Component | Responsibility | Must not silently become |
| --- | --- | --- |
| Helm | conversational pilotage within one jurisdiction and one pilot level | root authority or universal executor |
| Governor | routing, coordination, delegation and escalation, under its explicitly delegated jurisdiction | source of human intent or authority outside its declared scope |
| Maker | approved structural/infrastructure materialization, under its explicitly delegated jurisdiction | autonomous product owner |
| Runtime authority | capability, permission, mandate, policy, evidence | a UI convention |
| Steward | human governance of major scopes, as the human of a root tandem | manual bottleneck for all low-risk work |

```text
Pilot request → Helm clarifies within jurisdiction and pilot level → declarative diff
→ Runtime authority/impact check → Governor plans
→ Maker materializes in DEV/TEST → counter-view/tests
→ authorized promotion → Workspace update → observe
→ accept or rollback
```

Helm may make shaping feel immediate; live appearance never permits bypassing authority, tests, migration or data preservation.

A jurisdiction root shapes through this chain like any pilot. Its request reaches the relevant governor and maker through the authorized desired-state contract. Governors and makers take direction through their declared governing owner and delegated jurisdiction. A feature that no class offers becomes a change to the class, made by its maker tandem, never an exception inside one instance.

The Governor/Maker pattern separates responsibilities: Governor holds delegated queues without broad host access; Maker alone materializes approved structural changes; parent/root levels repair compromised children; human plus directly controlled root-capable agents remain ultimate authority.

## Coordination is a role, not an outbound execution privilege

In the SHAPER engineering mechanism, coordination is expressed through the
ledger and dated desired state. Makers retrieve authorized work, execute the
permitted materialization recipes and report observed facts. “Governor plans” in
the diagram does not mean that the governor connects to hosts, possesses their
private keys or runs infrastructure commands. “Maker” names an execution role;
it does not by itself require an LLM or authorize autonomous policy decisions.

A PodMesh infrastructure manager coordinates its delegated technical operations.
A business governor owns approved desired state for its declared service scope;
makers realize permitted changes and return attributable results. Several
scoped governors may coexist in a fractal. The containing tandem's explicit
jurisdiction/delegation determines their authority, not the name “manager” or
physical nesting. [Composition/source ownership](../00-META/08_COMPOSITION_AND_SOURCE_MAP.md)
and the [ecosystem owner](https://github.com/xavdp-pro/shaper-ecosystem) maintain
the relation to concrete product/workshop owners.

Packaging governance tooling separately from work tooling is useful defense in depth; it never creates a second interface beside Helm. Runtime authorization and cryptographic identity remain the real boundary.

## Fractal observation and parent-led correction

Every Shaper universe participates in the same loop, regardless of its host or
business specialization. This section describes the architectural relationship;
it follows the selected [framework](https://github.com/xavdp-pro/SHAPER-OS-V1.15)
and the realization's explicit authority and recovery contract.

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

The owning realization and companion lab record integration outcomes for local
detection, parent-visible evidence, authorized correction, external verification
and escalation. [Persistent acting agents](16_PERSISTENT_ACTING_AGENTS.md) and
[state ownership](17_APPLICATION_STATE_OWNERSHIP.md) supply the shared contracts.
