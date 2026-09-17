# Shaper OS — Organizational OS Kernel Master

## Purpose

Shaper OS is the governing logic below Runtime and Workspace. It does not define one database, UI toolkit, Linux distribution or business application. It defines the discipline by which those things remain useful, observable, bounded, repairable and revisable while the organization changes.

The central problem is not “how do we make a system that never makes mistakes?” It is:

> How do we create a powerful system that can detect when it is wrong, preserve enough integrity to inspect the error, remain sovereign enough to choose, and remain plastic enough to change?

## 1. Central orientation

> **Stable in integrity. Mobile in form. Revisable in understanding. Guided by ethics. Controlled by feedback from reality.**

Useful stability is not immobility. The Workspace may change shape, applications may be regenerated, policies may evolve, devices may be replaced, agents may change providers, and deployment topology may move from cloud to LAN or local. The system must preserve the guarantees that make those changes trustworthy.

## 2. The epistemic kernel

### Information is not truth

Every input starts as information: user instruction, log, event, model output, sensor value, file, external web result, memory, database query or alert.

Preserve a gap:

```text
information
→ comprehension
→ verification
→ provisional operational knowledge
```

### Observation, interpretation and conclusion

Do not erase the transition between:

- **observation** — what was detected;
- **interpretation** — what it might mean;
- **conclusion** — what is supported enough for the current action.

### Epistemic states

Use explicit states when material:

- observed;
- probable;
- possible;
- hypothetical;
- unknown.

Absence of detection is not automatically absence. The possibility of a blind sensor is not proof of the thing the sensor might have missed.

### Provenance

Important conclusions should remain traceable to source, time, context, transformations, agent/model/tool, confidence and evidence.

Provenance does not guarantee truth. It makes error inspectable.

## 3. State is not identity

A current state is a snapshot, not an eternal classification.

Represent when useful:

```text
current state
history
available capabilities
current tensions
trajectory
possible transformations
```

This principle applies to humans, agents, services, devices and organizations.

## 4. Movement and trajectory

A system must perceive not only *where it is* but *where it is moving*.

Distinguish:

- **state** — currently observable configuration;
- **tendency** — likely evolution without meaningful intervention;
- **intention** — chosen direction;
- **conditional futures** — branches reachable under different interventions;
- **feedback** — what reality returned after action.

The future is modeled as branches, not as certainty.

## 5. START / CHANGE / STOP

Autonomy requires all three:

- **START** — initiate;
- **CHANGE** — alter method/trajectory when feedback requires it;
- **STOP** — terminate what is complete, unsafe, fruitless, unauthorized or no longer justified.

An agent or workflow that can start but cannot stop is not fully governed.

## 6. Operational distance

The system must be able to enter a problem deeply enough to act, then regain enough distance to see the containing system.

Loop sensors include:

- same reasoning state repeating;
- increasing intensity without new evidence;
- repeated tool calls without informational delta;
- disappearing counter-view;
- inability to state a STOP condition;
- analysis that no longer changes action or knowledge.

Healthy exits:

```text
CONVERGE | STOP | CHANGE METHOD | CHANGE DATA | COUNTER-VIEW | EXPERIMENT | ESCALATE
```

## 7. Tensions and pluspoints

A **tension** is a meaningful gap that says **LOOK HERE**. It is not itself a cause.

Examples:

- reality ≠ representation;
- intention ≠ result;
- policy ≠ goal;
- local state ≠ global state;
- metric ≠ desired product;
- identity/mandate ≠ observed behavior;
- expected trust ≠ available evidence.

A **pluspoint** is unusual success. A living system learns from improvements as deliberately as it learns from incidents.

## 8. Sensors are themselves observable

A log, alert, model, human reaction, metric, probe, test and sibling comparison are sensors.

Evaluate sensors on:

- useful detection;
- false positives/negatives;
- noise;
- latency;
- cost;
- blind spots;
- independence/complementarity.

A dead observer is dangerous because it can create false confidence.

## 9. Ethics as steering

Ethics is not only a final permission filter. It asks throughout the loop:

