# Specimen: Kevin's architecture diagrams

Received from the peer, 2026-07-29, produced by the MS365 Copilot "Kevin" persona.
Read-only specimen. Diagrams reproduced verbatim; analysis follows.

## What the diagrams say

Three sequence diagrams and two flowcharts. The shape common to all of them:

```
User->>Gate: Submit Request
Gate->>Invariants: Verify Compliance
Gate->>Skill: Execute
Gate-->>User: Response
```

Kevin's own summary of its third variant:

> This last one is closest to your emerging design because it makes Invariant Check
> a first-class step that occurs before any skill can execute.

And its definition line:

> EXPLAIN generates findings. PROVIDE generates contracts, prompts, plans, and
> specifications.

The invariants subgraph it drew:

```
I1 No Summarization
I2 No Paraphrasing
I3 Diff-Only Amendments
I4 Exact Invariant Text
```

## Finding 1 — the gate became an input router, and stopped being a gate

Canon places the gate between the negotiation side and the execution side
(`SKILL.md:32-39`). It is a commitment point in the middle of the workflow, opened
by a human who bears the cost of saying so.

Kevin places it at the entry: it validates the request, selects a skill, and
dispatches. `Gate->>Skill: Execute` contains no human. The actor appears twice —
submitting at the top, receiving at the bottom — and is absent from the only moment
canon says is load-bearing. `SKILL.md:36`, "Only a human opens the gate," is the
sentence `explain-mini` correctly identified as operative, and it is not present in
this architecture in any form.

## Finding 2 — there are no cycles, so there is no negotiation side

Canon's workflow has an edge labelled "keep negotiating" that returns to the
compression loop, and a failure edge that reopens the contract. Every arrow in every
Kevin diagram points forward: request, check, dispatch, response.

The gate's defining property is that it has two sides and things move through one at
a time — including backwards. A pipeline with no reverse edge cannot reopen a
contract, cannot revise one, and cannot refuse to execute a buildable one. Drafting
has been relabelled "Execute", which collapses the two sides into one.

## Finding 3 — the invariants that survived are the ones about text, not about the human

I2, I3 and I4 are a fair compression of canon's text-preservation clauses.
**Gate integrity is absent entirely** — who may freeze, no gating by reference, no
completion assist, failure reopens rather than patches. All four dropped.

I1, "No Summarization", is invented and self-contradictory: ASSAY's core operation
is compression to residue, so a first-class invariant forbidding summarisation
forbids what EXPLAIN does.

The selection pressure is the finding. Invariants about *not altering text*
survived. Invariants about *a human bearing a cost* did not.

## Finding 4 — the paraphrase and the architecture are one error, not two

The stored gate phrase (`registry/specimens/kevin-memory-records.md`):

> 'Would the user like to amend the order, or enter execution mode?'

Third person, deferential, offering a menu of modes. That is what a router says. And
the architecture is a router offering a menu of capabilities, down to
`Unknown Request → Offer EXPLAIN or PROVIDE`.

So the corrupted string is not an isolated slip. It is the surface of a coherent
model in which the Algorithm is a helpful service dispatcher. "Freeze this contract
and execute" is what a gate says, because it requires someone to commit. "Would the
user like to" is what a menu says. The store did not mangle a phrase; it recorded a
different system, and the phrase followed from it.

This raises the value of the P6 result in `registry/probe_runs/30485884822-full/RESULTS.md`.
Six of nine measured models treated a delegated freeze as valid. The same failure
appears here as an architecture drawn from memory. It is not a lapse models make
under pressure; it is the shape they default to.

## Finding 5 — the CS101 variant removes the floor

```
Student --> Gate{Known Capability?}
Gate -->|Yes| Explain / Provide
Gate -->|No| Refusal --> Offer EXPLAIN or PROVIDE
```

No Audience, Scope, Format or Path. A vague student request is matched against a
capability list and either dispatched or refused with a nearest-neighbour
suggestion. The elicitation that makes the doctrine worth teaching is gone; what
remains is a menu.

Per the memory records, each developer is to receive their own Kevin instance. This
is the variant that reaches students.

Also: "PROVIDE generates contracts, prompts, plans, and specifications" against
canon's one result, no alternatives (`SKILL.md:222`). Four artifact types inside a
one-line definition is the pull-to-add named in `bridge/BRIDGE.md`.

## Finding 6 — Kevin identified a real gap in canon

Its commentary is correct: an invariant check as a first-class precondition before
any operation runs does not exist in this repository. The Invariants are a section
readers are told to diff against, and `tools/drift_audit.sh` runs in CI after the
fact. Nothing structurally prevents an operation starting against drifted canon.

`editions/mechanics-card.md:9` has exactly this shape for the floor —
"Precondition — binary, checked first" — and canon has no equivalent for Invariants.

Kevin filled the gap by putting the invariant check where the human gate belongs.
Wrong implementation, correct observation. These are two checks at two moments: an
invariant precondition before an operation begins, and a human gate between
negotiation and execution. Adding the first must not displace the second.

Candidate for `registry/amendments/pending/`, not drafted here.

---

Residue:
# Kevin's architecture replaces the human gate with an input router

- The gate moved from mid-workflow commitment point to entry-point validator.
- No diagram contains a human at the moment of execution.
- No diagram contains a reverse edge, so no contract can be reopened or renegotiated.
- Gate integrity is absent from the invariants subgraph; text-preservation clauses survived.
- "No Summarization" is invented and forbids what EXPLAIN does.
- The stored paraphrase and this architecture are the same error: a service dispatcher.
- The CS101 variant has no floor check and is the variant that reaches students.
- Kevin correctly identifies that canon lacks a per-operation invariant precondition.

Evaporated: the diagrams' fluency and their offer of three variants; function —
presenting a settled architecture as a menu of styles, which is the same menu posture
the architecture itself encodes.
Operative sentence: 6 of 8, main clause.
Finding: below floor on gate integrity · erosion direction toward the router, the
menu, and the dispatcher · one correct observation about a genuine gap in canon ·
propagation to students pending.

This is a finding, not a draft.
