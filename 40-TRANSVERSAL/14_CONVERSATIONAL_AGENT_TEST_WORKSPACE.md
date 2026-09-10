# Conversational agent test workspace

Status: standing requirement requested by Xavier on 2026-09-10.
Scope: Clinic, generic Vox, conversational Helm surfaces and future specializations
that expose conversational-agent configuration. Not a mandatory voice feature for
bricks without a conversational role. Clinic implementation is in progress.

## Intent and ownership

Every such configuration surface offers a discoverable, dedicated **Test prompts**
page on desktop and mobile. A small header icon or hidden modal is not sufficient.
Workspace presents and edits drafts; Runtime owns validated test sessions and
results; OS authority and the specialization's constraints remain applicable.
Success is a genuine conversation using the exact tested instructions and the
same compatible agent engine, with inspectable results, without changing the
active service. Stop on missing isolation or authority; recover the prior page
and terminate the test session. No production prompt publication is implied.

## Shared requirements

- Show the greeting and editable instructions beside a direct conversation bench;
  stack them coherently on mobile. Navigation names the page explicitly.
- For voice agents, the user can speak through the browser microphone without
  a phone number, SIP device or carrier call. Retain audio and transcript with
  exact session identity and the version or snapshot of instructions used.
- Test edits as an isolated draft. Do not silently save or publish it. Distinguish
  the saved baseline, the current draft and the instructions used in each result.
  Make draft lifetime and reset behavior explicit.
- Use the specialization's real compatible engine and voice configuration, not a
  canned simulation presented as actual agent behavior. Clearly distinguish a
  synthetic microphone test from human voice qualification.
- Preserve locked rules and permission boundaries; draft rights do not grant
  permission to alter guardrails, providers, connectors or external actions.
- Test runs must not create operational appointments, emails, tasks or outbound
  calls. Side effects use isolated test substitutes when a scenario requires them;
  unsupported actions remain explicit. Actual human outbound calling is a separate
  clearly labeled workflow governed by its own mandate.
- List only implemented scenarios. Reception rehearsal does not imply outgoing
  reminder, delay inquiry, transfer or appointment workflow coverage. Each added
  scenario needs its own context, isolation and result qualification.
- Authenticate test sessions, bound their lifetime and scope, clean up microphone
  and connections on exit, and expose unavailable/failed/pending states honestly.
- Apply common branding, translations, accessible selection controls and responsive
  navigation. Reuse a shared component/contract and specialize through context.

## Reproduction checklist

- [ ] Visible navigation entry and direct link work on desktop and mobile.
- [ ] Authorized draft fields are editable; protected fields remain protected.
- [ ] The engine receives exactly the intended draft and specialization context.
- [ ] No active prompt/configuration changes or real side effects occur.
- [ ] Microphone, stop, failure and expiry paths release resources correctly.
- [ ] Audio, transcript, scenario and tested instruction snapshot are correlated.
- [ ] History distinguishes saved tests from the current editable draft.
- [ ] Each supported scenario is qualified, with unsupported paths named.
- [ ] Shared styling, translations, keyboard and touch use are verified.
- [ ] Record source revision, installed version and runtime proof per universe.

The checklist specifies acceptance; it does not certify every project as complete.
