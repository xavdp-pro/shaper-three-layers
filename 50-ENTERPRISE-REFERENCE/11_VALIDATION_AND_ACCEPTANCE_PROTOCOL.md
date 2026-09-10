# Validation and Acceptance Protocol

A capability is not implemented because a screen exists or an agent produced a plausible sentence.

```text
INTENTION → OBJECTS/CONTEXT → AUTHORITY/MANDATE → ACTION
→ RESULT → EVIDENCE/CAUSALITY → HUMAN EXPLANATION
→ FAILURE/STOP → RECOVERY/RECONCILIATION → REVIEW
```

## Four mandatory passes

1. **Kernel/architecture:** layer ownership, invariants, authority separation, epistemic states and reversibility.
2. **Human/business:** comprehension, manual fallback, context, decision, accessibility and recovery from confusion.
3. **Implementation/production:** contracts, state machines, idempotency, concurrency, side effects, versioning, observability and restoration.
4. **Adversarial/drift:** isolation, hostile input, stale authority, deceptive schema, unsafe plugin, resource pressure, sensor failure and model/provider drift.

## Execution responsibility

The constructing agent owns the before-build checklist and the after-assembly
functional acceptance run for every scoped feature, as defined in
[the scope-first inventory](../90-REVIEW/SCOPE-FEATURE-INVENTORY.md#the-constructing-agent-owns-the-functional-acceptance-run).
The records below carry its actual execution evidence. Independent review and
human acceptance remain separate; neither replaces the agent's own checks.

## Test record

```yaml
scenario_id:
version:
persona:
initial_state:
intent:
resolved_objects:
epistemic_state:
required_capabilities:
interaction_surfaces:
test_driver_and_version:
required_equipment_and_access:
test_means_verified:
observation_channel:
coverage_limits:
execution_actor:
test_data_and_cleanup:
permission_and_mandate:
expected_events:
expected_result:
expected_evidence:
executed_at:
installed_target:
source_revision:
executed_steps:
observed_result:
actual_evidence_reference:
blocker_and_next_step:
human_explanation:
failure_injections:
stop_condition:
rollback_or_compensation:
trust_effect:
acceptance_status:
reviewer:
```

## Thirteen scenario gates

| Scenario | Critical failure injection | Required proof |
| --- | --- | --- |
| Owner tour | fabricated trend explanation | source objects and calculations |
| Supplier update | duplicate retry or wrong product | attachment, matches, dated versions |
| Receipt | uncertain extraction silently accepted | source, confidence, validation |
| Voice invoice | wrong customer/order | resolved IDs, preview, validator |
| Search to call | wrong number/recording policy | contact resolution and call event |
| Live shaping | data exposure or damaging migration | diff, tests, version, rollback |
| Decision memory | missing reason or approver | decision object and review condition |
| Observability proof | success claim with missing events | evidence view plus observer health |
| Optimization | recommendation stated as fact | observation/hypothesis/options |
| Learning path | maturity treated as authority | encountered-capability record only |
| Missing email | absence treated as proof | mailbox, ingestion and observer checks |
| Prospect claim | double ownership/stale lock | lease, conflict event, recovery |
| Standing mandate | scope creep/format drift | mandate, exceptions, run trace, review |

## Status vocabulary

`NOT STARTED` → `PARTIAL` → `DEMO VALIDATED` → `PRODUCTION CANDIDATE` → `PRODUCTION VALIDATED`, with `DEGRADED/REVOKED` when trust or compatibility changes.

Every simulated integration declares what is fictional, what behavior is real, what production connector replaces it, and which legal/security constraints appear in production.

## Perimeter completeness prerequisite

Use [the scope-first feature inventory](../90-REVIEW/SCOPE-FEATURE-INVENTORY.md)
before implementation and reconcile the same rows before delivery. The checks
above evaluate quality; they do not establish that every scoped requirement has
been identified. Record source coverage, dependencies and omissions separately.
