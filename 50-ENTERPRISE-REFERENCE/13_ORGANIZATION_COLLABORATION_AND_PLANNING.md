# Organization, collaboration and planning

Status: functional intent added by Xavier on 2026-09-09. This is a conceptual
extension, not a statement of implemented features. It complements reference 12.

## Organizational structure

Provide a reusable organization primitive and operator interface: departments,
teams, positions, people, memberships, reporting relationships, responsibility
and temporary delegation. Membership and assignments can be dated; one person
may participate in several teams or projects. Vacancies and substitutes must be
representable. Organizational hierarchy, project responsibility and authorization
are distinct: a reporting line alone must not grant data access or execution rights.

Services used for call routing, shared inboxes and notifications should reference
the same organizational identities. Do not create independent copies of support
or sales in every subsystem. Operational destinations may differ from reporting
units, with explicit links and authorized members.

## Projects and planning

Link projects, milestones, tasks/subtasks, dependencies, owners, participants,
priorities, due dates, capacity and calendar commitments to organizational people
and teams. Offer appropriate list, board and timeline views over the same objects.
An appointment is a calendar object; a project task may reference it without
becoming a duplicate appointment. Handle reassignment, absence, overdue work,
dependency changes and conflicting resource allocation visibly.

Directions can lead to objectives, projects and tasks, with links preserving why
work exists. Changes to an announcement must not silently rewrite approved plans.
Automatic scheduling or task creation requires explicit policy/mandate; a proposed
plan remains distinguishable from an accepted commitment.

## Three complementary communication surfaces

| Surface | Purpose | Shared links |
| --- | --- | --- |
| Internal chat | Direct/team/project conversations, attachments and collaboration | People, teams, projects, tasks, decisions |
| Customer web chat | External widget/portal, visitor/customer conversation, human or AI reception and handoff | Party/contact, service inbox, communication timeline |
| Internal social feed | Company/team announcements, management directions, discussions and feedback | Author, audience, objective, decision, project and acknowledgement |

Reuse identity, messages, attachments, subscriptions, permissions and notifications
where appropriate, while preserving distinct external and internal visibility.
Sharing a conversation does not expose internal notes to customers. A visitor may
be unknown; link identity only on sufficient evidence. Support human/AI attribution,
availability, assignment, unread state and recovery of unattended customer chats.

The social feed provides official announcements, pinned notices, comments,
targeted audiences, publication dates and revision history. Distinguish informal
discussion, an official direction and a recorded decision. Read receipts are not
agreement; explicit acknowledgement is separately recorded when requested.
An AI summary or suggestion is not an instruction from management.

## Cross-subsystem workflows

1. Management publishes a direction to a declared audience; authorized recipients
   are notified, with acknowledgement if required.
2. A responsible person links it to an objective/project and proposes a plan.
3. Accepted tasks reference real owners and calendars; changes remain traceable.
4. Team discussion and customer exchanges attach to the appropriate work objects.
5. Results, exceptions and decisions feed back to project status and permitted
   company/team views, without leaking restricted customer or employee data.

Telephony follows the same organization graph: an AI receptionist can resolve a
service, find permitted available recipients, transfer or leave a team message.
The telephony baseline requires only the necessary organization/team subset;
full project planning, customer chat and social feed are separate increments.

## Acceptance and implementation checklist

- [ ] Inventory existing organization, project/planning and chat code before
  creating new implementations. Identify the previously discussed planning tool;
  its name/source is not established by this clarification.
- [ ] Define shared organizational identities and dated membership/delegation.
- [ ] Link service routing/inboxes to this graph without duplicating teams.
- [ ] Define project/task/milestone ownership, dependency and calendar links.
- [ ] Deliver internal conversations with explicit team/project visibility.
- [ ] Deliver web customer chat with service assignment, human/AI handoff and
  complete communication history; internal comments remain private.
- [ ] Deliver announcement feed with audience, author, revisions, comments,
  pinned notices and optional explicit acknowledgement.
- [ ] Link direction → decision/objective → project → task → result.
- [ ] Reuse notification delivery and deduplication across these surfaces.
- [ ] Verify membership changes and role revocation, multi-team participation,
  absent owner replacement and external/internal visibility boundaries.
- [ ] Verify an announcement edit cannot silently alter an accepted plan, and
  a chat message cannot execute an action without its required authorization.

Modeling refinements such as dated delegation, separate acknowledgement and
visibility boundaries are proposed safeguards supporting Xavier's requested
features. They do not prescribe a database or override the existing layer rules.
