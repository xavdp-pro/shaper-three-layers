# Naming and Deprecations

## Shaper remains the umbrella name

The commercial/product name may remain **Shaper** because shaping is the central behavior: the environment adapts to the organization rather than forcing the organization into a fixed software form.

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

Do not copy old names into new implementation merely because they exist in a historical document.

## “OS” in marketing

Architecturally, `Shaper OS` remains valid. In marketing, the word `OS` can create the false expectation that Shaper must replace Windows/macOS/Linux.

The product can be described as:

> **A portable organizational workspace that runs above your current operating system — and can later run on a sovereign Shaper host if required.**

## Naming rule

Canonical internal names optimize architectural precision. User-facing names optimize comprehension. They may differ deliberately.
