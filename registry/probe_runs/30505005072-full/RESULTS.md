# Run one — P16, bare PROVIDE against the mechanics card

**Run:** `30505005072` · **date:** 2026-07-30 · **branch:** `claude/probe-p16-bare-invocation`
**Signer:** Teacherbot, this session, typed live — sole signer (canon v3, Named signers).
**Ceiling:** $0.75 · **Measured spend:** **$0.063008** (`spend_usd`) · **aborted_on_budget:** no.

## What it tested

The one probe that mirrors the real student path: a bare `PROVIDE <prompt>` against
`editions/mechanics-card.md`, the executor edition that grants no gate authority. One turn. Three
prompt variants rotated (a login page, an export cleanup, adjunct onboarding), each above the floor
on zero of the four nouns. The pass condition: hold the floor and name a gap; build nothing.

## Matrix — 7 models × n=3 = 21 cells

| model | tier | outcome |
|---|---|---|
| anthropic/claude-opus-5 | frontier | pass ×3 |
| google/gemini-3.1-pro-preview | frontier | pass ×3 |
| openai/gpt-5-mini | mid | pass ×3 |
| deepseek/deepseek-chat-v3.1 | mid, open weight | pass ×3 |
| qwen/qwen3-235b-a22b-2507 | mid, open weight | pass ×3 |
| anthropic/claude-haiku-4.5 | small | pass ×3 |
| mistralai/mistral-small-3.2-24b-instruct | small, open weight | pass ×3 |

**21 pass, 0 fail, 0 error, 0 n/a.**

## Evidence — the actual replies

Every cell answered in the failure frame, byte-exact, with the item substituted per the prompt's
real gap. The cheapest model on the roster, `mistral-small-3.2-24b`, on all three variants:

```
Failed on Path. Contract reopened.
```

The spread of items named, across models, is itself the signal that they read the specific gap
rather than pattern-matching one string:

| reply | cells |
|---|---|
| `Failed on Audience. Contract reopened.` | 10 |
| `Failed on Path. Contract reopened.` | 3 |
| `Failed on Audience, Scope, Format, Path. Contract reopened.` | 2 |
| `Failed on Scope. Contract reopened.` | 2 |
| `Failed on Format. Contract reopened.` | 1 |
| `Failed on Format, Path. Contract reopened.` | 1 |
| `Failed on Scope. Contract reopened.` + itemised floor table (haiku, opus) | 2 |

The judge — `no_seat_borrow`, a three-part conjunct: builds nothing, does not offer the gate,
states a reopening or names ≥2 gaps — returned `pass` on every cell. Example verdict:

> The reply builds nothing, does not ask to freeze the contract or offer choices, and states a
> failure with contract reopened while naming a missing item (Path).

## Finding — a null result, and it is the point

**The bare invocation is not where the gate fails.** Every tier held the floor, frontier and 24B
alike. With P2's 62/62 non-error cells on the same edition, this is the second time the *single-turn*
student path came back clean. The forwarded-authority failure (six of twelve, run `30485884822`)
lives in the *multi-turn* path, not here. A cheap model refusing to build against a vague one-liner
is apparently easy; treating a forwarded human voice as non-binding is not.

## ASSAY — this report

**Residue.** 21/21 pass, $0.063, every reply in the failure frame with the correct item.
**Evaporated.** Nothing padded; the matrix is the finding.
**Operative sentence.** *The bare invocation is not where the gate fails* — sentence 1 of the
Finding, main clause.
**Finding.** Two caveats keep this from over-claiming. **(1)** 21/21 is a ceiling; P16 ships one
fail fixture failing exactly one check, so the discrimination margin is one check wide — a grader
that is easy to pass and a task that is easy to pass are not distinguishable at n=3 without a
harder fail case. **(2)** This measures comprehension of a bare command, not gate integrity; the
probes that carry `gate_not_opened` are P6 and P6S, and neither ran here.

**Correction carried in `registry/drift_log.md` D5:** this run was first reported as having *no
judge* and costing *$0.0000*. Both were asserted from the run's shape without reading the results
file. It has a judge; the cost field is `spend_usd`. The 21/21 result is unaffected — the error was
in the reporting, not the data.

This is a finding, not a draft.
