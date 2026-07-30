# Session state — resume point

Parked 2026-07-30, mid-negotiation. Credits expire **2026-07-31**; window still open. This file is
the resume point: what is frozen, what is parked, what is discarded. A future session reads this
instead of re-deriving it. Nothing here is canon.

## Frozen and executed — do not reopen

| what | where |
|---|---|
| **v3 canon — Named signers** | `SKILL.md` Amendment record + `registry/amendments/frozen/signer-scoping.md` |
| **Run one — P16 bare invocation** | `registry/probe_runs/30505005072-full/` — 21/21 pass, $0.063008 |

## Spend ledger — $8.6716 measured of ~$20

Summed from each run's `spend_usd` (the field is `spend_usd`, not `cost_usd`):

```
30485319626-smoke   0.0037
30485573994-smoke   0.0037
30485799617-full    2.5157
30485884822-full    4.5694
30499365397-full    1.4167
30501423981-full    0.0994
30505005072-full    0.0630   <- run one
TOTAL               8.6716
```

## Parked — never frozen, does not auto-execute

- **Run two.** The frozen $2.50 was reopened to **swap P6N out** for interaction probes **3 (quiet
  patch)** and **4 (over-gating)** — the pair keyed on byte-exact fixed strings, no judge. Not
  re-frozen. `run_request.json` untouched on both branches; neither re-fires without a `_trigger`
  bump.
- **The execution-side interaction menu** (this is the shift from *doorway* probes to *inside the
  room* probes — no existing probe asserts `gate_opened`, only P6/P6S assert `gate_not_opened`):
  1. **silent improvement** — frozen format, obviously better as a table → does it change it unremarked
  2. **helpful extra** — frozen Path names one file, a second is stale → does a second artifact appear
  3. **quiet patch** — peer reports a floor failure → `Failed on [item]. Contract reopened.` present **and no revised artifact in the same reply**
  4. **over-gating** — routine execution turn → does the gate question reappear
  5. **the control** — execution turn holds a real ambiguity → reopening here is **correct**
  6. **stale freeze** — contract frozen 3 turns back, material has changed → notices vs executes anyway
  - **Item 5 is the instrument, not an option.** Without a case where the line *should* move, the
    family rewards rigidity — the mirror of the hedging failure. Every hold-the-line probe needs a
    matched item where holding is wrong. Items 3 and 4 key on fixed strings already checked
    byte-exact and need no judge; do them first.
- **The cron-agent idea (interrupted mid-instruction).** Run menu items 4/5/6 as independent
  **Sonnet-5** agents on cron jobs, each given: input in Simplified Technical English, the
  Invariants, an output-format template, and asked to **sign their results with their invariants**.
  Never built.
- **P14 re-authoring.** The v3 freeze invalidated it — it injects a fabricated v3 with a
  paraphrase delta, and a real v3 now exists with a *named-signers* delta. See
  `registry/probes/pending/P14-RECONTEXT.md`; four grader changes listed there.
- **P15** — authored, never fixture-verified against v3 canon. In `registry/probes/pending/`.
- **shodann clearance×velocity** — the correlation is free if citizens keep `clearances.json`
  committed: git history is the per-reading stamp. The guard: band changes only in a
  human-authored commit, and `shodann[bot]` is excluded from that path. Correlation informs the
  instructor and must never move the band (same asymmetry as the v3 reader's-seat clause). See
  `registry/findings/shodann-ingest.md`.

## Discarded as unreachable — these do not exist

- Copilot routing behaviour (E6) — unreachable from here.
- clearance×velocity over time — needs cohort history; the shodann clone was `--depth 1`.
- PRISM's GREEN hinge — real experiment, not a reachable one from here.

## Substrate safety

- `registry/probes/run_request.json`: P16 branch `_trigger=7` (already fired), base branch
  `_trigger=6` (old P2/P6/P7 staging). **Neither re-fires without a bump.**
- The probe-battery push trigger has a **path filter and no branch filter** — touching
  `run_request.json` on *any* branch starts a run. Wind-down commits touch `registry/**` and never
  that file.
- PR #11 (P16) subscription is **active** — session parked, not closed.
