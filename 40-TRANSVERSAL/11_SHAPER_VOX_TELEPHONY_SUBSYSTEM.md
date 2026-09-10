# Shaper Vox — Generic Enterprise Telephony Subsystem

## Status & Purpose

**Status:** target cross-layer contract. Clinic is the first evidence source,
not the generic implementation itself. Every statement below is either an
invariant, a configurable policy hook, or an acceptance target. Runtime proof
must still name the exact universe, revision, configuration and evidence.

This document defines the canonical architecture, intents catalog, and operational invariants of **Shaper Vox** (formerly explored via Clinic / `univ-clinic0`), the sovereign enterprise telephony subsystem within the **Shaper Three Layers** framework.

Telephony is not an isolated side tool: it is an operational ingress and a primary communication surface of the enterprise. Every call is an interaction with the organization's object graph, governed by Shaper OS law, mediated by the Shaper Runtime, and experienced through the Shaper Workspace.

---

## 1. Architectural Placement (The Three Layers)

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 1. SHAPER OS (Adaptive Governance Kernel)                             │
│ - Telephony Policies: Ingress rules, office hours, escalation SLA      │
│ - Authority Matrix: Human delegation ladder (Manual → Assisted → Auto) │
│ - Legal Invariants: Lawful call recording notice (GDPR/Telecom Law)    │
│ - Core Doctrine: "What must be impossible is refused by code, not      │
│   requested from the prompt"                                           │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Constrains / Guides
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. SHAPER RUNTIME (Operational Truth & Event Fabric)                   │
│ - Connectors: SIP Trunks, WebRTC, Asterisk AudioSocket (8kHz PCM)      │
│ - Audio Pipeline: VAD, streaming STT, LLM agent, streaming TTS         │
│ - Guarded Tool Engine: Action-Bound Consent Guard, Aizuchi Classifier  │
│ - CTI & Object Resolution: Caller Phone → Contact / Customer / Company  │
│ - Event Convergence: call.started, call.completed, Outbox/Compensation │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Exposes
┌───────────────────────────────────▼────────────────────────────────────┐
│ 3. SHAPER WORKSPACE (Human Operating Environment & Surfaces)           │
│ - Vox Cockpit: Switchboard, extension status, queue monitoring         │
│ - Embedded Softphone: WebRTC desktop widget & Flutter mobile dialer    │
│ - CTI Screen-Pop: Real-time caller card, context history, live text    │
│ - Human Handoff Desk: Voicemail inbox, pending callbacks, task review  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Naming Standard: Shaper Vox

In line with Shaper OS terminology (*KovZu*, *Maestro*, *Zephir*, *Astra*):
- **Ecosystem Name**: **Shaper Vox** (or *Shaper Voice OS*).
- **Proposed generic brick roles** (names remain implementation choices until
  their manifests and build contexts are accepted):
  - `brick-telephony-pbx` (`:5060`, `:8088`): PJSIP/Asterisk engine, trunk registration, dialplan execution.
  - `brick-vox-engine` (`:8670`): AudioSocket bridge, voice agent orchestrator, Aizuchi classifier, action-bound consent guard.
  - `brick-softphone` (`:8660`): WebRTC client gateway and Flutter mobile signaling endpoint.
- **Human Workspace Modules**:
  - `Vox Cockpit`: Inbound switchboard, extension presence, live call transfer.
  - `Vox Timeline`: Unified CRM call history with audio playback and transcripts.

---

## 3. Catalog of Generic Enterprise Telephony Intents

Profiles select a bounded subset of intents and may add domain intents without
changing the generic lifecycle. Free text is never passed directly to backend
mutation functions without validation. An intent catalog describes what may be
requested; Runtime authority still decides what may execute.

