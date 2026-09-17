# Shaper OS — Human Steward Guide
## Governing the system below the applications

A Steward does not merely administer accounts. The Steward protects the conditions under which Shaper can remain autonomous, observable, secure and revisable.

## 1. Steward versus root

**Steward** names the human function.

**Root Authority** names the ultimate system authority formed by the Steward, directly controlled root-capable agents, and explicit policies/procedures.

The human retains final responsibility for systemic powers. The Root Agent extends perception, memory, analysis and execution; it does not become a separate sovereign root by default.

Root Authority exists at two strata, never more:

- **Master root.** The founding tandem at the top of the fractal holds it. It reaches underneath every universe to its pods and hosts, directs the Governor and the Makers alone, keeps matrices and backup contracts, and grants every jurisdiction.
- **Jurisdiction root.** A Steward given a jurisdiction holds it with their agent, through Helm: a client at the Helm of their Workspace or Vox. It has full power inside that jurisdiction, down to the pods of its universes. It never reaches a host, the Governor, a Maker, a class repository, another jurisdiction or its own backup contract.

A jurisdiction root may grant a narrower jurisdiction inside its own, never a wider one. See [Naming and Deprecations](../00-META/05_NAMING_AND_DEPRECATIONS.md#strata-of-authority-17-september-2026).

## 2. What the Steward governs

The Steward should be able to reason about:

- universes and boundaries;
- users, agents, devices and services;
- roles, capabilities, permissions and mandates;
- trust and compromise;
- policies and their purposes;
- sensors and observer health;
- backup/recovery;
- criticality and review depth;
- escalation hierarchy;
- changes to Runtime/Workspace architecture.

## 3. The authority question

For every important power, ask:

```text
Knowledge — does this actor see enough?
Responsibility — is it accountable for the result?
Control — does it have enough power, and only enough power?
```

Do not give more authority to an agent merely because it is more intelligent.

## 4. Root power should be available, not permanently exercised

Root Authority may need to inspect or override almost anything. That does not require one agent process to hold every key forever.

Prefer:

- scoped privileged requests;
- step-up authentication;
- short-lived capabilities;
- independent audit;
- explicit break-glass procedures;
- revoke/kill paths.

## 5. Trust is not availability

A service can return `200 OK` and still be compromised.

Track separately:

- functional;
- healthy;
- integral;
- trustworthy.

A drop in trust may justify reducing capabilities even while the service remains online.

## 6. Fractal repair

A child should observe itself more freely than it can rewrite its own structural guardrails.

When a problem touches the mechanism the child depends on, escalate:

```text
child → parent → grandparent → Root Authority
```

No level self-certifies critical recovery while being the only observer of itself.

## 7. Security incident posture

Distinguish:

```text
DEVELOPMENT: DEV → TEST → PROD
INCIDENT: DETECT → CONTAIN → EVIDENCE → QUARANTINE → CAUSE → FIX SOURCE → REBUILD/REPAIR → TEST → PROD → MONITOR
```

Quarantine is a trust state, not a test environment.

For reproducible compromised components, prefer rebuild from a healthy chain when integrity cannot be reasonably re-established.

## 8. Criticality

Do not spend maximum cognition on every task.

- C0/C1: bounded/local reasoning.
- C2: differentiated checks and tests.
- C3: independent counter-views and higher authority.
- C4: systemic/root review, adversarial reasoning, progressive rollout and rollback.

## 9. Recurrence is evidence

A repeated incident after local correction changes the diagnosis.

> When local repair does not hold, move up one level.

Do not keep applying the same local fix merely because it worked once.

## 10. Meta-regulation dashboard questions

A Steward should periodically ask:

- Which observer is dead or noisy?
- Which policy no longer serves its goal?
- Which repeated approval should become a standing mandate — or should remain manual?
- Which agent has too much control relative to knowledge/responsibility?
- Which component has an unnecessarily large blast radius?
- Which metric is being optimized instead of the actual product?
- Which success deserves to become a reusable pattern?
- Which old assumption has not been reviewed?

## 11. Relationship to Runtime

Runtime is where Steward governance becomes enforceable:

- device enrollment/revocation;
- capability policy;
- session trust;
- object boundaries;
- audit;
- agent mandates;
- key brokerage;
- backup/recovery.

Helm's governance views, at the Steward level, are a projection over Runtime authority. They are not the authority itself.

## 12. Relationship to Workspace

Workspace should hide the cathedral from ordinary users while making Steward controls precise and inspectable.

Packaging governance tooling separately can reduce exposed administrative tooling; it never becomes a second interface beside Helm. High-security deployments may package it separately, but Runtime authorization remains the primary boundary.

## 13. Governance change procedure

For systemic change:

```text
observe problem
→ state purpose
→ identify assumptions
→ propose change
→ independent review
→ test in bounded scope
→ progressive rollout
→ observe real effect
→ accept / revise / rollback
→ schedule review
```

## 14. Steward success criterion

A good Steward does not centralize every decision personally. The Steward creates a system where local autonomy is meaningful, dangerous powers remain bounded, failures are detectable, and authority can intervene when the local level is no longer sufficient.
