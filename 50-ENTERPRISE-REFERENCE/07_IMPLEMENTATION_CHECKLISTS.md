> Canonical integration note
>
> Enterprise OS is preserved here as the business reference manifestation of Shaper. It is not a fourth technical layer: governance belongs to Shaper OS, durable truth and execution to Runtime, human interaction to Workspace, and domain specialization to Packages.

---

# Implementation Checklists
## Human-readable + agent-operational checks

# 1. Universal feature checklist

For every feature:

### Human check
- Is the purpose obvious?
- Is the responsible person visible?
- Is the next action obvious?
- Can the user reach context directly?
- Is the result visible?
- Can the user understand what happened?
- Can the user stop or undo when appropriate?

### Agent/system check
- Is the object model explicit?
- Are relationships explicit?
- Are permissions explicit?
- Is the action traceable?
- Are events emitted?
- Are success criteria testable?
- Are failure states testable?
- Is rollback defined?
- Are persistent-data effects understood?
- Are notifications correct?
- Is the deep link correct?

---

# 2. Decision checklist

- Decision object created?
- Initiator identified?
- Validator identified?
- Scope explicit?
- Reason explicit?
- Expected result explicit?
- Affected users identified?
- Notifications sent?
- ACK required where necessary?
- Execution evidence linked?
- Review condition defined?
- Decision revisable?

---

# 3. Automation checklist

Before automation:

- Repetition actually observed?
- Pattern sufficiently stable?
- Exceptions understood?
- Risk understood?
- Human owner identified?
- Correct automation level chosen?
- Approval mode needed?
- Logs available?
- Success/failure sensor available?
- STOP available?
- Rollback available?
- Notification policy defined?
- Review cadence defined?

---

# 4. Task checklist

- Parent object linked?
- Subtask relation works?
- Multiple participants supported?
- One lead/driver supported?
- Priority?
- Urgency?
- Due date?
- Status?
- Notifications?
- WebSocket update?
- Kanban?
- Global attention view?
- Client/object aggregate view?

---

# 5. Notification checklist

- Trigger defined?
- Correct recipients?
- Severity?
- ACK policy?
- Deep link?
- Context visible?
- History visible?
- Duplicate/noise control?
- Result acknowledgment when needed?

---

# 6. Email checklist

- Personal mailboxes?
- Shared mailboxes?
- Role permissions?
- Customer/contact matching?
- Thread/context link?
- Attachment ingestion?
- Document indexing?
- Task/decision creation?
- Audit?
- Safe sending policy?

---

# 7. Telephony checklist

- SIP provider?
- Number?
- Concurrent-call capacity?
- Routing mode?
- Schedule?
- Human queue?
- AI mode?
- Direct extensions?
- WebRTC?
- Mobile softphone?
- CRM screen-pop?
- Recording legality?
- Transcription?
- Summary?
- Click-to-call?
- Call result trace?

---

# 8. GED/RAG checklist

- Upload?
- Extraction?
- OCR if needed?
- Classification?
- Metadata?
- Customer link?
- Source preserved?
- Qdrant indexing?
- Retrieval test?
- Grounded answer test?
- Permissions?
- Deletion/update propagation?

---

# 9. ERP checklist

- Product?
- Supplier?
- Purchase lot?
- Historical purchase price?
- Historical sale price?
- FIFO rule?
- Quote?
- Discounts?
- Delivery fee?
- Order conversion?
- Stock reservation?
- Margin calculation?
- Historical prices frozen?

---

# 10. Observability checklist

- Event logs?
- Filter by module?
- Filter by customer?
- Filter by workflow?
- Filter by agent?
- Filter by decision?
- Filter by error?
- Evidence available?
- Human-readable status?
- Technical detail available on demand?
- Sensor health monitored?

---

# 11. Rollback checklist

Before claiming rollback:

- What exactly is being rolled back?
- UI?
- code?
- config?
- runtime?
- database?
- documents?
- email state?
- external side effect?

Never treat container rollback as equivalent to data rollback.

---

# 12. Final coherence check

For every implemented capability, verify:

```text
INTENTION
→ AUTHORITY
→ ACTION
→ RESULT
→ EVIDENCE
→ NOTIFICATION
→ SENSOR
→ TENSION / SUCCESS
→ LEARNING
```

If one link is missing, the graph is incomplete.


---

# 13. Concurrency / idempotency checklist

- Can the operation retry safely?
- Stable operation ID?
- Duplicate detection?
- Concurrent editor behavior defined?
- Version conflict behavior defined?
- Claim/lease needed?
- Stale lock recovery?
- External side effect duplication prevented?

---

# 14. Appointment checklist

- Customer/contact link?
- Employee/resource link?
- Start/end?
- Timezone?
- Status?
- Change history?
- Reschedule?
- Cancellation?
- Source call/email?
- Notification?
- Next-appointment retrieval for Helm/AI?

---

# 15. Prospecting checklist

- Prospect source?
- Ownership/claim state?
- Mutex/lease?
- Read-only visibility to other operators?
- Call/email result?
- Follow-up date?
- Conversion state?
- Trace?
- Release stale claims?

---

# 16. Observer-health checklist

- Observer registered?
- Event/condition explicit?
- Last run visible?
- Lag visible?
- Failure visible?
- Missed-event detection?
- Duplicate handling?
- Noise level measured?
- Owner defined?
- Escalation path?

---

# 17. Authority checklist

Before agent execution:

- Technical capability available?
- User role permits it?
- Object-level permission permits it?
- Current or standing mandate exists?
- Criticality acceptable?
- Confirmation required?
- Trace created?
- STOP available?

---

# 18. Data / external-side-effect checklist

- Source of truth explicit?
- Historical values preserved?
- Schema/rule version recorded?
- External send/call/payment/submission involved?
- Compensation strategy?
- Data retention rule?
- Cross-tenant isolation?
- Backup/recovery path?

## Perimeter completeness prerequisite

Use [the scope-first feature inventory](../90-REVIEW/SCOPE-FEATURE-INVENTORY.md)
before implementation and reconcile the same rows before delivery. The checks
above evaluate quality; they do not establish that every scoped requirement has
been identified. Record source coverage, dependencies and omissions separately.
