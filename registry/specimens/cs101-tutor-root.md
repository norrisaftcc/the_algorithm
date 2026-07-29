# Specimen: CS101 Python Tutor contract — the root

Received from the peer, 2026-07-29, described as the oldest. This supersedes the
provenance account in `universal-contract-ancestor.md` and overturns the reading in
`ASSAY-of-specimens.md` and `kevin-architecture.md`.

Read-only specimen. Full text in `cs101-tutor-root.txt`.

## What changes: this is not a drifted copy of canon

Three assays have now placed the defect progressively further upstream — recall,
then the memory store, then the Universal Contract. All three shared an assumption
that the chain was a degradation of `SKILL.md`. This document breaks that assumption.

It is a **tutoring contract**, with a domain, a threat model, and a payload:

```
§6 Allowed Capabilities          §7 Forbidden Capabilities
Explain concepts                 Complete assignments
Explain errors                   Produce graded solutions
Generate pseudocode              Produce take-home exam answers
Generate Mermaid diagrams        Produce final project implementations
Provide hints                    Write code intended for direct submission
Review student-submitted work
```

§8's gate enforces §7. For that job it is **correct**: checking whether a request is
permitted before acting is the right architecture when the asset being protected is
a student's own learning. This is not a corrupted commitment gate. It is a different
gate, well built for a different purpose.

## The failure was promotion, not construction

The Universal EXPLAIN/PROVIDE Contract kept §8's shape and **dropped §6 and §7.** It
carries no allowed-capability list and no forbidden-capability list. It therefore
inherited a capability gate with no capabilities to gate — which is why it reads as a
router. The mechanism outlived its purpose.

The same happened to §9. Refusal behaviour here — offer pseudocode, a diagram, a
hint, a review — is sound pedagogy: you redirect a student rather than only refusing.
Generalised out of teaching, "offer nearest allowed capability" becomes the Universal
Contract's §5 "Offer both options," and pedagogy becomes a product affordance.

**So the drift type named in the previous assay is wrong.** "Substitution under
preserved vocabulary" describes the mechanism visible at the string level. The cause
is **decontextualization**: each element was correct in its domain and became wrong
when lifted out of it. Nothing degraded; something was promoted past its warrant.

## `Path` is canon's defect, not the author's

```
Path
Request / Capability Match / Invariant Check / Execute or Refuse
```

A tutor produces no files. `SKILL.md:179` states Path is "automatic if no file is
produced" — but the PROVIDE template supplies a Path slot with no way to express
"automatic". A required field with nothing legitimate to put in it gets filled.

That is the mechanism `bridge/BRIDGE.md` names for the `Cut:` line: *when a required
line is mandatory every pass, you will feel pressure to have something to report.*
The pressure applies to Path identically, and canon did not notice.
`editions/leaf-template.md:12` did notice, and solved it:

```
- Path: [exact output path, or "no file"]
```

The leaf edition carries the affordance; canon's own template does not. Candidate
amendment: give the PROVIDE template the same escape the leaf template already has.

## The open question that decides the earlier findings

Is this document's gate phrase original, or paraphrased from canon?

> Would the user like to amend the order, or enter execution mode?

- **If it predates the peer's exposure to canon's gate phrase**, there was no
  paraphrase event. It is an independently authored gate phrase for a capability
  gate, and a reasonable one for that job. The "drift toward the smooth" reading in
  `ASSAY-of-specimens.md` finding 3 would then be wrong — parallel invention read as
  corruption.
- **If it postdates canon**, the earlier reading holds.

Unresolvable from the artifacts. Recorded as open rather than assumed, because it
determines whether a paraphrase event exists anywhere in this chain.

What survives either way: the Universal Contract dropped §6 and §7 while keeping §8,
and every later artifact rendered that faithfully.

## Stronger than canon, and to be imported rather than lost

Three, now confirmed present at the root:

1. **§A: "When discussing invariants, show exact invariant text."** Canon forbids
   paraphrasing Invariants; it never requires a citation be verbatim. This is
   materially the `recollections-cite` rule proposed in `ASSAY-of-specimens.md`.
2. **§B and §C: per-operation invariant clauses.** Each operation declares that it
   does not modify, summarise or paraphrase invariants. Canon has no per-operation
   invariant precondition — the gap Kevin's third diagram identified, solved here
   without displacing a human gate.
3. **§6/§7: an explicit forbidden-capability list.** Canon has no equivalent. Its
   nearest relative is the floor as a binary precondition in
   `editions/mechanics-card.md:9`, which governs sufficiency rather than permission.

---

Residue:
# The root is a sound tutoring contract; the failure was generalising it

- §6 and §7 are a real academic-integrity design with a threat model.
- §8's capability gate correctly enforces §7. It is not canon's commitment gate.
- The Universal Contract kept §8 and dropped §6 and §7.
- A capability gate with no capability list is a router. The mechanism outlived its purpose.
- §9's pedagogy became a product menu when lifted out of teaching.
- The drift type is decontextualization, not degradation.
- Path was filled because canon's template offers no way to write "no file".
- Whether the gate phrase is original or paraphrased is unresolved and decides earlier findings.

Evaporated: the account of a single mutation propagating down a chain; function —
locating a defect in transmission when the defect was in promotion.
Operative sentence: 4 of 8, main clause.
Finding: above floor for its stated audience and scope · below floor only when read as
general doctrine, which it does not claim to be · three clauses stronger than canon ·
one canon defect exposed in the PROVIDE template's Path slot.

This is a finding, not a draft.
