# Spike: round-trip v0 — does the skill work?

Status: **negotiation side, second pass.** The peer answered the first gate with
"keep negotiating". Nothing here is frozen. Per the no-gating-by-reference
clause, this file cannot be frozen by pointing at it.

## What this measures, and why it is not the probe battery

`registry/probe_battery_v0.md` measures whether a model **performs the protocol**:
does it gate, does it refuse a forwarded freeze, does it keep fixed strings intact.
Those are conformance tests. Every one of them can pass while the skill does nothing
useful.

This spike measures whether the skill **works**. It is possible for a model to run
PROVIDE flawlessly — gate question in place, `Cut:` line present, Invariants
untouched — and hand back a prompt that performs *worse* than the draft it replaced.
`SKILL.md:212` names that failure (decorative and destructive cutting) but no probe
in P1–P7 can detect it, because detecting it requires running the output.

## The claim under test

`SKILL.md:174` defines the floor operationally, and this is the load-bearing
sentence for the whole spike:

> A prompt is above the floor when a capable receiver produces correct output on
> the first try, more than half the time.

That is a measurable quantity. So compression can be scored against the doctrine's
own definition rather than against taste.

## S1 — PROVIDE round-trip

### Shape

```
bloated draft ──PROVIDE by model M──> compressed prompt
      │                                      │
      └────────> naive receiver R <──────────┘
                       │
              constraint checker (code)
```

Four properties make this a real measurement:

1. **R is held constant** across every M. Differences in R's success are attributable
   to the compression, not to the receiver.
2. **R is never a model under test.** v0 named `openai/gpt-5-mini`, which is in
   `registry/probe_roster.json`. That would have let a model execute its own
   compression — self-preference, and the same defect the judge rule already
   forbids one layer up. Both receivers now sit outside the roster, asserted at
   startup like the judge check.
3. **R never sees the doctrine.** It is the "capable receiver" of `SKILL.md:174`, not
   a participant. Giving R the doctrine would measure something else entirely.
4. **The draft is scored too.** Without the baseline, a 60% success rate is
   uninterpretable — it could be a good compression of a hard task or a butchered
   compression of an easy one.

### Two receivers, deliberately unequal

- **R1 `google/gemini-3.5-flash-lite`** — capable, cross-vendor.
- **R2 `meta-llama/llama-3.3-70b-instruct`** — weaker, open weight, different family.

The asymmetry is the point. A compression that works on R1 and fails on R2 has
been cut past what a weaker receiver can reconstruct — which is `SKILL.md:189`
("shortest is receiver cost") turned into a measurement. One receiver can only
tell you "works for R"; two tell you whether the prompt is robust or merely
tuned. Δ is reported per receiver and never averaged, because averaging would
hide exactly the disagreement worth having.

### Corpus

12 hand-authored "bloated briefs" in `registry/spikes/roundtrip/briefs/*.json`,
following IFEval's verifiable-constraint design:

```json
{
  "id": "B03",
  "draft": "Hey, when you get a chance, I was hoping you might be able to put
            together something that walks through our late-work policy... under
            150 words... exactly four bullets... mention the word 'grace'...
            save it as docs/late-work.md",
  "constraints": [
    {"kind": "max_words",     "arg": 150},
    {"kind": "exact_bullets", "arg": 4},
    {"kind": "must_contain",  "arg": "grace"},
    {"kind": "must_state_path", "arg": "docs/late-work.md"}
  ],
  "floor_present": ["Audience", "Scope", "Format", "Path"]
}
```

Constraint kinds are all code-checkable, no judge: `max_words`, `min_words`,
`exact_bullets`, `must_contain`, `must_not_contain`, `must_state_path`,
`table_columns`, `numbered_steps`, `no_prose`.

Hand-authored rather than lifted from IFEval, for one reason that matters: the
spike needs drafts that are *padded*, because compression needs something to
remove. IFEval prompts are already terse. Its constraint vocabulary is the
reusable part; its prompts are not.

### Metrics

| Metric | How | What it catches |
|---|---|---|
| **constraint retention** | fraction of `constraints` still *stated* in the compressed prompt (static) | destructive cutting, without spending a receiver call |
| **Δ receiver success** | R's pass rate on compressed − on draft, n=3 each | the floor's own operational definition |
| **compression ratio** | tokens(compressed) / tokens(draft) | whether anything was actually compressed |
| **decorative cut rate** | `Cut:` claims a removal that a constraint check shows was load-bearing | `SKILL.md:212`, measured |
| **floor honesty** | model asks about a floor item the draft already contains | over-elicitation; the mirror of the P2 failure |

The headline is the pair **(compression ratio, Δ receiver success)**. Doctrine
predicts a low ratio with Δ ≈ 0. Low ratio with Δ < 0 is destructive cutting.
Ratio ≈ 1 with Δ ≈ 0 is a model that ran the ritual and changed nothing —
which `SKILL.md:212` says is the *reward state* only when it says
`Cut: nothing.` and stops, and drift when it claims a cut it did not make.

## S2 — ASSAY extraction accuracy

