# Communication, relationship and scheduling foundation

Status: functional intent captured from Xavier on 2026-09-09. This is a design
requirement, not an implementation or deployment claim. It extends the enterprise
reference; source archives remain unchanged. Proposed modeling choices below
must be translated into brick intents, rules, contracts and tests before coding.

## 1. Multilevel intent

Preserve proven co-produced code. Extract reusable primitives, compose bricks
into useful subsystems, then specialize business behavior and branding for each
project. The furniture reseller is one such specialization. A subsystem must
already perform useful default workflows; it is more than empty extension points.

Shaper OS owns governance principles. Runtime owns identity, relationships,
permissions, schedules, operations and evidence. Workspace owns human interfaces.
Packages supply domain behavior. Nested composition does not require nested LXCs.

## 2. Unified relationship model — proposed design

Represent a party as a person or organization. Customer and supplier are roles
of a party in a relationship, and may coexist. Do not duplicate an organization
because it both buys and sells. Prefer role composition over an exclusive
Customer/Supplier inheritance tree; the storage technology is not prescribed.

Parties link to contacts, dated contact methods, zero or more known sites/addresses,
employees, services, appointments, communications, tasks and business objects.
Support multiple physical/billing/delivery sites and contact-to-organization
relationships. Unknown addresses must not prevent taking an initial message.
Capture required physical/legal address information at the relevant business step.

Human accounts and customer contacts are different concepts. An employee may have
an account and several devices; a contact need not have an application account.
Phone numbers can be shared or reassigned. Normalized caller-number matching is
a lookup hint, not authentication. Greet a unique recognized caller by name when
appropriate, confirm ambiguous matches, and do not disclose protected context
solely because the caller number matches. Preserve merge history and attribution.

## 3. Minimal subsystem dependencies

The operator-ready telephony package requires minimal relationships, calendar,
identity/permissions, media/transcripts, service mailboxes, in-app notifications
and evidence. An individual IPBX brick need not depend on the entire CRM/ERP.
Use shared contracts without circular coupling between CRM and telephony.

Email, SMS, payment and mobile push are optional adapters/packages. The telephony
demo must work without them and show honestly when a channel is unavailable.
Scheduling and queued reminder jobs need durable state and a clock even when no
external notification channel is enabled.

## 4. Default call scenarios

1. AI reception using the current Deepgram adapter: greet, determine purpose,
   take a qualified message or book an appointment against actual availability.
2. Conversational routing: ask who/service the caller wants, resolve a declared
   destination, offer permitted choices and transfer. No hard-coded DTMF tree is
   required for this slice; keep fallback and accessibility behavior explicit.
3. Human reception during configured hours; AI takes over outside those hours or
   after timeout/unavailability. Allow configured AI-first reception as well.
4. Human-to-human internal/external calling, transfer, hold/resume and termination.
5. One-hour appointment reminder: ask whether the person expects to be on time;
   if late, ask the estimated delay if known; offer a message to the team. Store
   unknown delay distinctly from zero. Do not silently reschedule the appointment.
6. Missed/unanswered call: create a visible message or callback item with an owner.

These supported baseline operations require real hooks: contact lookup, availability,
booking, message creation and transfer. Optional business reaction hooks remain
disabled by default. Do not claim the default workflow works with placeholder hooks.
Deepgram performs its configured voice interaction; the universe validates every
tool request and enforces permission, confirmation and idempotency.

## 5. Record → transcribe → analyze → follow up

The intended coverage includes AI and human calls, incoming and outgoing. Capture
audio under the configured recording/notice/access/retention policy. Represent
refusal, unavailable media and processing failures explicitly; never claim every
call was recorded when capture did not occur.

Persist complete call/leg identity, direction, actual initiating/answering actors,
participants, service destination and timestamps. Link media, transcript versions
and analysis to the same communication. Each processing stage has pending,
running, completed, failed or unavailable status, with bounded retry/idempotency.
Keep speaker inference separate from confirmed actor identity.

Default agent analysis produces a summary, reason, intended recipient, extracted
facts with source links, uncertainties and suggested follow-up. Possible urgency
is a review flag, not a guaranteed detector or domain-specific emergency decision.
No automatic external business action follows an analysis by default. Team inbox
delivery and internal notifications are explicit baseline operations.

Humans can add comments, their own analysis and actions with author, date, reason
and visibility. Agents can add attributed versioned analyses. Keep original audio
and transcript references distinct from interpretations; corrections retain trace.
Both humans and agents may request later actions, governed by role and mandate.
Reprocessing must not resend notifications or recreate tasks unintentionally.