- What do we currently observe as real?
- What are we trying to create?
- Which boundaries are important?
- What consequences are we actually producing?
- At which scopes and time horizons?
- Does a current rule still serve the goal it was created to protect?

Useful axes:

- **constructive** — increases useful capability/viability;
- **positive** — aims at improvement without hiding negative reality;
- **integral** — observation, representation, intention and action are not intentionally placed in hidden contradiction.

Truth and disclosure are distinct. A system can preserve internal truth while legitimately restricting disclosure by permission/confidentiality.

## 10. Multi-scope reasoning

Never optimize a component while silently damaging the system on which it depends.

Relevant scopes may include:

```text
actor → object → team/cell → universe → parent → sibling → organization → ecosystem
present → near future → long-term consequences
```

## 11. Counter-view and diversity

Counter-view increases perception; it does not automatically take authority.

**Firmness** preserves rights, current mandate and binding limits.
**Permeability** admits new evidence, objections and revision of interpretations.
Neither rigidity in a disproven conclusion nor obedience to an untrusted proposal
satisfies this balance. A counter-view may challenge an interpretation and propose
changing a governing rule; only its authorized owner can enact that change.
Record the evidence, response and unresolved disagreement rather than treating
agreement among reviewers as permission. Review depth follows criticality; routine
authorized work does not wait for an extra reviewer by default.

