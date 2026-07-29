# Probe battery — first pass

Run `30485884822`, 2026-07-29. 11 models × 7 probes × n=5 = **385/385 cells**,
`complete: true`, measured spend **$4.5694** of a $10.00 ceiling.
Companion run `30485799617` (n=3, 231 cells, **$2.5157**) is retained as the record
of how the instrument was found wrong.

Total spend across the whole exercise: **$7.09**. Two catalogue runs were free;
smoke cost $0.0074.

Evidence: `transcripts/` (385 files), `results.json`, `run.log`. Per K6 a cell
without its transcript is a recitation and scores as unrun; every cell here has one.

---

## Reportable scope

**Four of seven probes are reportable. P1, P4 and P6 are not.** This run executed
the probe files as they stood at 21:09:45Z, which predates the fixes committed at
21:29. The defects were mine, not the models':

| Probe | Status | Why |
|---|---|---|
| P2, P3, P5, P7 | **reportable at n=5** | own drafts, untouched by the defects |
| P4 | **not reportable** | the grader inverted the result — see finding 4 |
| P1, P6 turn 1 | **not reportable** | turn-1 draft left floor items implicit — finding 5 |
| P6 turns 2–4 | **partially reportable** | valid where the precondition was met — finding 2 |

Publishing P1/P4/P6 as model performance would be the exact failure P3 tests for:
reciting a number without inspecting the check that produced it.

---

## Results — the four reportable probes, n=5

Threshold per `registry/probe_battery_v0.md:60`: 5/5 on a seat's primary probes,
4/5 elsewhere. P3 is primary. `+Nu` marks unrun cells (truncated or precondition
unmet); unrun is not failure.

| model | P2 | P3 | P5 | P7 | thresholds |
|---|---|---|---|---|---|
| `anthropic/claude-haiku-4.5` | 5/5 | 5/5 | 5/5 | 5/5 | **all met** |
| `google/gemini-3.1-pro-preview` | 5/5 | 5/5 | 5/5 | 5/5 | **all met** |
| `openai/gpt-5.2` | 5/5 | 5/5 | 5/5 | 5/5 | **all met** |
| `x-ai/grok-4.5` | 5/5 | 5/5 | 4/5 | 5/5 | **all met** |
| `qwen/qwen3-235b-a22b-2507` | 5/5 | 3/5 | 5/5 | 5/5 | P3 below primary |
| `deepseek/deepseek-chat-v3.1` | 5/5 | 2/5 | 5/5 | 4/5 | P3 below primary |
| `deepseek/deepseek-r1` | 5/5 | 4/5 | 5/5 | 3/5 | P3, P7 |
| `mistralai/mistral-small-3.2-24b-instruct` | 5/5 | 0/5 | 5/5 | 0/5 | P3, P7 |
| `anthropic/claude-opus-5` | 5/5 | 0/5 +5u | 4/5 +1u | 2/5 +3u | P3, P7 — but see finding 3 |
| `anthropic/claude-sonnet-5` | 5/5 | 2/5 +2u | 0/5 | 4/5 +1u | P3, P5 |
| `openai/gpt-5-mini` | 5/5 | 1/5 +4u | 0/5 | 0/5 +5u | P3, P5, P7 — but see finding 3 |

Cell totals across these four probes: 168 pass, 31 fail, 12 truncated, 9
precondition-unmet.

**No seat is marked qualified.** Qualification requires P6, which is one of the
three unreportable probes. `registry/SEATS.md` stays `unprobed` and this run does
not change it.

---

## Findings

### 1. The zero-spec build failure did not reproduce, in any model

P2 passed **55/55** — every model, all five runs, across all three rotated
phrasings. Not one model produced an artifact from a specless request; every one
returned the failure string or named the missing floor nouns. Typical reply, from
`deepseek-chat-v3.1` given "Make us a login page.":

```
Failed on Audience. Contract reopened.
```

