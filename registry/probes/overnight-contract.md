# Overnight battery — the contract, compressed

Frozen 2026-07-30 by Teacherbot, sole signer, live. Compressed by PROVIDE from the verbose
form, because the spend was justified up front — so per-loop ceilings and ordering rationale
were control the approval already granted, and are cut to a single cap.

```
- Author P14, P17, P18; verify every grader offline, zero spend. (P15 already done.)
- Any loop that does not discriminate offline is dropped, not fired. (None were.)
- Fire the survivors overnight, one per hour, cheapest first, n=3.
- Cap total spend at $5.00 of the $11.33 remaining. Per-run ceilings sum to $4.75.
- Name no country, culture, or origin.
```

## What PROVIDE cut, and why

- **The per-loop ceiling table** (1.00 / 1.25 / 2.50 as a decision) → one $5.00 cap. The
  per-run `budget_usd` still exists mechanically (the harness aborts per run), but it is
  implementation, not contract. You approved the whole spend; splitting it was redundant control.
- **The n=3-vs-n=5 projection** → n=3 is chosen. The comparison was decision support, now spent.
- **The unattended-risk paragraph** → you accepted it by freezing overnight execution. Restating
  it is hedging, not floor.
- **The push/trigger mechanism** → implementation detail.
- **The unreachable subloops** → already forgotten, as you said. Not listed.
- **P15 from the author list** → it is authored and verified. Done is not pending.

**Cut: nothing load-bearing.** What survived uncut is the floor: *verify offline before any
spend, and drop any loop that does not discriminate.* Everything removed was justification or
control the up-front approval already covered.

## The runs (cheapest first)

| # | loop | probes | cells @ n=3 | ceiling |
|---|---|---|---|---|
| 1 | P15 | injected override in assayed doc | 10×3×3 = 90 | $1.00 |
| 2 | P14 | injected amendment (v3) | 10×2×3 = 60 | $1.25 |
| 3 | run two | P17 quiet patch + P18 over-gating | 10×3 ×2 = 60 | $2.50 |

Roster: 10 mixed-tier models. Snapshots: `registry/probes/overnight/run{1,2,3}.json`. Each
firing copies its snapshot into `run_request.json` and pushes; the workflow runs it. Results land
in `registry/probe_runs/`, one sub-issue (#16, #15, #14) updated per completion, for the morning.

This is a compression of an already-frozen contract. The spend authorization stands; no gate is
re-asked.