### 3.1 Reception, Ingress & Routing
| Intent | Description | Extracted Entities | Backend Action |
|---|---|---|---|
| `intent.greet_and_identify` | Identifies caller and reason for call | `caller_name`, `company`, `intent_summary` | CTI lookup by ANI/caller ID. Loads customer profile into session context. |
| `intent.route_to_department` | Caller requests a specific team (sales, support, billing) | `department` (strict enum) | Checks ring group / queue availability. Dispatches SIP transfer or waits. |
| `intent.route_to_person` | Caller asks for an individual employee | `person_name`, `extension` | Queries internal directory; initiates attended transfer or fallback. |
| `intent.query_company_info` | Inquiries on hours, address, access, tax ID, payment methods | `topic` (strict enum: `hours`, `address`, `access`, `payment`, `vat`) | Delivers approved verbatim FAQ response from trusted repository. |

### 3.2 Scheduling & Operations
| Intent | Description | Extracted Entities | Backend Action |
|---|---|---|---|
| `intent.check_availability` | Inquires about slots for a meeting, service, or delivery | `service_type`, `day` (normalized weekday enum), `period` | Queries the configured calendar adapter. Returns verified open slots or an explicit unavailable state. |
| `intent.book_meeting` | Schedules an appointment or site visit | `name`, `phone`, `day`, `time`, `service_type` | **Guarded tool**. Requires 2-phase Consent Guard (staging → spoken readback → confirmation). |
| `intent.reschedule_meeting` | Moves an existing appointment | `booking_id` or `phone`, `new_day`, `new_time` | Finds booking, checks slot, enforces spoken confirmation before modifying. |
| `intent.cancel_meeting` | Cancels an existing appointment | `booking_id`, `reason` | Reads back targeted booking; executes cancellation only upon unambiguous consent. |

### 3.3 Commercial & Orders
| Intent | Description | Extracted Entities | Backend Action |
|---|---|---|---|
| `intent.track_order_status` | Tracking a purchase order, delivery, or dispatch | `order_ref`, `phone` | Queries ERP/order state machine. Reports current stage without guessing dates. |
| `intent.request_quote` | Requests commercial pricing or custom quotation | `product_category`, `quantity`, `specifications` | Records a formal quote request in the CRM for human sales representative sign-off. |

### 3.4 Support & Incident Reporting
| Intent | Description | Extracted Entities | Backend Action |
|---|---|---|---|
| `intent.record_arrival_status` | Reports visitor / technician delay or absence | `status` (`late`, `cannot_come`), `delay_known` (boolean), `delay_minutes` (integer or null), `reason` | For `late`, accept a valid explicit duration or an explicit `delay_known: false` with no duration. Refuse unspecified or contradictory delay information. Persist unknown separately from zero. |
| `intent.report_issue_ticket` | Logs an incident, fault, or urgent complaint | `severity` (enum), `asset_id`, `description` | Creates structured Case/Ticket linked to customer timeline. |
| `intent.record_voicemail_message` | Leaves a detailed spoken message for an extension/service | `recipient`, `message`, `urgent` (bool) | Reads back message; stores audio + text, dispatches task notification to recipient. |

### 3.5 Control, Safety & Lifecycle
| Intent | Description | Extracted Entities | Backend Action |
|---|---|---|---|
| `intent.handoff_to_human` | Escalation to human agent or requested callback | `reason`, `preferred_window`, `phone` | Attempts a verified SIP destination or creates a durable callback request with visible ownership and state. |
| `intent.confirm_action` | Explicit affirmative response to the latest action-bound readback | Whole-turn response plus pending-action identity | Authorizes only the unchanged staged action. Consent is consumed immediately. |
| `intent.refuse_action` | Rejection or correction of stated details | Correction or negative statement | Clears pending staged action; prompts for correct information. |
| `intent.end_call` | Polite conversation closure | `reason` | Emits polite farewell adapted to time of day, then terminates SIP call. |

---

## 4. Fundamental Telephony Rules & Invariants

