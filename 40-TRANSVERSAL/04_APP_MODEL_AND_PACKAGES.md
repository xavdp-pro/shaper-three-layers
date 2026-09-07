# Declarative App Model and Packages

## Why not generate arbitrary Flutter code for every request?

Agents can generate code, but making generated executable code the default application unit recreates dependency, security, migration and compatibility problems.

Prefer a declarative model for the common 80–95% of business tooling.

## Trusted primitives

Candidate primitives:

```text
Object type
Field / relation
Query
Table / list
Form
Document
Dashboard / chart
Board
Action
Workflow / state machine
Notification
Decision
Approval
Agent action
External connector action
```

## Example

```yaml
app:
  id: supplier-contracts
  schema_version: 3
objects:
  - contract
views:
  - type: table
    query: active_supplier_contracts
    columns: [supplier, annual_amount, renewal_date]
actions:
  - open
  - ask_agent
  - request_renewal_review
policies:
  - finance_contract_access
```

The Workspace renders it. Runtime owns object truth and authorization.

## Shaping lifecycle

```text
human intention
→ agent plan
→ schema diff
→ validation
→ test data / TEST universe
→ authorized rollout
→ observe
→ accept or rollback
```

## Versioning

Persist versions for:

- app schemas;
- workflows;
- rules;
- templates;
- agent instructions;
- connector mappings.

Historical events should be interpretable under the rules that existed when they occurred.

## Packages

A package is a reusable starting graph for a domain, not a fixed SaaS cage.

Examples:

- B2B sales pack;
- association pack;
- legal-office pack;
- restaurant pack;
- property-management pack.

Install → specialize → observe → reshape.

## Plugin escape hatch

When primitives are insufficient, a plugin can provide custom behavior. Treat it as higher risk:

- explicit package/signature/source policy;
- sandbox;
- capabilities;
- tests;
- lifecycle/version compatibility;
- uninstall/recovery semantics.

## Preventing agent-made spaghetti

Every generated change should carry:

- request/intention;
- actor/agent;
- diff;
- reason;
- dependencies;
- test evidence;
- rollout;
- rollback;
- version.

The system should later answer “why does this field/workflow exist?”

## Success criterion

Applications become plastic projections over stable organizational primitives without making every customization a new ungoverned software project.
