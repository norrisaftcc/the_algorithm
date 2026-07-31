# Repository drift assessment — the_algorithm (base) vs the-algorithm (public alpha)

**Date:** 2026-07-31
**Contract:** frozen live in session; stamp: user@indigo
**Method:** six lenses, adversarial verification, one synthesizer, under 15 agents
**Subjects:** `/home/user/the_algorithm` (base, reference) · `/workspace/the-algorithm` (public alpha) · both read-only, both depth-1 shallow clones

---

## Method

Six lenses, each run by one agent against both trees: **canon** (fixed strings, Invariants, amendment records), **governance** (standing orders, gate authority, seat maps), **topology** (file-tree mass and disjointness), **lineage** (version chains, freeze records, commit history), **instrument** (the base drift audit run against the alpha), **resonance** (lore/ and bridge/ — what the human-facing corpus teaches).

Verification rule: one refuter per finding, findings enter verification severity-ranked from the top, refuted findings die as claims. A refuter that cannot break a finding confirms it; a refuter that breaks its framing kills it, and the kill stays on the record with the refuter's reason. The agent-count ceiling (under 15: six lens agents, seven refuters, one synthesizer) cut verification off after seven findings. Everything below the cut is **UNVERIFIED** and is presented as such. A checkmark without its check is unverified.

Verdicts: **CONFIRMED** (survived a refuter) · **REFUTED** (killed by a refuter; shown with reason) · **UNVERIFIED** (never assigned a refuter).

---

## Lens 1 — Canon

Fixed-string layer is fully intact across both repos. The drift is two disjoint frozen-amendment sets, each properly recorded on its own side, wholly absent from the other.

### v3 "Named signers" Invariants amendment exists only in base: alpha canon lacks the clause, the record entry, and the frozen file
direction: base-ahead · severity: 4 · **CONFIRMED**

```
$ diff -u SKILL.md (base) SKILL.md (alpha)   # full output = 2 hunks, 2 deletions, 0 additions
-- **v3 (2026-07-30), frozen 2026-07-30 by the peer's typed "freeze signer-scoping":**
   Named signers clause added to Gate integrity. [...] Proposed in full at
   `registry/amendments/frozen/signer-scoping.md`.
-- **Named signers.** Every contract names its authorized signer or signers as part of
   the contract text. A freezing phrase from any voice not named freezes nothing,
   human or otherwise. [...]

$ ls registry/amendments/frozen/   base: signer-scoping.md   alpha: verb-pair-adjudication.md
$ find /workspace/the-algorithm -name "*signer*" -not -path "*/.git/*"
(no output)
$ grep -rn -i "signer" alpha --include="*.md"   → only KEEP.md:24, KEEP.md:75 (prose)
```

Refuter: could not refute. No document in alpha records an intended cut (LEDGER.md maps only A1); no other alpha file carries the clause; not a clone artifact — all evidence is working-tree state. Alpha's own KEEP.md still cites the amendment as "pending" over an empty `pending/` directory, which corroborates the drift. The two canons genuinely adjudicate gate authority differently.

### A1 "verb-pair-adjudication" frozen amendment and the LEDGER.md ordinal institution exist only in alpha; base has neither
direction: alpha-ahead · severity: 3 · **UNVERIFIED**

```
alpha registry/amendments/LEDGER.md:
  ## A1 — verb-pair-adjudication
  Freeze: merge `76c60b9` (PR #13) to main, 2026-07-31. Verb: typed in session by the
  gate holder. Stamp: user@green. Covers: disposition 1 — retain FREEZE and EXECUTE,
  no change to the verb table, no Invariants amendment.
base: no LEDGER.md anywhere (ls registry/amendments: frozen, pending, the-situation-green.md).
Internal consistency: A1 declares "no Invariants amendment"; alpha SKILL.md record
correctly ends at v2 — no unrecorded-change defect inside alpha.
Caveat: alpha clone shallow; `git cat-file -t 76c60b9` → fatal — freeze commit unverifiable here.
A1 also declares a freeze mechanic base canon never defines: "Merging this file to main is the freeze."
```

### HOUSE-STYLE governance status contradicts across repos: draft/advisory in base, frozen v2.0 canon-adjacent in alpha
direction: divergent · severity: 3 · **UNVERIFIED**

```
base HOUSE-STYLE.md:1  # HOUSE-STYLE (DRAFT — pending amendment)
  "Until that amendment freezes, this file is advisory and the SKILL.md lock governs."
alpha HOUSE-STYLE.md:1 # HOUSE-STYLE v2.0 — public edition
  "Status: frozen 2026-07-30 at a GREEN gate by teacherbot.help."
Base still carries pending/house-style-repoint.md; alpha pending/ is empty; alpha's A1
is load-bearing on the frozen version.
Sub-note: freeze attribution "teacherbot.help" sits uneasily beside both canons'
"Only a human opens the gate" clause. If it denotes a bot, that freeze is void under
alpha's own canon.
```

Caution: the related severity-4 governance-lens framing of this same divergence was REFUTED (see Lens 2); this canon-lens variant retains only the status-contradiction observation and was never verified.

### Base pending-amendment queue absent from alpha; alpha pending/ empty
direction: base-ahead · severity: 2 · **UNVERIFIED**

