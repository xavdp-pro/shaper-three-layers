# Universe recovery catalogue and Registry

Status: design direction recorded with Xavier on 2026-09-10; implementation and
restore-time qualification remain open. This document does not declare the
current development Registry a production backup service.

## Intent and ownership

Expose a coherent **Universe backups / recovery** view for restoring a production
assembly of Podman services. Reuse the canonical Shaper names, exact image
digests and universe manifest. The objective is recovery of an organizational
environment, including its data and authority, with measured restoration time.

Shaper OS owns authority and recovery rules. Runtime owns backup preparation,
recovery manifests, execution and evidence. Workspace/Helm provides the view and
requests operations through the responsible Governor and Maker. A visible
Restore button is not itself execution authority.

## What a recovery point contains

- Universe identity, environment, source Git revisions and deployed manifest.
- Exact OCI image digests for every participating `brick-*` / `img-*`, with
  recovery availability verified independently of the original host.
- Consistent database exports and universe-owned `vol-*` contents, including
  recordings, objects, pending jobs, agent contexts, policies and event history.
- The necessary `cfg-*` and provider/connector binding metadata. Sensitive
  configuration and data are encrypted; keys have a separate recovery path.
- Start order, mounts, networks, compatibility constraints and health criteria.
- Checksums, creation time, consistency boundary, retention, encryption/key
  reference and a `proof-*` record for an actual isolated restoration attempt.

The proof is absent until an attempt occurs; its absence explicitly means
**not restore-tested**, never implicit success. Establish one recoverable
consistency boundary across databases, recordings and Queue, not merely one
individually valid export per store.

Container images alone do not include the persistent business state. A running
process checkpoint may be an optional acceleration mechanism; it does not replace
consistent data backups or a reproducible reconstruction path.

## Registry catalogue and protected backup storage

OCI registries can hold typed artifacts as well as images. A recovery manifest
can therefore be an OCI artifact that references the assembly's image digests and
encrypted data archives. The human view can group these as production recovery
points without treating them as executable images.

The authoritative backup store retains the **pull** direction already established
by Shaper OS V1.14, `doctrine/BACKUPS-ARE-PULLED.md`: the source prepares a consistent
backup; the protected collector retrieves it using narrowly restricted read
access. Production services receive no credentials to delete their backup history.
The collector may publish catalogue metadata through its own scoped path; sources
do not push into the protected backup destination.

The protected collector/store has no inbound door and retains append-only
history under its retention policy. An optional OCI backend must preserve that
boundary; turning the protected vault into a writable Registry endpoint is not
an implementation of the pull doctrine. The visible catalogue can be separate.

Preferred initial split: Registry for image references and non-secret recovery
catalogue; protected, versioned, encrypted storage for data archives. Storing
encrypted archives as OCI artifacts is an optional backend, subject to verified
registry compatibility, retention/deletion controls, capacity and recovery tests.
No raw patient/client data or secrets enter the ordinary image namespace.

Keep an independently recoverable copy of the catalogue, required images and key
recovery procedure outside the original host and Registry failure domain. Registry
garbage collection must not delete image/artifact digests referenced by retained
recovery points. A missing backup or failed collection produces an incident.
Test retrieval of actual decryption material after total loss of the operational
Vault and Registry. A key identifier or a procedure without recoverable keys is
insufficient. Backup encryption has its dedicated key, never a fallback to the
operational vault master key.

## Naming without a second vocabulary

Use the existing naming contract from Shaper OS V1.14
`docs/architecture/NAMING.md`. Do not invent a new `brick-*` for a mere JSON file.

Illustrative catalogue entry (path organization is proposed, not a new prefix law):

```text
Registry repository: shaper/pra/univ-vox0-dev
Recovery tag:        20260910T084500Z
Immutable identity: sha256:<artifact-digest>

cfg-univ-vox0-dev-recovery.json
proof-univ-vox0-dev-restore-20260910T090000Z.json
vol-univ-vox0-dev-contacts
vol-univ-vox0-dev-recordings
```

The recovery manifest maps canonical volume IDs to actual source and restored
mounts. Existing `/opt/...` bind mounts are explicitly mapped; naming a volume
in this document does not claim that a named Podman volume already exists.
`univ-vox0-dev` is an existing DEV instance, never a production snapshot disguised
as a reusable template. Class repositories retain the established class grammar.

## Restore sequence and human view

Show universe, recovery point, consistency time, last verified restore, measured
duration, recoverable data range and unresolved dependencies. Distinguish backup
created, collected, integrity-checked, restore-tested and activated.

1. Resolve the existing mandate and target; select an immutable recovery point.
2. Verify archives, images, keys, capacity and compatible restore environment.
3. Restore into an isolated target with external side effects disabled.
4. Restore volumes/configuration, then start the pinned services in declared order.
5. Verify actual workflows, object relationships and observer health, not only
   HTTP health. Record measured recovery time and data loss window.
6. Reconcile queues, pending calls, notifications, payments and external connectors.
   Prevent duplicate sends and simultaneous SIP trunk registration.
7. Fence the previous active writer/instance before activating the recovered one.
   Preserve logical universe identity; record the replacement physical instance.

Apply a technical egress/activation barrier before any worker, agent or SIP
service starts; a prose instruction inside an agent context is not that barrier.
An unreachable old instance is not proof that it has stopped writing or sending.

Stop activation on uncertain ownership, missing keys/data, failed integrity,
unresolved concurrent writers or unverified destructive side effects. Keep the
previous recovery point and the failed attempt evidence; do not overwrite the
original production state merely to test restoration. No fixed recovery duration
is promised before it has been measured with representative data.

## Delivery checklist

- [ ] Recovery artifact schema and validator with explicit volume mapping.
- [ ] Consistent local backup preparation for each participating data store.
- [ ] Restricted collector, encryption, retention and missing-backup alerts.
- [ ] Image pinning and independent Registry/catalogue recovery availability.
- [ ] Governed restore job with isolated rehearsal and activation fencing.
- [ ] Human catalogue and agent-readable context expose the same facts.
- [ ] Destructive-loss exercise; measure duration and data loss; save proof.

References: [universe recovery requirements](08_OBSERVABILITY_RECOVERY_UPDATES.md),
[OCI artifacts and registries](https://oras.land/docs/1.1/).
