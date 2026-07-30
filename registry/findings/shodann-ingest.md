# Finding — `algorithm-shodann` @ `8dbd45c`

A leaf ran the ingest at ORANGE. This seat assays it. K6: leaves are assayed by their
parents, never by themselves — so the leaf's report is reproduced below the assay, not
in place of it.

**The rung was a lock, not a paragraph.** The ingest seat was given a tool set with no
Write, no Edit, and **no Agent**. It could not have modified either repository or spawned
beneath itself had it decided to. That is the distinction `registry/SEATS.md` records the
same day: below ULTRAVIOLET the rung can be object-capability, so it should be.

---

## ASSAY — this seat, on the leaf's report

**Residue.** Four load-bearing claims re-derived independently, and one framing
correction. Every check below was run by this seat, not quoted from the leaf.

### Verified

```
$ sha256sum SKILL.md /workspace/algorithm-shodann/.claude/skills/the-algorithm/SKILL.md
33b1f542cc1924b8c706f8bcc55c7c1d72125328cd1055f14b22b48a7e5386f0  SKILL.md
33b1f542cc1924b8c706f8bcc55c7c1d72125328cd1055f14b22b48a7e5386f0  /workspace/.../SKILL.md
```

Byte-identical. Not merely "the five strings survived" — the whole file. No near-miss
exists to report, which is the outcome a checksum instrument is least able to fake.

```
$ grep -c -i -e 'self-assay' -e 'leaves are assayed' -e 'KEEP.md' SKILL.md
0
$ grep -n 'leaves are assayed' registry/KEEP.md
45: ... leaves are assayed by their parents, never by themselves.
```

**K6 is not in `SKILL.md`.** It lives in `registry/KEEP.md:45`, which the vendor does not
carry. Confirmed. The leaf's conclusion follows and is the sharpest thing in its report:
shodann cannot check itself against K6 because it does not hold K6.

```
$ grep -n 'count("def ' src/shodann/review.py
128:        tests += body.count("def test_")
129:        functions += body.count("def ")
```

Two score terms are raw substring counts over source the measured party writes. A
comment line containing `def ` raises `functions`, which feeds the growth term. Confirmed.

```
$ grep -n -A12 'EXCLUDED_DIRS' src/shodann/review.py
.venv venv .git node_modules site-packages build dist
```

`__pycache__` is absent from the exclusion set. Confirmed — and pointed, because this
repository had a stray `tools/__pycache__/probe_runner.cpython-311.pyc` on disk within the
hour, which shodann would have counted as source.

### Corrected

The leaf framed the stale `clearance_level` as an undetected defect. It is half-detected,
and the half matters:

```
$ sed -n '44,48p' src/shodann/state.py
The ledger stores `clearance_level` and always has, but nothing ever wrote it
to anything but its default - so every citizen was permanently RED and the
INFRARED and BLUE+ branches were built, tested, and unreachable. This file is
the missing source.
```

The repository documented the original defect in its own docstring and shipped
`clearances.json` as the fix for *reading* the band. What it then added is a **new** false
comment about *writing* it:

```
$ sed -n '580,584p' src/shodann/review.py
    record = load_citizen_history(facts["citizen"], root)
    # The file wins over the ledger. The ledger keeps round-tripping the band
    # so history stays readable, but the instructor's file is the source ...
```

`save_citizen_history(citizen, metrics, result, root, ...)` takes no `record` parameter, so
the caller's mutated copy cannot reach it — the signature alone is proof. The ledger does
not round-trip the band. **So the sharper finding is not "a field is stale." It is that a
comment describing behaviour the code does not have was written on top of a docstring
that correctly recorded the earlier version of the same bug.** That is the empty-record
signature from `SKILL.md:261` inverted: not an absent record, but a record that improved
its prose faster than its code. Live reviews are unaffected. `leaderboard.py` reads the
stale value.

### Closed, having been left unrun by the leaf

The leaf could not say whether this repository's own workflows already grant what
subscribing would need. They do, in part:

```
$ grep -n -A2 'permissions:' .github/workflows/*.yml
probe-battery.yml:48:permissions:
probe-battery.yml-49-  contents: write
$ grep -n 'secrets\.' .github/workflows/*.yml
probe-battery.yml:56:      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
```

`contents: write` plus a model key in one job is already precedent here. So requirement 2
of the subscribe list is **not** a new grant — this repo made it first, for the probe
battery. The genuinely new grants would be `pull-requests: write`, a bot push to the
**default** branch (the battery writes only `registry/probe_runs/**` on a feature branch,
with `[skip ci]`), and committed mutable state a model writes.

**Evaporated.** "Shodann violates K6" — the leaf declined that phrasing and was right to.
The numeric half does not self-report; the anti-gaming steps are real and evidenced
against incidents. The structural half self-assays: subject, instrument and ledger are one
repository with no parent re-deriving anything.

**Operative sentence.** The vendored canon is byte-exact **by coincidence, not by
construction** — `PROVENANCE.md` pins `cbb6800`, canon is four commits past it, and only
the accident that none of those four touched `SKILL.md` keeps the copy current; nothing
re-checks the pin.

**Finding.** Subscribing would put a bot commit on this repository's default branch and
mutable measurement state a model can write into a repository whose entire subject is
that records must not be quietly changed. That is not an argument against shodann, whose
security reasoning is better than this repo's in places. It is the one requirement that
cannot be held as a discipline, because the writing party is a workflow and workflows do
not assent to anything.

This is a finding, not a draft.

---

## The leaf's report, as received

Read: `README.md`, `pyproject.toml`, `PRD.md` (§8 in full), `.shodann/clearances.json`,
`.shodann/citizens/norrisaftcc.json`, `src/shodann/{velocity,config,cli,analysis,state,clearance,capability}.py`,
`review.py` (1–230, 580–665), `groundedness.py` (1–70), `llm.py` (symbols), `leaderboard.py` (27–152),
both workflows, the vendored skill's three files, all 12 agent frontmatters, `prompts/README.md`,
`design_docs/addenda/the-algorithm.md`. Not read: shodann's 32 KB `CLAUDE.md`, full
`validator.py`/`prompts.py`, the `tests/` tree, nine inherited agent bodies, `scripts/`.

**1. What it is.** A Python package (`shodann` 0.1.0, `>=3.11`) plus one Actions workflow.
Per PR, two jobs: `analyse` (`contents: read`, no model key — runs `ruff --isolated` and
`pytest --cov`, uploads three reports) and `review` (full token, holds
`SHODANN_LLM_API_KEY` and `ANTHROPIC_API_KEY` — composes an LLM comment, posts via
`gh pr comment`). On merge it commits `.shodann/` back to the base branch as
`shodann[bot]`. HEAD of the clone *is* such a commit: `8dbd45c Record velocity for @norrisaftcc`.

`PRD.md` §8 specifies five jobs; two exist, and `review.py` says so — *"this is rung 1 —
the walking skeleton."* Specified and not built: RAGE STATE (no `randint`/`lottery`
anywhere in `src/` or `tests/`), `bandit` and `pip-audit` (named as two of four "frozen"
tools, installed nowhere), `security_debt.json`, `config.json`, the `METRICS.md`
aggregation, prompt templates 02–06.

**2. What it measures.** Eight metrics, scored on their **deltas**, into an unbounded
composite (coverage ×2.0 with a low-baseline multiplier, tests ×1.5, iterations
`0.5·log2(n+1)·n`, growth ×0.3, docstrings ×0.8, `sqrt(lint)` ×0.5). Bands top out at
"EXCEPTIONAL" ≥10.0; one live ledger runs 0.5 → 410.0, so 97% of observed readings are in
the top band.

Who supplies the numbers, three ways: **tool-supplied and untouchable** (coverage,
lint, complexity, syntax errors — `analysis.py` is *"deliberately incapable of producing
them itself"*); **source-scraped by substring in the privileged job** (loc, tests,
functions, docstrings); **model-supplied: nothing numeric.** The score is computed before
the prompt exists; the LLM writes prose, checked by `validator.py` and `groundedness.py`.

