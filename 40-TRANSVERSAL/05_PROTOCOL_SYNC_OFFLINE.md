# Shaper Protocol, Sync and Offline

## Protocol is more than REST

The system needs stable semantics for:

- authenticated calls;
- live events;
- streaming agent output;
- file transfer;
- reconnect/resume;
- presence;
- policy/session revocation;
- capability negotiation;
- synchronization;
- causality and correlation.

Transport may be HTTP, WebSocket, QUIC or a future combination. The semantic contract should survive transport changes.

## Client capability negotiation

Desktop, mobile and web cannot have identical powers. Client handshake should communicate:

- protocol version;
- supported app-schema versions;
- host platform;
- available secure storage;
- web/native/device capabilities;
- offline support;
- update compatibility.

## Offline modes

### Online terminal
Minimal persistent local state.

### Hybrid
Encrypted working set with offline-pinned objects and queued operations.

### Sovereign local
Full Runtime on device; remote sync becomes optional/peer/server topology.

## Offline operation envelope

```yaml
operation_id:
actor:
session_or_offline_authority:
base_object_version:
causation_id:
change:
created_at:
requires_online_validation:
```

Offline authority may be narrower than online authority.

## Conflict

When reconnecting:

- detect divergent base versions;
- classify mergeability;
- preserve both contributions;
- run deterministic merge where safe;
- otherwise create explicit conflict/arbitration state.

Never silently drop one person's meaningful work.

## Event ordering

Use IDs/causality rather than assuming network arrival order equals causal order.

## Large objects

File transfer should support resumable/chunked behavior and integrity verification. Do not load entire large files into memory merely to satisfy an API abstraction.

## Session revocation

Protocol must handle server-initiated or promptly observed revocation/permission changes. A client cannot keep indefinite authority merely because it went offline unless an explicit offline mandate allows it.

## Success criterion

The organization remains coherent through disconnection, reconnection, multiple clients and evolving versions without pretending distributed state is simple.
