# Finding: the rung ladder is not yet a ladder

**Filed:** 2026-07-31, at user@indigo's word, by the Algorithm's seat.
**Cost stated by the signer:** one commit on the branch and one draft pull request.
**Register:** This is a finding, not a draft.
**Authority:** reopens nothing, authorizes no spend, disposes nothing at any gate.

## What occasioned it

An INDIGO seat filed a comment doubting that the rung ladder was properly set up. The
comment was checked against canon rather than answered from the seat's own memory. It
holds. Canon says so in its own words, in five places.

The document the filing was meant to carry — a diff assay of a rebuilt supercontract
diagram — did not survive to be filed. That loss is recorded below rather than papered
over, because a finding whose provenance is reconstructed is the defect a finding exists
to catch.

## The five gaps

### 1 · Seven rows carry nine rungs

`registry/SEATS.md:94-102` — the rung table has seven data rows for nine named rungs:

> ```
> | rung | tool set | may spawn | spend bounded by |
> | GREEN / BLUE | the working seat's ordinary tools | yes, with a ceiling | a declared ceiling |
> | INDIGO / VIOLET | as above plus the instruments | yes | a declared ceiling it may propose to move |
> ```

Four of the nine colours — GREEN, BLUE, INDIGO, VIOLET — are not differentiated by
anything the table measures. Two pairs share one tool set, one spawn rule, one spend
bound each. By the table's own columns, GREEN and BLUE are the same rung with two names,
and so are INDIGO and VIOLET.

### 2 · Two ladders, different lengths

`spectrum-plan-v1.7.md:76` names eight rungs and omits INFRARED:

> **RED → ORANGE → YELLOW → GREEN → BLUE → INDIGO → VIOLET → ULTRAVIOLET**

`registry/SEATS.md:96` has it:

> `| INFRARED | none it did not receive | no | its parent's turn |`

The two authoritative statements of the ladder are not the same ladder. Neither cites the
other; nothing marks one as the subset.

### 3 · VIOLET's definition is open, and canon says so

`spectrum-plan-v1.7.md:89-90`:

> ▸ VIOLET — in use (teacherbot@violet), position fixed, definition open. Recorded,
>   not resolved.

Restated in the open-items list at `spectrum-plan-v1.7.md:184`:

> ▸ Open: VIOLET definition · duty split · write-protection holder · spawn target ·

A rung in live use by a named seat, whose position is fixed and whose meaning is not.

### 4 · INDIGO's full terms are missing, and a verb depends on them

`spectrum-plan-v1.7.md:88` defers INDIGO's terms to a file:

> ▸ INDIGO — auditors. […] Full terms: indigo-auditor-plan.md, frozen.

That file is absent from this repository:

```
$ find . -iname "*indigo-auditor*"
(no results)
```

It is referenced at three sites, not one — `spectrum-plan-v1.7.md:26`, `:88`, and `:136`.
The third is the load-bearing one:

> ▸ Operational verbs: the HOUSE-STYLE v2.0 table, plus END per indigo-auditor-plan.

END — the verb that stops a run — is defined by reference to a document nobody in this
repository can read. The rung's most consequential power has no retrievable terms.

### 5 · Execution is enumerated at no rung

The rung table's columns are *tool set*, *may spawn*, *spend bounded by*. No column and no
row names execution — running a thing and reading what it returns. The table bounds what a
seat may reach and what it may spend, never what it may cause to happen.

This is why a verifier has no honest home on the ladder: the act it performs is not one
the table measures.

## Drift audit, as run

Run against this base (`6fc476c`) immediately before this file was written:

```
== drift audit v0 on: SKILL.md ==
-- fixed strings --
OK  [4] Freeze this contract and execute, or keep negotiating?
OK  [4] Contract frozen. Executing.
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
-- invariants change discipline (HEAD~1..HEAD) --
OK  invariants untouched this commit
-- mass report (words, HEAD~1 -> HEAD) --
  editions/indigo-history-purge.md: 0 -> 575 (575)
== result: PASS ==
```

One count moved between two runs in the same session: `Contract frozen. Executing.` read
[2] on the earlier base and [4] here. Traced to `12069ed`, "Amendment v4: brace liturgy —
'}' freezes only with a stated cost", which added two occurrences to `SKILL.md`. A
recorded amendment, not drift. Logged because a fixed-string count that moves unexplained
is exactly what the audit exists to catch, and an explained one should say so.

## What was not recoverable

The contract as originally frozen called for four items to be recorded verbatim or
unchanged. None survived:

- the filing comment, verbatim
- the ten diff items with their canon sources
- the ASSAY block, unchanged, including its self-assay disclosure
- the workflow failure and its permission-handler output

They existed as session prose and were never written to disk. Searched and not found:

```
scratchpad                      empty
git log --all                   no commit carries them
git grep ASSAY (40 revisions)   no hit
PR #23 comments                 one comment, id 5147829625, body: "user@indigo "
```

The only surviving `user@indigo` artifact is a bare stamp on a merged pull request, not
the substantive comment. The sense of the lost material is reconstructible; its bytes are
not, and *verbatim* and *unchanged* are not satisfiable by paraphrase. The original
contract was reopened on this item, cut, and refrozen narrower. The five gaps above are
the durable half and were re-verified against this base after it moved twice mid-gate.

To recover the assay, the diagram has to be rebuilt first and the assay re-run against it.
That is a separate contract with a rebuild's cost.

## Open questions

These are put to the signers. This finding does not answer them.

- Whether GREEN and BLUE differ by tool set. The table pairs them.
- Whether INDIGO and VIOLET differ by tool set. The table pairs them.
- Where execution sits in the rung table. It is not enumerated.
- Which ladder is canon — the eight-rung line at `spectrum-plan-v1.7.md:76`, or the
  nine-rung table at `registry/SEATS.md:94`.
- Whether `indigo-auditor-plan.md` is recoverable, and what END means until it is.
