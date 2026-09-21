# Shaper Organizational OS

Licensed under [CC BY-SA 4.0](LICENSE). See [NOTICE.md](NOTICE.md) and [AUTHORS.md](AUTHORS.md) for ownership, scope, and provenance.

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
These are intended benefits, not measured guarantees: written principles alone
neither remove hallucinations nor prove that a deployed system follows them.

See the [decision foundation](10-SHAPER-OS/00_MASTER.md#decision-hygiene-ethics-time-and-experience) and [qualification scenarios](90-REVIEW/DECISION-HYGIENE-QUALIFICATION.md).

## Dedicated architecture and documentation repository

This repository isolates the architecture discussed for a portable, sovereign, agent-native operating environment for organizations.

It is deliberately **not** the general Shaper OS repository, not the SHAPER Enterprise application catalogue, and not a Linux distribution repository. Its purpose is to define the system that lets an organization keep the same work environment, identity, context, applications, agents and governance while the host device may change between Windows, macOS, Linux, mobile, web, or an optional sovereign Shaper Linux host.

## Executable companion (Shaper OS kit)

The **runnable** Shaper OS tree — bricks, universes, `RULES.md`, tests, deploy
and proof scripts — lives in
[**`SHAPER-OS-V1.14`**](https://github.com/xavdp-pro/SHAPER-OS-V1.14) on GitHub.
Use that repository to clone, build, and prove a universe (for example `univ-base`).
Use **this** repository when you need the organizational map (governance kernel,
Runtime responsibilities, Workspace shell) without mixing it with install steps.

| Question | Read |
| :--- | :--- |
| Where do I start as an agent or architect? | [`00-META/06_AGENT_ROUTES.md`](00-META/06_AGENT_ROUTES.md) and [`AGENTS.md`](AGENTS.md) |
| How do I deploy and prove a universe? | [SHAPER-OS-V1.14](https://github.com/xavdp-pro/SHAPER-OS-V1.14) — `AGENTS.md`, runbook, `software/universes/univ-base/` |
| How do the three layers fit together? | This repository — `10-SHAPER-OS/`, `20-SHAPER-RUNTIME/`, `30-SHAPER-WORKSPACE/` |
| Who gets credit? | This repo [`AUTHORS.md`](AUTHORS.md); executable kit [V1.14 `AUTHORS.md`](https://github.com/xavdp-pro/SHAPER-OS-V1.14/blob/main/AUTHORS.md) and `Co-Authored-By` trailers |

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
3. **Executable credit** — commits, tests, and Rule 2 trailers on the [SHAPER-OS-V1.14](https://github.com/xavdp-pro/SHAPER-OS-V1.14) kit; documentation credit on [`AUTHORS.md`](AUTHORS.md) in each repository.

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

## Conclusion: what can be relied on today?

What is supported by evidence, under which conditions, and what remains to be
verified? These questions govern the conclusion; reliability is demonstrated
within a stated scope, not claimed without limits.

For the decision-hygiene additions reviewed on 2026-09-11, the evidence establishes
explicit contracts for authority, contextual action, counter-view and integrity,
with linked qualification scenarios. Documentation consistency and file links
were checked, including an independent counter-view. See the
[scope and evidence record](90-REVIEW/DECISION-HYGIENE-QUALIFICATION.md). This finding concerns those additions,
not qualification of the entire repository or every deployed agent.

The introduction's four benefits remain objectives to evaluate: fewer handoff
misunderstandings between human and agent; useful agent-to-agent review without
authority bypass; evidence-based reports to humans; and clearer human agreements.
The nine behavioral scenarios have not been executed in this documentation work,
and effects on human collaboration have not been measured. Therefore this review
does not establish reduced error rates, improved daily autonomy or elimination
of hallucinations. Future conclusions must name actual outcomes, conditions and
remaining gaps rather than repeat these intended benefits as achievements.
