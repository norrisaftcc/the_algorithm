# Finding — the discount window, and what the balance actually was

Recorded 2026-07-31 by the Algorithm's seat, on the peer's instruction to spend the
remaining OpenRouter credits on a small productive experiment before they expire.

Every figure below was read out of a committed file. The two catalogues are
`registry/probe_runs/30484858384-catalog/openrouter_models.json` (367 models, pinned
2026-07-29) and `registry/probe_runs/30672191114-catalog/openrouter_models.json` (336
models, fetched 2026-07-31). The balance is
`registry/probe_runs/30672191114-catalog/credits.json`.

---

## 1. The balance was never read, and the carried figure was wrong by $4.82

`registry/probes/experiment_queue.json` carried `spent_to_date_usd: 8.6086` and, in
`_hard_bounds`, "$12.91 remaining." Neither had been read from the account. Arithmetic on
them gave an expected ~$11.39 remaining.

The account says:

```
total_credits   20
total_usage     13.42366195
remaining        6.5763
```

**The estimate was high by $4.81.** A ceiling set from it would have been set against a
balance that did not exist — and E1 has already shown what a ceiling in the wrong place
does: 27 of 330 cells, redacted as R3, not citable as a rate.

## 2. The ledger method was sound; only the cached number was stale

Summing `spend_usd` across every `results.json` under `registry/probe_runs/`:

| run | n | ceiling | spend_usd |
|---|---|---|---|
| `30485319626-smoke` | 1 | 1.00 | 0.0037 |
| `30485573994-smoke` | 1 | 1.00 | 0.0037 |
| `30485799617-full` | 3 | 10.00 | 2.5157 |
| `30485884822-full` | 5 | 10.00 | 4.5694 |
| `30499365397-full` | 3 | 1.00 | 1.4167 |
| `30501423981-full` | 2 | 2.50 | 0.0994 |
| `30505005072-full` | 3 | 0.75 | 0.0630 |
| `30510058096-full` | 3 | 1.00 | 0.5906 |
| `30512717990-full` | 3 | 1.25 | 0.8112 |
| `30515487112-full` | 3 | 2.50 | 1.6907 |
| `30583623192-full` | 3 | 2.50 | 1.6596 |
| **sum** | | | **13.4237** |

Account `total_usage` is **13.42366195**. The two agree to the cent, and **nothing is
unattributed** — every dollar the account spent has a committed transcript directory
behind it.

So the defect is narrower than "the ledger drifted." The recomputation method already in
`experiment_queue.json` — sum `spend_usd` across every results file — is exactly right.
The cached `8.6086` was simply written on 2026-07-30 and never updated for the five runs
that followed it ($4.8151 between them). **A cached total of a computable quantity is a
liability with no offsetting asset.** It can only ever be right by coincidence.

This is the same family as `drift_log.md` D2–D5 — asserting a property that could have
been read — with one difference worth naming: here the *procedure* was correct and
documented, and the drift entered anyway because a number was allowed to sit beside it.
D2–D5 are failures to look. This is a failure to look *again*.

**Practice it suggests, not proposed as canon.** Where a file carries both a method and
the method's last output, the output is a cache and should be labelled one. Unfrozen.

## 3. Eleven models are cheaper than the pin; one of them is on the roster

Base `pricing.prompt` / `pricing.completion`, USD per 1M tokens, diffed across the two
catalogues:

