# Documentation session handoff

Use this when ending a coherent documentation or architecture session. It
complements [`SCOPE-FEATURE-INVENTORY.md`](SCOPE-FEATURE-INVENTORY.md) and
[`SESSION-CLOSEOUT-THREE-PASS.md`](SESSION-CLOSEOUT-THREE-PASS.md). It does not
replace them and does not add approval gates.

Copy the block below into the session note, PR description, or operator handoff.

```markdown
## Doc handoff — <perimeter>

- **Objective and revision:** ...
- **Feature IDs (if any):** F-... / none (doc-only)
- **Sources read / OPEN gaps:** ...
- **Three-pass closeout:** linked or N/A — counter-view: present / absent
- **Delivery state:** COMPLETE / PARTIAL / OPEN within <perimeter>
- **Next safe step:** ...
```

## Rules

- One authoritative inventory table per perimeter; **do not** create a separate
  checklist per agent or per engine.
- Executable credit and commit trailers belong in
  [SHAPER-OS-V1.14](https://github.com/xavdp-pro/SHAPER-OS-V1.14), not in this
  repository.
- Record when human product acceptance is still pending separately from the
  constructing agent's functional acceptance run.
