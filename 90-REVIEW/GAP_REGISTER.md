# Gap Register

## Status legend

- **INTEGRATED** — addressed in current architecture documents.
- **OPEN** — requires an explicit implementation/product decision.
- **FUTURE** — intentionally deferred but architecturally reserved.

| Gap / boundary | Status | Current treatment |
|---|---|---|
| Three-layer responsibility split | INTEGRATED | OS / Runtime / Workspace defined |
| Shaper Linux placement | INTEGRATED | Optional host, transversal |
| A1/A2/A3 preserved | INTEGRATED | Separate guide per layer |
| Agent route hub and master → A* links | INTEGRATED | `00-META/06_AGENT_ROUTES.md`, master footers, `layers/README.md` redirect |
| `layers/` vs numbered directories | INTEGRATED | Bootstrap snapshot; canonical edit targets documented |
| Agent intelligence vs authority | INTEGRATED | Explicit invariant |
| Two human pedagogical depths | INTEGRATED | Foundations / Steward |
| Old human H0-H3 modes | INTEGRATED | Retained as R0-R3 situation modes |
| Words / Gradient / Reality pedagogy | INTEGRATED | Meta authoring model |
| Device continuity | INTEGRATED | Runtime source-of-truth model |
| Object Space vs filesystem | INTEGRATED | Files remain projection |
| Declarative app model | INTEGRATED | Schema-first + plugin escape hatch |
| Multi-monitor | INTEGRATED | First-class Workspace concern |
| Web browser question | INTEGRATED | Web Surface + Web Agent; engine external |
| Host import/export | INTEGRATED | Controlled gateways |
| Specialist native applications | INTEGRATED | Temporary export/re-import gateway |
| Audio/voice | INTEGRATED | Replaceable audio/STT/agent/TTS pipeline |
| Server/LAN/cloud/local topologies | INTEGRATED | Logical topology independence |
| Local encrypted cache | INTEGRATED | Bounded working set, not fixed giant disk |
| Device key identity | INTEGRATED | Asymmetric keys; hash not secret |
| Root Agent privilege lifetime | INTEGRATED | Scoped/ephemeral privilege preferred |
| User vs Steward app separation | INTEGRATED | Defense in depth, Runtime auth primary |
| Idempotency | INTEGRATED | Runtime invariant |
| Concurrency / claim / leases | INTEGRATED | Runtime invariant |
| External side effects | INTEGRATED | Compensation/reconciliation |
| Schema/rule versioning | INTEGRATED | Historical interpretability |
| Observer health | INTEGRATED | Observe the observers |
| Tenant isolation | INTEGRATED | Data + files + indexes + agent context |
| Trust ≠ availability | INTEGRATED | functional/healthy/integral/trustworthy |
| Repair/rebuild/quarantine | INTEGRATED | Kernel/security lifecycle |
| Sensor → trust bridge | INTEGRATED | Kernel + Runtime health/trust |
| Repetition → standing mandate | INTEGRATED | Explicit mandate object/policy |
| Org structure → workflow | INTEGRATED | Runtime graph + package mapping |
| Enterprise feature corpus | INTEGRATED | Mapped in Enterprise Primitives Mapping |
| Bootstrap first Root Authority | OPEN | Need enrollment/trust ceremony |
| Root/recovery key design | OPEN | Need customer/vendor/escrow policy |
| Exact RBAC/ABAC/ReBAC composition | OPEN | Conceptual composition fixed, mechanics open |
| OIDC/SAML/SCIM/enterprise federation | OPEN | Connector design needed |
| MDM/enterprise client deployment | OPEN | Fleet/update model reserved |
| Flutter multi-window implementation | OPEN | Logical model fixed, package/native choice open |
| Web engine choice | OPEN | Must prioritize security updates/compatibility |
| Secure runtime implementation language | OPEN | Use fit-for-purpose native components |
| Shaper Protocol transport | OPEN | Semantics listed, transport open |
| Offline merge per object class | OPEN | No universal last-writer-wins |
| Offline authorization expiry | OPEN | Mandate/session model needed |
| Object/graph/search storage technology | OPEN | Conceptual graph independent |
| App schema formal specification | OPEN | Need versioned normative schema |
| Plugin trust/signing model | OPEN | Higher-risk escape hatch reserved |
| Package registry/distribution | FUTURE | Architecture reserved |
| Reproducible builds/SBOM | FUTURE | Recommended production security track |
| Vulnerability disclosure program | FUTURE | Needed before broad external adoption |
| Shaper Linux base/distribution | OPEN | Minimal requirements defined |
| Screen capture / hostile-host limits | INTEGRATED | Explicitly non-absolute on normal hosts |
| Crash dump / swap / temp policy | OPEN | Data-lifecycle controls per platform |
| Printing/spool policy | OPEN | Host gateway capability |
| Data residency/jurisdiction | OPEN | Runtime deployment/policy decision |
| Legal retention/right-to-erasure | OPEN | Object lifecycle policy per deployment |
| Resource quotas / AI cost budgets | OPEN | Steward/Runtime operational policy |
| Agent provider/model trust changes | INTEGRATED | Cause class + provenance/trust monitoring |
| Accessibility/no-agent fallback | INTEGRATED | Workspace requirement |
| Remote support access | OPEN | Must not create silent vendor root |
| Backup restore validation | INTEGRATED | Universe restore is required |
| External connector reconciliation | INTEGRATED | Part of recovery/side-effect model |

## Rule

An OPEN item is not permission for an implementing agent to guess. Record the choice, rationale, migration path and review condition when it is resolved.
