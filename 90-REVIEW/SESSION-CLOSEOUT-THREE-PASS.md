# Session Closeout: Three-Pass Cross-Layer Review

> **Status:** mandatory review protocol after a coherent advance in one or more
> layers. It is a quality gate for understanding, not a ceremony that declares
> a design complete.

## Purpose

A change that looks correct inside one layer may contradict a contract, create a
human dead end or fail under runtime conditions elsewhere. At the end of a
design or documentation sequence, inspect the same change from three deliberately
different positions before treating the sequence as coherent.

This protocol applies to changes in Shaper OS, Shaper Runtime, Shaper Workspace,
Enterprise reference material or transversal contracts. It applies especially
when a concept crosses layers.

## Review rule

Complete all three passes before closing the sequence. Record:

- what was observed in the repository or evidence;
- what is interpretation or design proposal;
- effects on each owning layer and contract;
- corrections made;
- unresolved questions and the next safe step.

When another independent agent or reviewer is available, obtain a counter-view
for at least one pass. If only one reviewer is available, perform the three
changes of view yourself and explicitly record that the counter-view was absent.
A single coherent voice is not evidence that no blind spot exists.

## Pass 1 — Kernel, meaning and governance

**Question:** Does the change preserve Shaper OS principles: reality before
claim, explicit authority, proportional action, evidence, repair and
revisability?

Check that it does not:

- turn intelligence, a chat, a role title or a document into implicit authority;
- collapse observation, interpretation, mandate and action;
- freeze a specialized business choice as a universal law;
- create an unobservable automation or an unrepairable decision;
- weaken sovereignty, tenant boundaries or the human-rooted governance model.

## Pass 2 — Human and organizational reality

**Question:** Would a real organization understand, adopt and benefit from this
without being forced into a rigid machine-shaped role?

Check:

- what a person, team, manager and Steward actually see and do;
- the value path from ordinary work to coordination, learning and shared
  prosperity;
- multi-role people, delegation, absence, growth, disagreement and handoff;
- whether automation clarifies and extends capacity rather than hiding
  responsibility;
- language, explanation, STOP and recovery from confusion.

## Pass 3 — Runtime, adversarial and operational reality

**Question:** What breaks under concurrency, interruption, external failure,
stale authority, hostile input or partial deployment?

Check:

- identity, capability, permission and mandate independently;
- object ownership, source of truth, event causality and audit evidence;
- idempotency, retries, leases, reconciliation and compensation;
- tenant isolation, visibility boundaries, secrets and execution-environment
  limits;
- proof of outcome, observability of observers, rollback and recovery.

## Cross-layer conclusion

Classify the result as one of:

| Verdict | Meaning |
| --- | --- |
| **COHERENT** | The change fits its owning layer, respects contracts and has no known blocking gap. |
| **COHERENT WITH CORRECTIONS** | The review found gaps and they were corrected with their rationale recorded. |
| **OPEN** | A material authority, contract or evidence question remains. Do not present the change as settled. |
| **STOP** | The change conflicts with a governing rule, creates unacceptable risk or lacks the authority to continue. |

The conclusion must name the affected layers. “Reviewed” alone is not a result.

## Closeout discipline

Do not run this protocol after every sentence. Run it when a session has made a
coherent advance: a new concept, a changed contract, an accumulated set of
business capabilities or a cross-layer integration.

Its purpose is to prevent local progress from silently becoming global
incoherence. The review may produce no change; that is still useful evidence.

## Perimeter completeness prerequisite

Use [the scope-first feature inventory](../90-REVIEW/SCOPE-FEATURE-INVENTORY.md)
before implementation and reconcile the same rows before delivery. The checks
above evaluate quality; they do not establish that every scoped requirement has
been identified. Record source coverage, dependencies and omissions separately.
