# Security Model

## 1. Objective

Create a materially stronger boundary than a normal business application without claiming impossible hermetic isolation from a Host OS that is already fully compromised.

Security is defense in depth:

```text
identity + device trust + encryption + isolation + least privilege
+ short-lived authority + gateways + audit + detection + recovery
```

## 2. Threat domains

Distinguish at minimum:

- external network attacker;
- malicious/compromised website;
- malicious file/content;
- compromised ordinary host application;
- compromised user account;
- compromised agent/model/provider/context;
- compromised Runtime service;
- compromised Host OS with user-level privilege;
- compromised Host OS with kernel/root-equivalent privilege;
- malicious insider with legitimate account;
- supply-chain compromise;
- stolen/lost device.

The deployment must state which threats it claims to resist.

## 3. Data at rest

Persist sensitive local material only in approved encrypted storage/cache. On the server, use encrypted storage and key scopes appropriate to the deployment.

Avoid exposing a fully decrypted mounted filesystem to unrelated host processes merely for convenience.

Preferred logical path:

```text
authorized request
→ secure broker
→ decrypt required object/block
→ process/memory
→ expire/relock
```

## 4. Keys

A hash embedded in an executable is observable and is not a secret.

Use asymmetric device identity and platform-backed secret storage where available. Keep root/master key exposure minimal.

Support:

- rotation;
- revocation;
- device loss;
- organizational recovery;
- user offboarding;
- tenant/project key separation where useful.

## 5. Process separation

Prefer:

```text
Workspace UI (low privilege)
↕ authenticated IPC
Secure Runtime/Broker
├── session/token broker
├── key access
├── encrypted cache
├── gateways
└── policy-enforced native operations
```

Agent workers may be further sandboxed and capability-bound.

## 6. Web isolation

Treat Web Surface as an external trust domain. Crossings are explicit capabilities:

- upload;
- download/import;
- clipboard directions;
- microphone/camera;
- passkeys;
- print;
- screen share;
- external navigation.

## 7. Host gateway

Host file access should default to user-selected or policy-selected resources rather than permanent global filesystem attachment.

Specialist native application flows use controlled temporary export/re-import.

## 8. Runtime authorization

Security decision is server/runtime-side, not UI-side.

Evaluate effective authority from identity, device/session state, capability, role/object/context policy, mandate, criticality and trust.

## 9. Separating governance tooling

Packaging governance tooling as a separate binary can reduce exposure of privileged tooling. It is useful defense in depth, especially when installation is controlled, and it is never a second interface beside Helm.

It must never be treated as sufficient authorization by itself.

## 10. Compartmentalization

Design for partial failure:

- tenant isolation;
- service scopes;
- agent scopes;
- data/control/key separation;
- independent audit where feasible;
- network segmentation where useful.

A local compromise should not automatically become a global compromise.

## 11. Runtime compromise

For reproducible compromised components:

```text
detect → contain → evidence → quarantine → identify path
→ fix source/trust chain → rebuild → test → promote → monitor
```

Do not return a merely “cleaned” component to production when integrity cannot be reasonably established.

## 12. Client compromise

Because central Runtime can remain source of truth, a lost/compromised client can often be treated as disposable:

- revoke device/session;
- invalidate relevant keys/tokens;
- inspect audit;
- replace/re-enroll device;
- recover Workspace from Runtime.

This is a major security and operational advantage over data living primarily on laptops.

## 13. Memory and active plaintext

While data is actively used, some plaintext necessarily exists in process memory or platform surfaces. A sufficiently privileged host attacker may observe it.

Mitigate with:

- least privilege;
- process isolation;
- reduced plaintext lifetime;
- no unnecessary master-key presence;
- protected temp/cache lifecycle;
- host hardening;
- Shaper Linux for stronger control where required.

Do not market normal-host deployment as cryptographically opaque to the Host OS itself.

## 14. Success criterion

An attacker must cross multiple independent boundaries; compromise should have bounded blast radius; persistent data should be unusable without keys; sensitive actions should require actual authority; and recovery should be designed, tested and observable.
