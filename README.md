# Shaper Organizational OS

Licensed under [CC BY-SA 4.0](LICENSE). See [NOTICE.md](NOTICE.md) and [AUTHORS.md](AUTHORS.md) for ownership, scope, and provenance.

## Understand together, give form, put it to use, learn

The human–AI tandem is the cornerstone. The human contributes intention and
lived context; agents contribute construction, useful initiative and counter-view.
[SHAPER OS V1.15](https://github.com/xavdp-pro/SHAPER-OS-V1.15) carries the common
intentions, laws and construction recipes. This repository projects them into
OS, Runtime and Workspace responsibilities.

Agents start from the task, resolve its source owners and required dependencies,
then construct or adapt the useful realization. New forms remain possible as
people, tools and circumstances evolve.

## Shaper: building reliable collaboration between humans and agents

Reliability means being able to rely on what is done, knowing what remains
uncertain, and correcting course when reality contradicts expectations. It
connects commitments, useful response deadlines, authority boundaries, verified
results and learning from discrepancies.

### Why this helps people work together

The aim is more useful autonomy, fewer misunderstandings and costly mistakes,
and clearer ways to correct them. A shared method makes intentions, limits,
evidence and responsibilities easier to carry between people, agents and projects.

| Relationship | Practical benefit sought |
| --- | --- |
| Human to agent | Express the desired result and scope without prescribing every step; distinguish verified work from assumptions |
| Agent to agent | Share context and independent objections without turning a recommendation into permission |
| Agent to human | Present results, uncertainty and decisions that need the person's judgment |
| Human to human | Discuss facts, commitments and consequences without reducing disagreement to a judgment of the person |

The same method can be reused in another team or universe while adapting its
values, roles and permissions. People retain their choices; agents act within
explicit mandates. Firm limits coexist with openness to evidence and correction.
The tandem evaluates these benefits through actual use and improves the method
from the discrepancies it observes.

See the [decision foundation](10-SHAPER-OS/00_MASTER.md#decision-hygiene-ethics-time-and-experience) and [qualification scenarios](90-REVIEW/DECISION-HYGIENE-QUALIFICATION.md).

## Dedicated architecture and documentation repository

This repository isolates the architecture discussed for a portable, sovereign, agent-native operating environment for organizations.

It is deliberately **not** the general Shaper OS repository, not the SHAPER Enterprise application catalogue, and not a Linux distribution repository. Its purpose is to define the system that lets an organization keep the same work environment, identity, context, applications, agents and governance while the host device may change between Windows, macOS, Linux, mobile, web, or an optional sovereign Shaper Linux host.

## Framework and realization sources

[SHAPER OS V1.15](https://github.com/xavdp-pro/SHAPER-OS-V1.15) owns generic
intentions, laws and construction recipes. The tandem builds or adapts a
realization with its exact implementation owner and companion lab.
[V1.14](https://github.com/xavdp-pro/SHAPER-OS-V1.14) preserves an earlier
implementation lineage and its own build/deployment contracts.

| Question | Read |
| --- | --- |
| Where does an agent start? | [Task routes](00-META/06_AGENT_ROUTES.md) and [instructions](AGENTS.md) |
| Which service and implementation are needed? | [Domain dispatcher](60-SERVICE-ROUTES/README.md) and the selected owner's versioned interfaces |
| How do composition and responsibilities connect? | [Composition/source map](00-META/08_COMPOSITION_AND_SOURCE_MAP.md) and the three masters |
| Who receives credit? | [AUTHORS.md](AUTHORS.md) here and the selected realization's attribution rules |

## The three primary layers

```text
SHAPER OS
living adaptive governance kernel
        ↓ constrains / guides
SHAPER RUNTIME
identity + authority + objects + events + agents + data + security
        ↓ exposes
SHAPER WORKSPACE
human operating environment + surfaces + dynamic applications
        ↓ runs on
HOST OS
Windows | macOS | Linux | mobile | web | optional Shaper Linux
```

**Shaper Linux is transversal and optional.** It is a sovereign host implementation, not a fourth conceptual layer.

## Composition and source owners

[Composition/source map](00-META/08_COMPOSITION_AND_SOURCE_MAP.md) relates
components, generic stem cells, specialized cells/services, logical spaces and
fractal governance to the three responsibilities above. [Class, specialization
and instance](00-META/09_CLASS_SPECIALIZATION_INSTANCE.md) distinguishes reusable
forms from their running identities. A logical space groups services and
jurisdiction independently of physical placement.

Use the [service dispatcher](60-SERVICE-ROUTES/README.md) for domain work,
[ecosystem](https://github.com/xavdp-pro/shaper-ecosystem) for composition ownership,
and [independent glossary](https://github.com/xavdp-pro/shaper-glossary) for terms
and historical aliases. Each product or mental-source project has a distinct
private `-lab` work repository. Public generic intentions/laws connect to private
user realizations through their permitted source registry; VOX implementation
and operational history remain private.

## Central architectural statement

> The host operating system owns hardware abstraction. Shaper owns the organization's operational environment.

The user may replace a Windows laptop with a Mac and recover the same organizational world after installation, device enrollment and authentication. The durable truth belongs to the organization universe, not to one workstation.

## Documentation audiences

Every primary layer is documented at five reasoning depths:

- **A1 — Bounded Executor**: local, explicit, reliable execution.
- **A2 — Operational Reasoner**: diagnosis, hypotheses, tests, bounded adaptation.
- **A3 — Systemic Reasoner**: architecture, governance, multi-scale effects and meta-regulation.
- **Human Foundations**: progressive, example-first understanding without requiring system internals.
- **Human Steward**: deeper operational/system understanding for people who steer or govern the environment.

Agent depth is **not** authority. Human documentation depth is **not** privilege. Permissions are governed separately.

Canonical file names per layer: `10_AGENT_A1.md`, `11_AGENT_A2.md`, `12_AGENT_A3.md` under `10-SHAPER-OS/`, `20-SHAPER-RUNTIME/`, and `30-SHAPER-WORKSPACE/`. See the [agent route table](00-META/06_AGENT_ROUTES.md).

### Three kinds of contribution (do not collapse them)

1. **Delivery and proof** — one shared feature inventory per perimeter ([`90-REVIEW/SCOPE-FEATURE-INVENTORY.md`](90-REVIEW/SCOPE-FEATURE-INVENTORY.md)); agents report against the same feature IDs. Do not create a disconnected checklist per engine.
2. **Cognitive role** — pick the A1, A2, or A3 guide for the owning layer; stay within mandate and escalate across depth or authority boundaries.
3. **Realization credit** — commits, tests and attribution follow the selected implementation owner; documentation credit lives in [`AUTHORS.md`](AUTHORS.md) and each source repository.

## Documentation method

Every important concept should be teachable through:

1. **Words** — terms are understood before they are relied on.
2. **Gradient** — concepts arrive in steps small enough to integrate.
3. **Reality** — every abstraction reconnects to an example, observation, test, or consequence.

And every substantial concept should answer:

1. What is it?
2. Why does it exist?
3. What does it look like in practice?
4. What can go wrong?
5. How do we verify that it works?

## Agnostic method translation

[**Agnostic Method Translation**](00-META/07_AGNOSTIC_METHOD_TRANSLATION.md) defines how SHAPER turns useful external conceptual structures into plain-language, testable methods without importing external authority.

## Repository map

- `00-META/` — scope, pedagogy, taxonomy, cross-layer architecture, open decisions, and [`06_AGENT_ROUTES.md`](00-META/06_AGENT_ROUTES.md).
- `10-SHAPER-OS/` — living adaptive governance kernel as applied to this product.
- `20-SHAPER-RUNTIME/` — operational truth, security, identity, agents, objects and services.
- `30-SHAPER-WORKSPACE/` — Flutter/Dart portable organizational workspace.
- `40-TRANSVERSAL/` — security, Linux host, object space, app model, protocol, web/host gateways, recovery.
- `90-REVIEW/` — three independent perspective passes, gap register, coverage matrix and source lineage.

## Foundational invariant

> **Stable in integrity. Mobile in form. Revisable in understanding. Guided by ethics. Controlled by feedback from reality.**

The architecture is intentionally revisable. A rule, implementation choice, agent, metric or even this documentation must remain inspectable when reality shows that it no longer serves its purpose.

## Enterprise reference and Helm restitution

The complete enterprise-facing proposition is canonicalized under `50-ENTERPRISE-REFERENCE/`: business primitives, the future-owner/tester journey, Helm capabilities, the office-furniture demo, thirteen scenarios, checklists and acceptance tests.

The unchanged September 2026 source pack is preserved under `99-SOURCE-ARCHIVE/`. Use `START-HERE.md` for reading routes.

The earlier `layers/` tree is retained only as an initial bootstrap snapshot; the numbered directories are canonical. See [`layers/README.md`](layers/README.md) before editing anything under `layers/`.

## Repository maintenance

- [`scripts/check-markdown-links.sh`](scripts/check-markdown-links.sh) — verify relative links in `*.md` (run from repo root after doc edits).

## Shared interface contracts

- [Branded selection controls and searchable lists](40-TRANSVERSAL/13_WORKSPACE_SELECTION_CONTROLS.md)

- [Conversational agent prompt-testing workspace](40-TRANSVERSAL/14_CONVERSATIONAL_AGENT_TEST_WORKSPACE.md)

- [Shared inline audio players](40-TRANSVERSAL/15_WORKSPACE_INLINE_AUDIO_PLAYERS.md)

- [Scope-first feature inventory and delivery checklist](90-REVIEW/SCOPE-FEATURE-INVENTORY.md)

- [Documentation session handoff checklist](90-REVIEW/DOC-HANDOFF-CHECKLIST.md)

- [Authors and agent roster](AUTHORS.md)

- [Agent and architect routes](00-META/06_AGENT_ROUTES.md)

- [Agent routes navigation review (2026-09-15)](90-REVIEW/AGENT-ROUTES-NAVIGATION-REVIEW-2026-09-15.md)

## Learning and source continuity

Use the [review records](90-REVIEW/DECISION-HYGIENE-QUALIFICATION.md) for the
historical scope and evidence of earlier documentation work. The mental source
keeps responsibilities and relationships readable; each realization and its
companion lab carry its delivery, operation and learning records.

## Dedication

[Personal dedication by Xavier de Poorter](DEDICATION.md).
