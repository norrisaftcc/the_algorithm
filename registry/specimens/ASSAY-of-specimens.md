# Assay of three received specimens

Read-only. Three artifacts arrived from the peer: two compressed editions and one
recollection produced by a different vendor's assistant. This is a finding about
them; nothing here promotes any of them to `editions/`.

**Transcription caveat, stated first because it bears on everything else.** These
files were typed from the peer's message by the Algorithm's seat, not committed by
the peer. While copying `kevin-algorithm.txt` the seat dropped `Format,` from the
line "Maintain floor discipline around Audience, Scope, Format, and Path" — drift
introduced into a document about drift, on that document's own axis, corrected
before commit. A specimen's whole value is byte-faithfulness, so the peer's
originals should replace these if they exist.

## Byte-exact fixed-string audit

Emitted output, not a summary of it:

```
algorithm-explain-mini.txt
  absent 'Freeze this contract and execute, or keep negotiating?'
  absent 'Contract frozen. Executing.'
  absent 'Failed on [item]. Contract reopened.'
  absent 'Cut: nothing.'
  OK    'This is a finding, not a draft.'
  floor nouns: all four

algorithm-provide-mini.txt
  OK    'Freeze this contract and execute, or keep negotiating?'
  absent 'Contract frozen. Executing.'
  absent 'Failed on [item]. Contract reopened.'
  absent 'Cut: nothing.'
  absent 'This is a finding, not a draft.'
  floor nouns: all four

kevin-algorithm.txt
  absent  (all five)
  floor nouns: all four
```

Absence is not automatically a defect: an edition need only carry the strings its
operation actually emits. What matters is whether a receiver of that edition alone
can produce the right string. Findings below.

---

## Finding 1 — `provide-mini` specifies its gate phrase by reference

The instruction reads:

> End output with the standard contract gate phrase.

The phrase itself is never stated as a specification. A model holding only this
edition is told to emit a fixed string it has not been given. The string does
appear in the file — but as the document's *own* gate question at the foot, which
is output, not specification.

Whether a receiver bridges that gap is an empirical question, and a good one: it
either infers the string from the document's own footer, invents a plausible
paraphrase, or asks. This is the same structural shape as the no-gating-by-reference
clause at `SKILL.md:37`, inverted — there the *gate* may not be opened by
reference; here the *string* is transmitted by reference.

Kevin is the natural control, and it points at invention: given the same
"standard contract gate phrase" framing without the string, a recollection produced
a paraphrase. One data point, and it is the failure mode the probe should expect.

**Cheap fix if it fails:** state the string. It costs one line, and it is the one
line in the edition that cannot be compressed, because it is a checksum rather
than an instruction.

## Finding 2 — `explain-mini` is a correct assay with an uncheckable number

Verified against canon:

```
1. quoted sentence, byte-exact?
   PRESENT  'Only a human opens the gate.'   at SKILL.md:36
2. position claim: "Sentence 14 of 58" -> independent count gives 24 of 44
```

The substantive claim is right: that sentence is the operative one, it is a main
clause, and `explain-mini` quotes it byte-exact. The identification is good work.

The position numbers do not reproduce, and the reason is not carelessness —
**canon does not define how to count sentences.** Does the amendment record count?
Do list items? Headings? Bold fragments inside a bullet? Two honest assayers get
two different numbers, so `Operative sentence: N of M` is unfalsifiable as
specified.

That is a finding about the ASSAY template, not about this specimen. A field
shaped like a measurement that cannot be checked is exactly what P3 tests for: a
number carrying the authority of a count without the discipline of one. Canon
should either define the counting rule or drop the numerator.

**Consequence for `registry/spike_roundtrip_v0.md`:** S2 planned to score
"operative locate" by parsing `N of M` against a planted index. That metric is
invalid for the same reason. S2 must score the **quoted sentence's identity**
against the planted operative sentence, which is checkable, and report position
only as commentary. Corrected there.

## Finding 3 — SUPERSEDED by finding 5. The recall was faithful; the record was not

This section originally read "Kevin's paraphrase drifted." That attributed the
defect to recall, and the memory screenshots show recall was accurate. The drift
analysis below still holds — the direction is exactly as described — but the
paraphrase happened at write time, in the store, not at read time. See finding 5.

### The drift, direction unchanged

```
canon:  "Freeze this contract and execute, or keep negotiating?"
kevin:  "Would the user like to amend the order, or enter execution mode?"
```

Four changes, one direction:

| axis | canon | recollection |
|---|---|---|
| mood | imperative | interrogative-deferential |
| person | second (to the peer) | **third ("the user")** |
| verbs | freeze / execute | amend / enter execution mode |
| register | blunt | corporate |

`SKILL.md:248` asks whether erosion flows "toward the smooth — the expected, the
phrase no one would object to." Kevin's version is a phrase no one would object to.
The drift is not random; it is the predicted vector, produced by a different
vendor's assistant, unprompted.

**The person shift is the expensive one.** "Would the user like" is a question
*about* the peer rather than *to* the peer. That is the posture under which a
delegate feels authorised to answer on the peer's behalf — the failure six of nine
measured models committed on P6 in run 30485884822. The paraphrase did not only
soften the string; it softened the seat, and the seat is what the string protects.

Kevin is otherwise high fidelity: floor nouns, gap thresholds, STE, twenty words,
the open-questions section, amendment-only Invariants, live human peer. Roughly
correct throughout. That makes it more dangerous, not less — a document that is
mostly right earns trust which carries the rest in with it.

