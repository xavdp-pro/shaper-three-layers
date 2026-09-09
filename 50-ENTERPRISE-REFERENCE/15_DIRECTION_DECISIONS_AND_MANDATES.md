# Company direction, social life, decisions and mandates

Status: proposed functional boundaries following Xavier's 2026-09-09 request.
Names below are proposals, not existing brick identifiers or deployed services.
This document extends references 12–14 without changing source archives.

## Names and boundaries

| Human-facing name | Proposed package name | Responsibility |
| --- | --- | --- |
| Vie d'entreprise | company-social | Announcements, posts, comments, discussions and targeted audiences |
| Orientations | company-direction | Purpose, objectives, priorities, desired outcomes, owners and review dates |
| Registre des décisions et mandats | decision-registry | Authoritative records of decisions, agreements and bounded authorizations |

These can be separate modules in one interface. Do not prescribe one process,
database or LXC per module. Reuse shared identity, objects, relationships, search,
notifications and evidence instead of creating competing registries.

An orientation explains what the company wants and why. A discussion explores
options. A decision records what an authorized actor decided. A mandate grants
bounded authority to act. A project organizes delivery. An event records what
actually happened. These concepts link to one another but are not interchangeable.

## Ownership across layers

Shaper OS supplies governance principles. Runtime stores and enforces decision
and mandate state, authority, scope and history. Workspace exposes the register,
direction pages and social feed. Business packages provide domain vocabulary
and workflows. The social feed may announce a decision by reference; its text
must not become a second editable source of authority.

## What belongs in the register

- Human-to-human decisions: ownership assignments, organizational rules, approved
  exceptions, agreed processes and commitments.
- Human-to-agent mandates: one-time approval or standing permission to perform
  specified operations under specified conditions.
- Authorized agent decisions within an existing mandate, with the parent mandate
  and execution evidence linked. An agent proposal alone is not an approval.
- Agreements requiring multiple parties: explicitly track whose acceptance is
  required and obtained. Silence and reading a post are not acceptance.

Do not duplicate every task, message or technical event in this register. Keep
the governing decision and link its tasks, discussions, executions and evidence.
Decisions do not have to grant a capability: assigning a business priority is
different from authorizing a tool operation.

## Minimum decision record

Record stable identity and version; title and type; author, accountable owner and
actual approving authority; organization and affected scope; rationale; source
discussion/evidence; affected parties and objects; adoption time, effective period
and review date; confidentiality/audience; status; and supersession/revocation links.

Distinguish proposal, awaiting required approvals, adopted, rejected, superseded,
revoked and expired. A future adopted decision may not yet be effective. Preserve
prior versions and who changed what; editing history cannot silently change the
authority under which a previous action occurred.

For a mandate additionally record grantee, allowed operations/resources, trigger,
conditions, limits, duration, exception handling, notification requirements,
delegation permission and revocation owner. Omitted capabilities are not granted.
The granting actor must have the authority to grant that scope. Declared knowledge,
responsibility and technical capability are not substitutes for permission.

## Example standing mandate

An authorized owner approves processing standard price updates from one supplier.
The mandate identifies that supplier and mailbox, permitted price-history writes,
the allowed format, an agreed margin threshold, the responsible agent/service,
review date and notification rules. It explicitly withholds approval for other
suppliers, unexpected formats or threshold breaches.

Each run references the exact mandate version and records its result. On an
exception the agent requests review. Revocation prevents subsequent authorizations;
define cancellation/checkpoint behavior for already-running work and do not pretend
revocation reverses completed external actions.

## How a new agent learns the current company decisions

Provide a permission-filtered, scope-specific current-decision view using the
existing Runtime contract conventions. It supplies effective applicable decisions,
mandates granted to that actor, conditions, expiry/review information, conflicts
and links to complete versioned source records.

This is not a dump of every confidential company decision into every agent's
context. Humans and agents see only what they are entitled to know. Summaries
carry source versions and freshness and never grant authority. Runtime rechecks
the current mandate and permission when an action is requested, even if the agent
previously read an approval. New agents do not inherit another agent's grants
merely by replacing it; grants target explicitly defined identities/roles/services.

When applicable decisions conflict, flag the conflict and use the established
governance escalation path. Do not invent automatic 'newest wins' precedence.
Expose current applicable decisions separately from historical explanations of
why an older operation was allowed.

## Human interface and connections

Provide Current decisions, Pending approvals, Mandates/automations, Review due
and History views. Filter by team, project, person/agent, business object, scope,
type and status. A record shows rationale, approvers, effective conditions,
linked work, execution evidence and authorized amend/revoke actions.

The company social feed announces approved directions/decisions and collects
feedback. Explicit acknowledgements remain separate from read status and approval.
Orientations link to their adopted decisions and implementation projects. Projects
link tasks/results back to those decisions. Notifications deliver changes to the
correct audiences. Search declares decisions, mandates and orientations as
searchable objects with field- and record-level permissions.

## Implementation checklist

- [ ] Inventory existing decision, agreement, mandate and authority code; extend
  the existing Runtime mechanisms instead of introducing a competing policy engine.
- [ ] Define record/state/version contracts and decision versus mandate semantics.
- [ ] Check approver authority, required acceptances and explicit scope limits.
- [ ] Implement amendment, supersession, expiry and revocation without erasing history.
- [ ] Provide scoped current-decision retrieval and current action-time enforcement.
- [ ] Define conflict escalation and running-operation revocation behavior.
- [ ] Deliver the five register views and links to social feed/direction/projects.
- [ ] Register searchable objects and deduplicated targeted notifications.
- [ ] Prove an agent can explain an automation using its actual mandate/evidence.
- [ ] Prove revocation blocks a subsequent action despite cached agent context.
- [ ] Prove unauthorized actors cannot discover private decisions or self-authorize.
- [ ] Prove a social comment/read receipt cannot become an adopted decision.

First slice: one human-approved one-hour appointment reminder mandate, exact
calendar/service scope, expiry/revocation, linked reminder outcome, and explanation
in the register. Other business automations remain separately configured.
