# Shaper Workspace — Master Architecture

## Purpose

Shaper Workspace is a portable, agent-native organizational work environment that runs above a Host OS. It should feel like a desktop/workspace, not merely a collection of web pages, while deliberately refusing to recreate every specialist desktop application.

The Workspace's job is to make the organization usable: context, objects, people, apps, agents, search, voice and controlled external surfaces.

## 1. Product proposition

```text
Host device may change.
The organization's work environment persists.
```

A user can move from Windows to macOS or Linux, enroll a new device, authenticate and recover the same Workspace state as policy permits.

The host is replaceable; the organizational universe is durable.

## 2. Technology stance

### Flutter + Dart

Use Flutter/Dart as the default Workspace shell because it provides a common UI language across desktop, mobile and web while still allowing native integration.

Dart should own what is natural in the UI/client layer. Do not force the entire backend/security stack into Dart merely to use one language.

### Native adapters

When needed, use platform adapters/FFI/native services for:

- multi-window/display behavior;
- secure key storage;
- audio devices;
- file picker/import/export;
- process/native app gateway;
- WebView/web engine;
- OS notifications;
- device features.

## 3. Workspace is a shell over contexts

Traditional desktop:

```text
apps + windows + filesystem + browser
```

Shaper Workspace:

```text
CONTEXTS + OBJECTS + AGENTS + SURFACES
```

Applications, windows, files and web pages remain available but are subordinate views of context rather than the only organizing principle.

## 4. Minimal user vocabulary

The default navigation should remain comprehensible with:

- Workspace;
- Spaces;
- People;
- Agents;
- Files;
- Apps;
- Search.

Deep architecture remains available in Steward tools, not in ordinary menus.

## 5. Context as the work unit

Opening `ACME` may produce a composed surface:

```text
ACME
├── people
├── communications
├── contracts
├── orders/invoices
├── tasks
├── decisions
├── web/external sources
└── agents / suggested actions
```

The user should not have to remember which legacy application “owns” each fragment.

## 6. Surface model

A Surface is a renderable interaction type such as:

- document;
- table/grid;
- form;
- dashboard;
- graph;
- task board;
- chat;
- terminal;
- image/PDF viewer;
- web surface;
- media player;
- agent activity/explanation.

Surfaces can be arranged as windows/panels on one or several screens.

## 7. Multi-window and multi-monitor

Multi-screen work is a first-class requirement, not a later desktop enhancement.

The Workspace model should store logical placement independent of physical display IDs.

```text
Workspace Layout
├── Surface Group A → preferred primary display
├── Surface Group B → preferred secondary display
└── Surface Group C → optional third display
```

When screens disappear, remap surfaces without losing state. When known screen topology returns, restore preferred layout where safe.

Do not couple business state to window geometry.

## 8. Files as a familiar projection

Users may browse folders/files, but internally Workspace interacts with Runtime objects.

The same document can be discovered by:

- filename;
- content;
- customer/context;
- date;
- person;
- semantic question;
- graph relation.

This preserves familiar ergonomics while enabling object-space behavior.

## 9. Host file import

Workspace does not need permanent unrestricted filesystem attachment.

Default model:

```text
user selects external file
→ host picker grants bounded access
→ Runtime import gateway
→ scan/hash/classify/encrypt/index/link
→ Shaper object
```

After import, normal work happens on the Shaper object. The host original may remain external and unmanaged.

## 10. Export and external-native application gateway

Shaper does not recreate DaVinci Resolve, Photoshop, Blender, CAD tools or every specialist editor.

When policy permits:

```text
Shaper object
→ authorized temporary export
→ native specialist application
→ save
→ controlled re-import
→ new object version + provenance
```

Temporary data should be cleaned according to policy.

## 11. Web Surface

The Web is a surface, not the Workspace's operating center.

Use an existing web engine/WebView. Do not build a browser engine.

Default trust boundary:

```text
WEB SESSION
│
├── isolated browser state/profile as policy requires
├── controlled upload
├── controlled download/import
├── controlled clipboard
└── explicit optional device capabilities
```

The webpage does not automatically receive Shaper objects, credentials or agent context.

## 12. Web Agent

Agents may search/fetch/use web resources without requiring the human to operate a tabbed browser. When source inspection or interactive authentication is needed, a visible Web Surface can be opened.

This allows three modes:

1. **Web as knowledge source** — agent retrieves and cites.
2. **Web as inspectable source** — human opens original.
3. **Web as interactive external system** — isolated session with controlled crossings.

## 13. Voice

Voice is a first-class interface:

```text
microphone
→ audio service / VAD
→ STT
→ agent/router
→ action/result
→ optional TTS
```

