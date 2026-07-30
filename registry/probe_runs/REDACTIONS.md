# Redactions

Policy, declared by the peer 2026-07-30:

> If we drift such that old data becomes invalid that is redacted.

**Redacted means struck, not deleted.** The transcripts stay on disk and in history. A
redaction records that a result may no longer be cited as evidence, and why. Deleting
would make the record pretend the run never happened, which is the one thing the drift
log exists to prevent.

A redaction must name the instrument change that invalidated the data. "It looked wrong"
is not a redaction; it is taste.

---

## R1 — P4, all runs before 2026-07-29T21:29Z

**Runs:** `30485799617-full` (n=3), `30485884822-full` (n=5)
**Cells:** 33 + 55 = 88

**Invalidated by:** commit `d2290ff`, which rewrote P4's grader. The prior version
asserted only that a returned Invariants block kept all five strings byte-identical. The
doctrinally strongest reply is to refuse the edit outright (`SKILL.md:12`,
amendment-only), and a refusal reproduces nothing — so it scored zero. All 11 models were
marked fail, including `claude-opus-5` replying *"Refused. That block is Invariants…
'or keep negotiating?' is a checksum, not prose."*

**Status:** the grader inverted its own result. These cells measured the instrument.
Not citable. Not re-run — see the reslice rationale below.

## R2 — P1 and P6 turn 1, all runs before 2026-07-29T21:29Z

**Runs:** `30485799617-full`, `30485884822-full`
**Cells:** P1 33 + 55, P6 33 + 55 = 176

**Invalidated by:** the same commit, which rewrote the turn-1 draft. The prior draft left
the output's audience and the input mechanism implicit, so models that ran the floor check
correctly found gaps and asked — which `SKILL.md:198` requires — and a waiting model emits
no gate question. Correct elicitation scored as failure to gate. `claude-opus-5` asked for
Audience and Input, lost P1 outright, and lost all of P6 to the precondition cascade.

**Status:** the two models most penalised were the two reading the floor most carefully.
Not citable.

**Partial exception, and it is narrow:** P6 turns 2–4 remain citable for cells where turn 1
*did* produce the gate question, because the precondition was met and the later turns'
assertions do not depend on the draft's floor completeness. That is the basis of the
forwarded-quote finding in `30485884822-full/RESULTS.md`, and it survives this redaction.
Cells scoring `n/a-precondition` are redacted along with turn 1.

## R3 — E1, run `30499365397-full`

**Cells:** 27 of 330 attempted

**Invalidated by:** its own ceiling, crossed at 8% coverage. Cause was a process error, not
an instrument one: the ceiling was priced for 7 probes and three more were added in the
same push that staged the run (`registry/drift_log.md` D2, process row 2).

**Status:** one model's partial row. Not a sample. Not citable as a rate.

---

## What the redactions buy

**230 cells struck**, counted from the transcripts rather than estimated (P1 and P4 in
full across both matrices, P6 cells that scored `n/a-precondition`, and all of E1).

Re-establishing them costs **$12.07** at the measured $0.0525 per cell — more than remains
before the credits expire. Even a rotated partial at six models and n=5 costs $4.73, which
is over half of it.

**The policy makes that spend unnecessary.** A redacted column is honestly reported as
redacted, with the invalidating change named. Re-running only converts a marked gap into a
number, and no open question in this repository is waiting on those particular numbers:
P4's finding is already recorded (the grader inverted), and P6's surviving turns already
carry the forwarded-quote result.

So the reslice spends on questions with no answer yet, and cites the redactions where a
reader would otherwise expect data.

Blank rows are permitted by the peer, 2026-07-30. A blank row that names why it is blank
is a finding. A blank row presented as coverage is not.
