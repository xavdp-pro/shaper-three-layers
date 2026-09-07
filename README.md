# Shaper Organizational OS

## Dedicated architecture and documentation repository

This repository isolates the architecture discussed for a portable, sovereign, agent-native operating environment for organizations.

It is deliberately **not** the general Shaper OS repository, not the Enterprise OS application catalogue, and not a Linux distribution repository. Its purpose is to define the system that lets an organization keep the same work environment, identity, context, applications, agents and governance while the host device may change between Windows, macOS, Linux, mobile, web, or an optional sovereign Shaper Linux host.

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

## Repository map

- `00-META/` — scope, pedagogy, taxonomy, cross-layer architecture and open decisions.
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

The earlier `layers/` tree is retained only as an initial bootstrap snapshot; the numbered directories are canonical.
