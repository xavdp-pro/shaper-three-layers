# Object Space, Files and RAG

## From filesystem-centric to context-centric

The filesystem remains a useful human view, but it is not the whole organizational model.

```text
File path
+ object identity
+ metadata
+ relations
+ versions
+ permissions
+ provenance
+ semantic representations
+ events/audit
```

## Managed object states

An external file can be treated at several depths:

- **Visible** — Shaper knows a reference/path exists.
- **Indexed** — metadata/content representations are searchable under policy.
- **Managed** — Shaper owns the governed encrypted object/version lifecycle.

Deployments can choose how aggressively to import existing filesystem estates.

## Document ingestion

```text
source file
→ provenance + hash
→ security/policy checks
→ encrypted object storage
→ text/metadata extraction
→ classification/entity relations
→ full-text + semantic indexing
→ context links
→ events/audit
```

Derived representations should point back to the canonical source/version.

## RAG authorization

Retrieval must obey object permissions. It is a security defect if an unauthorized object can influence an answer even when its filename is hidden afterward.

## Search modes

One search experience may combine:

- exact names;
- structured filtering;
- full text;
- semantic retrieval;
- graph neighborhood;
- time/history;
- agent-generated synthesis.

Keep evidence/source links available.

## Versioning

Documents can have mutable working versions and immutable/signed milestones according to policy. Retention/legal-hold requirements may override normal deletion.

## Derived indexes

Vector/search/graph projections may be rebuildable. Their lifecycle should not silently change canonical object history.

Re-indexing should preserve which source version produced each derived chunk/embedding.

## Context

A context is not a folder. It is a connected working set.

Example:

```text
Customer ACME
→ contacts
→ contracts
→ messages
→ meetings
→ invoices
→ tasks
→ decisions
→ external sources
```

Folders can still render a convenient hierarchy over this graph.

## Success criterion

The user retains familiar file ergonomics while the organization gains semantic, relational, permission-aware and historically traceable knowledge.