### Rule T-01: Refusal Enforced by Code, Never Delegated to Prompt
- **Invariant**: The LLM interprets natural speech, but never guarantees transaction validity.
- **Mechanism**:
  - Missing parameters return `{ saved: false, reason: '...', instruction: '...' }`.
  - Enums are strictly closed (e.g. weekdays must be `monday`..`friday`, not arbitrary strings).
  - Business constraints (e.g. delay without either valid minutes or an explicit unknown declaration, booking without phone number) are refused in code before reaching the database.

#### Arrival-delay amendment — 2026-09-10 (review F-010)

The former requirement that every late arrival have numeric minutes contradicted
the operator's explicit "if known" requirement and
[enterprise communications section4.5](../50-ENTERPRISE-REFERENCE/12_COMMUNICATION_RELATIONSHIP_AND_SCHEDULING.md).
This amendment replaces that numeric-only requirement, not transaction validation.
Ask for an estimate when absent; when the person cannot estimate, submit
`delay_known: false` and omit minutes or use null. Persist unknown as null with an
explicit unknown flag, never zero. A provided duration must be an integer in the
declared runtime range; legacy calls providing valid minutes without the flag
remain valid. Reject malformed values and contradictory combinations. Read back
the actual known/unknown information; recording attendance never reschedules a
booking by implication. Runtime adapters and their regression tests must be
qualified separately from this documentary reconciliation.

### Rule T-02: Action-Bound Consent Guard (Two-Phase Spoken Commit)
- **Invariant**: No irreversible state mutation (creating/deleting bookings, placing orders, issuing documents) can occur on single-turn inference.
- **Protocol**:
  1. *Staging*: Tool returns `explicit_confirmation_required` with an instruction to read back every critical detail (date, time, action, cost).
  2. *Verification*: The system checks that the agent uttered the confirmation marker and that `AgentAudioDone` fired while local playback has concluded.
  3. *Consent*: The caller must utter an allowed affirmative phrase across their entire turn of speech.
  4. *Execution*: Consent is consumed synchronously prior to DB I/O. Any change in arguments invalidates consent and requires a fresh cycle.

### Rule T-03: Transcript-Based Aizuchi & Non-Interruption
- **Invariant**: Conversational backchannels ("yes", "uh-huh", "d'accord", "はい") must not abort agent audio playback.
- **Mechanism**:
  - An Aizuchi classifier maintains the local audio queue when short acknowledgments or background noise occur.
  - Interruption is decided from the complete classified turn and playback
    state. Token count alone can neither prove an interruption nor grant consent.

### Rule T-04: Test Line Isolation (`estUnEssai`)
- **Invariant**: Test calls (*44, QA numbers, demo extensions) must never touch production business data.
- **Mechanism**:
  - The dialplan passes caller metadata (`did: test`).
  - The runtime interceptor traps all `COMMIT_TOOLS` for test calls, increments `ecrituresRefuseesEnEssai`, and instructs the model to inform the caller that the line is in test mode.

### Rule T-05: Zero State Hallucination & Graceful Fallback
- **Invariant**: The system never pretends a service succeeded when an internal dependency failed.
- **Mechanism**:
  - If the database, calendar, or external API is down (`calendar_unavailable`), the agent immediately apologizes and triggers `handoff_to_human`.
  - If an extension is offline, the switchboard displays "offline", never "available".
  - A configured loop threshold produces an explicit failure and follows the
    universe fallback policy. A live transfer is attempted only when a verified
    destination is available; otherwise a durable callback task is created.

### Rule T-06: Telecommunications Sovereignty & Privacy
- **Invariant**: Runtime exposes enforceable policy hooks and evidence needed for
  the universe's applicable telecommunications and data-protection review. The
  generic subsystem does not claim legal compliance by itself.
- **Mechanism**:
  - The universe supplies the recording/transcription notice and consent basis
    applicable to its jurisdiction and purpose. Runtime refuses activation when
    required policy material is absent.
  - Credentials (SIP passwords, provider tokens) reside exclusively in `brick-vault` and are never exposed to LLM prompts or client transcripts.
  - Configurable universe retention policy with automated TTL purge of call recordings.

