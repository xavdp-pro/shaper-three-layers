# Vocabulary Projections

## Principle

The same underlying graph should be described at the resolution useful to the person or agent looking at it.

Internal complexity must not leak into ordinary use without a functional reason.

## User projection

```text
Workspace
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
```

## Steward projection

Adds canonical architecture:

```text
Universe
Root Authority
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
| Universe | Workspace / Organization |
| Sub-universe | Space / Team / Business scope |
| Object | File, customer, task, record, item |
| Capability | Permission / allowed action |
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

## Rule

A UI label is not required to match the internal canonical noun. The internal model exists for architectural consistency; the external term exists for human usefulness.