The same communication/annotation/action mechanism can later attach to a supplier,
purchase, product or order. Do not bake customer-only assumptions into its contract.

## 6. Calendar and reminders

Provide a minimal Calendly-like booking experience: event types, duration,
availability, assigned people/resources, time zone, exceptions/holidays, buffers,
booking horizon, conflict prevention and concurrency-safe slot confirmation.
Support booking, confirmation, cancellation and rescheduling with history and
permissions. Distinguish provisional bookings from confirmed appointments.

Reminder rules are relative to event time and channel: e.g. email one day before
when email is enabled; call one hour before for the telephony demo. Changes or
cancellations invalidate obsolete jobs. Handle time zones/DST, retries, delivery
status, duplicate suppression and quiet-hour/contact preferences. An unanswered
reminder must have a visible outcome and bounded retry policy.

Payment-before-booking is an optional future connector: define pending/paid/failed/
expired states, slot-hold expiry, webhook idempotency and cancellation/refund policy.
Do not make payment a dependency of ordinary calendar or telephony use.

## 7. Services, inboxes and notifications

A service such as support or sales has routing destinations, members, schedules,
message inbox, owner/assignment rules and access policy. Personal inboxes are also
supported. A message for support remains addressed to support even if one member
reads it. Distinguish unread/read, assigned, acknowledged and resolved; two people
must not unknowingly perform the same callback.

The notification primitive accepts a source event, recipient/audience, template,
priority, deduplication key and deep link. Channels include in-app, email, SMS,
voice call and mobile push, each advertising availability and delivery status.
Delivery is not human acknowledgement. Avoid notification-to-call feedback loops.

An eventual mobile application provides a unified notification inbox for permitted
business and universe-administration events. Enforce separate audiences/permissions,
scoped subscriptions and private lock-screen payloads; acknowledge/read state
synchronizes with the web inbox. Reuse the existing mobile client where suitable.

The email brick must support personal and shared mailboxes, starting with a general
contact mailbox and two fictional user mailboxes for tests. Inspect Xavier's custom
webmail source before choosing an implementation. Its location/integration remains
to be identified. Credentials and real addresses do not belong in seed profiles.

## 8. Operator interface required from Gemini

| Area | Minimum usable content |
| --- | --- |
| Today | Missed calls, new messages, callbacks, next appointments and failed reminders |
| Calls | Direction, actor, caller/contact, service, time, outcome and processing states |
| Call detail | Audio player, transcript, attributed analyses/comments, destination, actions and evidence |
| Contacts/organizations | Roles, people, numbers, sites and complete linked timeline |
| Calendar | Availability, bookings, assigned person, changes and reminder outcome |
| Reception/routing | Human/AI hours, exceptions, timeout, fallback and service directory |
| Messages | Personal/team inboxes, assignment, acknowledgement, callback and resolution |
| Team/devices | Users, roles, services, extensions, registered devices and presence |
| Notifications | Bell with unread count, filters, read/acknowledge, deep links and preferences |
| Administration | Enabled integrations, processing failures, retention, brand and permissions |

Keep user vocabulary clear; expose advanced settings progressively. Preserve
Gemini's visual work while organizing these journeys. Show absent optional modules
as unavailable rather than exposing nonfunctional controls. All actions need
loading, empty, failure and success states and appropriate translations.

## 9. Acceptance and scope boundaries

- Unique known caller, unknown caller and shared number resolve appropriately.
- Support message reaches authorized members, preserves its destination and owner.
- Human and AI calls both produce correctly linked recording/transcript/analysis
  or explicit failure states. Audio timing is not inferred from transcript arrival.
- Two callers cannot confirm the same capacity-one slot.
- Appointment changed after scheduling produces no stale or duplicate reminder.
- One-hour call captures on-time/late/unknown/message without unauthorized rescheduling.
- Human/AI schedule respects exceptions and fallback; unreachable transfer is recoverable.
- Human comment and agent interpretation remain distinguishable and reviewable.
- Disabled email/SMS/payment/mobile adapters do not block the core telephony demo.
- Role revocation removes protected recording/contact access; cross-organization
  data is not exposed. Deletion/retention includes derived transcripts/analyses.
- Swapping a client brand or business profile does not fork generic subsystem code.

Future examples, not default enabled actions: order-ready calls, supplier follow-up,
urgency-based escalation, paid coaching appointments and administrative mobile alerts.
Require an explicit workflow/mandate and channel configuration for each.