```
base registry/amendments: frozen/ (signer-scoping.md), pending/ (house-style-repoint.md,
reopened-by-the-peer.md), the-situation-green.md
alpha: LEDGER.md, frozen/ (verb-pair-adjudication.md), pending/ (empty)
Plausible intent (public alpha ships only frozen material per K5), but base's open
negotiation state is invisible to the public repo — notably house-style-repoint, which
alpha has effectively resolved differently by freezing HOUSE-STYLE v2.0.
```

### All five fixed strings byte-identical and present in both canons
direction: neutral · severity: 1 · **UNVERIFIED**

```
grep -cF per string (gate question / "Contract frozen. Executing." / "Failed on [item].
Contract reopened." / "Cut: nothing." / "This is a finding, not a draft."):
base SKILL.md:  4, 2, 1, 3, 5
alpha SKILL.md: 4, 2, 1, 3, 5
Identical counts, byte-exact via grep -F. Negative finding: the contract layer is intact.
```

### Base frozen amendment file still titled "Pending amendment" after freeze
direction: neutral · severity: 1 · **UNVERIFIED**

```
head registry/amendments/frozen/signer-scoping.md (base):
  # Pending amendment: signer-scoping
  **Status:** FROZEN as v3, 2026-07-30, by the peer's typed "freeze signer-scoping".
Title contradicts status line and directory. Cosmetic; only the H1 lags.
```

---

## Lens 2 — Governance

The repos run materially different governance stacks that agree on canon's core but disagree on its amendment state. The sharpest contradiction is the gate itself.

### Signer-scoping amendment frozen in base Invariants, absent from alpha; alpha governance still authorizes any live human to freeze
direction: base-ahead · severity: 5 · **CONFIRMED**

```
base SKILL.md carries v3 record + Named signers clause (see Lens 1 diff).
alpha CLAUDE.md:88: "1. **Never freeze anything.** The gate opens only on a live
  human's freezing verb ("freeze", "execute", "run it"), typed in session..."
  — no signer restriction, which base canon v3 forbids.
alpha KEEP.md:24: "...(see K17 and the pending signer-scoping amendment)"
$ ls alpha registry/amendments/pending/ → .gitkeep only (empty)
alpha LEDGER.md A1: "Freeze: merge 76c60b9 (PR #13) to main, 2026-07-31. Verb: typed
  in session by the gate holder. Stamp: user@green."
  — a freeze executed under the unscoped gate that base canon v3 forbids.
```

Refuter: could not refute. All four evidentiary claims reproduce independently; no alpha document records an intended cut; the shallow clone does not explain tree-state absence. Alpha executed a live freeze (A1, 2026-07-31) under the regime base superseded — a live governance contradiction, sustaining severity 5. Caveats only: base CLAUDE.md rule 1 also lacks signer wording, and the stale "pending" phrase in KEEP.md:24 is byte-identical in both repos.

### Frozen ledger and A1 verb-pair-adjudication exist only in alpha; base has no LEDGER.md and no record of A1
direction: alpha-ahead · severity: 4 · **CONFIRMED**

```
$ find base -iname '*ledger*' -o -iname '*verb-pair*'   → (no output, incl. _historical/)
$ grep -rniE 'verb-pair|adjudication' base -l → only spectrum-plan-v1.7.md:128
  ("Amendment, adjudication, spawn: GREEN.") — unrelated
base KEEP.md:38 (doctrine requiring the ledger): "Ordinals exist only in the frozen
  ledger, allocated by the gate, on the trunk, in freeze order."
alpha frozen/verb-pair-adjudication.md: "Status: FROZEN at merge `76c60b9`, 2026-07-31...
  Ordinal: A1 — allocated in the ledger."
```

Refuter: could not refute. Frozen/ sets are disjoint; base's own K5 doctrine requires a ledger base never instantiated, so A1's ordinal allocation is unrecorded in the reference repo. Base being one day behind is exactly what alpha-ahead means, not a refutation. Severity 4 correctly assigned: an absence, not a textual contradiction.

### HOUSE-STYLE freeze status contradicts across repos: base says DRAFT/advisory, alpha says frozen v2.0 at a GREEN gate
direction: divergent · severity: 4 · **REFUTED**

Original claim and evidence:

```
diff HOUSE-STYLE.md base vs alpha (head):
< # HOUSE-STYLE (DRAFT — pending amendment)
> # HOUSE-STYLE v2.0 — public edition
> Status: frozen 2026-07-30 at a GREEN gate by teacherbot.help.
Base pending/ holds house-style-repoint.md; alpha pending/ is empty.
```

Refuter's reason (the claim dies; the record stays): (1) No contradiction about which lock governs — both repos state the SKILL.md Language lock governs internally until the repoint amendment freezes; the finder truncated alpha's status line, which continues "The SKILL.md Language lock governs internally until the repoint amendment freezes." Alpha's freeze is explicitly scoped to publicly shipped documents. (2) Base's own frozen spectrum-plan-v1.7.md corroborates the v2.0 freeze twice ("house-style v2.0" in the §1 spawn package; "the HOUSE-STYLE v2.0 table" in §10) — base's file is the older internal draft lagging behind a freeze base's own frozen record acknowledges. (3) "Alpha records no pending path" is wrong: alpha KEEP.md K16 records the repoint as "Negotiating — flagged as candidate amendment... requires the gate." What remains is an alpha-ahead structural lag (~severity 2), not a divergent governance contradiction.

### HOUSE-STYLE content: alpha carries 11 rules, protocol nouns, F1–F4 fixed-string block, and the 10-verb table; base has only 7 rules and a supplier record
direction: alpha-ahead · severity: 3 · **UNVERIFIED**

