# Application state ownership

Source role: cross-layer projection of the [ecosystem persistence contract](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/30-APPLICATION-STATE.md).
Terms: [application state](https://github.com/xavdp-pro/shaper-glossary/blob/main/TERMS.md#application-state)
and [partitioning](https://github.com/xavdp-pro/shaper-glossary/blob/main/TERMS.md#partitioning).

## Intention

Durable application facts persist in MariaDB under explicit ownership. Services
resume useful work, explain history and evolve schemas while preserving their
jurisdiction and relationships.

## Stable operating foundation

The [persistence/recovery rationale](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/32-PERSISTENCE-AND-RECOVERY-RATIONALE.md)
owns the shared explanation. MariaDB continues the Turbinobash `noweb` operating
foundation: a familiar,
long-lived path for maintenance, backups, restoration and predictable recovery.
Component-owned state keeps failures local and lets a service be rebuilt or
restored from a known form. Each functional boundary retains a private MariaDB
owner; this does not require a complex SQL cluster inside each component.

Distributed redundancy, continuity and disaster recovery are coordinated mainly
at service and infrastructure level. Their contracts name source/target identity,
consistent state, restore or promotion conditions and useful operation after
recovery. The local development-to-production journey preserves those contracts
through the [local-to-production profile journey](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/09-LOCAL-TO-PRODUCTION.md)
and explicit Linux, macOS or Windows host/provider contracts.

## Responsibility and state map

OS expresses ownership and governing invariants. Runtime maintains state,
transactions, access and lifecycle. Workspace presents permitted projections.

Every state family records its entity identity, owning function, database/schema,
access account, transaction boundary, retention, partition policy, migration and
restore relationship. Distinct functional services retain their isolated MariaDB
ownership according to the applicable governing profile. Runtime DML access and
schema administration have separate rights.

Coverage includes domain records, jobs/attempts, logs, protected records, schedules,
idempotence, desired state, membership, maintenance decisions and persistent CLI
sessions/context. Adapter-owned durable application state participates in the same
capture/restore contract. Transient media, IPC, binaries and exports have their
declared roles alongside authoritative application persistence.

## Integration and partitioning

Services exchange governed requests/events and stable references. A shared logical
graph preserves each source of record; its consumers use the owning interface.

Partition tables according to volume, retention, queries and maintenance needs.
Record the key, lifecycle and index/uniqueness interactions. Preserve identity,
deduplication and lease semantics. Cross-service work records its operation,
progress and reconciliation; recovery declares participating state owners and
the consistency boundary.

## Navigation

- [Class/instance](../00-META/09_CLASS_SPECIALIZATION_INSTANCE.md): schema/version binding.
- [Acting agents](16_PERSISTENT_ACTING_AGENTS.md): durable sessions.
- [Service routes](../60-SERVICE-ROUTES/README.md): domain state boundaries.

