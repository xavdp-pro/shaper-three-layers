# Workspace selection controls

Status: standing interface requirement requested by Xavier on 2026-09-10.
Recorded policy; project-wide implementation and qualification are pending.

## Intent, scope and ownership

Use attractive, consistent, branded selection controls throughout Clinic, generic
Vox, Helm, demo workspaces and subsequent specializations. Shaper Workspace owns
presentation; Runtime retains validation and authorization. This is a shared UI
contract, not a new grant of authority or a prescribed JavaScript dependency.
Success means a consistent, accessible selection experience on desktop and mobile.
Do not change stored values, permissions or business semantics during migration.
Stop a replacement if it loses accessibility or functional behavior; recover the
previous component and fix the shared implementation before continuing.

## Rules

1. Replace visible browser/system-default select widgets with the shared branded
   selector. Apply the active theme, language and client branding consistently.
2. Short, fixed lists may use a simple styled dropdown. Potentially long or growing
   lists must use a searchable combobox, in the spirit of Select2, even when their
   current dataset is small. Six options is the existing Clinic default threshold;
   growth potential takes precedence over the current count.
3. The search field has an accessible cross button to clear the search text and
   restore the option list while keeping the selected value unchanged. Keep focus
   in the search input after clearing it.
4. Clearing the selected value is a separate operation, offered only when an empty
   selection is allowed. Label the two actions distinctly; required fields must
   not silently become empty when the user clears a search.
5. Support keyboard navigation, Enter to select, Escape to close, focus restoration,
   screen readers, visible focus and touch. Preserve disabled options, group labels,
   validation messages and the currently selected value.
6. Display loading, no matches and loading errors explicitly. Large remote lists
   need bounded result loading and protection against stale search responses.
   Search must respect the same universe and account visibility as the source data.
7. Reuse and improve the existing component before creating another selector.
   Select2 describes the expected interaction; it does not mandate jQuery or a
   specific library. A visually hidden native control used for semantics is not a
   violation, provided the resulting selector remains accessible and its only
   accessible semantics are not removed.

## Implementation checklist

- [ ] Inventory remaining native selectors across Clinic, Vox, Helm and demo.
- [ ] Verify shared component search clearing versus selection clearing.
- [ ] Mark growing object lists searchable regardless of current option count.
- [ ] Migrate screens without changing values, authorization or form behavior.
- [ ] Qualify keyboard, screen reader semantics, touch, themes and translated labels.
- [ ] Check long lists, empty states, remote failures and rapid query changes.
- [ ] Record actual deployed coverage and outstanding screens in each handoff.

Clinic already contains `src/components/CustomSelect.jsx`; that observation is
not evidence that all controls conform. The browser rehearsal language picker,
for example, still uses a native select at this checkpoint.