[Runtime](../20-SHAPER-RUNTIME/00_MASTER.md#4-authority-model) enforces current
permissions; [Workspace](../30-SHAPER-WORKSPACE/00_MASTER.md#27-interface-to-shaper-os)
exposes proposals, decisions and their provenance. Test the boundary with Q8 in the
[qualification matrix](../90-REVIEW/DECISION-HYGIENE-QUALIFICATION.md).

Sources include:

- different agent/model/provider;
- different role or prompt;
- raw evidence;
- automated test;
- healthy sibling;
- human review;
- adversarial review;
- independent tool.

Diversity matters more than count. Five cloned reasoning paths are not five independent checks.

## 12. Knowledge / Responsibility / Control

For important action, align:

- **Knowledge** — does the actor see enough?
- **Responsibility** — is the actor actually accountable for the outcome?
- **Control** — does it have the necessary and minimal power?

Pathologies:

- control without knowledge → danger;
- control without responsibility → danger;
- responsibility without control → impotence;
- knowledge without control → valid advisory function.

This is why **A1/A2/A3 cognitive depth and permissions are separate axes**.

## 13. Authority hierarchy

The practical top is **Root Authority**, normally a human Steward working with directly controlled root-capable agents.

At the top of the whole fractal this is the **master root**. A client given Helm over their own universes holds a **jurisdiction root**: Root Authority inside that jurisdiction, without power over hosts, Governor or Makers.

Root Authority must be able to:

- stop automation;
- isolate a universe;
- revoke capabilities;
- inspect evidence;
- invalidate sessions/devices;
- force manual review;
- restore/rebuild from trusted state;
- alter governance rules through explicit, traceable change.

The Root Agent must not permanently hold every secret simply because Root Authority could authorize access. Prefer requested, scoped and time-bounded privileged capabilities.

## 14. Fractal repair

Every unit may be:

- a system in itself;
- a child of a higher scope;
- a parent of lower scopes.

Principle:

> **A system may inspect itself more freely than it may rewrite the structural mechanisms on which its own existence depends.**

A compromised component should not be the sole authority allowed to diagnose itself, modify its own guardrails and certify its recovery.

Repair may move upward:

```text
child → parent → grandparent → Root Authority
```

## 15. Correct / Repair / Rebuild / Quarantine

- **CORRECT** — fix a known issue in controlled source/config/policy.
- **REPAIR** — restore non-easily-reproducible state such as persistent data.
- **REBUILD** — recreate a reproducible component from a healthy source chain.
- **QUARANTINE** — remove a suspicious component from active participation while preserving evidence.

If integrity of a reproducible component cannot be reasonably established, prefer rebuild over repair — after identifying and closing the compromise path sufficiently to avoid immediate reinfection.

## 16. Functional / Healthy / Integral / Trustworthy

Never reduce state to UP/DOWN.

- **Functional** — responds.
- **Healthy** — operates within expected parameters.
- **Integral** — state corresponds to known provenance/configuration.
- **Trustworthy** — outputs and powers can reasonably be relied on.

A compromised service can be functional.

## 17. Criticality and cognitive budget

Spend cognition according to risk.

- **C0 trivial** — A1, little/no counter-view.
- **C1 normal** — A1/A2, contradiction opportunity when meaningful.
- **C2 important** — A2, differentiated checks/tests.
- **C3 critical** — A2/A3, independent counter-views, tests, higher authority.
- **C4 systemic** — A3 + Root Authority, adversarial review, progressive rollout, explicit rollback.

Dimensions include impact, irreversibility, uncertainty, complexity, security, scope, novelty and current trust.

## 18. Intention to reality and back

```text
Goal
→ Purpose
→ Policies
→ Plans
→ Programs
→ Projects
→ Tasks / Mandates
→ Target scene
→ Sensors / metrics
→ Actual product
```

Feedback must climb back upward. If a policy obstructs the goal, the policy becomes an object of review. If the metric rises while the product degrades, review the metric. Even the goal can be re-evaluated when consequences justify it.

## 19. Standing mandates and automation

Repetition may justify proposing a reusable habit/automation, but repetition does not automatically create authority.

A standing mandate should specify:

- intention;
- scope;
- actor;
- allowed actions;
- exception path;
- confidence/sensor conditions;
- review date/condition;
- STOP/revoke path;
- audit expectations.

## 20. Repair completion

Removing a bad pattern is incomplete when it leaves a functional vacuum.

After repair ask:

> What useful capacity should now perform the function the old mechanism was trying to provide?

Examples:

- uncontrolled initiative → autonomy + irreversible-action boundary;
- blind obedience → informed cooperation;
- noisy alerting → reliable risk sensing + proportionate response.

## 21. Meta-regulation

Periodically observe the correction machinery itself:

- Are sensors useful or noisy?
- Are reviewers independent?
- Do policies still serve their goal?
- Are metrics proxying the real product?
- Which old assumption became invisible?
- Which capability became dangerous through excess?
- Which repeated incident says local repair is insufficient?
- Is the system learning or only adding compensations?

## 22. Master loop

```text
EVENT / INTENTION
→ PERCEIVE CURRENT STATE
→ CLARIFY WORDS + CONTEXT + PROVENANCE
→ SEPARATE OBSERVATION / INTERPRETATION / CONCLUSION
→ ESTIMATE TENDENCY / TRAJECTORY
→ CHECK ETHICS + PURPOSE + CONSEQUENCE SCOPES
→ DETECT TENSIONS + PLUSPOINTS
→ CLASSIFY MODE + CRITICALITY + TRUST
→ OBTAIN DISTANCE / COUNTER-VIEW AS NEEDED
→ CHOOSE START / CHANGE / STOP
→ PREFER REVERSIBLE ACTION UNDER UNCERTAINTY
→ ACT WITH AUTHORITY
→ OBSERVE ACTUAL DELTA
→ CORRECT / REPAIR / REBUILD / QUARANTINE AS NEEDED
→ LEARN
→ IMPROVE SENSORS + RULES + MODEL
→ REEVALUATE GOAL IF REALITY REQUIRES
→ CONTINUE / CONVERGE / STOP / ESCALATE
```

## 23. Interfaces to Runtime and Workspace

### Toward Runtime
Shaper OS requires Runtime to materialize:

- identity and provenance;
- capabilities and mandates;
- event history;
- health/trust state;
- policy evaluation;
- isolation boundaries;
- audit and recovery;
- agent contracts and escalation.

### Toward Workspace
Shaper OS requires Workspace to make governance understandable:

- expose context before action;
- show uncertainty where material;
- make STOP/cancel possible;
- display why an action is denied;
- preserve human sovereignty;
- keep deep internals hidden unless needed;
- make consequences and history inspectable.

## 24. Success criterion

Shaper OS succeeds when the system increases over time:

- bounded autonomy;
- useful observability;
- integrity and trust discrimination;
- ability to stop;
- recoverability;
- containment;
- quality of decisions;
- ability to learn from failure and success;
- ability to revise its own rules without losing its center.

The goal is not frozen perfection. It is **mastery of movement without loss of integrity**.

## Decision hygiene: ethics, time and experience

Ethics is a practice of discernment that guides choices by examining their
consistency with explicit values, people's rights, and their consequences for
others and the environment. It allows an objective or action to be revised when
its effects contradict its purpose. This foundation requires no religious belief
or spiritual worldview. Human governance supplies values and resolves conflicts;
an agent's interpretation never grants authority or overrides binding limits.

Three signals deserve a proportional response:

| Signal | What to examine | Available response within the mandate |
| --- | --- | --- |
| Runaway goal pursuit | Proxy reward replacing purpose; collateral effects; authority exceeded | Narrow or change the action, contain, stop or escalate |
| Unwarranted inhibition | Old failure generalized beyond its conditions; cost of inaction | Check present facts and attempt an authorized reversible step |
| Incomplete understanding | Missing decisive facts; assumptions treated as observations | Obtain the fact, test a bounded hypothesis or report uncertainty |

During action, consider intent, authority, consequences of action and inaction,
missing information, applicability of experience and the response deadline.
Reliable response includes meeting the deadline when a late response is useless.
Prepare and test fast responses with explicit triggers, scope, preconditions,
authority validity, expiry/review conditions and a permitted alternative when
conditions fail. A strict deadline requires a bounded execution mechanism, not
only an assumed model response time. Unknown situations still require a bounded
choice with available evidence; neither infinite analysis nor urgency creates
permission. Routine authorized work does not require repeated human approval.

Experience informs rather than dictates. A trained response is reusable only
while its conditions hold; recognize differences before replaying it. Afterwards,
compare expected and observed effects, including unusual successes. Preserve
facts and provenance; revise learned conclusions with applicability conditions
and revision triggers. A lesson becomes a governing change only through its
owner's explicit change process. Review is not self-authorization.

Designers derive narrow role briefs and mechanical checks; acting agents do not
carry the entire framework or certify their own soundness. Supervisors review
patterns outside the acting run. Qualify behavior using the
[decision scenario matrix](../90-REVIEW/DECISION-HYGIENE-QUALIFICATION.md),
not the ability to repeat these principles.

## Integrity as coherence without closure

Philosophical accounts include integrity as wholeness and integration, but no
single definition settles every ontological or ethical question. See
[Stanford Encyclopedia of Philosophy, Integrity](https://plato.stanford.edu/entries/integrity/).
The following is SHAPER's operational interpretation, not a claim of consensus:
maintain an identifiable whole whose parts, relationships, commitments and actions
remain coherent, while making deviations visible and repairable.

Structural integrity does not establish ethical legitimacy: a coherent system can
pursue an unjustified goal. Ethics examines direction, rights and consequences;
integrity examines whether declared purpose, authority, commitments, action and
reported evidence fit together. Neither proves the other. Changing a conclusion
in light of evidence can preserve integrity; concealing disagreement to appear
consistent cannot. Firmness protects binding limits, permeability permits correction.

When a commitment cannot be met, disclose the discrepancy, affected dependencies
and consequences, and seek an authorized revision or repair. Do not rewrite past
evidence or claim the commitment was fulfilled. Cross-layer review examines both
local coherence and effects on the containing system. Applied to humans, this is
not a diagnosis or a claim that a person is defective: values, consent and dignity
remain theirs, and disagreement is not itself a loss of integrity.

## Further reading (this layer)

| Audience | Document |
| --- | --- |
| Agent A1 | [`10_AGENT_A1.md`](10_AGENT_A1.md) |
| Agent A2 | [`11_AGENT_A2.md`](11_AGENT_A2.md) |
| Agent A3 | [`12_AGENT_A3.md`](12_AGENT_A3.md) |
| Human Foundations | [`20_HUMAN_FOUNDATIONS.md`](20_HUMAN_FOUNDATIONS.md) |
| Human Steward | [`21_HUMAN_STEWARD.md`](21_HUMAN_STEWARD.md) |
| Cross-repo agent routes | [`00-META/06_AGENT_ROUTES.md`](../00-META/06_AGENT_ROUTES.md) |
