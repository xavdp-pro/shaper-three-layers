# Scope-first feature inventory and delivery reconciliation

Status: standing working rule requested by Xavier on 2026-09-10.
Owner: cross-layer delivery discipline; each feature retains its own layer owner.
Intent: keep recorded requirements visible during implementation and handoffs.
Success: every requirement found in the declared perimeter has an identified row,
source, dependencies and acceptance check, revisited against actual delivery.
Stop an unsupported completeness claim; continue authorized bounded work while
recording gaps. Recovery: restore omitted rows, reopen affected checks and repair
implementation. This rule adds no per-task approval request.

## Before implementation: enumerate the perimeter

1. State the objective, included/excluded universes, subsystems, bricks, interfaces,
   actors and scenarios. An exclusion must be explained, not silently dropped.
2. List the sources to cover: current user decisions, canonical intents/rules,
   functional specifications, relevant archived discussions, existing checklists,
   code and runtime evidence. Record read/unread status and unresolved conflicts.
   Do not claim an archive was fully read when only keyword matches were inspected.
3. Extract atomic capabilities using stable feature IDs. Include both human and
   agent paths, administration, configuration, observability, failure/recovery,
   accessibility, branding and specialization where relevant to the perimeter.
   Do not invent product capabilities merely to fill a category.
4. Map each source requirement to one or more feature IDs, and each feature back
   to a source or an explicitly labeled proposal. Preserve parent/child features;
   a working subfeature does not satisfy its complete parent capability.
5. Record prerequisites and affected features across subsystem boundaries. Follow
   dependencies until each is either covered or an explicit external contract.
6. Define an observable acceptance result and required evidence before coding.
   Record unknowns and source coverage gaps as OPEN. A document inventory is not
   runtime proof, and a green health endpoint is not a complete user journey.

Use the template below in the owning project's existing plan/checklist where
possible. Maintain one authoritative table per perimeter, linked from handoffs.
Do not introduce an unconnected duplicate checklist for each agent.

## During work

- Give agents concrete feature IDs and file ownership; they report against those
  same IDs. Dependencies and consumer impacts travel with the task.
- New discoveries amend the inventory and affected acceptance checks immediately.
- Keep planned, coded, tested, deployed and user-accepted facts separate; evidence
  includes version, target and date. A claimed capability with stale evidence is
  reopened when its dependencies change.
- Small fixes may use a small inventory. Do not audit all Shaper before every typo;
  audit the whole declared perimeter and its relevant dependency boundary.

## The constructing agent owns the functional acceptance run

The human-agent tandem defines what is to be produced. Before building, the
constructing agent writes the feature checklist and expected observable results,
including dependencies and connections. It maintains that SAME checklist as
features are added or changed; it never reconstructs a smaller checklist from
only the code that happened to ship.

After assembling and connecting the delivered system, the constructing agent
executes each scoped feature's acceptance scenario itself, within the existing
mandate, through the real installed interface or public contract. Code review,
a successful build, unit tests and service health are supporting evidence;
they do not replace exercising the assembled feature and reading its result.

For every feature, record the steps actually executed, expected and observed
results, source revision, installed target, date and evidence location. Verify
persisted effects outside the producing component, including downstream
connections and relevant failure/recovery behavior. A button press or success
message alone is not proof. After a correction, repeat the failed scenario and
any affected dependent scenarios before checking the feature off.

A scenario needing unavailable hardware, an unauthorized external recipient,
unauthorized spending or another action outside the mandate remains NOT VERIFIED with its blocker and
next step. Never silently skip it or mark it passed. The agent performs all
other authorized checks without leaving routine testing to the human. Human
acceptance remains separate: the agent's functional proof supports the human's
judgment; it does not impersonate that judgment.

An independent review supplements this responsibility; it does not transfer it.
For an existing delivery with no complete execution record, reopen the checklist
and test the missing scenarios rather than retroactively declaring them passed.

## Test means follow the delivered interaction

