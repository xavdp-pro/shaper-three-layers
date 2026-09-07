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
