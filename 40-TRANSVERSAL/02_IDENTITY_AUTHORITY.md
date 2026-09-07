# Identity, Authority and Stewardship

## Actor identities

Canonical actor types:

```text
Human
Agent
Service
Device
Automation identity
```

Each important action should preserve actor identity and relevant human/system mandate.

## Root Authority

Root Authority is not merely a Unix-like UID. It is the ultimate governance capability of the universe.

Default model:

```text
Steward (human)
      +
Root Agent(s) under direct control
      +
explicit policies / break-glass procedure
      ↓
ROOT AUTHORITY
```

## Authority composition

Effective permission can depend on:

- actor identity;
- organization/universe membership;
- role;
- relationship/object ACL;
- contextual attributes;
- device/session trust;
- technical capability;
- current mandate;
- standing mandate;
- criticality;
- step-up approval.

## Why capabilities matter

A capability makes power explicit. It is easier to reason about:

```text
finance.invoice.read
finance.invoice.prepare
finance.invoice.submit
```

than one broad “Finance Admin” role that silently grants unrelated powers.

Roles can group capabilities while object/context policies constrain them.

## Agents inherit neither user omnipotence nor model omnipotence

An agent acting for a user should receive the narrow authority needed for the action, not the user's entire latent permission set by default.

For sensitive flows, use delegated scoped capabilities.

## Standing mandate

Repeated work can be authorized without constant confirmation when a human explicitly creates a standing mandate.

Example:

```yaml
intent: keep supplier catalogue prices updated
actor: supplier-price-agent
scope: approved suppliers
allowed_actions: parse, compare, propose, update draft ranges
forbidden: publish customer prices, change supplier banking data
exceptions: discrepancy > 15% requires approval
review: monthly
stop: steward/user revoke
```

## Explainability

Runtime should be able to answer:

```text
Why was action X allowed?
Why was it denied?
Which rule/mandate/capability mattered?
Which authority can change that?
```

## Break-glass

Emergency root override should be:

- rare;
- explicit;
- step-up authenticated;
- time-bounded;
- heavily audited;
- reviewed after use.

## Offboarding

Offboarding a human or agent should revoke sessions/capabilities without erasing historical attribution. Device revocation is independent from user deletion.

## Success criterion

Authority remains understandable enough to govern, granular enough to contain damage, and flexible enough to model real organizations without rebuilding Active Directory complexity for its own sake.
