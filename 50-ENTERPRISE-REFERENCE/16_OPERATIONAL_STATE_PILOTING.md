# Operational State Piloting

> **Status:** target operating method. This document specifies a SHAPER
> Enterprise capability; it does not claim that a runtime state machine,
> dashboards, agent actions or automatic transitions have been implemented.

## Purpose

Organizations should not use the same response for a new service, a live
incident, a stable operation and a period of rapid growth. Operational State
Piloting gives a person and their authorized agents a shared way to:

1. assess the present state of a bounded scope from evidence;
2. choose the response appropriate to that state;
3. define the evidence required before changing the response; and
4. retain the assessment, decision and outcome for later review.

A scope can be an Organization, Cell, product, service, programme, project or
workflow. It is never a permanent classification of a person.

## Core rule

> Do not operate a scope as though it has reached a later state until the exit
> evidence for its present state is recorded and accepted by the actor who has
> authority over that transition.

This prevents a new service from being treated as a scaling success, an incident
from being treated as ordinary improvement, or a good metric from being treated
as proof that the whole system is healthy.

## Operating states

The model uses ordinary terms. A scope may move backward when reality changes;
the sequence is a guide to response, not a claim that progress is inevitable.

| State | What it means | First response | Evidence required before leaving |
| --- | --- | --- | --- |
| **Unknown** | Evidence is insufficient or contradictory. | Establish facts, scope, sources, affected people and immediate risks. | A bounded assessment with known unknowns and a review owner. |
| **Establishing** | A new activity has no dependable place in the organization yet. | Define purpose, useful outcome, responsible role, audience, first route in and first route out. | A real, observed use or exchange; a feedback loop; baseline measures. |
| **Incident** | Safety, continuity, integrity or a critical commitment is presently at risk. | Protect people and data, contain change, preserve evidence, restore a safe fallback. | Harm contained, essential service or fallback restored, cause still explicitly known or open. |
| **Recovery** | The immediate risk is contained and the trend must be reversed. | Concentrate on the few actions that restore reliable delivery; do not widen scope. | Improvement sustained for the declared observation period without a guardrail breach. |
| **Stable operation** | Delivery is predictable enough for ordinary work and incremental improvement. | Maintain, document, remove recurring friction and rehearse recovery. | Consistent outcomes, understood variance, fallback and ownership in place. |
| **Growth** | Demand, reach or workload is increasing beyond the current operating baseline. | Add capacity and reach without weakening quality, rights, safety or support. | Capacity, quality and response measures remain healthy across the expanded load. |
| **Resilient operation** | Delivery is reliable, repeatable and not dependent on one fragile path or person. | Preserve the working pattern, improve selectively and prepare continuity. | Recovery and handover evidence, documented ownership and repeated useful outcomes. |
| **Handover** | Responsibility, ownership or operating context is changing. | Transfer context, obligations, access, evidence and recovery paths deliberately. | The receiving role accepts the scope and can operate or restore it independently. |

The first six operational states describe a common path for a service. Handover
can occur from any state, but its acceptance record must say which unresolved
risks and obligations travel with it.

## State gates

A state gate is not a score. It is a reviewable claim with its supporting
material.

```text
observation
  -> assessment
  -> proposed operating state
  -> response plan
  -> evidence collection
  -> authorized review
  -> recorded transition or continued state
```

Every gate records:

- the scope and its current state;
- the date, assessor, owner and review deadline;
- the outcome at stake;
- relevant observations, source objects and evidence references;
- indicator definitions, time window and data-quality limits;
- risks, counter-signals and unresolved questions;
- permitted response actions and actions deliberately deferred;
- exit criteria for the next state; and
- the accepting actor, or the reason a transition remains open.

An agent may prepare the assessment and evidence pack within its mandate. It may
not silently assign a state, redefine the exit criteria, or approve a transition
that requires another actor's authority.

## Statistics and indicators

Statistics are evidence for a state assessment, not a verdict about a person or
a reason to optimize one number at the expense of the organization.

Each operating state uses three kinds of signal:

| Signal | Question answered | Example for a call-handling service |
| --- | --- | --- |
| **Outcome signal** | Is a useful result occurring? | A caller reaches an appropriate response or a verified follow-up. |
| **Quality and safety guardrail** | Is the result causing unacceptable harm or degradation? | Incorrect customer record, consent error, missed urgent escalation, privacy breach. |
| **Capacity or flow signal** | Can the service keep delivering under actual load? | Queue age, response delay, abandoned calls, unresolved follow-ups. |

A transition requires an explicitly declared observation window and enough
context to interpret the numbers. A growing count can be good or bad; for
example, more calls may mean healthy demand, a product defect or an emergency.
A person can challenge a measurement, its meaning or the proposed state.

## How Helm helps

Helm is the conversational surface for this method. It should be able to answer,
within the caller's permissions:

- “What state is this service in, and what evidence supports that?”
- “What must be true before we expand it?”
- “Which indicators disagree with the proposed transition?”
- “Show the actions that are appropriate now and the actions we have deferred.”
- “Who is responsible for the next review?”
- “What changed since the last assessment?”

Helm may also propose a concise next-action plan, open the underlying objects,
request missing observations and schedule a review. It must distinguish source
facts, its interpretation, a hypothesis and a requested decision.

## Runtime model

The Runtime is the source of truth for state assessments. A conceptual record
contains at least:

```text
OperationalStateAssessment
  scopeId
  state
  assessedAt
  assessedBy
  outcomeRef
  evidenceRefs[]
  indicatorSnapshots[]
  dataQualityNotes[]
  risksAndCounterSignals[]
  responsePlanRef
  exitCriteria[]
  reviewDueAt
  proposedNextState
  acceptedBy
  acceptedAt
  transitionDecisionRef
```

The Workspace displays only the scopes and evidence a person is authorized to
see. It must show uncertainty and missing proof rather than presenting an
optimistic state as settled fact.

## Example: establishing a new business communication service

A new communication service begins in **Establishing**, not Growth. Its first
work is to make the service real and inspectable:

1. describe the useful result for callers and the organization;
2. assign a responsible role and escalation route;
3. define the first target audience and how they discover or reach the service;
4. create a two-way feedback path for callers and the operating team;
5. instrument outcome, quality and capacity signals; and
6. record the first real use, its outcome and what failed or remained uncertain.

Only after this evidence exists can the organization assess whether it is in
Recovery, Stable operation or needs another Establishing iteration. Promotion,
higher call volume or broader automation are not substitutes for this proof.

## Guardrails

- No state is a judgment of a person's worth, loyalty, competence or intent.
- No agent may punish, restrict, expose or rank a person because of an inferred
  state.
- A state change does not create permissions, alter roles or bypass a mandate.
- Emergency protection may be authorized by an existing safety policy; it does
  not authorize unrelated expansion or permanent changes.
- The model remains open to revision when evidence shows its categories or
  thresholds are unhelpful.

## Relationship to existing SHAPER contracts

This target method extends, but does not replace:

- [Agnostic Method Translation](../00-META/07_AGNOSTIC_METHOD_TRANSLATION.md),
  which supplies the outcome-to-evidence alignment stack;
- [Validation and Acceptance Protocol](11_VALIDATION_AND_ACCEPTANCE_PROTOCOL.md),
  which governs evidence for delivered capabilities; and
- [Direction, Decisions and Mandates](15_DIRECTION_DECISIONS_AND_MANDATES.md),
  which governs authority for decisions and action.
