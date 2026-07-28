# Pending amendment: reopened-by-the-peer

**Target:** SKILL.md → Invariants → Fixed strings; Gate integrity
**Status:** pending — unnumbered until frozen
**Resolves:** the execution-side human seat (K4) — the invariants defined the human at the gate and were silent about the human during execution.

## Proposed changes (full text)

Add to Fixed strings:

> - "Reopened by the peer."

Add to Gate integrity:

> **Observe and abort, never patch.** During execution the human's powers are exactly: read everything, and end the workflow. A human abort issues "Reopened by the peer." and reopens the contract tree — reopen cascades downward exactly as freeze did. No participant, human or model, edits a contract in flight; patching a running workflow is the third side, and there is no third side.

## Rationale

Substrate corroboration: CI systems already pin the in-flight run to the definition at trigger time; edits touch only the next run. The amendment makes the substrate's semantics doctrine, and gives the human abort its own receipt string, distinct from "Failed on [item].", so the log records who reopened and why-shaped-how.
