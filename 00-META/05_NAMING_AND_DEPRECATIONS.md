# Naming and Deprecations

## Shaper remains the umbrella name

The commercial/product name may remain **Shaper** because shaping is the central behavior: the environment adapts to the organization rather than forcing the organization into a fixed software form.

## Definition owner and compatible evolution

The [independent glossary](https://github.com/xavdp-pro/shaper-glossary) owns
stable terms and historical aliases. [Composition/source ownership](08_COMPOSITION_AND_SOURCE_MAP.md)
projects them across responsibilities; [class, specialization and instance](09_CLASS_SPECIALIZATION_INSTANCE.md)
separates reusable forms from installations and placement.

Use **component** for the current concept and **specialized cell/service** for
a base with domain capability. A **logical space** groups services and jurisdiction.
Earlier brick, package, FUnit and organizational-cell wording remains traceable;
existing `brick-*`, `funit-*`, image, socket, API and storage IDs stay compatible
until their owner publishes an explicit transition.

## Canonical names in this repository

- **Shaper OS** — living adaptive governance kernel.
- **Shaper Runtime** — operational truth, authority, data, events and agents.
- **Shaper Workspace** — portable human work environment.
- **Shaper Linux** — optional sovereign Host OS profile.
- **Steward** — human function responsible for system/universe governance.
- **Root Agent** — privileged agent working under Root Authority.
- **Root Authority** — human-led ultimate authority model.
- **Governor** — orchestration role/component.
- **Maker** — materialization/infrastructure-change role/component.
- **Helm** — the conversational interface between a human and the ecosystem in their charge, for every pilot.
- **Jurisdiction** — the universes a pilot is in charge of, down to their constituent pods.
- **Master root** — the founding human–agent tandem at the top of the fractal.
- **Jurisdiction root** — the tandem a jurisdiction is granted to, with full power inside it.
- **Pilot level** — E0 to E5, what a person at the Helm has proven in pilot training, for one class of universe.

## Strata of authority (17 September 2026)

The engineering canon sealed these words in Rules 0F, 24 and 37 of
[SHAPER OS V1.14](https://github.com/xavdp-pro/SHAPER-OS-V1.14/blob/main/software/RULES.md). The current glossary and explicit delegation resolve their present application;
the dated engineering source remains available for lineage.

| Stratum | Who holds it | Full power over | Never reaches |
| --- | --- | --- | --- |
| **Master root** | The founding tandem: a human Steward and the root agent under their direct control | Every host from underneath, the Governor, the Makers, matrices, backup contracts, every universe and its pods | Nothing above it; it is the top of the fractal |
| **Jurisdiction root** | A pilot and their agent at the Helm, given a jurisdiction by the root above: a client over their Workspace or Vox | The universes of that jurisdiction and their constituent pods, their features and configuration | A host, the Governor, a Maker, a matrix, a class repository, another jurisdiction or its own backup contract without explicit delegated authority |
| **Pilot inside a jurisdiction** | A person the jurisdiction root grants a narrower jurisdiction or mandate to | What that grant and their pilot level allow | Anything wider than the grant |

**Root Authority** keeps its meaning: the Steward, their directly controlled
root-capable agents and the explicit policies, for one scope. The master root is
the Root Authority at the top of the fractal; a jurisdiction root is the Root
Authority of its jurisdiction. Governors and makers belong to explicitly owned scopes and take direction from
their governing tandem through the declared delegation. Business and infrastructure
governors retain separate purposes and may coexist.

A **blank universe** describes a logical service scope granted to an
infrastructure client, whose jurisdiction root composes what its selected profile
and mandate allow, within its backup contract.

## Product names and their layers

| Name | Kind | Meaning |
| --- | --- | --- |
| **SHAPER Enterprise** | Public product name | The composed, connected business system of one organization |
| **SHAPER Workspace** | Public product name | The daily work surface for people: cases, documents, follow-ups, dashboards, conversations, specialized applications |
| **SHAPER Vox** | Public product name | Business telephony and communications; stands alone or connects to Enterprise and Workspace |
| **Helm** | Interface, internal and public | The conversational interface every pilot uses over their jurisdiction |
| **Shaper Workspace** | Architectural layer | The human-facing layer present in every universe, including a Vox universe's console |
| **`univ-vox-core`** | Class repository | The generic telephony class; each client is an instance of it, never a new class |

When both meanings of Workspace could be read, write **SHAPER Workspace** for the
product and **the Workspace layer** for the architecture.

Retired or refused names: `Enterprise OS` (historical source term, below),
`Workspace OS` (never a product name), `Shaper Voice OS` (replaced by SHAPER Vox),
`KovZu` (the former name of Helm), `Control Hub` (refused as a second name for
Helm), `Shaper Steward` (retired 17 September 2026: a separately named governance
application; governance views live in Helm at the Steward level, and *Steward*
remains the human of a root tandem), `Shaper Portfolio` (retired the same day: a
cross-organization view is a **jurisdiction**, and Rule 37 refuses "portfolio").

## “Enterprise OS”

`Enterprise OS` is retained as a historical/source term, but it is **not a primary architectural layer in this repository**.

Its substance is redistributed into:

```text
Shaper OS      → governance principles
Runtime        → business truth, identity, workflows, agents, events
Workspace      → human applications and work environment
Packages       → domain-specific business forms
```

This avoids describing one hybrid layer as both backend and desktop.

## “Helm” and “Maestro”

Earlier Enterprise OS documentation used `Helm` and `Maestro` for interaction/orchestration concepts. Those names were **not canonical here** unless deliberately reintroduced later.

> **Amended.** That reintroduction happened, deliberately, and for `Helm` only.
> The fourth review pass restored the enterprise experience together with the
> canonical Helm model ([`90-REVIEW/PASS_4_ENTERPRISE_RESTITUTION.md`](../90-REVIEW/PASS_4_ENTERPRISE_RESTITUTION.md));
> its capability contract is [`50-ENTERPRISE-REFERENCE/10_HELM_CAPABILITY_MODEL.md`](../50-ENTERPRISE-REFERENCE/10_HELM_CAPABILITY_MODEL.md)
> and its boundary against Governor and Maker is
> [`40-TRANSVERSAL/10_HELM_GOVERNOR_MAKER_MAPPING.md`](../40-TRANSVERSAL/10_HELM_GOVERNOR_MAKER_MAPPING.md).
> `Maestro` was **not** reintroduced: its functions remain distributed as the
> table below states. This page is amended rather than rewritten — the
> deprecation was real, and the condition it carried was met for one name.

Preserved functions map to:

- human-facing agent interaction → **Agents / Agent Surface**;
- orchestration/routing/escalation → **Governor**;
- structural materialization → **Maker**;
- standing automated execution → **automation actor under mandate**.

This deprecation concerns the architectural role vocabulary in this repository.
It does not remove a software brick named `Maestro` from the engineering kit or
instruct an implementer to rename/delete it. Changing that implementation requires
its own contract and migration review. Map its actual responsibilities to these
roles rather than equating a component name with a governance function.

Do not copy old names into new implementation merely because they exist in a historical document.

## “OS” in marketing

Architecturally, `Shaper OS` remains valid. In marketing, the word `OS` can create the false expectation that Shaper must replace Windows/macOS/Linux.

The product can be described as:

> **A portable organizational workspace that runs above your current operating system — and can later run on a sovereign Shaper host if required.**

## Naming rule

Canonical internal names optimize architectural precision. User-facing names optimize comprehension. They may differ deliberately.
