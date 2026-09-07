# Shaper Runtime — Human Steward Guide
## Governing identity, authority, data and recovery

## 1. Runtime is the organization's operational trust layer

The Steward should treat Runtime as the place where organizational policy becomes enforceable behavior.

The Workspace can request; Runtime decides whether the request can be fulfilled and records what happened.

## 2. Identity graph

Manage separately:

- human identity;
- agent identity;
- service identity;
- device identity;
- organization/universe membership.

A person can use several devices. A device can be revoked without deleting the person. An agent can be replaced without erasing the history of what the old agent did.

## 3. Authorization graph

Avoid a single flat `is_admin` model.

Think in layers:

```text
technical capability
+ role
+ object/relationship permission
+ contextual attribute
+ current mandate / standing mandate
+ criticality
→ effective authorization
```

The system should explain denials and sensitive grants.

## 4. Key and session lifecycle

The Steward should know:

- where root trust lives;
- how devices enroll;
- how private keys are protected;
- how sessions are issued and revoked;
- how keys rotate;
- how recovery works if a device/human credential is lost;
- what break-glass can and cannot do.

Do not confuse a build hash with a secret credential.

## 5. Data classification and lifecycle

For each important class decide:

- source of truth;
- retention;
- deletion/legal hold;
- export policy;
- offline-cache policy;
- index/RAG policy;
- encryption/key scope;
- external connector ownership.

## 6. Object history

Historical business operations must remain interpretable after rules change. Version:

- app schemas;
- automations;
- decision rules;
- agent instructions;
- templates;
- connector mappings.

Corrections normally append new truth rather than silently rewriting the fact that an earlier state existed.

## 7. External effects

Treat these as irreversible until proven otherwise:

- sent emails;
- phone calls;
- submitted invoices;
- payments;
- exports/shared files.

Require preview/outbox/compensation/reconciliation according to criticality.

## 8. Observer health

Monitoring itself must be monitored.

A Steward dashboard should expose lag, failures, missed-event suspicion, duplicate processing and noise for critical observers.

## 9. Offline and conflict policy

Do not choose one global merge rule. Define object-class policies and make conflict visible.

For sensitive objects, a conflict may require explicit arbitration with provenance preserved.

## 10. Tenant isolation

If several organizations share infrastructure, isolate:

- object data;
- files;
- secrets;
- indexes;
- agent contexts;
- logs;
- connectors;
- capabilities.

Cross-tenant traversal is a deliberate feature, never an accidental join.

## 11. Recovery

Backups are not enough. Test restoration of a complete universe.

Know which parts are canonical and which can be rebuilt (for example derived indexes).

Have procedures for:

- data corruption;
- compromised runtime service;
- lost client device;
- key rotation;
- bad deployment;
- connector divergence;
- region/server failure.

## 12. Client compatibility

Steward should be able to see client versions and capability compatibility across the fleet. Signed updates and rollback are operational governance, not cosmetic packaging.

## 13. Runtime success

The Steward should be able to answer:

- Who can do what and why?
- Where is the source of truth?
- Which devices/sessions are trusted?
- What changed and under whose mandate?
- What happens if this component disappears?
- How do we restore the universe?
- Which assumptions are still open decisions?
