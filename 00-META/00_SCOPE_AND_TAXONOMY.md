# Scope and Taxonomy

## 1. What this repository names

### Shaper
The product and ecosystem name. It expresses the idea that software should shape itself around the organization rather than forcing the organization to conform to a fixed product.

### Shaper OS
The **living adaptive governance kernel**. It defines how the system perceives, separates observation from interpretation, carries intention, detects tensions, acts proportionately, verifies consequences, repairs, learns, escalates and revises itself.

It is not the host operating system.

### Shaper Runtime
The operational substrate that materializes Shaper OS principles: identity, authority, capabilities, object graph, events, files/data, RAG, agents, policies, audit, synchronization, security and services.

### Shaper Workspace
The human operating environment: desktop/workspace shell, windows/surfaces, files/object views, apps, search, chat, voice, web surfaces, notifications and device interaction.

### Shaper Linux
An optional minimal sovereign host for deployments that want Shaper to control the machine below the Workspace as well. It remains replaceable by Windows, macOS or another Linux host.

## 2. Internal system vocabulary

| Term | Canonical meaning |
|---|---|
| **Steward** | Human responsible for governing a Shaper universe or major system scope. |
| **Root Agent** | Privileged agent that works with the Steward under explicit authority. |
| **Root Authority** | The governing authority formed by the human Steward plus directly controlled root-capable agents and policies. |
| **Governor** | Orchestrator that routes, delegates, evaluates state and escalates. |
| **Maker** | Actor/agent permitted to materialize approved structural or infrastructure changes. |
| **Universe** | Sovereign organizational/system scope with identity, policies, data and children. |
| **Sub-universe / Cell** | Child scope with bounded autonomy and an explicit parent. |
| **Actor** | Human, agent, service or device able to request or perform an action. |
| **Capability** | Explicit technical ability to perform an action. |
| **Permission** | Authorization derived from identity, role, object, context and policy. |
| **Mandate** | Current or standing human/system authorization to pursue a defined intention. |
| **Object** | Governed entity: document, customer, task, decision, message, app, etc. |
| **Context** | Connected working set of objects, people, events, policies and intentions. |
| **Surface** | Human-visible representation: document, table, graph, terminal, web page, dashboard, chat. |
| **Vault** | Encrypted storage and key-governed data boundary. |
| **Gateway** | Controlled crossing between Shaper and another trust domain. |
| **Event** | Recorded occurrence with actor, origin, time and causality. |
| **Sensor** | Observation mechanism; not automatically truth. |
| **Tension** | Meaningful gap that says “look here”; not automatically a diagnosis. |
| **Pluspoint** | Unusual success worth understanding and potentially preserving. |
| **Counter-view** | Independent perspective used to expose blind spots without automatically owning the decision. |
| **Repair** | Restoration of non-trivially reproducible state. |
| **Rebuild** | Re-creation of a reproducible component from a known healthy chain. |

## 3. User vocabulary

Normal users should need only a small vocabulary:

- **Workspace**
- **Space**
- **People**
- **Agents**
- **Files**
- **Apps**
- **Search**

Terms such as Governor, Maker, event bus, vector index, capability graph, root authority and repair hierarchy should not leak into ordinary UX without a functional reason.

## 4. Three distinct dimensions that must not be collapsed

### Cognitive depth
A1 / A2 / A3 — how much an agent must understand.

### Human learning depth
Human Foundations / Human Steward — how deeply the documentation exposes the system.

### Authority
Roles, capabilities, permissions, mandates and root powers — what an actor may actually do.

**Intelligence is not authority. Documentation depth is not authority.**

## 5. Human functional roles

The product may expose functional roles such as:

- **User** — performs work.
- **Operator** — coordinates recurring work, exceptions and workflows.
- **Manager** — delegates and steers a business scope.
- **Steward** — governs Shaper itself or a major universe.

These roles are orthogonal to the two documentation depths above.

## 6. Host terminology

Windows, macOS and Linux are called the **Host OS** when Shaper Workspace runs above them.

The host remains responsible for hardware abstraction, drivers, graphics, sound, networking and specialist native applications. Shaper should delegate what the host does better rather than recreate it.
