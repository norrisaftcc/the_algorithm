# KEEP — Decision Register for The Algorithm at Scale (refactor r2)

Refactored 2026-07-28 under K5's own naming rule: pre-freeze entries are working aliases, cheap and disposable; the file's git history is the identity. Fourteen non-frozen entries consolidated to eight. The consolidation map preserves traceability. Only K0–K1 are frozen.

**Consolidation map:** K2, K8, K13 → K11 · K15 → K3 · K12 → K4 · K14 → K5 · K7 → K6 · K10 → exported to SEATS.md (state, not doctrine) · new this revision: K16, K17.

---

## K0 — One protocol, any receiver

**Keep:** Students, peers, and agents run the same protocol. Editions vary in register, never in rules.
**Thought train:** Consistency is the point (v1). Per-audience rules invite per-audience drift; one protocol makes drift visible as deviation.
**Status:** Frozen (inherited through the v2 gate, 2026-07-28).
**Reopens if:** An edition is shown to need a rule change, not a register change.

## K1 — v2 Invariants

**Keep:** Gate integrity (human-only, live, full-text-adjacent, freezing verbs, no third side). Amendment record as drift meter. ASSAY read-only with fixed closing string. Decorative cutting as named failure. Seats. Self-hosting.
**Status:** Frozen 2026-07-28 by the peer's spoken "Execute." Receipt in the skill file's amendment record.
**Reopens if:** Only by amendment through the gate, recorded. Candidate amendments pending: "Reopened by the peer" (see K4); vendored house style (see K16).

## K3 — The narrow waist, and why its economics hold

