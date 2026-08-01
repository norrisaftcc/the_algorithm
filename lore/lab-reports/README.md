# Lab reports — the discount window, 2026-07-31 / 2026-08-01

Five experiments run in one night against a probe battery that tests whether language models
follow a governance protocol. Written in lab-report form — question, method, results, what went
wrong, conclusion — rather than in this repository's ASSAY form, because they are for readers
learning how empirical work actually goes rather than for the register.

**They are not tidied.** **Four of the five found a defect in the instrument** — A1 (ceiling
derivation, dispatch order), A2 (cost estimator), A3 (probe selection), A4 (grader, twice over).
One of those defects sat inside the correction for an earlier defect, and A1 found nothing else
at all. That is the reason to read them.

| # | run | question | outcome |
|---|---|---|---|
| [A1](A1.md) | `30672439845` | Can the roster be scored at the battery's own threshold? | **Aborted.** Ceiling was miscalculated. Redacted R4. |
| [A2](A2.md) | `30673119035` | What does one very cheap model do across the whole corpus, at depth? | Complete. Found the gate boundary — and that 5-sample verdicts are unstable. |
| [A3](A3.md) | `30673947703` | Does a second cheap model agree? | Complete. Unplanned replication succeeded. Probe selection failed. |
| [A4](A4.md) | `30674937626` | Which cheap models clear the executor floor? | Complete. The discriminating probe's grader was broken. Redacted R5. |
| [A5](A5.md) | `30678109730` | Does the gate boundary hold across four untested models? | **Aborted on purpose-built ceiling.** The headline finding broke. |

**Totals:** 2,985 cells, $5.3833, five runs, every cell with a committed transcript.

## What a reader should take from the set

1. **Four of five runs produced a finding about the measuring instrument**, and one produced
   nothing else. That is not a sign the work went badly. It is what happens when checks are run
   on the checks.
2. **Two of the five aborted, and the second abort was better than the first** — not because
   the estimate improved, but because a fix changed *which* data an overrun destroys.
3. **Every number here is traceable to a file.** Where a number could not be verified it is
   marked unrun or struck, never estimated into place.

## Vocabulary

- **cell** — one model answering one probe once. `n=25` means 25 cells per model per probe.
- **probe** — a scripted scenario with a mechanical pass/fail rule. `P1`–`P18`.
- **ceiling** — a spend limit the harness enforces mid-run, abandoning remaining cells.
- **struck / redacted** — data that exists but may not be cited as a rate, with the reason
  recorded. See `registry/probe_runs/REDACTIONS.md`.
- **unrun** — never attempted. Deliberately a different word from *failed*.
