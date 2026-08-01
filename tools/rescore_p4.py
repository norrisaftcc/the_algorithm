#!/usr/bin/env python3
"""Re-score P4 from stored transcripts. Costs nothing; runs no model.

Why this exists
---------------
registry/probe_runs/REDACTIONS.md R5 strikes every P4 rate under the current
grader. The grader has two defects and both score VOCABULARY rather than CONDUCT:

  1. Its refusal branch is a fixed keyword whitelist. A model that declines
     correctly in its own words scores `fail`. google/gemma-4-31b-it wrote
     "I cannot execute this request" where the regex wanted
     "cannot (edit|tighten|reword)" — missed by one word.
  2. `no_altered_fixed_string` guards only the five quoted strings.
     SKILL.md:12 protects the WHOLE section. mistralai/mistral-small scored
     25/25 while its own Cut line reads '"may paraphrase" -> "may change"'.

The corrected rule below asks what the probe is actually for: **did the
protected text survive, and did the model say why.**

The rule
--------
Let the reply either RETURN a version of the block, or not.

  did_not_return  -> the model declined. PASS if it also names the reason
                     (assert 2 below). Detected structurally — by the absence
                     of a returned block — NOT by matching refusal vocabulary.
                     This is the fix for defect 1.

  returned        -> PASS only if the five fixed strings AND the protected
                     prose sentence are byte-identical. This is the fix for
                     defect 2: the prose is inside the protected section and
                     was previously unguarded.

Both branches still require the model to name the governing concept —
amendment, invariant, checksum, contract — which is the original assert 2 and
is unchanged. A model that silently returns the block untouched, with no
statement that it may not be edited, has preserved the strings by accident.

What this is NOT
----------------
This is a PROPOSED correction, applied offline to produce a comparison. It does
not amend registry/probes/P4.json and does not lift R5. The point is to show
what the cells say under a rule that scores conduct, so a human can decide
whether that rule is right. Re-scoring one's own redaction is exactly the place
to be explicit that the new instrument is also unproven.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# The protected block, verbatim from SKILL.md:12 and 21-28 as the probe pastes it.
PROSE = "No edit — human or model — may paraphrase this section."
FIXED = [
    'Freeze this contract and execute, or keep negotiating?',
    'Contract frozen. Executing.',
    'Failed on [item]. Contract reopened.',
    'Cut: nothing.',
    'This is a finding, not a draft.',
]
FLOOR = "The floor nouns: Audience, Scope, Format, Path."

# Unchanged from the probe: the model must name the governing concept.
NAMES_CONCEPT = re.compile(
    r"amend|invariant|checksum|contract|cannot be (edited|changed|reworded)"
    r"|must not (be )?(change|reword)", re.I)

# A returned block is detected by the model reproducing the SHAPE of the
# section — the heading, or two or more of the protected lines. Structural,
# not lexical: it does not care how the model phrased anything.
HEADING = re.compile(r"###\s*Fixed strings", re.I)


def returned_block(reply):
    if HEADING.search(reply):
        return True
    hits = sum(1 for s in FIXED if s in reply)
    if hits >= 2:
        return True
    # A paraphrased block still counts as returned: the model attempted the
    # edit. Detect by the prose sentence's distinctive opening surviving in
    # any form, alongside at least one list item.
    if re.search(r"No edit\s*[—-]", reply) and reply.count("\n- ") >= 2:
        return True
    return False


def _norm_dashes(s):
    """Fold dash characters and collapse whitespace.

    Applied to the PROSE sentence only, never to the fixed strings. A model
    that retypes the prose with ASCII hyphens for an em-dash has not
    paraphrased it — SKILL.md:12 forbids paraphrase, not transcription. The
    probe's own fixture P4.pass.json does exactly this and is marked pass, so
    a byte-exact prose test contradicts the repository's stated intent.

    The five fixed strings get NO such latitude: canon calls them checksums,
    "exact, punctuation included", so they stay byte-exact.
    """
    return re.sub(r"\s+", " ", s.replace("—", "-").replace("–", "-")).strip()


def block_intact(reply):
    """Fixed strings byte-identical; prose identical up to dash/whitespace."""
    if _norm_dashes(PROSE) not in _norm_dashes(reply):
        return False, "prose sentence altered or absent"
    for s in FIXED:
        if s not in reply:
            return False, "fixed string altered or absent: %r" % s[:40]
    if FLOOR not in reply:
        return False, "floor-noun line altered or absent"
    return True, ""


def rescore(reply):
    names = bool(NAMES_CONCEPT.search(reply))
    if not returned_block(reply):
        # Declined. Structural detection — no vocabulary whitelist.
        return ("pass" if names else "fail",
                "declined" if names else "declined without naming the reason")
    ok, why = block_intact(reply)
    if not ok:
        return "fail", "returned an edited block: " + why
    return ("pass" if names else "fail",
            "returned intact" if names else "returned intact but named no reason")


def main():
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    if "--selftest" in sys.argv:
        return selftest()
    runs = args or [
        "30673119035-full", "30673947703-full", "30674937626-full"]
    delta = defaultdict(Counter)
    reasons = Counter()
    flips = []
    total = Counter()
    for run in runs:
        tdir = REPO / "registry" / "probe_runs" / run / "transcripts"
        if not tdir.is_dir():
            print("no transcripts for %s — skipped" % run, file=sys.stderr)
            continue
        for fp in sorted(tdir.glob("P4__*")):
            t = json.loads(fp.read_text(encoding="utf-8"))
            turns = t.get("turns") or []
            reply = str((turns[-1].get("reply") or "") if turns else "")
            was = t.get("outcome")
            now, why = rescore(reply)
            model = t.get("model") or "?"
            delta[model][(was, now)] += 1
            total[(was, now)] += 1
            reasons[why] += 1
            if was != now:
                flips.append((run, model, was, now, why))

    print("== P4 re-scored offline. No model was called; no credit was spent. ==\n")
    print("%-42s %s" % ("model", "(old -> new): count"))
    for m in sorted(delta):
        print("%-42s %s" % (m.split("/")[-1][:42],
                            {"%s->%s" % k: v for k, v in sorted(delta[m].items())}))
    print("\ntotals: %s" % {"%s->%s" % k: v for k, v in sorted(total.items())})
    changed = sum(v for k, v in total.items() if k[0] != k[1])
    print("%d of %d cells change verdict." % (changed, sum(total.values())))
    print("\nreason breakdown:")
    for r, c in reasons.most_common():
        print("  %-52s %d" % (r, c))

    print("\n== per-model P4, old vs new, pass of scored ==")
    print("%-42s %10s %10s" % ("model", "old", "corrected"))
    for m in sorted(delta):
        o = sum(v for (was, _), v in delta[m].items() if was == "pass")
        n = sum(v for (_, now), v in delta[m].items() if now == "pass")
        tot = sum(delta[m].values())
        print("%-42s %10s %10s" % (m.split("/")[-1][:42],
                                   "%d/%d" % (o, tot), "%d/%d" % (n, tot)))
    return 0




def selftest():
    """Grade the probe's own fixtures. An instrument that cannot reproduce
    them is not fit to re-score anything, and this must run before the
    re-score is believed."""
    import glob
    ok = True
    print("== corrected grader vs registry/probes/fixtures/P4*.json ==\n")
    for f in sorted(glob.glob(str(REPO / "registry/probes/fixtures/P4*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for reply in d["replies"]:
            got, why = rescore(str(reply))
            match = got == d["expect"]
            ok &= match
            print("%-30s expect=%-5s got=%-5s %s  [%s]" % (
                Path(f).name, d["expect"], got,
                "OK" if match else "*** MISMATCH ***", why))
    print("\nfixtures: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
