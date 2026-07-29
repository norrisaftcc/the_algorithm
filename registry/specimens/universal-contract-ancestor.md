# Specimen: the Universal EXPLAIN/PROVIDE Contract (earliest recovered ancestor)

Received from the peer, 2026-07-29, described as "back as far as I could" go. This
is the earliest artifact in the chain and it resolves where the drift entered.

Read-only specimen. Full text is in `universal-contract-ancestor.txt`.

## It corrects two of my earlier findings

`ASSAY-of-specimens.md` finding 5 claimed the corrupted gate phrase was written into
Copilot Memory — that recall was faithful and the store was not. That was already a
correction of finding 3, which had blamed recall. Both were wrong, in the same
direction: too far downstream.

This document already contains:

> Would the user like to amend the order, or enter execution mode?

and:

```
# §4 Execution Gate
For every request:
1. Check §A Invariants.
2. Determine skill.
3. Execute EXPLAIN or PROVIDE.
4. Produce output.
5. Preserve invariants.
```

So the memory store copied this accurately, `kevin-algorithm.txt` copied the store
accurately, and Kevin's diagrams are a correct rendering of §4. **There was one
mutation event, early, and every layer after it transmitted faithfully.**

That is the finding, and it is a better one than either of the versions it replaces:
the copying fidelity across three systems and two vendors was high. A single
unrecorded authoring change propagated perfectly, which is precisely what
`SKILL.md:261` describes — *an empty record and a changed section is the defect
signature*. There was no amendment record anywhere in the chain.

## The mechanism: substitution under preserved vocabulary

Not compression, and not primarily paraphrase. Two words survived while the objects
behind them were exchanged.

### `Path`

Canon (`SKILL.md:179`): *the exact path of each file produced* — a floor noun about
where output lands. This document:

```
Path
Request → Skill Match → Invariant Check → Execute
```

That is control flow. The floor noun list is intact and correctly ordered — Audience,
Scope, Format, Path, all present in §C — and one member now denotes something else.

### `Gate`

Canon (`SKILL.md:32-39`): a commitment boundary with two sides, which only a human
opens, and through which a contract can be sent back. §4: a five-step dispatch
checklist the system runs on itself, with no human in it and no reverse step.

### Why this is worse than the paraphrase

Canon's defence is checksums on strings. **A checksum cannot detect a changed
referent.** This document passes a byte-exact fixed-string audit on the floor nouns
and would pass `tools/drift_audit.sh` unchanged, because its vocabulary is correct.
The failure sits underneath the layer canon inspects.

The paraphrased gate phrase is the *visible* half of the same event and the only half
any current instrument can catch. The `Path` substitution is invisible to all of them.

## §A protects itself and nothing else

Seven of §A's eight bullets govern §A: invariants cannot be summarised, cannot be
paraphrased, change only by amendment, amendments shown as diffs, exact text when
discussed, no rewritten versions, wording preserved exactly.

Gate integrity is absent in full — no clause about who may freeze, no gating by
reference, no completion assist, no failure-reopens. The section became very good at
protecting its own wording and stopped protecting the workflow.

The eighth bullet — "This algorithm has two skills: EXPLAIN, PROVIDE" — makes the
skill inventory unamendable. The invariants have begun protecting the product
catalogue.

## The direction: from discipline to product

Canon is a discipline in which a human bears a cost. This is a service with a
capability menu. Everything else follows from that single substitution:

| this document | canon |
|---|---|
| §3 want-lists routing to a skill | a floor check on four nouns |
| §5 "Offer both options" | ask about the missing floor items and wait |
| §4 gate executes | only a human opens the gate |
| "Would the user like to..." | "Freeze this contract and execute..." |

And downstream: Kevin's router diagrams, and a CS101 tutor variant with no floor
check at all. Not four drifts — one, rendered faithfully four times.

## What it does better than canon

Recorded because it is true and because the peer should not lose it.

**§A: "When discussing invariants, show exact invariant text."** Canon forbids
paraphrasing Invariants. It does not require that a *citation* be verbatim. This is
an operational rule canon lacks — and it is materially the rule proposed as
`recollections-cite.md` in `ASSAY-of-specimens.md` finding 4. The peer had already
written it; the assay re-derived it from the failure it was meant to prevent.

**§B and §C: per-operation invariant clauses.** Each operation states that it does
not modify, summarise or paraphrase invariants. Canon has no per-operation invariant
precondition — the same gap Kevin's third diagram identified, present here in better
form because it does not displace the human gate to get it.

**The document obeys PROVIDE's own template.** Audience, Scope, Format and Path are
stated up front, an Open Questions section is present, and it closes with a gate
phrase. Structurally it is doing the thing it describes. "Open Questions: None." is
the one place that reads thin.

---

Residue:
# One unrecorded change entered early and every later layer copied it faithfully

- The corrupted gate phrase and the router gate are both present in the earliest artifact.
- Copilot Memory, the recollection, and the diagrams all transmitted accurately.
- Two words kept their spelling and changed their referent: Path and gate.
- Path denotes control flow here, not an output location.
- A fixed-string audit cannot detect a changed referent, so no current instrument catches this.
- §A's clauses protect §A; gate integrity is absent entirely.
- The skill inventory is listed as an invariant.
- §A already contains the citation rule the specimen assay later proposed.

Evaporated: the framing of the drift as a sequence of degradations; function —
distributing blame across the chain, when the chain was faithful and the mutation was
singular.
Operative sentence: 5 of 8, main clause.
Finding: below floor on gate integrity · drift type is substitution under preserved
vocabulary, invisible to checksum instruments · one mutation, four faithful renderings
· two clauses here are stronger than canon and should be imported by amendment.

This is a finding, not a draft.
