# Agent Working Rules

## Purpose

Contributors must preserve the separation between Shaper OS, Shaper Runtime, and Shaper Workspace.

## Before changing anything

1. Identify the layer that owns the concern.
2. State the intended result and success criterion.
3. Separate observations from interpretations.
4. Identify permissions, mandate, blast radius, and rollback.
5. Reuse an existing concept before adding a duplicate.
6. Preserve provenance and links to evidence.

## Layer discipline

- Do not place application-specific behavior in Shaper OS.
- Do not place interface concerns inside Runtime contracts.
- Do not let Workspace bypass Runtime authorization or evidence.
- Do not turn implementation choices into universal kernel rules.
- Do not create a fourth layer implicitly through inconsistent terminology.

## Change discipline

Every structural change must explain:

- why it is needed;
- what boundary it changes;
- which existing documents it supersedes or refines;
- how it can fail;
- how it will be tested;
- how it can be rolled back or revised.

## Authority

Intelligence is not authority. An agent may propose a cross-layer change without automatically receiving permission to execute it.

For ambiguous, security-sensitive, irreversible, or systemic changes: STOP and escalate.
