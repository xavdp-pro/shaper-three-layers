# Future Business Owner and Tester Journey

## Purpose

The demonstration is not a feature catalogue. It guides a person from familiar work to evidence-based organizational steering. The future owner asks whether Shaper makes the company more visible and governable; the tester verifies that each promise has objects, authority, events, evidence, failure behavior and recovery.

## Entry into the demo universe

1. The visitor discovers the promise on the Shaper site.
2. Email registration and a magic link or bounded token open a private demo space.
3. A personal demo Universe or Cell is provisioned from a known, versioned template.
4. The visitor enters a believable office-furniture company containing fictional historical activity.
5. Helm offers a guided tour while manual exploration remains possible.

The demo may simulate mail, documents, customers, suppliers, decisions and telephony. Every simulation needs an explicit production connector boundary; demo assumptions never silently become production assumptions.

## Progressive experience

### E0 — Familiar manual work
Browse customers, products, stock, tasks, documents, emails, quotes and orders without an agent. Core work must remain available when an agent provider is down.

### E1 — Ask Helm
Ask what changed, which product produced the highest margin, where the supplier update is, or which source documents support an answer. Context, provenance and uncertainty remain visible.

### E2 — Delegate once
Prepare a quote, ingest a receipt, create a task, prepare an invoice from an email, or create dated supplier prices without erasing history. Show resolved objects, planned action, authority, preview, result and evidence.

### E3 — Pilot
Ask what deserves attention, what is improving or deteriorating, where responsibility is unclear, and which repeated work could become assisted. Helm separates observations, hypotheses, recommendations and decisions.

### E4 — Establish a standing mandate
A stable repeated process can become automatic only with scope, owner, exception rules, notifications, STOP conditions and review conditions. Helm must later explain why it ran without asking.

### E5 — Shape the environment
An authorized Steward may ask Helm to add a bounded Workspace projection. Helm clarifies; Runtime checks authority; Governor coordinates; Maker materializes in DEV/TEST; tests and a counter-view run; Workspace updates; rollback and provenance remain available.

These six experiences are also the six **pilot levels**. The next section is how a person proves each one.

## Pilot training: proving each level

**Status: target.** Nothing below is implemented. The engineering canon records the gap.

### Purpose

A person learns to steer by steering. Pilot training lets them practise every level in a formal demo universe, where breaking things costs nothing, before Helm executes that level for them in a production universe. It also makes sure they can name what they steer: a pilot who cannot name an object, a mandate or a jurisdiction cannot yet be trusted to change one.

### Where it runs

- **A `demo` instance only.** It is stamped from a versioned training rig and populated with the fictional company of this journey. It is never production, and a robot may end it.
- **No production connector.** Mail, documents and telephony are simulated, as the demo already requires.
- **Breakage is part of the game.** The pilot may break the instance. It is reset by reaping and stamping it again, at any moment.
- **One thing leaves the instance.** The validation record is kept with the person's account, which outlives the instance.

### Missions

Helm proposes the missions of a level one by one. Each mission contains:

1. **A situation.** A believable event in the fictional company.
2. **The words.** The pilot names the objects, roles and authority involved, in their own words. This is the *Words* check of the [pedagogical model](../00-META/01_PEDAGOGICAL_MODEL.md).
3. **The action of the level.** The pilot performs it through Helm.
4. **A planted difficulty.** For example a wrong object, an ambiguous request, a STOP to issue or a change to roll back.
5. **The evidence.** The pilot reads back what happened and why.

Helm guides, explains and hints. It never performs the mission in the pilot's place.

### What validates each level

| Level | What the pilot practises | What validates it |
| --- | --- | --- |
| E0 — Familiar work | Finding customers, orders and documents without an agent | Finding them, and saying where the truth of each lives |
| E1 — Ask Helm | Asking, demanding sources, noticing uncertainty | Telling a sourced answer from an inference |
| E2 — Delegate once | Having Helm prepare a quote or a task, reading the preview | Catching a planted wrong object before approving |
| E3 — Pilot | Reading attention signals and tensions | Recording a decision with its reason, apart from observations and hypotheses |
| E4 — Standing mandate | Defining scope, owner, exceptions, STOP and review | A mandate that stops correctly on a planted exception |
| E5 — Shape the environment | Adding, configuring or removing a feature the class offers | A change taken through tests and counter-view, applied, then rolled back cleanly |

A level is **observed, never declared**. It is validated only by the instance's own events and by the pilot's correct naming, never by a self-assessment or by Helm's opinion.

### The record and its use

- **The record.** For each person and each class: the levels validated, when, on which training rig version, with references to the evidence. A level proven on a Vox universe says nothing about a Workspace universe.
- **In production.** Helm reads the record. For an action above the validated level, it prepares the request and routes it to a pilot validated at that level, or offers the missing training.
- **Validity.** A level stays valid until the training rig changes what the level means. Helm then offers the new missions.
- **Authority stays separate.** A validated level grants no power. A person at E5 without a jurisdiction root or a shaping mandate shapes nothing.

### Who writes the missions

The maker tandem writes them. Generic missions come with the base. Each class adds the missions of its own domain: a Vox class, for example, would train changing a welcome message, routing a caller and handling a voicemail.

### Not a score

Pilot training follows the [steering guide](02_HUMAN_FROM_DOING_TO_STEERING.md#pedagogical-maturity): a map of capabilities the person has learned to use. It has no points, no ranking between people and no badge that outlives its meaning.

### Public gradient

The website may group the six levels into four steps: **see and learn** (E0–E1), **prepare and propose** (E2–E3), **act within a mandate** (E4), **shape your system** (E5).

## Tester viewpoints

- Business reality: believable roles, prices, margins, history, communications and exceptions.
- Human factors: vocabulary, next action, accessibility, explanation, STOP and recovery from confusion.
- Runtime: objects, relations, capabilities, permissions, mandates, causality, idempotency, concurrency and state machines.
- Adversarial: injection, wrong-object resolution, tenant leakage, stale authority, repeated side effects, schema abuse, provider drift and failed sensors.
- Steward: trust degradation, escalation, quarantine, rollback, rebuild and Universe restoration.

## Demonstration success

> I understand what happened, why it happened, who or what was allowed to do it, what evidence exists, what I can stop or change, and how the system would behave if the same process became routine.

A visual effect without this chain is not accepted as a Shaper capability.
