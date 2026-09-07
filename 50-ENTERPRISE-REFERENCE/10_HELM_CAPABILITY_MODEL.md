# Helm Capability Model

## Definition

Helm is the **conversational operating interface for organizational pilotage**. Through language, voice and contextual actions, it lets a human perceive, question, navigate, prepare, delegate, review and—when explicitly authorized—shape the organization.

Helm is not the database, policy engine, universal orchestrator, infrastructure root or unrestricted code generator.

## Canonical chain

```text
HUMAN
→ HELM / AGENT SURFACE
→ explicit intention + resolved context
→ RUNTIME authority and mandate check
→ GOVERNOR routing and coordination
→ specialist agents / workflows
→ MAKER for approved structural materialization only
→ tests + result + evidence
→ WORKSPACE explanation and control
```

Historical Maestro functions map mainly to Governor, workflow execution and specialized agent coordination. The name remains preserved in source documents but need not become a canonical component.

## Capability families

| Family | Examples | Default mode | Evidence |
| --- | --- | --- | --- |
| Understand | summarize, compare, explain, answer over RAG | read/assist | sources, context, uncertainty |
| Navigate | open customer, filter dashboard, focus control | visible assist | navigation trace |
| Prepare | quote, invoice, task, email, report | draft | inputs, artifact, preview |
| Act | update, send, call, schedule | explicit mandate | authority, side effect, result |
| Pilot | attention, trends, tensions, pluspoints | advisory | observations separated from recommendations |
| Propose automation | detect stable repetition | proposal | pattern, exceptions, owner, review |
| Execute mandate | run approved workflow | bounded automation | mandate, trace, STOP and exceptions |
| Shape Workspace | change a declarative app/surface | Steward shaping | diff, tests, migration, rollback |

## Visible modes

1. Observe.
2. Assist and prepare.
3. Delegate once.
4. Approval workflow.
5. Standing mandate.
6. Governed shaping.

Conversation must never silently expand authority when the mode changes.

## What Helm introduces

- explicit intent and contextual reference resolution;
- visible separation between proposal and execution;
- clarification when “this customer” or “that order” is ambiguous;
- operation identity, causality and partial-success representation;
- cancellation and STOP propagation;
- preview, outbox, compensation or reconciliation for external effects;
- provenance and confidence for material answers;
- identical authorization semantics for voice, text and clicks;
- disableable UI control;
- versioned declarative shaping instead of arbitrary production code by default;
- durable reasons and review conditions for standing mandates.

## Human sovereignty

The user can ask: What do you know? What are you inferring? What do you intend to do? Which permission and mandate will you use? What will change? Show me the evidence. Stop. Undo what is truly reversible. Escalate.

When context, authority, side effects or evidence cannot be resolved, Helm clarifies, limits the experiment, refuses or escalates rather than improvising confidently.
