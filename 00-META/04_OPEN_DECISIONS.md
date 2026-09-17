# Open Decisions

These are intentionally unresolved implementation choices. Agents must not silently turn them into immutable architecture.

## 1. Product naming

- Public product may be simply **Shaper**.
- **Shaper Workspace** remains the architectural term in this repository.
- Final marketing naming remains open pending domain/trademark/product testing.

## 2. Flutter desktop multi-window strategy

Decide the exact library/native architecture for:

- multiple native windows;
- multi-monitor restoration;
- shared engine/state versus isolated processes;
- crash containment across surfaces.

The logical Workspace model must not depend on a particular package.

## 3. Local runtime language

Dart is preferred for Flutter UI and shared app-facing SDK logic. The secure/system runtime may use Rust/C/C++ or other appropriate languages where native isolation, crypto, process control or performance requires it.

Do not force the entire stack into Dart merely for language uniformity.

## 4. Identity model

Decide:

- one organization per universe versus group hierarchies;
- cross-organization actors;
- external guests;
- service identities;
- support/root break-glass model;
- device enrollment lifecycle.

## 5. Authorization composition

Define the practical composition of:

- RBAC;
- ABAC/context rules;
- relationship/object permissions;
- capabilities;
- current mandates;
- standing mandates;
- temporary delegation;
- root override/break-glass.

## 6. Cryptographic storage

Decide exact formats for:

- server vault encryption;
- client encrypted cache;
- per-object/project/tenant keys;
- TPM/Secure Enclave/OS keystore adapters;
- recovery and rotation;
- key escrow policy where customers require it.

A compiled fingerprint or SHA-512 value may identify a build/device enrollment package, but must not be treated as a secret root of trust.

## 7. Web engine strategy

Options include platform-native WebViews and a standardized Chromium-based surface. Choose based on:

- consistent behavior;
- security update cadence;
- enterprise authentication compatibility;
- automation/control requirements;
- footprint.

Do not implement a browser engine.

## 8. Object storage / graph / search implementation

Keep the conceptual object graph independent of whether implementation uses:

- PostgreSQL relational model;
- object storage;
- graph projection;
- search index;
- vector database;
- hybrid architecture.

## 9. Offline conflict strategy

Different object classes may require different resolution:

- append-only events;
- optimistic versioning;
- CRDT-like merge;
- human/agent conflict review;
- locked/leased editing.

There is no universal “last writer wins” rule.

## 10. Shaper Protocol transport

Define semantics first, transport second. Needs include:

- request/response;
- live events;
- reconnect/resume;
- large objects;
- streaming agent output;
- presence;
- capability/policy changes;
- offline synchronization;
- causal IDs and replay boundaries.

## 11. Declarative application schema

Decide:

- versioning format;
- extension model;
- migration rules;
- signed package model;
- plugin escape hatch;
- test/rollback gates;
- compatibility window across Runtime versions.

## 12. Packaging of governance tooling

Settled on 17 September 2026 for the interface: there is one conversational
interface, Helm, for every pilot (Rule 0F), and no separately named governance
product (`Shaper Steward` is retired). Governance views appear in Helm at the
Steward level, within the jurisdiction.

Still open, as packaging only:

- optionally a separately signed binary for governance tooling in
  high-security deployments.

A packaging split is defense in depth, not the primary authorization boundary.

## 13. External application integration

Define lifecycle for controlled “open externally” flows:

```text
Shaper object
→ authorized temporary export
→ native specialist app
→ save/import gateway
→ new object version
```

Need policy for temporary file destruction and failure cases.

## 14. Shaper Linux base

Ubuntu/Debian-like versus another minimal base remains open. The invariant is:

- secure boot chain where possible;
- encrypted storage;
- minimal attack surface;
- controlled applications;
- reliable updates/rollback;
- Wayland/audio/network/device functionality needed by Workspace.

## 15. Cloud, LAN and local parity

The product should preserve conceptual parity but may have different capabilities across topologies. Explicitly document what cannot be identical, especially browser-only restrictions and host-level local capabilities.
