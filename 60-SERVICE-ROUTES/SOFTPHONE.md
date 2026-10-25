# Softphone route

Owning integration: [softphone](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/65-SOFTPHONE.md).
Related contract: [telephony](../40-TRANSVERSAL/11_SHAPER_VOX_TELEPHONY_SUBSYSTEM.md).

## Useful intention

A person communicates through a clear call surface connected to authorized
telephony service operations. Human control and agent assistance share the same
governed call context.

OS supplies authority principles. Runtime owns permitted call operations and
authoritative state. Workspace presents call controls and device information.
A client class has versioned service contracts; a user/device instance binds to
an identity and jurisdiction. Client, extension and call-leg identities remain
distinct.

## Required dependencies and consumers

Resolve client-session authority, telephony operations and device/media contracts.
[Telephony](TELEPHONY.md) owns call handling; [CRM](CRM.md) supplies permitted
relationship context. Workspace integration presents these results and requests
actions; Runtime evaluates authority.

Durable client application state has an explicit
[MariaDB owner](../40-TRANSVERSAL/17_APPLICATION_STATE_OWNERSHIP.md), distinct from
transient device/media resources. Private implementation and work-lab records
remain separate from reusable public mental references.

Return: [service dispatcher](README.md).

