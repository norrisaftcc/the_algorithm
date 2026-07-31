# Finding — the same report at every clearance, and why students would work it out

Recorded 2026-07-31 by the Algorithm's seat. **Not a contract.** No freezing verb was
spoken and nothing here is staged; this is the reader's seat writing down a direction so it
is not lost.

The peer, customer seat at BLUE:

> we should have some of these reports in every clearance level, eventually, and then the
> students will eventually figure out why we needed them

## The pair built tonight is already an accidental instance

Two artifacts were filed within an hour of each other, and they differ almost exactly the
way the idea describes:

| | `lore/big-board.html` | `lore/assay-orange.html` |
|---|---|---|
| shows | every cell, every model, every run | four verdicts and their reasons |
| redactions | hatched *in place*, still countable | named in prose, not countable |
| unrun cells | 83 of 224, visibly hollow | absent — nothing to be hollow |
| what a reader can do | **re-derive the conclusion** | **read the conclusion** |
| rung it behaves like | ULTRAVIOLET | ORANGE |

Neither was designed as a clearance edition. They came out that way because the *operation*
differed — a board is a matrix, an assay is read-only by doctrine — and the operations are
already rung-shaped. That is evidence the idea has a real spine and is not a theme.

## The distinction that makes it teach, and the failure mode that makes it decorative

`SKILL.md` K11 governs editions: **never port doctrine down.** An edition is a capability
manifest, not a summary. Applied to reports, that draws a hard line:

- **A report that withholds *volume* teaches nothing.** Same conclusions, fewer words, is
  just an abstract. A student reading the short one is not missing a capability; they are
  missing paragraphs, and they will correctly conclude the levels are ceremony.
- **A report that withholds *the ability to re-derive* teaches the whole thing.** The ORANGE
  sheet says "six of eighteen probes flip." The board lets you count them yourself and find
  which six. A student holding only the first cannot check the second, and **that** is the
  moment the rung becomes legible — not because they were told, but because they reached for
  a number that was not there.

The `SEATS.md` two-mechanism table already names this: object-capability binds because the
doctrine is never issued; discipline binds because both parties hold a line. **A report
edition is object-capability applied to evidence.** The lower rung does not promise not to
re-derive. It cannot.

## Why the students work it out rather than being told

`SEATS.md` records the exit ticket as "evidence that the constraint can be held," and the
peer's own framing was "as you take on increasing complexity" — taken on, not received. The
same shape applies here, and it inverts the usual order of teaching:

A student handed the ULTRAVIOLET board first learns that clearance means *more*. A student
handed the ORANGE sheet first, who then needs a number it does not carry, learns that
clearance means *responsibility for a claim you can check*. The second is the lesson. It
arrives only if the lower rung is genuinely useful on its own — a frustrating stub teaches
resentment, not structure.

So the sequencing matters more than the rendering: **every edition must be complete for its
own purpose, and incomplete only for the purpose one rung up.**

## What this would cost, honestly

The two artifacts here were hand-built. Seven rungs × every report is not hand-buildable and
should not be attempted that way. The tractable shape is one dataset and a per-rung
projection — the board already reads a generated `board.json`, so the data layer exists and
the rung is a filter over it. That is a real build, not an afternoon, and it wants its own
contract at the gate with its own floor.

## Open questions, for the customer

- Which rungs actually get an edition? Seven is the ladder; three or four may be the lesson.
- Does a redaction stay visible at every rung? Hiding the *existence* of a struck cell is a
  different act from hiding its contents, and only one of them is honest.
- Does a student ever hold two rungs at once, or is the discovery ruined by seeing the diff
  directly? The finding above assumes they meet the rungs in sequence, and that assumption is
  untested.

## ASSAY

**Survives:** the utterance, recorded verbatim; the observation that tonight's two artifacts
already differ along a capability axis rather than a volume axis, with the table above read
off the filed files.

**Does not survive:** nothing yet — nothing has been claimed.

**Not established:** that students do work it out; that a rung-projected report is buildable
at reasonable cost; that the sequence assumption holds. All three are untested.

**Reopened by this:** whether `editions/` should hold report editions alongside the seat
editions it holds now. That touches K11 and would be proposed at the gate in full.

This is a finding, not a draft.
