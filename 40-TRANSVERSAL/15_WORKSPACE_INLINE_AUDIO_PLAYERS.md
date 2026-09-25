# Shared inline audio players

Status: standing interface requirement requested by Xavier on 2026-09-10.
Owner: Shaper Workspace. Runtime retains recording access and retention policy.
Scope: Clinic, generic Vox, Helm, demo workspaces and subsequent specializations
where people play recordings. This presentation contract adds no OS authority.

## Intent and rules

1. Recorded audio uses an attractive inline player consistent with the active
   brand, theme and interface language. Reuse a shared component within each
   application; do not leave visible browser-default audio controls on migrated
   surfaces. The hidden native audio element remains the playback engine.
2. Provide play/pause, elapsed time and duration, seeking, ten-second backward and
   forward navigation, and mute. Controls require accessible names, visible
   keyboard focus, keyboard seeking and usable touch targets. Narrow screens
   must not overflow or hide essential controls; light and dark themes must work.
3. Display actual media state and duration. Unknown duration is not a claim of an
   empty recording; disable seeking until valid metadata is available. Do not
   draw invented speech waveforms or label transcript timings acoustic evidence.
4. Loading or playback failures are visible. Switching recordings stops the old
   recording and resets position, playback/error state and source identity. A
   failure on one recording must not poison the next selection.
5. Preserve transcript-to-audio navigation and active-turn tracking when the
   owning screen supports them. Migration must preserve callbacks, media refs,
   endpoint authorization and the exact selected recording.
6. Historical recording playback must not start a new call, publish a prompt,
   create business side effects or change recording access/retention. Avoid
   autoplay on page entry; playback initiated explicitly from a listen action
   may continue directly. These controls are not DRM or an access-control layer.
7. Live softphone audio and the browser microphone are separate transport paths;
   their hidden media elements do not need recording-player controls. Videos and
   third-party embeds require a separate inventory rather than silent exclusion.

## Perimeter acceptance checklist

| ID | Capability | Required evidence |
| --- | --- | --- |
| AUDIO-01 | Inline branded player on every named recording surface | Screen-level migration inventory, no visible native audio controls |
| AUDIO-02 | Playback, pause, progress, seek, skip and mute | Actual browser media fixture and installed recording playback |
| AUDIO-03 | Accessible responsive presentation | Keyboard interaction, translated names, mobile overflow and both themes |
| AUDIO-04 | Failure and source replacement | Failed recording followed by working recording, old audio stopped |
| AUDIO-05 | Conversation synchronization | Existing transcript seek/ref/callback contract preserved and exercised |
| AUDIO-06 | Scope and operational boundaries | No microphone/call/profile mutation; read-only recording endpoints retained |

Each project records coded, tested, installed and human-accepted status separately.
A shared requirement is not evidence that every project has migrated. Stop a
replacement if it loses functional or accessibility behavior; restore the prior
component/image and repair the shared implementation.

## Current adoption

Clinic owner: `tools-app/src/components/LecteurAudio.jsx` in the separate
application repository. Scope and evidence: `tools-app/INLINE-AUDIO-2026-09-10.md`
in that repository.
Generic Vox, Helm and demo migration remain pending until recorded by their owners.

## Three-pass review

- Governance: presentation only; no new runtime authority or recording policy.
- Human journey: consistent playback controls and transcript navigation, including
  keyboard/mobile and recoverable media failures.
- Runtime: source identity, browser media events and access boundaries survive
  migration. Actual application tests/deployment evidence belong to the linked
  adoption report, not this policy declaration.

Independent read-only documentary counter-review completed; unknown duration
wording was checked against the corrected Clinic implementation. This review does
not certify migration of Vox, Helm or demo applications.

Read with [scope inventory](../90-REVIEW/SCOPE-FEATURE-INVENTORY.md) and
[prompt-test workspace](14_CONVERSATIONAL_AGENT_TEST_WORKSPACE.md).
