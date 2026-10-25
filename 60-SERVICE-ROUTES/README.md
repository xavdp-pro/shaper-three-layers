# Service task routes

Source role: task dispatcher for Three Layers domain projections.
Composition owner: [SHAPER ecosystem](https://github.com/xavdp-pro/shaper-ecosystem).
Terms: [independent glossary](https://github.com/xavdp-pro/shaper-glossary).

## Agent entrance

Start with the tandem's task and jurisdiction. Select the domain route, read its
owning intention/laws and required interfaces, then resolve the exact private or
public implementation owner and required capabilities from the permitted registry.
Follow required dependencies to their owners; optional modules retain explicit
selection. Governing law, integration interpretation and product implementation
remain distinct source roles.

| Task family | Domain entrance |
|---|---|
| Reception, calls and communication follow-up | [Telephony](TELEPHONY.md) |
| Parties, contacts and relationship history | [CRM](CRM.md) |
| Human call interaction and device context | [Softphone](SOFTPHONE.md) |
| Shop management and approved service provisioning | [Shops](SHOPS.md) |

Shared required routes: [composition](../00-META/08_COMPOSITION_AND_SOURCE_MAP.md),
[class/instance](../00-META/09_CLASS_SPECIALIZATION_INSTANCE.md),
[state ownership](../40-TRANSVERSAL/17_APPLICATION_STATE_OWNERSHIP.md).
Agent execution additionally uses [persistent agents](../40-TRANSVERSAL/16_PERSISTENT_ACTING_AGENTS.md).

Each domain route links its consumers and dependencies. Reverse navigation uses
the ecosystem relationship registry. A complete reading follows these shared
routes, the three masters and each domain route, then task-relevant owning
contracts. Public common references connect to users' private realizations through
their authorized source registry.


## Optional domains and client distinction

The [optional domain dispatcher](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/68-OPTIONAL-DOMAINS.md)
adds observation/maintenance and summarization, and identifies the shared
entrances for identity/membership, billing/entitlement, booking and user workspaces.
Its resolution column distinguishes a generic public owner from a product
contract that the task must select. No row asserts that a concrete implementation
is installed or makes every domain part of a generic base.

A softphone task constructs a client consuming telephony interfaces. Its
`concept:softphone` route does not inherit service-base construction. Constructing
the telephony service is a separate selected task. Service recovery follows the
[recovery owner](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/32-PERSISTENCE-AND-RECOVERY-RATIONALE.md)
through state, identity, authority and reconciliation, then the actual affected
component/domain contracts and profile; it does not infer all-domain recovery.