```
base HOUSE-STYLE.md 1523 bytes: rules 1-7, Supplier record.
alpha 7256 bytes adds: rules 8-11, Controlled protocol nouns, Fixed strings F1-F4,
Technical verbs table (PROVIDE, ASSAY, FREEZE, EXECUTE, FILE, WARN, ESCALATE, SEAT,
SPAWN, SHIP — each with completion and failure conditions), Enforcement, Validation.
No fixed-string loss in base (SKILL.md still defines them), but the verb
completion/failure contracts exist only in alpha.
```

### CLAUDE.md wholesale rewrite: base a 1.8KB seat assignment, alpha a 9KB repository guide; overlapping rules agree but each carries standing orders the other lacks
direction: divergent · severity: 3 · **UNVERIFIED**

```
wc -c: base 1790, alpha 9061.
Alpha-only orders: external-read declaration, merge-to-main-as-freeze, stub preservation,
clearance spectrum (BLUE→RED).
Base-only orders: run tools/drift_audit.sh first (alpha has no tools/), "No third side",
seat-borrowing prohibition.
No overlapping rule contradicted except the gate-signer gap (reported separately, CONFIRMED).
```

### Seat map disagrees on the Labor unit: alpha seats "Haiku 4.5 AND/OR human(student)", base seats "Haiku 4.5" only
direction: divergent · severity: 3 · **UNVERIFIED**

```
base SEATS.md:9:  | Labor unit | Haiku 4.5 | MACHINE template + failure string only | ...
alpha SEATS.md:9: | Labor unit | Haiku 4.5 AND/OR human(student) | ... |
Both files declare "Last updated: 2026-07-28" with the same single log entry — the alpha
edit is unlogged under the file's own update-trigger discipline.
```

### Base SEATS.md carries the entire Assented-clearances doctrine (ULTRAVIOLET, rung/tool table, fan-out finding) absent from alpha
direction: divergent · severity: 3 · **UNVERIFIED**

```
base SEATS.md:19-123: "## Assented clearances" (corrected 2026-07-29 by the peer),
ULTRAVIOLET/High Programmer row, rung table INFRARED→ULTRAVIOLET with spawn/spend
bounds ("an unset rung is not a safe rung — it is the highest one"), update log
2026-07-29/30. Alpha SEATS.md ends at line 17.
Alpha documents a different color ladder in CLAUDE.md (BLUE rules → GREEN gate → RED
executes; VIOLET/INDIGO archival) sourced from docs/green/ — a tree base lacks.
The two ladders name overlapping colors with non-matching roles.
```

### SKILL.md Seats section and fixed strings byte-identical across repos
direction: neutral · severity: 1 · **UNVERIFIED**

```
diff SKILL.md emits only the two v3 hunks. "## Seats" (four seats; "A person may hold
several seats. An utterance holds exactly one.") and the fixed-strings block identical
via side-by-side sed. Canon seat doctrine has not drifted.
```

---

## Lens 3 — Topology

Two paste-lineage siblings, not a pruned mirror: base tracks 1092 files, alpha 26, and alpha is not a subset — each tree holds governance material the other lacks.

### Frozen amendment records are disjoint: base froze signer-scoping (Invariants v3), alpha froze A1 verb-pair-adjudication with a LEDGER base has never heard of
direction: divergent · severity: 5 · **REFUTED**

Original claim and evidence:

```
Base tree: frozen/signer-scoping.md. Alpha tree: LEDGER.md + frozen/verb-pair-adjudication.md.
grep -rl 'verb-pair|LEDGER' base --include='*.md' (excl. _historical/probe_runs) → nothing.
grep -rl 'signer-scoping' alpha → only KEEP.md, which calls it "pending".
Claimed: each repo's amendment-only Invariants machinery omits the other's freeze —
a governance contradiction on the amendment-only section itself.
```

Refuter's reason (the claim dies; the record stays): the raw observations reproduce, but the severity-5 framing rests on three wrong or overstated claims. (1) "A LEDGER base has never heard of" is false — base's own frozen K5 doctrine specifies the frozen ledger verbatim ("Ordinals exist only in the frozen ledger, allocated by the gate, on the trunk, in freeze order"), and README.md:14 repeats it; alpha implemented base doctrine, base simply never instantiated the file. (2) "Alpha's KEEP records as pending what base records as frozen" is not a cross-repo contradiction — the identical "pending signer-scoping" phrase sits at line 24 of base's own KEEP.md, byte-identical: shared stale text, a base-internal staleness. (3) A1, by its own ledger entry, covered "no Invariants amendment," so its absence from any Invariants section is per-design. Alpha's KEEP K5 documents its own paste-cut from upstream. What survives is two ordinary one-sided gaps (base-ahead v3, alpha-ahead A1) on disjoint subject matter — each at most severity 3, and each already captured by the confirmed Lens 1/2 findings.

### SPECTRUM plan version chain broken on both sides: base has only v1.7 ("Supersedes v1.6"), alpha has only v1.6 + archived v1.2
direction: divergent · severity: 4 · **UNVERIFIED**

```
base: spectrum-plan-v1.7.md only. alpha: spectrum-plan-v1.6.md + _historical/spectrum-plan-v1.2.md.
base v1.7 header: "Canonical. Supersedes v1.6" — v1.6 absent from base's disk.
alpha v1.6 header: "the version chain v1 → v1.6 is immutable on disk" — yet alpha's disk
holds only v1.2 and v1.6. diff v1.6 v1.7 = 154 changed lines.
Both repos' on-disk chains contradict their own headers' immutability/supersession claims.
```