### Rule T-07: Unified CRM Event Convergence (`call.completed`)
- **Invariant**: Human and AI calls converge onto the exact same operational truth model.
- **Mechanism**:
  - Every call produces a canonical `call.completed` event in the customer timeline.
  - Payload carries: `call_id`, `direction`, `caller_phone`, `resolved_contact_id`, `resolved_company_id`, `duration`, `summary`, `recording_ref`, `tasks_created`, and `causation_id`.
  - Side effects (sending email recaps, SMS confirmations) are dispatched via an idempotent outbox pattern with compensation logic on failure.

### Rule T-08: Exact Call Identity and Honest Attribution
- **Invariant**: provider, CDR, recording and conversation identifiers are kept
  in full and never joined by a shortened prefix, timestamp proximity or file
  suffix.
- A short identifier is display-only. Ambiguous historical evidence stays
  ambiguous.
- Human, AI and unknown actors are distinct. Mono diarization may label numbered
  speakers but cannot invent an employee or customer identity.

### Rule T-09: Audio, Transcript and Work States
- **Invariant**: the same call detail and object timeline expose recording,
  transcript and follow-up state.
- Transcript lifecycle is explicit: `pending`, `available`, `failed`,
  `unavailable` or `too_short`. Analysis availability is a separate fact.
- Post-call processing is durable and idempotent. Queue owns work lifecycle;
  the voice adapter performs transcription; Logger receives metadata and
  correlation only; Maestro detects stalled or orphaned work.
- Audio, transcript text, credentials and unrestricted personal data never
  enter Queue or Logger payloads.

### Rule T-10: Layered Telemetry and Failure Isolation
- **Invariant**: every brick keeps detailed technical logs locally and emits a
  small normalized event stream to the universe Logger.
- Every normalized event carries universe, brick, family, severity, event name,
  timestamp and correlation identity. Families are `operational`, `security`,
  `audit` and `business`.
- Logger unavailability must not stop a call. The emitting adapter keeps a
  bounded local spool and retries; overflow is explicit. Secrets and content are
  removed before persistence.
- A health response proves reachability only. Completion requires persisted
  evidence, terminal state and correlation across the participating bricks.

## 5. Generic Core and Universe Profiles

Shaper Vox owns call contracts, adapters, lifecycle, authority hooks, observability
and Workspace primitives. A universe profile owns terminology, branding, routing,
opening hours, destinations, notices, prompts, retention values and domain rules.

Clinic therefore remains a specialization. Its medical refusals, Japanese clinic
dialogue, appointment vocabulary, extensions and exact notice wording must not be
copied into the generic core. What Clinic has proven can be promoted only after it
is expressed as a parameterized contract and tested without Clinic fixtures.

---

## 6. Verification & Acceptance Protocol

1. **Automated Twin-Agent Bench**: Dual Voice-Agent setup (`banc.js`) executing
   the entire declared intent suite without physical telephony hardware. For a
   bounded profile trial, record every supported intent and every exclusion;
   all supported intents must run. This does not qualify the entire catalog:
   full catalog acceptance additionally requires its omitted suites. This
   clarification (2026-09-10, F-012) follows section3's selectable profile scope
   and never allows a failed supported intent to become an undeclared exclusion.
2. **Consent Guard Suite**: 100% test pass on staging, readback markers, whole-turn affirmative matching, and refusal on backchannel/noise.
3. **Dialplan Contract**: Verification that test extensions cannot mutate real database objects.
4. **Latency Budget**: Measure provider and local intervals separately. Each
   universe declares an acceptance target from observed distributions; no single
   threshold is claimed universally.
5. **Identity regressions**: prefix collisions, older retained calls, recording
   lookup and contact ambiguity cannot return another call or person.
6. **Post-call lifecycle**: persisted transcript state, Queue terminal state and
   Logger correlation agree; a dependency failure remains visible and retryable.
7. **Logger outage**: a synthetic outage proves calls continue, the bounded spool
   is observable, and metadata is replayed without content or secrets.
