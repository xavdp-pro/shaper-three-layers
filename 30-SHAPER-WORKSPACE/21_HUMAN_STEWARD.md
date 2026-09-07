# Shaper Workspace — Human Steward Guide
## Governing the visible operating environment

## 1. Workspace is a projection, not the source of authority

The Steward controls what the Workspace may expose and request, but Runtime remains the enforcement layer.

A hidden admin menu is not security. An absent admin binary is defense in depth, not the primary boundary.

## 2. User versus Steward distribution

Recommended default:

- **Shaper** — normal work client;
- **Shaper Steward** — identity, policy, devices, audit, trust, recovery and deep configuration.

High-security deployments can distribute Steward separately and restrict its installation. Sensitive operations still require Runtime authorization and step-up policy.

## 3. Workspace capability policy

Decide what each platform can expose:

- desktop local file import/export;
- web sandbox limitations;
- microphone/camera;
- clipboard;
- Web Surface;
- external native apps;
- print;
- terminal/CLI;
- local models/runtime.

Clients negotiate capability rather than pretending every platform is identical.

## 4. Web trust boundary

A Web Surface should be treated as an external zone.

Policy choices include:

- persistent or disposable cookies/profile;
- approved domains;
- upload/download gateways;
- clipboard direction;
- camera/microphone;
- passkeys/authentication;
- printing;
- agent control and audit.

Do not expose the whole object graph to a web page just because it is rendered inside Shaper.

## 5. Host application gateway

For specialist applications define:

- which object types may open externally;
- temporary export location/security;
- allowed application selection;
- re-import/version semantics;
- cleanup;
- audit and DLP rules.

## 6. Multi-monitor policy

Treat layouts as user/workspace preferences, not business truth. Ensure that losing a monitor never makes critical information unreachable.

## 7. Dynamic app governance

Agents may shape apps, but changes need a lifecycle:

```text
request → plan → diff → test → apply → observe → accept/rollback
```

The Steward decides which roles can enter shaping mode and which changes require stronger confirmation.

Arbitrary executable plugins are a separate higher-risk class from declarative schema changes.

## 8. Accessibility and agent independence

Core work should remain possible if the agent provider is down. The Steward should preserve deterministic navigation and accessibility paths.

## 9. Client fleet

Steward visibility should include:

- device/client version;
- platform;
- trust/enrollment state;
- pending updates;
- incompatible schema/protocol state;
- failures and rollback state.

## 10. Local cache policy

Choose by user/device/classification:

- cache size;
- offline pinning;
- plaintext temp restrictions;
- expiration/eviction;
- logout/revocation cleanup;
- screenshot/clipboard considerations where enforceable.

Do not promise protection against a fully compromised host kernel; reduce exposure and keep canonical truth away from the client where topology allows.

## 11. What the Steward should test

Before declaring a Workspace feature complete, test:

### Human side
- understandable?
- context available?
- STOP/cancel clear?
- failure visible?
- jargon minimized?

### System side
- Runtime authority correct?
- object/event trace correct?
- local data lifecycle correct?
- external side effects explicit?
- recovery path known?
- works/degrades on supported platforms?

## Success

The Steward maintains a Workspace that is simple for ordinary people, powerful for the organization, portable across hosts, and incapable of silently bypassing the Runtime and kernel governance beneath it.
