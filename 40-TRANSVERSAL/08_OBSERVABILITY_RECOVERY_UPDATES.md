# Observability, Recovery and Updates

## Observability is part of the product

A Steward should be able to ask:

> Why is Shaper slow or failing for this user/context?

and receive a causal view across:

```text
client
network
session/auth
Runtime service
object store/database
search/RAG
agent provider/local model
external connector
```

## Health dimensions

Expose separately:

- availability;
- performance/health;
- integrity;
- trust.

## Observer health

Observe the observers. A monitoring pipeline that silently stops is itself an incident.

## Audit

Important history should be append-oriented and attributable. Corrections generally add superseding events/versions rather than erase the fact that an earlier state existed, subject to privacy/retention law and policy.

## Universe recovery

Recovery scope includes:

- objects/data;
- files/blobs;
- identities/roles/policies;
- app schemas/packages;
- agent definitions/mandates;
- event/audit history;
- key recovery metadata;
- external connector reconciliation;
- indexes that may be rebuilt.

Test actual restoration.

The [universe recovery catalogue](12_UNIVERSE_RECOVERY_CATALOG.md) records the
proposed Registry-backed recovery view, protected pulled backups, existing
Shaper naming, activation fencing and measured recovery proof.

## Client recovery

A client should be disposable in server-centric topology:

```text
replace device
→ install
→ enroll
→ authenticate
→ restore Workspace state
```

## Application/runtime deployment

Use DEV → TEST → PROD for intentional changes. Use incident lifecycle separately for compromised systems.

## Client updates

Enterprise requirements:

- signed packages;
- channels (stable/canary if used);
- organization policy;
- compatibility checks;
- progressive rollout;
- rollback;
- fleet status.

## Schema migrations

An app/UI schema update may be reversible while a destructive data migration is not trivially reversible. Distinguish rollback classes explicitly.

## External side-effect recovery

A rollback plan must mention effects that cannot be rolled back internally. Define compensation/reconciliation.

## Success criterion

Failures are detectable, explainable and recoverable without treating “the screen is back” as proof that integrity and trust have been restored.