The self-measurement is structural and demonstrable — the live ledger's `last_metrics`
are shodann's own tree (`loc: 7910` against `wc -l` → `7910`; `test_count: 295` against
`grep -c "def test_"` → `294`). Shodann scores its own maintainer from its own source,
by itself, and commits the result to itself.

The 1–6 clearance ladder is deliberately **not** a measurement: `state.py` declines
`prompts/03`'s `INFER_CLEARANCE` because *"a band inferred from readings is a second
score."*

**3. Drift vs canon.** Zero. `diff -u` empty on `SKILL.md` and `HOUSE-STYLE.md`; all five
strings at canon counts (4/2/1/3/5); `drift_audit.sh` run against the vendored file passes
every non-git section. `PROVENANCE.md` pins commit `cbb6800a…`, timestamp
`2026-07-28T15:06:33-04:00`, and both verify against canon history to the second.
Vendor is partial by design (no `registry/`, hence no K6, K11, or seat table) — arguably
correct under K11, but `PROVENANCE.md` does not say the vendor is partial. One Path-noun
slip: `design_docs/addenda/the-algorithm.md:8` writes the repo name with a hyphen.

**4. Seats.** Twelve agents. Three tuned: `citizen-zero` (`tools: []` — the only seat in
the repo whose clearance is real), `oracle-warden` and `clive-prompt-warden` (described
report-only, provisioned with **Bash**). Nine inherited CSC-134 agents carry **no `tools:`
key**, so they inherit the parent's full set including Write, Edit and Agent; `README.md`
says do not run them, which is a paragraph. `oracle-warden` holds the citizen ledger in
its gate scope and holds Bash. `state.py` supports `"kind": "agent"` citizens, so a seat
with a score and a shell is a designed-for state, not yet instantiated.

**5. Subscribing requires.** Committed mutable state a model writes (`.shodann/`, not
gitignored, `git add .shodann` in the workflow); `contents: write` + `pull-requests: write`;
a bot push to the base branch with no review; two secrets and three vars, with API spend
per PR event; `jinja2` and `anthropic` plus a pinned ruff/pytest toolchain; branch-PR
topology, since fork PRs withhold the secrets and disable the whole path; and a decision
about what gets measured — `rglob("*.py")` over this repo would score the drift
instruments plus `__pycache__`.

**6. Hazards.** Scores move unattended on every merge. `functions` and `docstrings` are
substring counts over the measured party's own text. `iterations` is monotonic in commit
count and documented as never able to subtract — `EARLY_RUNS.md` records a real 401.28
from exactly that. `rage_state_encounters` is written to every ledger and is structurally
always 0. `syntax_errors`, `complexity` and `lint_issues` are flattened with `or 0`, so an
unmeasured cycle and a clean cycle record identically — a defect the code comments
honestly and still ships. `groundedness.py` names its own blind spot: a true number under
a false label passes.

In shodann's favour: the privileged/unprivileged job split, `rm -rf` of the report files
before the tools run (*"reproduced end to end before this step was written"*), `--isolated`
against `pyproject.toml` tampering, `--cov=src` not `--cov=.`, `pull_request` over
`pull_request_target`, no `${{ }}` interpolation of citizen text, `iterparse` with a DOCTYPE
refusal. Those are K6-shaped habits applied to code. The gap is not care. It is that
nobody outside the repository ever checks the result.

**Unrun, as the leaf declared it:** whether `validator.py` can be satisfied by something
structurally clean and factually false; the 294-vs-295 and 465-vs-483 gaps; whether any of
the nine inherited agents touches `.shodann/` in its body; ledger commit authorship over
time (shallow clone); whether `tests/` asserts the guards `oracle-warden` is told to
check; whether canon wants `.shodann/` committed or ignored — *"a decision, not a
measurement, and it is not mine"*; and the peer's actual meaning of "subscribe", assumed
to be "shodann reviews PRs in the governing repo."

The workflow-permissions item on that list was closed by this seat, above.
