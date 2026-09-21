# Enterprise Piloting Model

> **Status:** target product and operating model. It describes the intended
> enterprise-piloting loop, not a delivered dashboard, autonomous agent or
> complete business-management product.

## The product idea

A SHAPER Enterprise universe gives an authorized business owner a way to pilot
an organization as a living system.

It does not reduce the company to a dashboard, a score or a set of agent
commands. It keeps the owner connected to the organization’s intended outcomes,
current facts, risks, work, people, customers and learning. Helm turns ordinary
questions into navigable, permission-checked objects, evidence and possible next
actions.

The useful question is not “What should the system optimize?” It is:

> What is true now, what matters most, what may we do, and what would show that
> the organization is moving in the right direction?

## The owner’s recurring pilot loop

```text
orientation
  -> observe
  -> assess operating state
  -> choose the limiting tension or opportunity
  -> prepare a bounded response
  -> authorize and act
  -> observe consequences
  -> learn, repair or scale
```

Each turn of the loop is linked to real records. A conclusion must distinguish
fact, interpretation, hypothesis, proposal, decision, execution and evidence.

## What a pilot should be able to understand

For their authorized Organization or Cell, the owner can ask Helm:

| Pilot question | Required answer shape |
| --- | --- |
| What are we trying to make real? | Current outcome, purpose, decisions and scope. |
| Where are we now? | Operating-state assessment with its date, evidence, uncertainty and review owner. |
| What deserves attention first? | Tensions and pluspoints, ranked by impact and confidence, never hidden as facts. |
| What is preventing progress? | Dependencies, bottlenecks, risks, missing decisions, blocked work or insufficient capacity. |
| What can we do now? | Permitted actions, proposed plans, required approvals and deferred actions. |
| What would prove progress? | Outcome, quality/safety and capacity signals with time window and data limits. |
| What changed? | Linked events, decisions, executions, external effects and observed results. |
| What did we learn? | Review record, corrected assumptions, reusable pattern and unresolved question. |

The answer is not a generic AI summary. It is a permission-filtered explanation
with links to the objects, evidence and authority it relies on.

## The pilotage substrate

The product needs a connected operational graph, not parallel reports that lose
their relation to the work.

| Concern | Runtime truth | Workspace and Helm use |
| --- | --- | --- |
| Orientation | Outcomes, purposes, decisions, policies and review dates | Explain why work exists and what is currently prioritized. |
| Organization | People, teams, roles, delegated responsibility and availability | Identify who owns a decision or can take the next step. |
| Work | Programmes, projects, tasks, dependencies, capacity and calendar commitments | Show progress, blockage, sequence and the next useful action. |
| Relationships | Customers, suppliers, partners, communications and shared history | Connect a business signal to the people and commitments it affects. |
| Operations | Services, workflows, automations, incidents, recovery and delivery events | Show whether ordinary work is safe, stable or under pressure. |
| Evidence | Sources, measurements, artifacts, external receipts and reviews | Let a person challenge or verify a conclusion. |
| Authority | Roles, permissions, mandates, decisions, limits and revocations | Prevent an answer or suggestion from becoming an unapproved action. |
| Learning | Reviews, corrections, recurring tensions and reusable patterns | Preserve what reality taught the organization. |

## State-aware response

[Operational State Piloting](16_OPERATIONAL_STATE_PILOTING.md) supplies the
response discipline. Helm should not propose the same intervention everywhere.

- In **Unknown**, it helps establish facts and limits claims.
- In **Establishing**, it helps make the first useful exchange and feedback loop
  real.
- In **Incident**, it emphasizes protection, containment, communication and
  recovery over feature work or growth.
- In **Recovery**, it focuses attention on the few actions that restore a healthy
  trend.
- In **Stable operation**, it supports incremental improvement and rehearsed
  recovery.
- In **Growth**, it tests whether capacity expands without degrading quality,
  safety, people or service.
- In **Resilient operation**, it protects the successful pattern and prepares
  continuity.
- In **Handover**, it makes obligations, access, evidence and recovery paths
  transferable.

