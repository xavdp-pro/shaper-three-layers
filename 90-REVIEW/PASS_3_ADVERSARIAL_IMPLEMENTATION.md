# Pass 3 — Adversarial, Security and Production-Failure Perspective

## Question

What breaks when the host is hostile, agents fail, devices go offline, users act concurrently, schemas evolve, external systems cannot be rolled back, and attackers can inspect open-source code?

## Findings

### 1. Encryption at rest is necessary but not hermetic execution

A privileged compromised Host OS may inspect memory/processes while plaintext is active. Normal-host deployment must never promise invisibility from the host kernel.

Mitigation: least privilege, process isolation, narrow decrypted lifetime, device-bound keys, remote source of truth and optional Shaper Linux.

### 2. A customized executable hash is not a secret

A per-person build identifier can help enrollment/distribution but can be extracted. Device asymmetric keys + challenge proof + secure keystore form a stronger identity basis.

### 3. The root agent must not be a permanent treasure chest

Root Authority can authorize almost anything; one agent process should not therefore hold every key. Use scoped, short-lived privilege and step-up authentication.

### 4. Separate User/Admin binaries are defense in depth only

A distinct Steward binary reduces exposed admin tooling. Runtime authorization remains the real boundary.

### 5. Offline creates an authority problem, not only a sync problem

A revoked user/device may remain offline. Offline mandates must define duration and scope. Reconnection must reconcile both data and authority changes.

### 6. Temporary plaintext is a real lifecycle

Threat surface includes:

- temp exports;
- external app autosave/recovery files;
- clipboard;
- thumbnails/previews;
- crash dumps;
- logs;
- swap/pagefile;
- screenshots/screen recording;
- print spool;
- browser downloads/cache.

Controls differ by host and cannot all be guaranteed on a hostile host. Document deployment strength honestly.

### 7. Web engine becomes supply chain

Even if Shaper does not build a browser, its chosen embedded engine must receive timely security updates. Browser state/cookies/extensions/download handling need policy.

### 8. Declarative schemas can still be malicious

A non-executable schema can cause data exposure, dangerous actions, resource exhaustion or deceptive UI if validation is weak. Treat schemas/packages as governed artifacts with signatures/provenance, permissions, limits, tests and rollback.

### 9. Plugins increase the threat class

Arbitrary plugin code requires explicit trust/sandbox/capability policy and should not silently inherit Workspace or Runtime privilege.

### 10. Supply-chain integrity must include Shaper itself

Open source does not remove signing needs. Future production model should include:

- signed releases;
- dependency/SBOM awareness;
- reproducible-build goals where practical;
- vulnerability disclosure process;
- key-rotation procedure;
- secure update channel;
- rollback.

### 11. Bootstrap of the first Root Authority needs design

Who creates the first organization? How is the first Steward verified? How are recovery credentials created without giving a vendor silent permanent root? This is a real trust-root decision and is added to the gap register.

### 12. Recovery keys can defeat security if poorly designed

Backup and encryption recovery must be designed together. “Everything encrypted” is useless operationally if one lost key destroys the company, and dangerous if one universal recovery key decrypts every customer.

### 13. Existing enterprise identity should be interoperable

Avoid reproducing Active Directory complexity, but large customers may require OIDC/SAML/SCIM/MDM/federation. Treat these as connectors into Shaper identity/authority rather than allowing an external directory to redefine the internal object model.

### 14. Multi-tenancy must include indexes and agent context

Isolation is not only SQL rows. Files, vector indexes, search caches, logs, prompts/context, connector secrets and observability data all require tenant boundaries.

### 15. Agent/model/provider compromise is a normal cause class

Identity alone does not prove integrity. Detect behavior drift, changed provider/model, prompt injection, poisoned RAG, compromised tools or credentials.

### 16. External side effects survive internal rollback

Email, calls, payment, legal submissions, external uploads require staged actions, outbox, compensation/reconciliation and explicit evidence.

### 17. Client protocol/schema version drift can become a security bug

Capability negotiation must fail safely. Old clients must not interpret a newer policy/schema in a way that silently broadens authority.

### 18. Observability can leak sensitive data

Logs/traces should preserve enough evidence without becoming a second uncontrolled copy of secrets, private files or RAG content.

### 19. Denial of service/resource budgets matter

Agents, semantic indexing, local models, web sessions and generated apps can consume CPU/GPU/RAM/disk/network/tokens. Resource quotas and backpressure belong in Runtime/Steward operations.

### 20. Human coercion/social engineering remains outside pure cryptography

Step-up confirmation, understandable permission prompts, provenance and review help, but the system cannot assume an authenticated human instruction is always wise or uncoerced. Criticality and counter-view remain relevant.

## Adversarial verdict

The idea remains sound if security is described as layered containment and recoverability, not absolute secrecy from a fully privileged host. The architecture is strongest when server/LAN Runtime is authoritative and clients are replaceable, and stronger still on a controlled Shaper Linux host.