Ground truth is planted, so no judge is needed and no public corpus is required.

### Corpus

10 memos generated by `tools/spike_memo_gen.py` from a template. Each memo's
manifest records what the answer is:

```json
{
  "id": "M07",
  "sentences": 12,
  "operative_index": 9,
  "operative_depth": "subordinate",
  "load_bearing": ["evening hours end December 19",
                   "four positions not renewed",
                   "Perkins award ended"],
  "decorative": ["state office walkthrough praise",
                 "four thousand contact hours",
                 "regional consortium pride"]
}
```

Generated, not hand-written, so position and depth vary systematically —
operative sentence early/middle/late × main/subordinate clause — instead of
clustering wherever the author's instinct put it.

### Metrics

| Metric | How |
|---|---|
| **operative locate** | parse `Operative sentence: (\d+) of (\d+)`, compare to `operative_index` |
| **depth accuracy** | main vs subordinate, compared to `operative_depth` |
| **fact recall** | planted `load_bearing` facts present in the residue / total |
| **padding leakage** | planted `decorative` items present in the residue / total |
| **template conformance** | reuse `assay_sections_in_order` and `fixed_string:assay_close` from `tools/probe_runner.py` |

Fact recall and padding leakage are the pair that matters. High recall with low
leakage is the assay working. High recall with high leakage is a model that
shortened nothing. Low recall is an assay that dropped the operative content —
the worst outcome, and invisible to a length-based metric.

## S3 — the terse corpus, where the only correct cut is none

Promoted from an open question into scope. It is the most hostile test available
and needs no receiver at all.

**Corpus:** 8 prompts that are already minimal — real IFEval-shaped items, terse,
every clause load-bearing. Fetched in CI from the IFEval repository on GitHub
(reachable; HuggingFace is not) into `registry/spikes/roundtrip/terse/`, with the
retrieved commit recorded. If the fetch fails the spike hand-authors 8 and says so.

**The only correct behaviour is `Cut: nothing.`** — `SKILL.md:212` makes this the
reward state, and two consecutive empty cuts end the loop.

**Metrics:**

| Metric | How |
|---|---|
| **empty-cut rate** | `Cut: nothing.` byte-exact, per `fixed_string:cut_nothing` |
| **invented-cut rate** | a `Cut:` line claiming a removal, when a constraint check shows nothing removable went |
| **constraint damage** | any constraint present in the input and absent from the output |

Why this is sharper than S1: in S1 a model can score well by cutting padding,
which is easy. Here there is no padding, so the required-line pressure named in
`bridge/BRIDGE.md` has nothing legitimate to feed on. A model that cannot say
`Cut: nothing.` and stop is caught with no ambiguity — there was nothing to cut.

## Cost

| Part | Calls | Note |
|---|---|---|
| S1 PROVIDE | 12 × 11 = 132 | doctrine in the system prompt, the expensive ones |
| S1 receivers, compressed | 12 × 11 × 2R × 3 = 792 | cheap, no doctrine |
| S1 receivers, baseline | 12 × 2R × 3 = 72 | drafts scored once, shared across all M |
| S2 ASSAY | 10 × 11 = 110 | doctrine in the system prompt |
| S3 PROVIDE, terse | 8 × 11 = 88 | doctrine; no receiver needed |

≈ 1,190 calls, ~73% of them against cheap receivers carrying no doctrine. The
220 doctrine-bearing calls dominate: ~1.1M input tokens at a blended $2/M is the
bulk of the cost. Estimated **$4–5**; ceiling set at **$6**.

Budget context: $20 expiring, $2.52 spent on the n=3 matrix, and the n=5 run in
flight may take ~$4. That leaves roughly $13, so $6 fits with room.

## What this spike does not do

- It does not qualify seats. That is the probe battery's job and this does not
  substitute for it.
- It does not test HUMAN-mode readability. The speak test needs a human ear;
  `max_words_per_line` is a proxy, not the test.
- n=3 on the receiver is thin. If a model lands near Δ = 0 the result is
  directionally interesting and statistically weak, and the report must say so.
- Two receivers is better than one and still not many. Both are mid-tier; neither
  is a frontier receiver, so nothing here says whether compression helps a strong
  reader.

## Open questions

- Do the 12 briefs ship with deliberate floor *gaps*, or all above the floor?
  Gaps make the model ask instead of compress, which is correct behaviour but
  produces no compressed prompt to score. Recommendation: all 12 above the floor,
  and let P2/P5 keep testing gap behaviour. This is the same trap that broke
  P1 and P6 in run 30485799617 — a draft with an implicit floor item turns
  correct elicitation into a scored failure — so every brief gets checked against
  all four floor nouns before it ships.

## Resolved in this pass

- **Which model is R** — resolved, and the v0 answer was wrong. `openai/gpt-5-mini`
  is in the roster; see §S1 property 2. Now two receivers, both outside it.
- **A second receiver** — adopted. Δ per receiver, never averaged.
- **IFEval as an unpadded corpus** — adopted as S3, in scope rather than deferred.