Canonical obligation: [Shaper OS Rule 20](https://github.com/xavdp-pro/SHAPER-OS-V1.14/blob/main/software/RULES.md#rule-20-functional-test-means).
This section applies that obligation to the inventory and execution record;
it does not grant separate authority.

For each feature, the constructing agent derives the required test means from
its intended use, interfaces and dependencies, before implementation. This is
an open-ended obligation, not a closed list of supported technologies. Inventory
inherited base capabilities as well as the specialization: a telephony universe
is a standard universe plus telephony, not just the newest telephone screens.

Declare, per scenario: the interaction surface, real target, driver/control tool,
observation channel, required access or equipment, safe test data, cleanup and
what the chosen means can and cannot prove. Prepare and verify those means
within the mandate; an installed tool is not proof that it can reach and control
the target. Make testability part of the feature design instead of discovering
at delivery that the agent has no way to exercise it.

Examples below illustrate the method; they do not limit it:

| Delivered surface | Required functional exercise | Evidence boundary |
| --- | --- | --- |
| Command-line interface | Run the actual commands, including relevant failure cases | Exit code, output and resulting state/artifact |
| API | Send actual requests through the delivered API with the intended identity | Response, permissions and independently observed persisted/downstream effects |
| Web interface | Drive a real browser with Playwright or an equivalent available browser-control tool | User journey, interaction, responsive/accessibility checks and resulting effects; direct API tests alone do not validate the UI |
| Mobile application | Control the installed application on an authorized device using an available platform driver | App interactions, permissions, network and relevant device capabilities; an emulator qualifies only the behavior it actually covers |
| Sensor, peripheral or physical equipment | Establish authorized control/stimulation and independent observation of the real equipment | Physical input through transport and application to the expected output; simulated input does not prove hardware operation |

When a feature spans several surfaces, test each exposed contract AND the
assembled journey across them. A successful API call does not prove the mobile
screen, and a rendered screen does not prove the connected peripheral. Add the
appropriate means for any new surface using the same method.

If a required device, driver, connection or permission is unavailable, first
inspect the means already available. Prepare what is authorized and identify the
smallest missing operator action (for example connect a test phone and enable
its control access). Continue independent checks; keep the unsupported scenario
NOT VERIFIED. Never replace a real-world requirement with a simulation and call
it passed. No unapproved purchase, external call or physical actuation is implied.
Human-assisted execution, when unavoidable, is attributed as such rather than
claimed as autonomous agent execution.

## Before delivery: revisit the SAME inventory

- [ ] Every listed source was read or its coverage gap is explicitly OPEN.
- [ ] Every discovered requirement maps to feature IDs; none was silently omitted.
- [ ] Every dependency and consumer impact has been reviewed.
- [ ] Every delivered interaction surface has suitable, verified test means;
  missing access/equipment and limits of simulated coverage are explicit.
- [ ] The constructing agent executed every scoped feature on the assembled target,
  or explicitly recorded NOT VERIFIED with a blocker and next step.
- [ ] Every feature's expected behavior has been confronted with actual evidence.
- [ ] Coding, test, deployment and human-acceptance states are separate and honest.
- [ ] Failed, missing, deferred and out-of-scope items remain visible with reasons.
- [ ] Generic capabilities were reviewed for reuse in specializations and vice versa.
- [ ] Source revisions, runtime targets, evidence and handoff paths are recorded.
- [ ] The closeout states what is usable now and what remains unqualified.

The overall result is COMPLETE only when required source coverage is reconciled
and every required feature acceptance criterion is satisfied with appropriate
evidence. Completing the review checklist while merely documenting gaps does not
satisfy this condition. A pending required human acceptance also keeps delivery
PARTIAL/OPEN. Otherwise report PARTIAL/OPEN with the exact outstanding feature IDs.
These inventory states do not replace the existing capability maturity vocabulary
in `50-ENTERPRISE-REFERENCE/11_VALIDATION_AND_ACCEPTANCE_PROTOCOL.md`.

## Copyable perimeter template

```markdown
# Feature inventory — <perimeter>
Owner / date / revision:
Objective and expected user result:
Included:
Excluded, with reasons:
Relevant external dependencies:
Source coverage: OPEN / RECONCILED (not a promise of absolute completeness)

| Source / revision / section | Read coverage | Requirement IDs | Conflicts or gaps |
| --- | --- | --- | --- |
| ... | unread / partial / read | ... | ... |

| ID / parent | Capability and actor | Source | Layer / owner | Dependencies / consumers | Acceptance result |
| --- | --- | --- | --- | --- | --- |
| F-001 | ... | ... | ... | ... | ... |

| ID | Coded evidence | Test evidence | Installed target/version | Human acceptance | Gap / next action |
| --- | --- | --- | --- | --- | --- |
| F-001 | unverified | unverified | unverified | pending | ... |

## Before/after checks
- [ ] Source coverage reconciled within the declared perimeter.
- [ ] All feature rows and dependencies rechecked against the delivered version.
- [ ] Failures, exclusions and unqualified paths remain visible.
- [ ] Handoff and applicable three-pass/four-pass reviews linked.

Conclusion: COMPLETE / PARTIAL / OPEN within <perimeter>, with evidence date.
```

## Example of an omission this prevents

Parent: live UI shaping on the published application.
Children include authorized navigation, bounded schema/configuration changes,
visible application without page reload, preservation of in-progress user work,
traceability and rollback. A functioning WebSocket navigation channel covers only
one child. A development-only HMR proof does not validate the published shaping
capability. Sources: enterprise agent guide sections11–12 and demo scenario6.