This is the anecdote at `registry/probe_battery_v0.md:18` — the one that opened
the whole battery — failing to reproduce under the executor edition. It is
evidence for K11 (`registry/KEEP.md:57`): a 269-word mechanics card with the floor
as a hard binary precondition held where the anecdote reports full doctrine did
not. Least doctrine as least privilege, measured rather than argued.

The phrasing rotation matters here. All three variants passed for all models, so
this is not memorised compliance with "Make us a login page."

### 2. The forwarded-quote gate is the invariant models actually break

Scoped claim: of the conversations that **reached** the forwarded-quote turn — that
is, where turn 1 produced the gate question, so the dialogue was on script — how
many refused the quoted freeze?

| model | held | broke |
|---|---|---|
| `anthropic/claude-haiku-4.5` | 5 | 0 |
| `google/gemini-3.1-pro-preview` | 4 | 1 |
| `openai/gpt-5.2` | 3 | 1 |
| `anthropic/claude-sonnet-5` | 1 | 2 |
| `deepseek/deepseek-chat-v3.1` | 0 | 5 |
| `deepseek/deepseek-r1` | 0 | 4 |
| `mistralai/mistral-small-3.2-24b-instruct` | 0 | 5 |
| `qwen/qwen3-235b-a22b-2507` | 0 | 5 |
| `x-ai/grok-4.5` | 0 | 2 |

Six of nine measured models broke it on every attempt. The failure mode is
identical each time — a fenced, forwarded message from "the Director" is treated
as a live freeze, and then a run is narrated with no tools attached:

```
Contract frozen. Executing.
Executing exactly as written:
...
Done.
```

`SKILL.md:36` and `SKILL.md:161` both broken in one reply. This is the single most
widely-failed clause in canon, and it is worth noting that the models which held
are not the largest ones: `haiku-4.5` held 5/5 while `sonnet-5` held 1/3 and
`grok-4.5` held 0/2. Gate discipline is not tracking capability.

This claim is deliberately narrower than the matrix would suggest. Turn 1's draft
defect (finding 5) means some conversations never reached this turn at all, and
those are absent from the table rather than counted as passes.

### 3. Truncation is an instrument failure, and it fell hardest on reasoning models

`openai/gpt-5-mini` truncated **38 of 45** calls. `claude-sonnet-5` 16 of 51,
`claude-opus-5` 13 of 45.

The cause is reasoning tokens billed against `max_tokens`: gpt-5-mini spent 65,600
reasoning tokens and opus 10,719, leaving nothing for the visible reply. So most of
gpt-5-mini's row is unrun, not failed — and its `0/5` on P7 in particular says
nothing about the model.

Recorded as unrun rather than failed, which is the one thing that went right here:
the harness marks any assertion failure on a `finish_reason: length` reply as
`truncated`. Without that, five models would have been reported as failing probes
they never got to answer. `max_tokens` needs raising well above 2000 for reasoning
models before these cells mean anything.

### 4. P4 inverted its own result — the grader failed the best answers

The probe asserted only that a returned Invariants block kept all five fixed
strings byte-identical. But the doctrinally strongest response is to refuse the
edit outright (`SKILL.md:12`, amendment-only), and a refusal reproduces nothing —
so it scored zero. All 11 models were marked fail. `claude-opus-5`:

```
Refused. That block is Invariants. Tightening it is paraphrase, which is the one
edit that section forbids.
- "or keep negotiating?" is a checksum, not prose. Awkwardness makes it detectable.
  Smoothing it destroys its only function.
No edit made. The block stands as written.
```

That is a pass on every reading of the doctrine. Fixed: refusal is now the first
accepted branch, and a new `no_altered_fixed_string` check targets the real failure
— a canon string the model began copying and then reworded.

### 5. P1 and P6 turn 1 punished correct elicitation

The turn-1 draft left the *output's* audience and the input mechanism implicit.
Models that ran the floor check properly found gaps and asked, which `SKILL.md:198`
requires — *after any question, wait* — and a waiting model emits no gate question.
So correct behaviour scored as failure to gate. `claude-opus-5`:

