# Vocabulary Projections

## Principle

The same underlying graph should be described at the resolution useful to the person or agent looking at it.

Internal complexity must not leak into ordinary use without a functional reason.

## User projection

```text
Workspace
Helm
Spaces
People
Agents
Files
Apps
Search
```

A normal user should be able to work almost entirely with these terms.

## Operator projection

Adds:

```text
Teams
Roles
Rules
Workflows
Approvals
Tasks
Exceptions
Automation
History
Pilot level
```

## Steward projection

Adds canonical architecture:

```text
Universe
Jurisdiction
Root Authority (master root, jurisdiction root)
Governor
Maker
Runtime
Capabilities
Policies
Vault
Events
Sensors
Tensions
Trust
Quarantine
Repair/Rebuild
```

## Agent A1 projection

Prefer explicit task contracts over architecture prose:

```yaml
objective:
inputs:
scope:
output:
success_criteria:
hard_rules:
stop_conditions:
escalation_conditions:
```

## Agent A2 projection

Add state reasoning:

```yaml
observations:
interpretations:
current_conclusion:
hypotheses:
tensions:
tests:
reversible_action:
feedback:
revision:
```

## Agent A3 projection

Add systemic relationships:

```yaml
purpose:
scopes:
assumptions:
authorities:
trust_roots:
policies:
trajectories:
cross_layer_effects:
meta_sensors:
rollback:
review_conditions:
```

## Translation table

| Internal | User/Operator projection |
|---|---|
| Universe / logical space | Space or organizational context according to actual membership |
| Specialized cell/service | Service, such as telephony, CRM or a shop |
| Component / functional unit | Component; expose technical detail when useful |
| Class / specialization / instance | Reusable form / selected domain form / identified service |
| Object | File, customer, task, record, item |
| Capability | Available action; distinguish it from granted permission |
| Mandate | Instruction / approved automation |
| Vault | Files / secure storage |
| Object graph | Connected company data |
| Semantic index / RAG | Search / Knowledge |
| Gateway | Import / Export / Open externally |
| Governor | Usually invisible |
| Maker | Invisible outside Steward tools |
| Event bus | Live updates / history |
| Observer | Monitoring / automation |
| Tension | Alert / inconsistency / thing to inspect |
| Pluspoint | Improvement / unusual success |
| Root Authority | System administration / Steward control |
| Jurisdiction | What you are in charge of |
| Jurisdiction root | Full control of your own system |
| Master root | Invisible outside the founding tandem's tools |
| Pilot level | Your level: see and learn, prepare and propose, act within a mandate, shape your system |

Use the [glossary and aliases](https://github.com/xavdp-pro/shaper-glossary) for
stable meanings. [Composition](08_COMPOSITION_AND_SOURCE_MAP.md) distinguishes
membership, dependency, authority and physical placement. Workspace names an
interaction responsibility/product; it is not a mandatory containment level.

## Rule

A UI label is not required to match the internal canonical noun. The internal model exists for architectural consistency; the external term exists for human usefulness.
