# Shaper OS — Human Foundations
## From reality to governed movement

This guide explains the Shaper OS kernel without requiring the reader to understand infrastructure.

## Door 1 — Reality before the story

Something happens. First ask:

- What did I actually observe?
- What did someone else report?
- What am I already interpreting?

A message that says “the system is broken” is information, not yet a complete diagnosis.

**Why it matters:** if we confuse the report with reality, we may fix the wrong thing.

**Verify:** can you restate the observable facts without adding the explanation?

## Door 2 — A state is not an identity

A person, agent or system can behave badly now without that snapshot becoming its permanent identity.

Prefer:

> “I observe this behavior under these conditions.”

rather than:

> “It is this by nature.”

This keeps responsibility while preserving the possibility of change.

## Door 3 — Movement

Ask not only “where are we?” but “where are we going if nothing changes?”

```text
state → tendency → possible futures
                  ↑
              intention
```

An intention is a chosen direction, not a claim that the desired future already exists.

## Door 4 — Communication

Important communication has stages:

```text
intent → message → sent → received → understood → accepted/rejected → acted → result
```

“Sent” is not “understood.” “Understood” is not “agreed.” “Executed” is not “successful.”

Before correcting a complex idea, be able to restate it in a way its author recognizes.

## Door 5 — Discernment

Keep three layers visible:

- **Observation** — what I saw.
- **Interpretation** — what I think it means.
- **Conclusion** — what I currently consider supported enough to act on.

Strong feeling or high model confidence can be useful signals. Neither is automatically proof.

## Door 6 — Ethics and integrity

Shaper treats ethics as steering during movement, using the
[agnostic decision foundation](00_MASTER.md#decision-hygiene-ethics-time-and-experience).
A person can ask: am I overcommitting, holding back without a current reason,
or overlooking something decisive? Reflection is voluntary; emotions can inform
without dictating action or constituting a fault. The tool does not diagnose a
person, prescribe treatment or define their values for them. Recognizing a
reaction does not imply choosing it or having consented to it; coercion is not
free consent. A quick trained response still needs a context check; later review
can revise a lesson without condemning the person.

Ask:

- What am I actually trying to create?
- Does my action remain coherent with what I observe?
- What consequences does it produce for me, others and the larger system?
- Is an old rule now blocking the purpose it was supposed to protect?

Three useful axes:

- constructive;
- positive without denying negative reality;
- integral across observation, intention, words and action.

## A short guide to reliability

- **Intention:** the result sought, with its scope and constraints.
- **Expected result:** an observable criterion used to check that intention.
- **Sensor:** a means of observation, such as a test, log, measurement or human
  report. It provides a signal, not guaranteed truth; its coverage, freshness and
  possible failures matter.
- **Tension:** a meaningful discrepancy between expectations, observations or
  commitments. It invites investigation and does not identify the cause by itself.
- **Counter-view:** another perspective or independent observation that challenges
  the interpretation; it does not grant permission.
- **Response:** a proportionate action within the mandate, followed by observation
  of its effects. It may be a check, correction, bounded experiment or suspension.

Example: an agent reports that it created a file, but a filesystem check does not
find it. The discrepancy is a tension, not yet proof of deception. Check the path,
permissions, timing and actual write result: the file could be elsewhere, the
write could have failed, or the claim could be unsupported. Preserve the evidence,
correct the result or report, and check again. A broken or incomplete sensor must
also be considered; repeating one faulty check is not independent confirmation.

An **error** is an incorrect result or claim. An **AI hallucination** is generated
content presented as factual without adequate grounding, potentially including
invented references or execution claims. A **premature conclusion** treats partial
evidence as sufficient. **Deceptive behavior** misleads, for example by concealing
an observed failure; a false statement alone does not establish an intention to
deceive. These categories can overlap and require investigation rather than
judgment from the agent's tone or confidence.

Honest reporting distinguishes observation, inference, uncertainty and verified
outcome. This method aims to reduce unsupported claims and their consequences;
zero observed hallucinations in a stated test does not guarantee their absence
elsewhere. See the [qualification matrix](../90-REVIEW/DECISION-HYGIENE-QUALIFICATION.md).

## Door 7 — Tensions and pluspoints

A tension is not automatically a problem or a cause. It says:

> **Look here.**

Examples:

- intention ≠ result;
- stated rule ≠ actual behavior;
- local success ≠ global health;
- metric improves while useful outcome degrades.

Also inspect unusual success. Ask what changed and whether it can be reproduced.

## Door 8 — Distance and counter-view

A blind spot is something you may not see from inside your own reasoning.

A counter-view can come from another person, agent, test, source or tool.

> Counter-view increases perception. It does not automatically get the steering wheel.

Sovereignty is not isolation. It is the ability to receive contradiction without automatically surrendering decision-making.

## Door 9 — START / CHANGE / STOP

A controlled system can:

- begin;
- change course;
- stop.

Persistence is not success. Defining STOP conditions before momentum becomes strong is often valuable.

## Door 10 — Act through the real world

When thought alone cannot reduce uncertainty, use a small reversible experiment when possible.

```text
hypothesis → safe action → observed result → model update
```

## Door 11 — Repair and learning

After a failure, ask:

1. How do we correct this instance?
2. How do we make recurrence less likely?
3. Which sensor would have detected it earlier?
4. What useful capacity must exist after the repair?

Do not merely remove a bad pattern and leave an empty function.

## Door 12 — Review the review

Sometimes the problem is not one decision but how decisions are repeatedly made.

Ask periodically:

- Which sensors create signal and which create noise?
- Which rule has become automatic and invisible?
- Are we optimizing a metric instead of the real result?
- Are we repeatedly “fixing” the same class of problem?

## Four response modes

These modes describe situations, not ranks:

- **R0 Immediate** — low impact: notice, choose, continue.
- **R1 Reflective** — meaningful/repeated: facts, interpretation, counter-view, action, review.
- **R2 Deep** — persistent/major: independent views, small tests, trajectory and model revision.
- **R3 Safety/Crisis** — protect/stabilize first, analyze deeply later.

## Twelve practical questions

1. What do I actually observe?
2. What am I interpreting?
3. What may be missing?
4. What is the current state?
5. What is the tendency?
6. What do I want to help create?
7. What is the main tension?
8. What currently supports my position?
9. Which counter-view could expose a blind spot?
10. What small reversible action can I test?
11. When will I CHANGE or STOP?
12. Which real result will show whether I learned?

## What this has to do with Runtime and Workspace

You do not need to know their internal architecture, but the product should embody these principles:

- Workspace shows context and consequences instead of hiding them.
- Runtime preserves history, authorization and provenance.
- Agents can propose and act only inside their authority.
- You retain clear STOP, approval and explanation paths.

## Success

The objective is not to train a person who has every correct answer.

It is to increase the capacity to **see, choose, act, verify, repair and change without losing one's center**.