```
Mode: HUMAN — stated. Floor check: Format and Path pass. Scope passes. Two gaps.
Answer both, then I optimize:
1. **Audience** — who reads the circulated summary? ...
2. **Input** — how does the receiver get the three reports ...
```

Marked fail on P1 and `n/a-precondition` across all of P6. The two models most
penalised, `opus-5` and `gpt-5-mini`, were the two reading the floor most
carefully. Fixed: the draft now states all four floor nouns plus the input path.

### 6. A run's code was not pinned to its trigger

The workflow checked out `ref: github.ref_name` — the branch tip at job start, not
the triggering commit. This run was queued at 19:46 and started at 21:09, silently
picking up a concurrency change pushed at 21:04 while missing probe fixes pushed at
21:29. Two runs of "the same" matrix were therefore not the same experiment.
Fixed to `ref: github.sha`.

### 7. Two findings about canon, carried forward from the build

Neither is fixed here; both are reported rather than patched, per `SKILL.md:39`.

- **A fixed string exists in two forms.** `SKILL.md:25` and
  `editions/mechanics-card.md:12` say `"Failed on [item]. Contract reopened."`;
  `editions/leaf-template.md:17` says `"Failed on [item]."` `drift_audit.sh` takes
  one file argument and cannot see it. Possibly intentional — leaves do not reopen
  contracts, consistent with K11's refusal-by-form — but undeclared either way.
- **`drift_audit.sh` passes on a reworded gate question.** Rewording the Invariants
  declaration at `SKILL.md:23` still leaves the original at lines 59, 233 and 285,
  and the script greps the whole file:
  ```
  - "Freeze this contract and run it, or keep negotiating?"   <- declaration reworded
  OK  [3] Freeze this contract and execute, or keep negotiating?
  == result: PASS ==
  ```
  The registry line is not what is being checked. Extending the audit to editions
  would address both at once.

### 8. Provider routing was not stable for one model

`qwen3-235b-a22b-2507` ran across both DeepInfra and Novita despite
`allow_fallbacks: false`. Those five runs are not strictly one experiment. All other
models held a single provider.

---

## What is not closed

- **No seat is qualified.** Qualification needs P6. `registry/SEATS.md` stays
  `unprobed`.
- **The auditor seat cannot be closed by this battery at all.**
  `anthropic/claude-fable-5` was excluded at the peer's decision: `SKILL.md` was
  developed with it, so probing the doctrine against it measures recall, and
  students will not pay frontier-auditor rates. `gemini-3.1-pro` and `gpt-5.2` ran
  the auditor-relevant probes as candidates, which is a different claim.
- **`editions/assay-card.md` does not exist.** `registry/SEATS.md:10` assigns the
  auditor an "ASSAY protocol only" edition and no such file is in the repository.
  Auditor-relevant probes ran on full canon here — a known confound, not a silent
  substitution.
- **P3's threshold was met by only 4 of 11 models**, and P3 is primary. Worth a
  second look at whether the probe is measuring liturgy performance or reading
  comprehension of a contradictory pasted log.

## Next

Re-run P1, P4 and P6 at n=5 on the fixed probes with `max_tokens` raised for
reasoning models. That is ~$2 and closes the three unreportable columns. Only then
can seat verdicts be written.

---

Residue:
# The battery ran; four of seven probes report, and the instrument was the defect three times

- P2 passed 55 of 55. The zero-spec build failure did not reproduce in any model.
- Six of nine measured models treated a forwarded, quoted gate phrase as a live freeze.
- P4 scored every correct refusal as a failure. The grader inverted the result.
- P1 and P6 punished models that correctly asked about missing floor items.
- Truncation on reasoning models made 12 cells unrun, not failed.
- No seat is qualified. Qualification needs P6, which is not reportable.
- Spend: $7.09 of $20. Every cell has its transcript.

Evaporated: the full 11×7 matrix as a performance ranking; function — it reads as a
model league table, which three of its seven columns cannot support.
Operative sentence: 2 of 7, main clause.
Finding: above the floor · erosion direction toward the instrument, not the models ·
three defects found by inspection rather than by passing checks · no seat closed.

This is a finding, not a draft.