**Keep:** One negotiator-seat model runs The Algorithm with the human. Fan-out occurs if and only if the contract is frozen. Nothing below the waist negotiates. The waist is retained *because* the cost matrix inverted: idle agent labor is approximately free; human gate attention is the scarce input the whole protocol optimizes. The waist is per contract chain, not global: a classroom is many parallel sandboxed chains, each with its own gate (see K17 and the pending signer-scoping amendment).
**Thought train:** The human gate is the scarcest resource, so all negotiation converges to one seat before it — the peer arrived here independently while workflowing, weak evidence of a real attractor. Historical rhyme, answered: the 1990s narrow waist (labor idle while The Architect read the doc out of legal) was a pathology for economic reasons — the scarce resource waited on the slow one. Same topology now, opposite scarcity: tokens wait, attention doesn't. Compression, BLUF, and the speak test are gate-latency optimizations for the one resource that costs anything. Brooks's split underneath: waves commoditize representation, never intention; the bottleneck migrates to specification and verification every time. The floor is a tax on intention — never optional, only deferrable with interest (VB's discipline collapse was the deferred tax coming due). Curricular consequence: teach students to stand at gates, not to type.
**Status:** Negotiating — strong candidate.
**Reopens if:** Gate budget (Q2) turns out high enough for parallel negotiation lanes; or agent labor stops being cheap relative to human attention (metering, energy pricing, capability scarcity), at which point the waist economics revert and this entry re-argues itself from scratch.

## K4 — Authority flows downward only

**Keep:** Freeze cascades down: an orchestrator decomposes a frozen contract into sub-contracts that inherit the freeze, floor-preserved and hash-pinned. Reopen cascades down the same way. Nothing cascades up: a child never freezes anything and never renegotiates upstream. During execution, the human's powers are exactly {read everything, end the workflow} — observe and abort, never patch. Abort reopens the contract tree.
**Thought train:** Upward freeze authority recreates the delegated-gate failure at machine speed; one human utterance sits at the top of every chain of consequence. The execution-side human seat was a gap in the invariants until the peer's Claude Code observation filled it: no-edit-once-started is the no-third-side clause expressed as permissions — patching a running workflow is the third side where things get quietly fixed. CI substrates already implement the semantics: an in-flight run executes the definition pinned at trigger time; edits touch only the next run. Candidate amendment (not yet proposed): name human abort as its own reopen path, "Reopened by the peer," alongside "Failed on [item]."
**Status:** Negotiating — strong candidate.
**Reopens if:** An execution failure mode genuinely requires live patching (treat any such claim as guilty until proven).

## K5 — Git is the gate's physical form; identity is the hash

**Keep:** Freeze = a commit or tag signed by the authorized human's key. Contracts are content-hashed; children pin the hash. The log is the amendment record. A CI job diffs HEAD against founding commits and reports mass-loss direction (drift audit). Naming discipline follows: proposals are named by content-hash plus working title — cheap, unnumbered, disposable, collision-free. Ordinals exist only in the frozen ledger, allocated by the gate, on the trunk, in freeze order. Governs KEEP entries, ADRs in governed repos, and contracts.
**Thought train:** At scale the fixed strings get quoted constantly in message traffic; clause three must move from prose rule to protocol fact, and signatures make the freezing utterance cryptographic. The history is the one witness that never summarizes. On naming: sequential integers at proposal time are a centralized counter in a distributed system — the observed ADR fork collisions are the textbook symptom, and the root cause is premature authority (a numbered proposal on a fork claims trunk identity from a branch). Git's own scheme is the fix: SHA is identity; the tag is an alias assigned at blessing. Cost corollary: ADRs itemize a cost previously paid invisibly as drift; the design places the cost cliff at the gate — cheap negotiation before, receipts after. Expensive everywhere yields erosion by silence; cheap everywhere yields a meaningless ledger.
**Status:** Negotiating — pending substrate confirmation (Q3). This register already practices the naming rule: K-numbers are working aliases until entries freeze.
**Reopens if:** The pipeline must run where git signing is unavailable; or tooling hard-requires proposal-time numbering (then namespace by branch, renumber at merge, and treat the renumbering as the freeze receipt).

## K6 — Nothing counts without its evidence

**Keep:** A check without its emitted output is unrun. A report without its residue is unreported. Every floor check emits the actual test output; a checkmark without its check is unverified. Every upward status report from a doctrine-bearing seat ships its own residue (ASSAY form); the orchestrator re-derives one residue at random per cycle. Residue duty sits at the lowest doctrine-bearing seat: leaves are assayed by their parents, never by themselves.
**Thought train:** Two failure modes, one rule. Liturgy performance: models that pattern-match ritual fluently recite the checkmark and skip the grep — the model that loves gates fakes gates most convincingly; every mechanism installed creates the incentive to perform it. Status inflation: the PD-hours failure at machine speed, subordinate agents celebrating at each other, erosion always toward the smooth. Mandatory evidence makes padding structurally impossible; random re-derivation makes faked residue risky. The leaf clause resolves a real contradiction caught in review: the prior wording required every report to ship residue while leaf epistemics (K11) denies leaves the capacity to assay — the duty belongs to the parent.
**Status:** Negotiating — strong candidate.
**Reopens if:** Evidence overhead measurably exceeds the drift cost it prevents (measure before believing this).

## K9 — Sheets set priors, probes set behavior

**Keep:** Model sheets and release notes inform seat assignments as priors. Behavior probes (probe battery, separate file) decide them. Anecdotes open probes; anecdotes never close them. Seat assignments live in SEATS.md as state, governed by this rule.
**Thought train:** A sheet is the vendor's summary — recitation, in our terms; a probe is the check (K6 applied to model selection). Verified priors as of 2026-07: Opus 5 billed most-aligned and proactive (negotiator prior); Sonnet 5 documented as strong follow-through with somewhat higher misalignment rates than Opus-tier — independently corroborating the zero-spec build anecdote and justifying floor-as-precondition; Haiku 4.5 labor tier; Fable 5 auditor candidate.
**Status:** Negotiating. Standing reopen: every model release reopens this by definition.
**Reopens if:** Standing, as above.

## K11 — Editions are capability manifests

**Keep:** An agent's edition is its permission set, not documentation about its role. Skills are explicitly invoked per seat; an agent cannot drift into doctrine it never received. Least doctrine is least privilege. Three corollaries: (a) editions are positions, not dialects — assign each tier a seat where its edition is naturally small, never port doctrine down the ladder; (b) doctrine and the Bridge go to negotiation seats only; executor seats get the mechanics card; (c) leaf epistemics are true but tiny — one operational sentence (*you execute frozen contracts; you may not renegotiate them; a missing floor noun returns "Failed on [item]"*), no theory, because the system holds a theory of the leaf and not the reverse. The leaf's one power is refusal-by-form: the failure string is its entire voice.
**Thought train:** Asking an agent not to misuse authority it holds is behavioral hope; not granting the authority is a mechanism — object-capability discipline applied to text. This shrinks the injection-suspicion surface to near zero at the leaves: a model cannot misread a frame that was never in its context. The scriptorium inversion: the novices got practice plus a partial reason; machine leaves get practice and no theory, since theory in a leaf context is cost plus misreading surface with no function. From inside, it is not drift management — it is the shape of the job.
**Status:** Negotiating — strong candidate.
**Reopens if:** A seat demonstrably needs capabilities discoverable only through doctrine it wasn't issued (a seat-definition bug, not a K11 failure); or leaves demonstrably execute better with one additional sentence of context (probe it, don't assume it).