Keep audio pipeline services replaceable so local or remote STT/TTS can be selected per deployment.

## 14. Dynamic applications

The Workspace renders declarative Shaper App Schemas provided by Runtime.

Trusted primitives include:

- table;
- form;
- document;
- chart;
- dashboard;
- workflow;
- object query;
- relation;
- action;
- notification;
- agent interaction.

An agent can create or reshape a business app without recompiling the Workspace client when the required behavior fits the schema.

## 15. Specialist plugin escape hatch

If the declarative model is insufficient, plugins may exist but should be:

- signed/trusted according to deployment;
- sandboxed;
- capability-limited;
- versioned;
- auditable;
- crash-contained where practical.

Generated arbitrary code is not the default app model.

## 16. Search

One search entry should cross the authorized organizational object space:

- names/filenames;
- structured records;
- full text;
- semantic knowledge;
- conversations;
- tasks;
- decisions;
- applications/actions.

Results should expose context and provenance rather than only a ranked title list.

## 17. Agents in the UX

Agents should appear as actors that can explain what they know, what they intend to do, what they are allowed to do, and what happened.

Do not make users learn prompt engineering as a prerequisite for routine work.

Useful patterns:

- “prepare X”;
- “show me why”;
- “compare”;
- “what changed?”;
- “what needs attention?”;
- “do this under these conditions”;
- “stop/pause/revoke.”

## 18. Notifications

A notification should take the user directly to actionable context.

Avoid:

```text
alert appears → user searches three apps to discover what it means
```

Prefer:

```text
alert → related object/context → reason → suggested/available action
```

## 19. User and Steward surfaces

Default distribution may separate:

### Shaper
Normal work client: Workspace, Files, Apps, Agents, Search, business actions.

### Shaper Steward
Governance/administration: identity, devices, policies, capabilities, audit, trust, infrastructure, recovery.

High-security deployments may use separate binaries/packages. The real authorization boundary remains Runtime policy and cryptographic identity, not the presence/absence of menu items.

## 20. Local security posture

Workspace UI should be unprivileged where possible. It should not hold master keys or direct infrastructure privileges.

Preferred local composition:

```text
Workspace UI
   │ authenticated IPC
   ▼
Secure Runtime / Broker
   ├── key access
   ├── encrypted cache
   ├── device identity
   ├── network/session
   └── controlled gateways
```

A compromised host with sufficient kernel/root privileges may still observe active plaintext/memory. Do not claim impossible hermeticity. Reduce exposure and make persistent theft difficult.

## 21. Local data modes

### Online terminal
Minimal persistent local data. Server is source of truth.

### Hybrid
Encrypted working-set cache and offline-pinned objects.

### Sovereign workstation
Local full Runtime/data as an explicit deployment topology, optionally syncing elsewhere.

One UI model should serve all three where feasible.

## 22. Browser/web deployment

Flutter Web can provide a Workspace projection but browser sandbox limitations mean it cannot equal native desktop capabilities such as unrestricted local process/file/device access.

Capability negotiation should allow the same app/context to degrade gracefully rather than pretend the platforms are identical.

## 23. Host device gateway

The Workspace may request controlled access to:

- printer;
- scanner;
- camera;
- microphone;
- barcode reader;
- smart card;
- USB/serial equipment;
- other supported host capabilities.

Host-specific drivers remain the Host OS responsibility.

## 24. Update model

Enterprise desktop deployment needs:

- signed releases;
- version/channel policy;
- atomic update where supported;
- rollback;
- fleet visibility;
- compatibility negotiation with Runtime.

Steward should be able to inspect deployment state across devices.

## 25. Accessibility and fallback

An agentic UI must remain usable without agents for core tasks. Important information and actions need keyboard/accessibility support and deterministic interfaces.

Agent assistance is an enhancement to agency, not a single point of usability failure.

## 26. Interface to Runtime

Workspace requests data/actions through explicit Runtime contracts. It does not become the source of truth or authorization engine.

Workspace must be able to display:

- denied action reasons;
- pending approval;
- offline/stale state;
- uncertainty/trust warnings;
- conflict resolution;
- action history and provenance.

## 27. Interface to Shaper OS

Workspace embodies the kernel pedagogically:

- reality/context before conclusions;
- visible distinction between proposal and executed result;
- human STOP/cancel/revoke paths;
- reversible shaping;
- counter-view/explanation access;
- no hiding of important failure merely to preserve a smooth UI.

## 28. Success criterion

A successful Workspace makes the user feel that they are working **inside their organization**, not shuttling between disconnected software products.

The user can change host device without rebuilding their working world, delegate to agents without losing traceability, use the Web and specialist native apps without making them the center of the system, and adapt applications without sacrificing governance.
