# Unified quick search

Status: functional requirement clarified by Xavier on 2026-09-09. Reuse the
existing co-produced quick-search implementation after locating and reviewing it;
its source and current proof are not established by this document.

## Intent

One quick-search entry aggregates authorized objects across the organization's
enabled subsystems: people, organizations, customers/suppliers, contacts, teams,
services, projects, tasks, appointments, products, orders, quotes, invoices,
documents, emails, calls, transcripts, messages, decisions and announcements.
The interface must not require the user to select a module before searching.
Unavailable modules contribute no fabricated results.

## Shared contract and ownership

Each participating subsystem declares searchable object types, stable identities,
canonical links, permitted summaries, filters and supported contextual actions.
Runtime enforces organization boundaries and current permissions before returning
titles, snippets, counts, facets or suggestions. Workspace renders the results.
Search indexing does not become a second authority or source of business truth.

Return object identity/type, title, relevant excerpt, related party/project,
source, useful date, canonical detail link and permitted actions. A party with
both customer and supplier roles appears as one entity with both roles. Related
calls/documents remain distinct objects linked to it; do not collapse their history.

## Human experience

- Provide an always-accessible search field/launcher on web and mobile, with
  keyboard navigation on desktop and appropriate touch interactions on mobile.
- Start with mixed ranked results; offer type, date, person/organization, project
  and service filters plus grouping when useful. Preserve the query on navigation.
- Search names, normalized phone numbers, email addresses, business references,
  document content and transcripts when those sources are enabled and indexed.
- Support exact identifiers and lexical matching as a reliable baseline;
  semantic matching is an optional capability, never a substitute for exact lookup.
- Show source context and a preview; opening a result reaches the actual record,
  call/transcript detail, document or discussion.
- Offer relevant actions such as call, open conversation, view appointment or
  create a linked task, subject to current authorization and confirmation rules.
- Display loading, no matches, partial results, unavailable sources and indexing
  delay distinctly. Bound retrieval with pagination and cancellation of stale queries.
- A search is read-only. Selecting a result must not place a call or trigger an
  external action without the separate action request.

Helm should use the same governed search capability so voice/text and manual
search refer to the same objects. Mobile search follows the same permission and
object-link contract; it does not require installing all business modules locally.

## Acceptance and reuse checklist

- [ ] Locate Xavier's existing search code and record repository, revision,
  supported sources, tests and reusable behavior before choosing changes.
- [ ] Define the shared result/source registration contract using existing
  Runtime conventions; avoid coupling core search to a fixed module list.
- [ ] Searching a known customer returns its party record and relevant permitted
  appointments, calls, documents and messages with correct detail links.
- [ ] Searching a phone/reference finds exact matches and handles ambiguity.
- [ ] Customer/supplier dual role does not produce duplicate party identities.
- [ ] Revoked access removes restricted titles/snippets/counts, including cached
  results, suggestions, previews and direct object retrieval.
- [ ] Deletions and updates propagate to the index; opening stale hits handles
  missing objects honestly. Recent/private searches follow user and tenant scope.
- [ ] An unavailable source yields explicit partial results without blocking all
  other sources; a slow old query cannot replace a newer query's results.
- [ ] Keyboard/mobile navigation and authorized contextual actions work end to end.
- [ ] Prove one cross-source query in the telephony demo before extending coverage.

First telephony slice: contact/organization, team/service, appointment, call,
transcript and team message. Extend through the same contract to ERP, documents,
email, projects and social feed as those subsystems become available.
