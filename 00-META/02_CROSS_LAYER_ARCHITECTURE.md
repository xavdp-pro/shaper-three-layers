# Cross-Layer Architecture

## 1. The system in one diagram

```text
                    HUMAN / ORGANIZATION
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│ SHAPER WORKSPACE                                           │
│ Flutter/Dart shell, surfaces, apps, search, voice, web     │
└───────────────────────┬────────────────────────────────────┘
                        │ Shaper Protocol / local IPC
                        ▼
┌────────────────────────────────────────────────────────────┐
│ SHAPER RUNTIME                                             │
│ Identity │ Authority │ Objects │ Events │ Agents │ RAG      │
│ Vault │ Sync │ Audit │ Policies │ App model │ Observers     │
└───────────────────────┬────────────────────────────────────┘
                        │ governed by
                        ▼
┌────────────────────────────────────────────────────────────┐
│ SHAPER OS                                                  │
│ Living adaptive kernel: reality, intention, tensions,      │
│ authority, feedback, repair, learning, revisability        │
└────────────────────────────────────────────────────────────┘

Host below Workspace/Runtime where local:
Windows | macOS | Linux | optional Shaper Linux
```

The arrows are not simple “calls.” They describe different responsibilities.

## 2. Shaper OS does not store the invoice

Shaper OS defines the principles by which the invoice is handled: provenance, authority, visibility, integrity, revision, trust and feedback.

The Runtime stores and governs the invoice object and its versions.

The Workspace renders it and lets authorized humans or agents act on it.

## 3. Workspace does not become the source of truth

The Workspace may cache local data for performance or offline work, but durable organizational truth belongs to the Runtime unless a deployment explicitly chooses a sovereign fully local Runtime.

This enables device continuity:

```text
old Windows device
      ↓ lost/replaced
new Mac
      ↓ install Workspace
      ↓ enroll device + authenticate
same universe, rights, objects, apps, agents, context
```

## 4. Runtime is deployable in several topologies

```text
A. Cloud / VPS
Workspace → Internet → Runtime

B. Company LAN
Workspace → LAN → Runtime appliance/server

C. Local sovereign laptop
Workspace → local IPC → Runtime on same device

D. Hybrid
Workspace ↔ local encrypted cache/runtime subset ↔ central Runtime
```

The logical model should not depend on one physical topology.

## 5. Host OS is a delegated capability provider

The Host OS remains responsible for:

- hardware drivers;
- screen configuration;
- audio stack;
- networking;
- printers/scanners/cameras;
- specialist native applications;
- process and device primitives.

Shaper accesses these through controlled adapters and gateways rather than pretending they do not exist.

## 6. Security boundary

On a normal host, Shaper can strongly protect data at rest and reduce attack surface, but it cannot claim perfect isolation from a host already compromised at kernel/root-equivalent privilege.

Therefore security is layered:

```text
host security
+ process isolation
+ encrypted vault/cache
+ device-bound keys
+ capability-based runtime authorization
+ short-lived session authority
+ controlled gateways
+ remote/source-of-truth separation
+ audit and detection
```

On Shaper Linux, more of the host itself becomes part of the trusted computing base.

## 7. Web is a surface, not the center

The Workspace may contain a Web Surface backed by an existing platform web engine. The web page does not automatically receive Shaper context.

Crossings are explicit:

- upload gateway;
- download/import gateway;
- clipboard gateway;
- optional microphone/camera/passkey/print/screen-share capabilities.

The agent may also access web sources without requiring the human to navigate tabs.

## 8. Applications are projections over the object graph

The default app model is declarative. An agent should usually generate a schema using trusted primitives rather than arbitrary executable code.

```text
Object types + relations + views + actions + policies + workflows
                        ↓
                Shaper App Schema
                        ↓
                 Workspace renderer
```

Arbitrary plugins are an escape hatch, sandboxed and capability-bound.

## 9. Core feedback loop across layers

```text
REALITY
→ OBJECT / EVENT
→ OBSERVER / SENSOR
→ TENSION or PLUSPOINT
→ INTENTION
→ DECISION / MANDATE
→ AUTHORIZED ACTION
→ RESULT
→ EVIDENCE
→ HEALTH / TRUST UPDATE
→ LEARNING
→ RULE / APP / SENSOR / POLICY REVIEW
```

Every layer participates, but no layer owns the whole loop alone.
