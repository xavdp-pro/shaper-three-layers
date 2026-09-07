
# Open Boundaries and Decisions
## Intentionally unresolved — do not silently guess

These points are not defects in the architecture.

They are places where implementation must choose a concrete policy.

---

# 1. Identity and tenancy

Decide:
- one enterprise per universe?
- group structures?
- shared users across enterprises?
- cross-company contacts?
- root support access?
- tenant-specific encryption?

---

# 2. Permission model

Decide the mix of:
- RBAC;
- object permissions;
- relationship-based permissions;
- temporary delegation;
- standing mandates;
- root override.

Do not infer that one role model fits every customer.

---

# 3. Event architecture

Decide:
- synchronous domain events?
- durable event bus?
- outbox?
- replay?
- event retention?
- correlation IDs?
- schema registry?

The conceptual event grammar should remain stable even if transport changes.

---

# 4. Search / graph implementation

Decide how universal search and relations are implemented:
- relational joins;
- graph projections;
- search index;
- hybrid approach.

Do not let a storage choice redefine the business graph.

---

# 5. Calendar

Decide:
- internal calendar as source of truth;
- Google/Microsoft/external calendar connector;
- synchronization direction;
- conflict policy.

---

# 6. Accounting

Decide per country:
- what Enterprise OS owns;
- what an official accounting/e-invoicing provider owns;
- which statuses are mirrored;
- which documents are legally authoritative.

---

# 7. Telephony

Decide per deployment:
- SIP provider;
- number ownership;
- trunk capacity;
- recording policy;
- AI calling policy;
- local legal constraints;
- failover.

---

# 8. Document lifecycle

Decide:
- versioning;
- immutable signed versions;
- retention;
- deletion;
- legal hold;
- re-index behavior in Qdrant;
- access inheritance.

---

# 9. Shaping architecture

Decide:
- schema-driven UI versus generated code;
- deployment unit;
- live-update transport;
- test gate;
- rollback granularity;
- database migration policy.

---

# 10. Automation trust

Decide per workflow:
- manual;
- assist;
- approval;
- automatic;
- exception-only approval;
- review cadence;
- confidence/sensor thresholds.

Do not encode one maturity path as a universal rule.

---

# 11. Demo versus production

The demo may simulate:
- email delivery;
- documents;
- historical data;
- customers;
- suppliers;
- decisions.

Production must never inherit a simulation assumption silently.

Every simulated integration should have an explicit production connector boundary.