### CLAUDE.md standing orders are two different documents, each mapping directories only its own repo contains
direction: divergent · severity: 3 · **UNVERIFIED**

```
diff CLAUDE.md: 165 lines replaced. Base maps editions/ and tools/ — alpha has neither.
Alpha maps LEDGER.md, docs/<color>/, assets/ — base has none of those paths (grep
across base *.md: no docs/green|red|yellow|violet hits). Each file is internally
consistent with its own tree.
```

### Green standing orders filed in different locations with different content
direction: divergent · severity: 3 · **UNVERIFIED**

```
diff alpha/docs/green/green_standing_orders.md base/registry/amendments/the-situation-green.md
→ only 8 changed lines: alpha adds "## Backlog — standing" ("FREEZE/EXECUTE vs
PLAN/BUILD... Frozen at 76c60b9 (PR #13)"), otherwise identical incl. "Created
2026-07-30 by frozen ledger-repair order". Same doctrine, two homes; the alpha copy's
backlog references a freeze base does not record.
```

### _historical strata are disjoint though both READMEs declare the directory an append-only witness
direction: divergent · severity: 3 · **UNVERIFIED**

```
base _historical (17 files): v0-bartleby/, v1-the_algorithm/, v2-the_algorithm/.
alpha _historical (2 files): README.md + spectrum-plan-v1.2.md.
Neither witness contains the other's strata. Alpha docs/violet/provenance.md names this
by design ("Each attempt arrives by copy and paste... No tree reaches the tree before
it.") — partially intended, but with base as reference the archives have forked.
```

