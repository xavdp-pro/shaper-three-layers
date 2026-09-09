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

### Searchable object declaration — Xavier's clarification

Xavier states that the existing quick search is in a CRM already delivered to a
customer. Treat it as a reuse source to locate and inspect, not as an application
to modify for this work. The required evolution is a common inter-brick object
declaration protocol, rather than a central list of hard-coded CRM searches.

An object type explicitly declares whether it is searchable. Opt-in does not
make all its fields searchable, nor grant anyone access to its records. A type
may expose only a safe subset of fields and apply per-record eligibility rules.
Contacts, addresses, parties, products and other business types participate by
declaration, without adding provider/module conditions to the search interface.

Proposed conceptual declaration (field names are illustrative, not an adopted
wire protocol):

```yaml
declarationVersion: 1
owner: relationships
objectType: contact
objectSchemaVersion: 1
searchable: true
identity: stable-object-id
fields:
  - name: displayName
    modes: [exact, text]
    display: title
  - name: phone
    modes: [exact]
    normalization: phone-number
  - name: organizationId
    modes: [filter]
relations: [organization, address]
authorization: runtime-current-record-and-field-policy
projection: permitted-contact-summary
resolver: canonical-contact-detail
updates: versioned-upsert-and-delete-events
```

The declaration must identify ownership, schema/contract version, stable object
identity, queryable/filterable fields and normalization, permitted projection,
relation references, detail resolver and update/deletion behavior. If semantic
indexing is supported, eligible fields and processing constraints are declared
separately. Sensitive fields and arbitrary object payloads are not indexed by default.

Runtime validates and registers declarations from installed authorized bricks.
Unknown/incompatible versions fail explicitly. A brick cannot register itself as
owner of another brick's object type or supply executable code through metadata.
Keep contract capability references separate from arbitrary URLs or expressions.

Registration lifecycle includes discovery, validation, activation, schema migration,
deactivation and removal. Updates carry record versions; duplicate/out-of-order
events do not restore stale or deleted records. Authorization is checked at query
and detail/action access, including relation previews. Removing a declaration or
setting searchable false withdraws its results and schedules index cleanup.

The contract must support a declared retrieval strategy (index, source query or
hybrid) without prescribing one engine. Each source reports availability, index
freshness and pagination behavior. Cross-brick identity and relations let the
aggregator group related records without merging distinct objects such as a
contact and its address. Display/action metadata never confers action permission.

- [ ] Locate the delivered CRM search with repository/revision and reuse rights;
  inspect an isolated source copy without changing the customer's deployment.
- [ ] Define and validate the searchable declaration schema with existing Runtime
  conventions; publish versioning and compatibility rules before implementation.
- [ ] Register contact, address and product declarations as the first examples.
- [ ] Prove a new declared object type appears without editing central search/UI
  routing, while respecting permitted field projections and record eligibility.
- [ ] Test activation/removal, searchable=false, migration, deletion, duplicate
  events, current authorization and a disconnected source.

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