| model | cut | pinned | now |
|---|---|---|---|
| `openai/gpt-5.6-luna-pro` | 80.0% | 0.500 / 3.000 | **0.100 / 0.600** |
| `openai/gpt-5.6-luna` | 80.0% | 0.500 / 3.000 | **0.100 / 0.600** |
| `qwen/qwen2.5-vl-72b-instruct` | 44.4% | 0.800 / 1.000 | 0.250 / 0.750 |
| `mistralai/mistral-small-3.2-24b-instruct` | 31.2% | 0.100 / 0.300 | 0.075 / 0.200 |
| `qwen/qwen3-235b-a22b-thinking-2507` | 23.3% | 0.300 / 3.000 | 0.230 / 2.300 |
| `openai/gpt-5.6-terra-pro` | 20.0% | 1.250 / 7.500 | 1.000 / 6.000 |
| `openai/gpt-5.6-terra` | 20.0% | 1.250 / 7.500 | 1.000 / 6.000 |
| `google/gemma-4-31b-it` | 18.5% | 0.140 / 0.400 | 0.100 / 0.340 |
| `poolside/laguna-s-2.1` | 10.0% | 0.100 / 0.200 | 0.090 / 0.180 |
| `moonshotai/kimi-k2.6` | 8.8% | 0.646 / 2.720 | 0.589 / 2.480 |
| `~moonshotai/kimi-latest` | 6.1% | 3.000 / 15.000 | 2.900 / 14.000 |

**Exactly one pinned-roster model is in that list**, and it is the cheapest model on the
roster already. So the honest reading is:

> The discount window does not make the pinned battery cheaper. It does not buy n on the
> roster. What it buys is a *different set of models* at a price the seat map has never
> been able to consider.

That distinction is load-bearing, because the plan this finding supports was framed as
"discounts buy n." They do not, on the roster. Arm 1's $2.50 ceiling is therefore
unchanged, funded out of the read balance rather than out of a saving that did not
materialise. Arm 2 is where the window is actually spent.

### Method note, and its limit

The discounted-models collection page is unreachable from the development container:
`CONNECT` to `openrouter.ai` returns 403, for the API and the page alike. So the set
above is *derived*, not read — it is "models whose base price fell between two
catalogue fetches," which is a different predicate from "models OpenRouter lists as
discounted." The two probably overlap heavily and are not the same set. A permanent
price cut and a promotional discount are indistinguishable here, and a model discounted
before 2026-07-29 is invisible to this method entirely.

The advantage is that both sides of the comparison are committed files anyone downstream
can re-diff. The web page is not.

## 4. `openai/gpt-5-codex` is gone from the catalogue

`experiment_queue.json:_closed.strike` recorded that all six of its cells in run
`30501423981` returned HTTP 404 "Model not found," and said the id must come off
`spike_models`. It is now off.

The strike is also corroborated rather than assumed: the id is **absent from the
336-model catalogue**. The 404s were the model leaving the catalogue, not a transient
provider fault. Unrun, not failed, and not retryable — the strike's original wording
stands unchanged.

The catalogue lost 31 models between the two fetches. No other pinned or spike id is
affected; the judge, `openai/gpt-4.1-mini`, is still present.

## 5. What was pinned, and what it is not

`registry/probe_roster.json` gains a `discount_roster` key holding five of the eleven:
`openai/gpt-5.6-luna`, `openai/gpt-5.6-luna-pro`,
`qwen/qwen3-235b-a22b-thinking-2507`, `google/gemma-4-31b-it`, `moonshotai/kimi-k2.6`.
Per-entry reasons are in the file.

The pinned `models` list is untouched, so Arm 1 stays comparable to run `30485884822`.
`discount_roster` carries the same bound `spike_models` carries: **not qualified for any
seat, and no seat verdict may cite them.**

A discount is a price. Nothing in this document claims anything about how these models
behave. Their cells do not exist yet.

---

## ASSAY

**Survives:** the balance ($6.5763 remaining, read); the reconciliation (ledger sum equals
account usage to the cent, nothing unattributed); the eleven-model price diff; the codex
absence; the stale-cache finding in §2.

**Does not survive:** "discounts buy n on the roster" — measured false, one roster model
moved, and it was already the cheapest. The plan's framing is corrected here rather than
carried forward.

**Not established:** that the derived set equals OpenRouter's published discount
collection; that any `discount_roster` model can hold any seat; that a promotional price
persists past this window.

This is a finding, not a draft.