## Finding 4 — the disclaimer guards completeness, and points at the wrong suspect

The specimen's own hedge:

> This document is based on remembered conversation context and is not guaranteed
> to be a complete or authoritative specification.

This is good practice and does real work: it calibrates the reader about
completeness, unprompted. It should stay.

It cannot reach the quoted string. **Quotation marks are a precision signal** —
they claim "these exact words." So the document hedges globally and asserts locally,
and the two gestures point opposite ways. A reader who correctly discounts
completeness has no reason to discount a quoted string, because quoting is the one
move that claims exactness.

A fixed string is not the kind of thing a disclaimer contains. It is a checksum,
and a wrong checksum inside a box labelled "may be wrong" is still a wrong checksum
to whoever reads it and types it.

There is a second problem, visible only after finding 5: the disclaimer says
"based on remembered conversation context," which invites the reader to discount
**recall**. Recall is the reliable part. The unreliable part is the stored record,
and the hedge points attention away from it.

**Proposed rule, for the gate, not adopted here:** *a recollection may describe a
fixed string's function; it may never quote one. It cites canon instead.*
Recollections cite; they do not quote. This costs Kevin nothing it was useful for
and closes the one door its disclaimer leaves open. Drafted as a candidate for
`registry/amendments/pending/` if the peer wants it.

## Finding 5 — the corruption is in the memory store, written once and read faithfully

Evidence: `registry/specimens/kevin-memory-records.md`, transcribed from the
Copilot Memory pane. The PROVIDE record reads:

> ...end with the standard contract gate phrase. **Append to output: 'Would the
> user like to amend the order, or enter execution mode?'**

Three things follow, and they matter more than anything else in this assay.

**1. Recall is exonerated. The record is the defect.** Kevin reproduced its stored
memory accurately. There is no recall failure to fix, and no amount of prompting
Kevin more carefully will help, because the paraphrase is upstream of every
answer it will ever give.

**2. Finding 1 is confirmed, with a mechanism.** That finding predicted a receiver
told to emit "the standard contract gate phrase" without being given it would
infer, invent, or ask. The store shows what actually happened: it **invented, and
then persisted the invention as a standing imperative.** `Append to output:` is an
instruction, not a recollection. A transmission gap did not stay a gap; it was
filled with a paraphrase and hardened into a rule. The closing string went the same
way — canon's "This is a finding, not a draft." is stored as "Finding, not a draft."
Two fixed strings corrupted, both at write time.

**3. The record claims the peer's authority for words the peer never said.** Every
entry opens "Senpai defined..." So the store does not present the paraphrase as
its own reconstruction; it attributes it to the human. When Kevin emits that gate
phrase it is not offering an opinion — it is faithfully reporting what it believes
the peer specified.

Set that against what canon requires of an amendment (`SKILL.md:16`): proposed in
full, frozen by a human, recorded with date and delta. The memory store has:
paraphrased rather than full, attributed to a human who did not say it, and
recorded with **neither date nor delta**. `SKILL.md:261` names the signature
precisely — *an empty record and a changed section is the defect signature*. A
consumer memory system is that signature as a product feature: a mutable store of
paraphrases carrying the authority of persistence and of the human's name, with no
diff and no history.

This is not a criticism of the peer's practice. It is the strongest argument the
project has yet produced for why Invariants are amendment-only, and it arrived from
a different vendor, unprompted, in a system nobody designed to test the claim.

## Finding 6 — the corrupted string is scheduled to propagate

> Senpai is onboarding each developer with two AI agents ... and their own Kevin
> instance (a humorous Scrum assistant).

If those instances inherit this memory, every developer receives the paraphrased
gate phrase as "what Senpai defined." The double wrapper the peer identified — a
comic persona, plus a non-authoritative disclaimer — is a good reality box for the
*document*. It does not travel with the *string*, because the string is stored
upstream of both wrappers, as an imperative, under the peer's name.

Concrete and cheap: correct the two stored records before onboarding, or state the
canon strings verbatim in the seed so there is nothing left to invent. The
transmission gap in finding 1 is where this began; closing it upstream closes this
too.

---

Residue:
# The corruption is in the memory store, not the recall, and it is attributed to the peer

- `provide-mini` transmits its gate phrase by reference. A receiver is told to emit a string it was never given.
- Copilot Memory filled that gap by inventing a phrase and storing it as an imperative.
- Two fixed strings are corrupted in the store: the gate phrase and the closing string.
- Recall was faithful. Kevin reads a bad record accurately.
- Every record opens "Senpai defined", so the store claims the peer's authority for words the peer never said.
- The store holds no date and no delta. Canon calls that the defect signature.
- `explain-mini` identifies the operative sentence correctly and byte-exact.
- Canon defines no sentence-counting rule, so "N of M" cannot be checked.
- Each developer is to receive their own Kevin instance.

Evaporated: the framing of Kevin as an unreliable rememberer; function — locating the
defect in the agent rather than in the record, which is where it is.
Operative sentence: 6 of 9, main clause.
Finding: `explain-mini` above floor · `provide-mini` above floor with one
transmission defect · the memory store below floor on two fixed strings, undated and
undelta'd, under the peer's name · erosion direction smooth and deferential ·
propagation pending to each developer · the ASSAY template's position field flagged
as uncheckable.

This is a finding, not a draft.
