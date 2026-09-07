# Pass 2 — Human, Operator and Business Reality Perspective

## Question

Would an ordinary person, manager and system Steward actually be able to use and understand this without being forced to learn the internal cathedral?

## Findings

### 1. Two human documentation depths are useful

- **Human Foundations** teaches the path from reality to action and feedback.
- **Human Steward** exposes the system guarantees and governance.

These are learning depths, not privileges.

### 2. Ordinary vocabulary must remain small

Default user concepts:

```text
Workspace | Spaces | People | Agents | Files | Apps | Search
```

Governor, Maker, capability graph and event causality belong in Steward/agent documentation unless they solve an immediate user problem.

### 3. Familiar work must remain possible

The user can still:

- browse files;
- use tables/forms;
- edit documents;
- perform work manually;
- open specialist native software;
- inspect a real web page.

Agentic behavior is added without making normal work impossible.

### 4. Context becomes the higher-level organizing unit

This is the major UX shift. Users think “ACME” rather than “which application has ACME?” while retaining access to app-like views when helpful.

### 5. Manual → assisted → delegated → automated remains a maturity path, not a moral ranking

Different workflows can remain at different maturity levels indefinitely.

### 6. Multi-monitor is not optional desktop polish

For real management/operations work, several simultaneous surfaces are common. The architecture now treats multi-screen layout as a first-class Workspace concern.

### 7. Notifications must carry context

The earlier Enterprise OS requirement survives: a notification should take the user to the object/reason/action instead of forcing a search through unrelated apps.

### 8. Changing computer should be boring

The strongest simple product demonstration may be:

```text
Windows today → Mac tomorrow → install/enroll → same organizational Workspace
```

This makes Runtime/Workspace separation understandable to non-technical users.

### 9. Specialist apps remain legitimate

The product is not weakened because video editing/CAD/etc. stays outside. Controlled external-app gateways are a better boundary than attempting to recreate every application.

### 10. Steward separation is useful but must not create two security truths

A distinct Steward app/surface improves clarity and reduces exposed tooling, but authorization remains one Runtime truth.

## Operational concerns added

- accessibility and keyboard paths;
- useful core operation when agent provider is unavailable;
- client update fleet visibility;
- offline/stale state clarity;
- conflict-resolution UX;
- external-app temporary-file lifecycle;
- web authentication and user takeover;
- printing/device workflows;
- user explanation for permission denial.

## Human/operational verdict

The idea remains economically and operationally plausible because it deliberately leverages the Host OS for hardware and specialist software while moving organizational continuity, context and generated business tools into Shaper.

The biggest usability risk is not technical complexity but **leaking internal architecture into the ordinary UI**. The vocabulary projection and two-depth documentation model explicitly counter this.
