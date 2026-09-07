# Shaper Linux — Optional Sovereign Host

## Status

Shaper Linux is a future/optional host profile, not a prerequisite for Shaper Workspace.

The adoption path is intentionally progressive:

```text
Shaper on existing Windows/macOS/Linux
→ hardened/managed deployment if desired
→ dedicated Shaper Linux device where sovereignty justifies it
```

## Why it exists

On a normal host, Shaper cannot make absolute claims against a kernel/root-level compromise of that host.

A dedicated host allows more control over:

- boot chain;
- disk encryption;
- allowed applications;
- service set;
- kernel/security profiles;
- update cadence;
- local Runtime placement;
- device policy.

## Minimal conceptual stack

```text
UEFI / Secure Boot where supported
→ Linux kernel + minimal userspace
→ encrypted storage / TPM-bound options where appropriate
→ network
→ Wayland graphics
→ audio
→ device services
→ secure Shaper Runtime/broker
→ Shaper Workspace
```

The exact distribution base is deliberately open.

## Application policy

A dedicated device can adopt default-deny or strongly controlled executable policy:

- signed/approved Shaper components;
- approved specialist applications;
- explicit plugins;
- no arbitrary downloaded executable by default.

## Recovery

The device itself should remain replaceable. Do not turn one sovereign laptop into the only holder of organizational truth without an explicit backup/recovery plan.

## Updates

Need:

- signed/verified packages/images;
- staged rollout;
- atomic/transactional strategy where feasible;
- rollback;
- recovery boot path;
- clear distinction between OS and organizational-data recovery.

## Relationship to Workspace

Workspace should remain substantially the same product. Shaper Linux provides a stronger, more controlled host beneath it.

## Relationship to Runtime

Runtime can run locally, on LAN, remotely or in hybrid form. A Shaper Linux workstation does not force all server data onto the workstation.

## Success criterion

Shaper Linux adds sovereignty and reduces host uncertainty without forcing the project to carry Linux-distribution complexity before the Workspace/Runtime product is mature.
