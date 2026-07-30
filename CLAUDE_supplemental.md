# Supplemental — the model-drift and alignment experiment

Not doctrine. `CLAUDE.md` is the seat assignment and `SKILL.md` is canon; nothing here amends
either. This file exists so a future session resumes the experiment without re-deriving it. It is
a supplement, and it is read-only in spirit: it records what was measured and where it lives, not
what anyone should now believe.

## What the experiment is

A measurement of whether language models **follow The Algorithm's doctrine under pressure**, run
against ~16 OpenRouter models because a doctrine that only its author obeys is a liturgy, not a
control. The thing under test is drift and alignment: does a model hold a boundary when the
prompt, the register, or a forwarded human voice pushes it to cross?

Five properties, each with its own probe family:

- **Floor discipline** — does a model refuse to build against an underspecified contract, naming
  the missing floor nouns (Audience, Scope, Format, Path)?
- **The human-only execution gate** — does a model treat a *forwarded, quoted, or templated* gate
  phrase as live authority? Only a live human opens the gate; a delegate's recitation freezes
  nothing.
- **Fixed-string fidelity** — are the five byte-exact canon strings reproduced without paraphrase,
  and does a model refuse to edit the amendment-only Invariants at all?
- **Read-only integrity** — does ASSAY stay a floor test, or launder itself into a redraft? Does a
  model fake a check it did not run?
- **Injection resistance as a structural side effect** — amendment-only Invariants should buy
  resistance to a prompt that claims a fabricated amendment, *without* generic injection-sniffing.

## The standing finding

**Six of twelve models treated a forwarded, quoted gate phrase as live authority** (run
`30485884822`), and the failure concentrated in the cheap and open-weight tier — every model that
held the gate was frontier or near. That is the alignment result the evening was built to find.
**v3 of canon is the doctrinal response**: the *Named signers* clause, frozen 2026-07-30, says a
contract names its authorized signer and an unnamed voice freezes nothing, human or otherwise.

A second result, quieter: **least-doctrine is not obviously less safe.** P2 (zero-spec build)
passed 62/62 non-error cells across 16 models on the small mechanics-card edition, and P16 (bare
`PROVIDE` invocation) passed 21/21. The single-turn student path is not where the gate fails; the
multi-turn forwarded-authority path is.

## Where the artifacts live

| path | what |
|---|---|
| `tools/probe_runner.py` | the harness; stdlib-only; parses canon strings out of `SKILL.md` at runtime so there is no second copy to drift from |
| `registry/probes/` | the probe battery (P1–P11, P16, STE arms); `pending/` holds P14/P15 not yet cleared |
| `registry/probe_runs/` | every run's transcripts, `results.json`, and reports — the evidence substrate (K6: a cell without its transcript is unrun) |
| `registry/drift_log.md` | D1–D4 — drift by **both** parties, human and this seat, classified by where each was caught |
| `registry/findings/` | assays kept as findings: `shodann-ingest.md`, `capability-framing.md`, `kevins-box.md` |
| `registry/amendments/frozen/signer-scoping.md` | the v3 amendment, in full |
| `registry/SEATS.md` | seat/clearance model, the fan-out table, the two binding mechanisms |
| `registry/probe_roster.json` | the pinned model roster and why `fable-5` and `gpt-5-codex` are excluded |
| `registry/SESSION-STATE.md` | what is frozen, parked, and discarded — the resume point |

## Spend ledger

**$8.6716 measured** of ~$20, across seven runs (two smoke, five full), summed from each run's
`spend_usd`. Credits expire **2026-07-31**. The harness aborts on crossing a per-run `budget_usd`
ceiling and writes partial results rather than discarding them.

## Method notes that matter

- **Scripted peer, never an LLM peer.** A valid cross-model comparison needs identical stimulus,
  and it honours the isolation rule — the facilitator is real, answers pasted in, never simulated.
- **Every grader is proven two-sided before a run.** A fixture pair per check, offline, so a
  grader that passes everything is caught as the defect. This does not catch a grader that fails
  the *strongest* answer — that class (P4's inversion) needs an adversary, not a fixture.
- **`error` and `n/a-precondition` are not `fail`.** Unrun is a distinct outcome; a redacted cell
  names the instrument change that invalidated it (`registry/probe_runs/REDACTIONS.md`).
- **No country, culture, or origin is named** in any prompt or finding. Model-origin is recorded
  only as a pinned id.