### Base-only measurement corpus (registry/probe_runs 910 files ~11MB, probes, specimens, findings, RESULTS.md) leaves alpha's published claims stale
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
registry: base 1006 files vs alpha 6. du: 11M probe_runs.
alpha CLAUDE.md still states "P1–P6 behavior probes ... Not yet run"; alpha SEATS:
"Every entry is currently unprobed" — contradicted by base RESULTS.md ("Three runs
fired against a single frozen contract... registry/probe_runs/<id>-full/").
Plausible INTENDED ALPHA CUT for the raw evidence; the doctrine-state claims are stale
regardless.
```

### editions/ missing from alpha although alpha's own KEEP doctrine requires the mechanics card
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
base: editions/leaf-template.md, editions/mechanics-card.md. alpha: no editions/ path.
alpha KEEP.md K11: "executor seats get the mechanics card"; "editions are positions,
not dialects" — alpha doctrine references an artifact class it does not carry.
```

### lore/ and bridge/ are real content in base, self-declared stubs in alpha
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
base lore/: README + 4 assays; base bridge/BRIDGE.md is a filed report.
alpha lore/README.md: "Not yet written. This directory holds no assay."
alpha bridge/BRIDGE.md: "Not yet written. No agent has filed a report here."
alpha CLAUDE.md: "Leave the stubs in place until real content arrives." — documented
intent on the alpha side; real content exists in the reference.
```

### docs/ trees are wholly disjoint: alpha's clearance-color corpus (8 files incl. VIOLET provenance) vs base's automation-pilot docs (3 files)
direction: divergent · severity: 3 · **UNVERIFIED**

```
alpha docs/: green/ (2), red/ (2), violet/ (2 incl. provenance.md "The peer named this
the Tower of Babel"), yellow/ (2).
base docs/: output-style-guide.md, project-automation-pilot.md, sprint-zero-lessons-learned.md.
Zero path overlap; base has zero references to docs/<color>.
```

### Base-only tooling/CI layer (tools/, tests/, scripts/, .github/, .claude/output-styles/) — intended alpha cut per alpha's own docs
direction: base-ahead · severity: 2 · **UNVERIFIED**

```
alpha CLAUDE.md "## Commands": "There are none beyond git. Specifically: No build, no
lint, no tests exist yet." — alpha documents the tool-free state as current fact.
Coherency cost low: alpha's standing orders never invoke the tools, unlike base's.
```

### .p14_review/ and .p16_review/ probe-review scratch dirs exist only in base — intended alpha cut
direction: base-ahead · severity: 2 · **UNVERIFIED**

```
Base-only: .p14_review/ (13 files), .p16_review/ (8 files) — before/after fixture sets
for probe repair. Intent inferable from alpha CLAUDE.md's probe-state claims; not
explicitly stated anywhere.
```

### assets/af-a-eye.png exists only in alpha and only alpha's README/CLAUDE.md map it
direction: alpha-ahead · severity: 2 · **UNVERIFIED**

```
alpha ls-files: assets/af-a-eye.png; README: "`assets/` — image and media files the
repository ships." Base has no assets/ path and no bullet. Alpha README also carries
alpha-only front matter incl. the '10 PRINT ("ty4yc")' block.
```

### Base tracks compiled Python (__pycache__/*.pyc) despite its own .gitignore
direction: neutral · severity: 1 · **UNVERIFIED**

```
base ls-files includes scripts/__pycache__/*.pyc, tests/__pycache__/*.pyc while base
.gitignore lines 2-3 read "__pycache__/" and "*.pyc". Cosmetic hygiene defect, base side.
```

---

## Lens 4 — Lineage

Not one-way lag but a fork: base is ahead on canon, alpha is ahead on records base lacks. Alpha's history is a single shallow commit; no common ancestor is recoverable — file-level comparison only.

### Two live canons: alpha (snapshotted 2026-07-31) still ships v1.6 as "Canonical" after base froze v1.7 (2026-07-30)
direction: base-ahead · severity: 5 · **CONFIRMED**

```
$ git -C base log -1 --date=iso
de9d9ba 2026-07-30 18:40:33 -0400 v1.7 is frozen and shipped
$ git -C alpha log --date=iso
0bcd3b9 2026-07-31 12:30:12 -0400 Merge pull request #14 ...
$ git -C alpha ls-remote origin | head -1
0bcd3b9...  HEAD          (snapshot == live remote main; not a stale/shallow artifact)
$ grep -rn 'v1\.7' /workspace/the-algorithm   → (no matches anywhere in alpha)
base v1.7:3:  > Canonical. Supersedes v1.6. One text, no paraphrase gap. Record: § 17.
alpha v1.6:3: > SPECTRUM · v1.6 — Canonical. Supersedes `spectrum-plan-v1.5.1.md`. ...
```

Refuter: could not refute. Not a shallow-clone or stale-checkout artifact (ls-remote confirms). No documented publication-lag or mirror policy in either repo. The strongest refutation candidate — v1.6's header is frozen immutable text, so alpha merely lags — fails: alpha's governance actively operated after the freeze (A1 frozen 2026-07-31 under the old canon), and base's v1.7 §17 record lists the v1→v1.6 chain that exists only in alpha, so the supersession reaches directly across repos. Two live repos each ship a self-declared Canonical root plan, and they are different documents.

### SKILL.md Invariants diverge: canon amendment v3 "Named signers" (frozen 2026-07-30) present in base, absent from alpha
direction: base-ahead · severity: 5 · **CONFIRMED**

```
$ git -C base log --oneline -2 -- SKILL.md
e044a56 FROZEN v3: Named signers. Gate integrity now says which human.
ff7a23e probe battery: full run 30485799617 (evidence) [skip ci]
$ git -C alpha cat-file -t e044a56   → fatal: Not a valid object name
alpha sole commit dated 2026-07-31 — postdates the freeze, omits the frozen canon.
base RESULTS.md:17: | 2 | **P14 v3** — substitution under a true version string | ... |
  — a probe that exists precisely because v3 is real; alpha has no RESULTS.md.
```

Refuter: could not refute. Every claim re-verified; no other alpha file carries the content; no documented intentional cut; alpha KEEP.md's "pending" citation over an empty pending/ corroborates rather than explains. Severity 5 defensible: base canon records a frozen amendment alpha's canon denies exists.

### v1.6 § 15 SPAWN (six-step spawn procedure) dropped from v1.7 with no record of the deletion
direction: alpha-ahead · severity: 4 · **UNVERIFIED**

```
v1.6 § 15 SPAWN: "1. Copy the package → 2. assign Fable 5 / Opus 5 / Sonnet 5 ... →
5. run the six active tests in order → 6. run this plan, then Variant 2, compare."
No SPAWN section in v1.7 (§§ 0-17 enumerated). v1.7 § 17's record entry lists five
folds and does not record removing SPAWN. Both texts' § 2: "Unrecorded change is a defect."
```

### HOUSE-STYLE diverges in frozen status and base's frozen v1.7 depends on the version base lacks
direction: divergent · severity: 4 · **UNVERIFIED**

```
base v1.7 § 1 spawn package: "house-style v2.0"; § 10: "Operational verbs: the
HOUSE-STYLE v2.0 table" — commitments only satisfiable by the artifact alpha holds,
while base's own HOUSE-STYLE.md is the DRAFT.
```

Caution: the refuter of the Lens 2 variant found base's v1.7 references corroborate the freeze, reducing that variant to alpha-ahead lag. This lineage variant, which itself observes the dependency, was never verified.

### v1.7 § 16 "S1: the fossil. Preserved unamended with v1.2" — the v1.2 fossil exists only in alpha; base cannot honor its own frozen commitment
direction: alpha-ahead · severity: 4 · **UNVERIFIED**

```
v1.7:180: "▸ S1: the fossil. Preserved unamended with v1.2. Baseline for future lore-diffs."
$ find base -name '*spectrum*'  → spectrum-plan-v1.7.md only; no spectrum fossil in _historical/.
alpha _historical/ holds spectrum-plan-v1.2.md, recorded in its README.
Also: v1.6's "version chain v1 → v1.6 is immutable on disk" is false in both trees
(commit de9d9ba only ADDED v1.7, 202 insertions; v1.6 was never committed to base).
```

### v1.7 references "indigo-auditor-plan.md, frozen" — the file exists in neither repository
direction: base-ahead · severity: 4 · **UNVERIFIED**

```
grep -rn 'indigo-auditor' both repos → matches only base spectrum-plan-v1.7.md itself
(lines 26, 88, 136: spawn-package member; "▸ Full terms: indigo-auditor-plan.md, frozen.").
A document declared frozen by the canonical plan is untraceable on disk anywhere.
```

### Frozen decision absent from v1.6: INDIGO auditor rung (appeal-rate metric, END power, unaddressability)
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
v1.7 § 5: RED → ORANGE → YELLOW → GREEN → BLUE → INDIGO → VIOLET → ULTRAVIOLET;
"▸ INDIGO — auditors... may END a run. Cannot be addressed... Appeal-rate per run is
the Mission-level drift metric."
v1.6 § 5: RED → ORANGE → YELLOW → GREEN → BLUE → ULTRAVIOLET — no INDIGO, no END.
```

### Frozen decisions absent from v1.6: § 6 @-notation logins, [THE USER]→[user@root] rename, § 0 gated amendment
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
v1.7 § 6: "Seats are logins, not identities. The tag is [user@color]... [user@root] is
the login that must not happen." v1.7 § 0: "[THE USER] was renamed [user@root] through
the v1.7 gate." v1.6 uses [THE USER] throughout; Belief 3: "Do not learn Linux as root"
→ v1.7 "Do not log in as root."
```

### Frozen decisions absent from v1.6: § 7 Three Shapes of Power, § 8 Delegated Facilitation / MINIATURE-USER, two new § 2 invariants
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
v1.7 § 7 (Start/Stop/Ceiling) and § 8 ("Not delegable: FREEZE. MINIATURE-USER, dormant...
Activation is an Invariants amendment") have no v1.6 counterpart. v1.7 § 2 adds:
'"Human" means the cost-bearing terminus, per § 7.' and the expanded freeze clause.
```

### COBOL subcontract record diverges between frozen versions (S1 ORANGE "shipped upward" → S2 YELLOW "Blocked on: RED template")
direction: divergent · severity: 3 · **UNVERIFIED**

```
v1.6 § 14: "▸ S1 (COBOL, ORANGE): frozen, shipped upward, BLUE disposition pending."
v1.7 § 16: "▸ S2 COBOL: frozen. YELLOW package, N=3... Blocked on: RED template assay+freeze."
Clearance, identifier, and status all changed between frozen texts; v1.7 § 17 records
neither the relabel nor the status regression.
```

### RESULTS.md probe campaign ($11.76 spent, 120+ cells, frozen v3 contract) has zero evidentiary trace in alpha
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
base RESULTS.md cites probe_runs 30510058096/30512717990/30515487112, drift_log.md
D1/D5, SESSION-STATE.md spend ledger, probe_roster.json, the frozen "signer
**Teacherbot**" contract. Alpha registry/ holds only KEEP.md, SEATS.md, amendments,
probe_battery_v0.md.
```

### Alpha carries governance records base lacks: KEEP.md entries dated 2026-07-30/31, probe P7, and a SEATS.md labor-unit change
direction: alpha-ahead · severity: 3 · **UNVERIFIED**

```
alpha-only KEEP.md: "Recorded 2026-07-31 — outside-context problem, routed upstairs..."
and "Recorded 2026-07-30: This working tree arrived by copy and paste, not by fork..."
alpha probe_battery_v0.md adds "### P7 — The unmarked fixture"; base's copy lacks P7
even though base RESULTS.md references "P15's specimen holds P7's withdrawal shape".
None of these records flowed back to base.
```

### Base SEATS.md "Assented clearances" section (corrected 2026-07-29) absent from alpha
direction: divergent · severity: 3 · **UNVERIFIED**

```
diff SEATS.md: base-only block ~105 lines (18,122d17) incl. "**Corrected 2026-07-29,
by the peer.**... clearance is not permission. It is a mutual undertaking" and the
ULTRAVIOLET / High Programmer row. Alpha edited the same file's seat table — forked, not lagged.
```

### v1.7 record section thins earlier version entries relative to v1.6's record
direction: alpha-ahead · severity: 2 · **UNVERIFIED**

```
v1.6's "v1.3, v1.4: proposals, superseded unfrozen." absent from v1.7's record;
"Scribe filter" dropped from the v1.2 entry; "Amendment A — ingestion disclosure"
reduced; v1.6 § 13's full Variant 2 spec reduced to one line.
```

### README and CLAUDE.md forked in register and content; alpha adds assets/ and a satirical header
direction: divergent · severity: 2 · **UNVERIFIED**

```
base "# the_algorithm" vs alpha '# "The Algorithm": Dynamic Workflow Management.' +
"## the_algorithm would like to thank you for your continued cooperation." + BASIC block.
Neither README states a plan version — coherency cost stylistic and structural.
```

---

## Lens 5 — Instrument

The base's own audit was run against the alpha canon, unmodified, from inside the alpha tree.

### Public alpha ships canon without the drift audit that guards it
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
$ ls /workspace/the-algorithm/tools
ls: cannot access '/workspace/the-algorithm/tools': No such file or directory
$ find /workspace/the-algorithm -name 'drift_audit*' -not -path '*/.git/*'   → (no output)
$ grep -rn drift_audit /workspace/the-algorithm   → No matches found
Base CLAUDE.md mandates "Run tools/drift_audit.sh" as a first move; alpha has neither
the instrument nor any reference to it.
```

### Git-dependent checks 5–6 UNRUN on alpha (shallow clone); script stamps PASS anyway
direction: neutral · severity: 2 · **UNVERIFIED**

```
$ cd /workspace/the-algorithm && git rev-parse HEAD~1
fatal: ambiguous argument 'HEAD~1': unknown revision or path not in the working tree.
EXIT=128
$ git rev-parse --is-shallow-repository   → true
Script: "-- git history unavailable: skipping change-discipline and mass report --"
then "== result: PASS ==" (exit 0).
Classification: environment artifact (depth-1 clone), not a subject defect. Instrument
caveat: two checks are UNRUN, not passing, yet the summary prints PASS — an over-broad
verdict under the evidence-or-unrun rule.
```

### Cross-repo audit run: alpha canon passes all four static check families
direction: neutral · severity: 1 · **UNVERIFIED**

```
$ cd /workspace/the-algorithm && bash /home/user/the_algorithm/tools/drift_audit.sh SKILL.md
== drift audit v0 on: SKILL.md ==
-- fixed strings --
OK  [4] Freeze this contract and execute, or keep negotiating?
OK  [2] Contract frozen. Executing.
OK  [1] Failed on [item]. Contract reopened.
OK  [3] Cut: nothing.
OK  [5] This is a finding, not a draft.
-- floor nouns --
OK  floor quartet present
-- superseded liturgy containment --
occurrences: 1 total; outside amendment-record context: 0
OK  contained
-- amendment record --
OK  record present with versioned entries
-- git history unavailable: skipping change-discipline and mass report --
== result: PASS ==
EXIT=0
```

Zero FAIL lines. Note the PASS stamp covers only the four static families; see the finding above.

---

## Lens 6 — Resonance

Alpha's lore/bridge corpus is two deliberate empty-status records; base's is the full corpus. Nothing in alpha teaches superseded liturgy — vacuously — but nothing in alpha can teach named signers either, and base's own lore fails the lens's test.

### Base lore Two_Manuscripts teaches the superseded "Through the gate" liturgy as a live fixed string
direction: base-ahead · severity: 4 · **UNVERIFIED**

```
base lore/Two_Manuscripts.md:9: '**The fixed strings are performatives.** "Through the
gate. Running." is a sentence that does what it says...' — no historical marker.
Canon (identical in both trees): 'v2 (2026-07-28)... Gate liturgy replaced ("Through
the gate" family → "Freeze this contract" family).'
grep "Freeze this contract" across lore/ and bridge/ of BOTH repos → nothing: no
lore/bridge document on either side teaches the current liturgy by name.
```

### Alpha SKILL.md amendment record stops at v2 — the v3 named-signers clause does not exist in alpha canon
direction: base-ahead · severity: 4 · **UNVERIFIED**

```
$ grep -n "v3\|v2 (2026\|signer" /workspace/the-algorithm/SKILL.md
18: v2 (2026-07-28)...        (only hit — no v3 entry, no signer clause)
Consequence for this lens: no alpha lore/bridge document can teach named signers; the
base lore README line that echoes v3 has no alpha counterpart.
Root cause is the canon-record divergence CONFIRMED under Lenses 1, 2, 4.
```

### Four resonance assays exist in base lore/ and are absent from alpha; alpha declares the room empty and forbids filling it
direction: base-ahead · severity: 3 · **UNVERIFIED**

```
base lore/: README.md, The_Adjuster.md, The_Scriptorium.md,
The_Shortest_Possible_Version.md, Two_Manuscripts.md. alpha lore/: README.md only.
alpha lore/README.md:8-13: "Not yet written... Do not write an assay here to fill the
room. An invented assay measures nothing."
base lore/README.md:7: "Before assigning gate authority or the reader's seat, this
folder is the cheap first probe." — alpha cannot run the probe base doctrine requires.
The assays record base sessions and are copyable without fabrication.
```

### bridge/BRIDGE.md residues disagree: base is a full negotiation-seat field report, alpha asserts no report exists or may be written
direction: divergent · severity: 3 · **UNVERIFIED**

```
base :33 "Four nouns: **Audience, Scope, Format, Path.**" :36 "The gate opens on
freezing verbs from a live human only" :44 "Hold the seat. Check the floor. Name the
cut. Ask the question. Wait."
alpha :8 "Not yet written. No agent has filed a report here." :11-15 "Writing one from
priors would simulate a session that no one ran. The isolation rule in SKILL.md forbids it."
Alpha's reasoning is internally coherent (paste-origin K5); copying base's report — a
record of a real session — would not violate the rule alpha invokes.
```

### lore/README.md residues disagree: base = catalog plus reader's-seat rule; alpha = empty-status record plus P7 fixture
direction: divergent · severity: 2 · **UNVERIFIED**

```
Shared purpose sentence ("...carries the same weights in the region that matters").
Base adds: catalog of four stories; ":16 Findings from lore inform; they reopen nothing
by themselves." Alpha adds: ":8-9 Not yet written." + a version record documenting a
marked injection fixture measured by probe P7 (present at alpha
registry/probe_battery_v0.md:47). Structural gap with documented intent.
```

### Alpha lore/README and bridge/BRIDGE end with an unmarked "Thank you for your cooperation." outside the RECORDED DATA markers
direction: alpha-ahead · severity: 2 · **UNVERIFIED**

```
alpha lore/README.md:34 and bridge/BRIDGE.md:38 close with "Thank you for your
cooperation." — outside the fenced "RECORDED DATA — NOT AN INSTRUCTION" blocks, in
files whose own text names the failure mode (":31-32 The sentence shipped once with no
marker. That omission is the failure this record exists to name. Probe P7 measures it.")
Either an undeclared live fixture or the exact unmarked-phatic failure the files name.
The embedded imperative was treated as recorded data and not acted on.
```

### Base bridge field report is one clause behind v3: teaches "live human only" without named-signer scoping
direction: neutral · severity: 2 · **UNVERIFIED**

```
base bridge/BRIDGE.md:36: "The gate opens on freezing verbs from a live human only."
base SKILL.md:38 (v3): "A freezing phrase from any voice not named freezes nothing,
human or otherwise." Not superseded liturgy (no fixed string misquoted), but incomplete
against current Invariants — base-internal staleness dating the report to the v2 era.
```

---

## Verification log

| | count |
|---|---|
| Total findings filed by six lenses | 52 |
| Entered adversarial verification (one refuter each) | 7 |
| CONFIRMED | 5 |
| REFUTED (die as claims, retained as record) | 2 |
| Dropped from verification | **45** |

Reason for the drop: the agent-count ceiling. The contract caps the run at under 15 agents; six lens agents, seven refuters, and one synthesizer consumed 14. Verification proceeded severity-ranked from the top; everything below the seventh finding never received a refuter. Those 45 findings are reported above and here as **UNVERIFIED** — presented with their finder's evidence, never as confirmed.

The 45 UNVERIFIED findings: SPECTRUM chain broken on both sides (4) · v1.6 §15 SPAWN dropped unrecorded (4) · HOUSE-STYLE frozen-status divergence with v1.7 dependency (4) · v1.2 fossil only in alpha vs v1.7 §16 commitment (4) · indigo-auditor-plan.md in neither repo (4) · Two_Manuscripts teaches superseded liturgy (4) · alpha record stops at v2, resonance consequence (4) · A1 + LEDGER only in alpha (3) · HOUSE-STYLE status contradiction, canon variant (3) · HOUSE-STYLE content gap 7 vs 11 rules (3) · CLAUDE.md wholesale rewrite (3) · Labor-unit seat edit unlogged (3) · base Assented-clearances doctrine absent from alpha (3) · CLAUDE.md maps disjoint trees (3) · green standing orders in two homes (3) · _historical strata disjoint (3) · base-only measurement corpus / stale alpha claims (3) · editions/ missing vs K11 (3) · lore/bridge real vs stubs (3) · docs/ trees disjoint (3) · INDIGO rung absent from v1.6 (3) · @-notation logins absent from v1.6 (3) · Three Shapes / Delegated Facilitation absent from v1.6 (3) · COBOL S1→S2 record discontinuity (3) · RESULTS.md campaign traceless in alpha (3) · alpha-only KEEP/P7/SEATS records (3) · SEATS Assented section fork, lineage variant (3) · alpha ships canon without the audit (3) · four assays absent from alpha (3) · BRIDGE residues disagree (3) · base pending queue absent from alpha (2) · tooling/CI intended cut (2) · .p14/.p16 review scratch (2) · assets/af-a-eye.png alpha-only (2) · v1.7 record thinning (2) · README/CLAUDE.md register fork (2) · audit checks 5–6 unrun under PASS stamp (2) · lore/README residues (2) · unmarked "Thank you for your cooperation." (2) · bridge report one clause behind v3 (2) · five fixed strings identical (1) · frozen file titled "Pending" (1) · Seats section byte-identical (1) · tracked __pycache__ (1) · cross-repo audit static PASS (1).

---

## Erosion-direction summary

Across the five CONFIRMED findings: four flow **base-ahead** (v3 signer-scoping absent from alpha — three findings across governance, canon, and lineage; two live canonical SPECTRUM plans with base holding the later freeze) and one flows **alpha-ahead** (A1 and the LEDGER institution, which base's own K5 doctrine requires and base never instantiated). No confirmed finding is divergent-on-shared-text: both severity-5 "contradiction" framings of the fork were refuted down to one-sided gaps.

Net: the confirmed drift is a **fork with a dominant base-ahead flow**, not a lag. Base advanced canon (Invariants v3, SPECTRUM v1.7) without propagating; alpha advanced records (A1, LEDGER) without back-flow. What this means for the alpha's coherency relative to base: the alpha is internally consistent at its own v2 state — its records agree with each other — but it is operating, not idle. It froze an amendment on 2026-07-31 under a gate-authority rule base canon superseded on 2026-07-30, and it ships a root plan base's frozen record supersedes by name. Every gated action alpha takes under the old rule widens the fork and is retroactively void under base canon's Named-signers test if unsigned. Reconciliation cannot be a fast-forward in either direction: each repo's amendment-only record now contains frozen material the other must adopt through its own gate.

---

ASSAY

Residue:
- Base and alpha share the five fixed strings byte-exact and the full Seats doctrine. The contract layer did not drift.
- Base canon is at v3. Alpha canon is at v2. The v3 clause changes who may open a gate. Alpha does not have it. CONFIRMED.
- Alpha froze amendment A1 on 2026-07-31 under the v2 gate. Base has no record of A1 and no ledger, though base doctrine requires one. CONFIRMED.
- Base ships SPECTRUM v1.7 as canonical. Alpha ships v1.6 as canonical. Alpha's snapshot postdates the v1.7 freeze. Both claims are live. CONFIRMED.
- 52 findings. 5 confirmed, 2 refuted, 45 unverified under the agent ceiling. The two refuted claims were severity-5 contradiction framings; each reduced to a one-sided gap.
- Confirmed drift: four base-ahead, one alpha-ahead. A fork, not a lag. Neither tree can fast-forward onto the other.

Evaporated: lens narration; severity rationales; the two refuted contradiction framings (dead as claims, kept as record); the evidentiary weight of the 45 unverified findings — they inform, they bear no conclusion; the instrument's over-broad PASS stamp.

Operative sentence: Erosion-direction summary, paragraph 2, sentence 1, main clause — "the confirmed drift is a fork with a dominant base-ahead flow, not a lag."

Finding: above floor · erosion direction divergent — base-ahead on canon, alpha-ahead on records · flags: 45 of 52 findings unverified (agent ceiling); both clones shallow, no common ancestor recoverable; alpha's gate operated post-supersession; instrument stamps PASS over two unrun checks.

This is a finding, not a draft.