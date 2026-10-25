# Telephony route

Owning integration: [telephony](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/50-TELEPHONY.md).
Domain contract: [Three Layers telephony](../40-TRANSVERSAL/11_SHAPER_VOX_TELEPHONY_SUBSYSTEM.md).

## Useful intention

People reach the appropriate organizational destination and obtain an attributable
communication outcome and next step. The tandem shapes reception within its
jurisdiction.

OS supplies authority and domain-policy principles. Runtime owns call identities,
validated actions and processing state. Workspace supplies reception, call context
and follow-up surfaces. A specialized cell/service combines the generic base and
telephony domain units; instances bind its version to private configuration/state.

## Required dependencies and consumers

Follow call/signaling, identity, permission and state contracts for call work.
Follow the selected scheduling interface for booking and [CRM](CRM.md) for contact
resolution or communication attachment. [Softphone](SOFTPHONE.md) consumes the
call-service interface. Exact call/leg references connect media and follow-up.

[MariaDB state ownership](../40-TRANSVERSAL/17_APPLICATION_STATE_OWNERSHIP.md)
covers durable call/processing state. Interface events preserve each service's
owner. Public VOX intentions/laws remain distinct from private commercial code;
its private product and companion lab retain their source roles.

Return: [service dispatcher](README.md).

