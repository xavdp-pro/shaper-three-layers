# Persistent acting agents

Source role: cross-layer projection of the [ecosystem bridge/session contract](https://github.com/xavdp-pro/shaper-ecosystem/blob/main/chapters/40-ACTING-AGENTS.md).
Term: [bridge](https://github.com/xavdp-pro/shaper-glossary/blob/main/TERMS.md#bridge).

## Intention

Agents continue useful delegated work across tasks and interruptions while the
human–AI tandem retains direction and judgment. OpenCode is the default prototype
for the acting CLI path; adapter capabilities describe each engine's actual role.

## Responsibility and interface

OS supplies mandate, jurisdiction and bounded action principles. Runtime owns
session identity, context revision, task/operation identity, permitted tools,
deadline/budget policy, cancellation, resumption and attributable results.
Workspace presents activity and meaningful stop/resume controls.

The bridge advertises inference, inspection, tool use, execution, streaming,
resumption and cancellation capabilities as applicable to its adapter. A task
selects the capabilities it requires and supplies exact source/dependency routes.

Persistent identity and context survive process interruption through the declared
capture/restore contract. Durable application session state follows
[MariaDB ownership](17_APPLICATION_STATE_OWNERSHIP.md). Resumption resolves current
authority and reconciles completed effects before retrying work.

Queue owns attempts; the bridge owns engine interaction; Logger receives scoped
metadata; Maestro coordinates scheduled work and stalled-work observation.
The owning component interfaces define their collaboration. Workers retain their
delegated role alongside governors and makers.

## Navigation

- [Composition/source map](../00-META/08_COMPOSITION_AND_SOURCE_MAP.md): governing owners.
- [Runtime master](../20-SHAPER-RUNTIME/00_MASTER.md): authority and events.
- [State ownership](17_APPLICATION_STATE_OWNERSHIP.md): session persistence.

