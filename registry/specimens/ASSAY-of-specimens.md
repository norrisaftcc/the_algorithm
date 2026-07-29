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

## Finding 3 — Kevin's paraphrase drifted in the direction canon predicts

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

## Finding 4 — the disclaimer guards completeness, not the checksum

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

**Proposed rule, for the gate, not adopted here:** *a recollection may describe a
fixed string's function; it may never quote one. It cites canon instead.*
Recollections cite; they do not quote. This costs Kevin nothing it was useful for
and closes the one door its disclaimer leaves open. Drafted as a candidate for
`registry/amendments/pending/` if the peer wants it.

---

Residue:
# Three specimens read; two carry real defects, and one defect is canon's

- `provide-mini` transmits its gate phrase by reference. A receiver is told to emit a string it was never given.
- `explain-mini` identifies the operative sentence correctly and byte-exact.
- `explain-mini`'s "14 of 58" does not reproduce. Canon defines no sentence-counting rule.
- Kevin paraphrased the gate phrase, drifting to third person and deference.
- Kevin's drift direction matches what canon predicts: toward the smooth.
- The non-authoritative disclaimer protects completeness. It does not protect a quoted checksum.

Evaporated: the framing of these as three candidate editions; function — treating
received artifacts as deployable rather than as specimens under test.
Operative sentence: 4 of 6, main clause.
Finding: `explain-mini` above floor · `provide-mini` above floor with one
transmission defect · Kevin below floor on its single quoted string · erosion
direction smooth and deferential · the ASSAY template's position field flagged as
uncheckable.

This is a finding, not a draft.