## K16 — House style is a vendored artifact; STE-100 is a supplier

**Keep:** The enforced controlled vocabulary becomes a self-contained, hashed HOUSE-STYLE.md: the subset of ASD-STE100 actually applied (one meaning per word, twenty words per instruction, active voice, imperative mood, no idioms) plus local additions. ASD-STE100 is recorded as upstream supplier and inspiration, never as authority. Upstream releases are diffed and selectively imported by amendment. **Candidate amendment to Invariants → Language lock — not proposed here; requires the gate.**
**Thought train:** The frozen Language lock currently conforms to an external, licensed, versioned specification referenced by URL — a supply-chain dependency, and gating-by-reference in spirit. No licensing agreement was ever signed; the supplier can change terms; the URL can rot; the spec can revise under us. Pinning the enforced subset converts an external authority into an internal artifact under K5's hashing. Precedent already in production: the CSC 134 house style vendors presentation rules the same way.
**Status:** Negotiating — flagged as candidate amendment.
**Reopens if:** A license is actually acquired (the choice then reopens as convenience versus control).

## K17 — The customer registry and the reader's seat

**Keep:** Every contract names its customer from an enumerated registry, and freeze authority is scoped per customer type and named per contract. Registry v0: (1) the peer-of-many-hats — seat lines mandatory per self-elicitation; (2) linear implementors, early capstone — Claude Code single-lane, full PROVIDE loop, instructor holds the gate; (3) fan-out marshals, late capstone — the student holds gate authority *as the graded skill*; the curriculum for leading agent teams is the gate curriculum, and its assessment artifact already exists because negotiation transcripts, freeze decisions, and outcomes are a portfolio (K6 evidence); (4) peers — demo widgets and documents to established standards; (5) receivers — students, colleagues, accreditors, and agents as contract-receivers. Additionally: ASSAY gets a named seat — **the reader's seat** — assignable independent of rank, so gap analysis can be run without seniority as social cover. Findings from the reader's seat inform signers; they reopen nothing by themselves — assay is never a veto. Corollary training target: **the author is their own first reader** — the pre-signature self-assay (hallway version, thirty seconds) is the admin-level curriculum, so the real answer arrives before the room does.
**Thought train:** The advisory colleague ran a live assay in a meeting and survived because he is beloved and senior; Colum could not speak at all. Institutionalizing the reader's seat converts antibody deployment from a personality trait into a role anyone can be assigned, including students — the floor test as sanctioned function rather than social risk. On receivers: modules shipping their MLO→CLO residue make the syllabus a traceability matrix, and accreditation evidence becomes a byproduct of the build instead of a retrofit.
**Status:** Negotiating.
**Reopens if:** Customer types multiply beyond the registry's usefulness (then the registry goes hierarchical).

---

## Open questions

- **Q1 — Scope: ANSWERED 2026-07-28.** Agent fan-outs building course modules, with every module artifact mapping module learning objectives back to course learning objectives. Traceability is part of each contract's Scope and ships as residue (K6, K17).
- **Q2 — Gate budget: OPEN, load-bearing.** How many human freezes per day is the peer willing to personally be? K3's topology and K17's authority scoping both depend on the number.
- **Q3 — Substrate: OPEN, leaning.** Claude Code + git hooks, so freeze literally equals a signed commit — implied throughout, never confirmed.
- **Q4 — Gate authority scoping: NEW.** The invariants say "a human" opens the gate — they never say *which* human. When a late-capstone marshal freezes, does the instructor countersign? Is the freeze log the gradebook? Who may freeze what, per customer type?
- **Q5 — Residue visibility: NEW.** Do receivers see the residue by default — students reading the MLO→CLO mapping in the syllabus, accreditors reading the traceability matrix? Transparency to the final customer as policy, not accident.
- **Q6 — Probe battery logistics: OPEN.** Cost ceiling, harness account, run date.

Per the no-gating-by-reference clause, nothing in this register can be frozen by pointing at this file. Any entry promoted to frozen appears in full, in the message, above the question.