The operating state is a reviewable model of a scope. It is not a label applied
to a person, a team’s worth or a customer’s value.

## Indicators that help rather than control blindly

A pilot view must combine:

1. **Outcome indicators** — whether something useful reaches a real person or
   business process.
2. **Quality and safety guardrails** — whether delivery remains correct, lawful,
   safe and respectful.
3. **Flow and capacity indicators** — whether the organization can sustain its
   actual workload.
4. **Learning indicators** — whether recurring failure, delay or confusion is
   being understood and reduced.

A single improving number never closes the question. Indicators must name their
source, calculation, time window, missing data and possible alternative
explanations. The pilot can inspect a trend’s underlying objects rather than
being forced to trust a graph.

## Attention is finite: find the constraint

Most organizations have more visible work than they can improve at once. Helm
should help identify the present constraint: the missing decision, blocked
handoff, overloaded role, weak supplier link, unclear policy, failing service or
unanswered customer need that limits the wider outcome.

This is not an automatic diagnosis. Helm presents the evidence and competing
hypotheses, then helps the authorized owner choose one bounded experiment. Once
the constraint moves, the system reassesses instead of mechanically continuing
an old optimization plan.

## How human and agent work together

| Human role | Helm and specialist agents |
| --- | --- |
| Names the outcome, values, boundaries and acceptable trade-offs | Keep those records linked to work and flag when a proposal conflicts with them. |
| Decides where authority rests and grants mandates | Resolve current authority at action time; prepare but do not self-authorize. |
| Challenges a diagnosis or metric | Show sources, confidence, counter-signals and alternative explanations. |
| Chooses a response to a material tension | Produce scoped options, consequences, prerequisites and rollback/recovery paths. |
| Reviews what happened | Assemble the trace, compare expected and observed result, record learning. |

The agent’s value is not to replace the owner. It is to keep the whole picture
legible while helping turn a decision into bounded, observable work.

## Minimum valuable pilot loop

The first useful implementation is not a complete ERP. It is one Organization
with a small set of connected objects and one end-to-end review loop:

1. record one outcome, its owner, scope and review date;
2. record one related operational state assessment with evidence;
3. connect a small set of outcome, quality and flow indicators to their sources;
4. record one tension or pluspoint and a bounded response proposal;
5. let an authorized owner accept, reject or request changes;
6. create the resulting project or task under the decision and mandate;
7. record the execution and independently observable result;
8. review the outcome against the original assessment; and
9. preserve the decision, evidence, uncertainty and learning for the next loop.

This slice proves the loop’s integrity. More dashboards, agents, automations,
packages and specialized applications may extend it only when they reuse the
same objects, authority and evidence model.

## Verification scenarios

Before calling Enterprise Piloting usable, prove at least that:

- a pilot can ask why a proposed action matters and see the linked outcome;
- a state proposal visibly separates facts, interpretation and missing evidence;
- an agent cannot move a state or execute a material action without the required
  current authority;
- an indicator graph links to its source records and reports missing data;
- a good outcome number alongside a guardrail breach is presented as a tension,
  not a success;
- a failed response produces a review and next-state reassessment rather than
  silently closing the work; and
- a person with reduced permissions cannot infer restricted customers, employee
  data, decisions or measurements from aggregate explanations.

## Related SHAPER contracts

This document connects existing work; it does not replace it:

- [Operational State Piloting](16_OPERATIONAL_STATE_PILOTING.md) defines state
  assessments and evidence gates.
- [Organization, Collaboration and Planning](13_ORGANIZATION_COLLABORATION_AND_PLANNING.md)
  defines shared organization, work and communication objects.
- [Direction, Decisions and Mandates](15_DIRECTION_DECISIONS_AND_MANDATES.md)
  defines who may decide and act.
- [Helm Capability Model](10_HELM_CAPABILITY_MODEL.md) defines the conversational
  control surface and its authority boundary.
- [Validation and Acceptance Protocol](11_VALIDATION_AND_ACCEPTANCE_PROTOCOL.md)
  defines proof for delivered capabilities.
