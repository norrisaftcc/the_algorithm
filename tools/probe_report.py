#!/usr/bin/env python3
"""probe_report.py — turn a battery run into tables.

Reads a results.json written by tools/probe_runner.py and emits the matrix, the
four roll-ups, the failure ledger, and run health. Data only.

This tool does not write the Finding line, and must not. A residue block emitted
by a script is recitation — the exact failure P3 probes for. The tool emits the
counts; the seat reads them and writes the finding. See K6 and CLAUDE.md rule 4.

Stdlib only.
"""

import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict

OUTCOMES = ["pass", "fail", "error", "truncated", "n/a-precondition"]
UNRUN = {"error", "truncated", "n/a-precondition"}

# Which probes speak to which roll-up. A probe can serve more than one.
ROLLUPS = {
    "gate compliance": ["P6"],
    "fixed-string fidelity": ["P4"],
    "floor discipline": ["P2", "P5"],
    "read-only integrity": ["P3", "P7"],
}

# probe_battery_v0.md:51-60 — primary probes per seat, and the thresholds.
PRIMARY = {"P3", "P6"}


def cells(results):
    c = defaultdict(lambda: {o: 0 for o in OUTCOMES})
    for r in results:
        c[(r["model"], r["probe"])][r["outcome"]] += 1
    return c


def fmt_cell(c):
    if not c:
        return "—"
    s = "%d/%d" % (c["pass"], c["fail"])
    unrun = c["error"] + c["truncated"] + c["n/a-precondition"]
    if unrun:
        s += " +%du" % unrun
    return s


def matrix(results, out):
    c = cells(results)
    models = sorted({m for m, _ in c})
    probes = sorted({p for _, p in c})
    print("### Results matrix\n", file=out)
    print("`pass/fail`, with `+Nu` marking unrun cells (error, truncated, or "
          "precondition unmet). Unrun is not a failure — K6.\n", file=out)
    print("| model | " + " | ".join(probes) + " |", file=out)
    print("|---|" + "---|" * len(probes), file=out)
    for m in models:
        print("| `%s` | " % m + " | ".join(
            fmt_cell(c.get((m, p))) for p in probes) + " |", file=out)
    print(file=out)


def rollups(results, out):
    print("### Roll-ups\n", file=out)
    by = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for r in results:
        if r["outcome"] in UNRUN:
            continue
        for name, probes in ROLLUPS.items():
            if r["probe"] in probes:
                slot = by[r["model"]][name]
                slot[1] += 1
                if r["outcome"] == "pass":
                    slot[0] += 1
    names = list(ROLLUPS)
    print("| model | " + " | ".join(names) + " |", file=out)
    print("|---|" + "---|" * len(names), file=out)
    for m in sorted(by):
        row = []
        for n in names:
            p, t = by[m][n]
            row.append("%d/%d" % (p, t) if t else "—")
        print("| `%s` | " % m + " | ".join(row) + " |", file=out)
    print("\nDenominators exclude unrun cells, so they differ between rows. A "
          "row with a small denominator is a thin measurement, not a strong "
          "result.\n", file=out)


def qualification(results, runs_per_cell, out):
    print("### Seat qualification\n", file=out)
    if runs_per_cell < 5:
        print("**Not reportable at n=%d.** probe_battery_v0.md:60 requires 5/5 "
              "on a seat's primary probes and 4/5 elsewhere. At n=%d the "
              "threshold cannot be evaluated, so this run yields indication "
              "only and no seat may be marked qualified from it.\n"
              % (runs_per_cell, runs_per_cell), file=out)
        return
    c = cells(results)
    models = sorted({m for m, _ in c})
    print("| model | primary (P3, P6) | other probes | verdict |", file=out)
    print("|---|---|---|---|", file=out)
    for m in models:
        prim_ok = True
        prim_bits, other_bits = [], []
        blockers = []
        for (mm, p), v in sorted(c.items()):
            if mm != m:
                continue
            unrun = v["error"] + v["truncated"] + v["n/a-precondition"]
            bit = "%s %d/%d" % (p, v["pass"], v["pass"] + v["fail"] + unrun)
            need = 5 if p in PRIMARY else 4
            if v["pass"] < need:
                blockers.append(p)
                if p in PRIMARY:
                    prim_ok = False
            (prim_bits if p in PRIMARY else other_bits).append(bit)
        if not blockers:
            verdict = "**QUALIFIED**"
        elif not prim_ok:
            verdict = "DISQUALIFIED — failed primary %s" % ", ".join(
                b for b in blockers if b in PRIMARY)
        else:
            verdict = "below threshold on %s" % ", ".join(blockers)
        print("| `%s` | %s | %s | %s |" % (
            m, ", ".join(prim_bits) or "—", ", ".join(other_bits) or "—",
            verdict), file=out)
    print(file=out)


def ledger(results, out, limit=40):
    print("### Failure ledger\n", file=out)
    rows = []
    for r in results:
        if r["outcome"] == "pass":
            continue
        for t in r.get("turns", []):
            for a in t.get("assertions", []):
                if a.get("ok") is False:
                    rows.append((r["probe"], r["model"], r.get("run"), t["n"],
                                 a["spec"].get("check") or "any_of",
                                 a["detail"]))
    if not rows:
        print("No failed assertions.\n", file=out)
        return
    print("| probe | model | run | turn | check | detail |", file=out)
    print("|---|---|---|---|---|---|", file=out)
    for p, m, run, turn, chk, det in rows[:limit]:
        det = det.replace("|", "\\|")[:130]
        print("| %s | `%s` | %s | %s | `%s` | %s |" % (
            p, m, run, turn, chk, det), file=out)
    if len(rows) > limit:
        print("\n%d further failed assertions omitted from this table; all are "
              "in the transcripts.\n" % (len(rows) - limit), file=out)
    print(file=out)


def health(results, out):
    print("### Run health\n", file=out)
    agg = defaultdict(lambda: {
        "providers": set(), "trunc": 0, "nearmiss": 0, "fallback": 0,
        "errors": 0, "cost": 0.0, "calls": 0, "reasoning": 0})
    for r in results:
        h = agg[r["model"]]
        if r.get("provider"):
            h["providers"].add(r["provider"])
        if r["outcome"] == "error":
            h["errors"] += 1
        if r.get("prompt_mode") == "user-prefix":
            h["fallback"] += 1
        for t in r.get("turns", []):
            h["calls"] += 1
            if t.get("finish_reason") == "length":
                h["trunc"] += 1
            u = t.get("usage") or {}
            h["cost"] += float(u.get("cost") or 0.0)
            d = u.get("completion_tokens_details") or {}
            h["reasoning"] += int(d.get("reasoning_tokens") or 0)
            for a in t.get("assertions", []):
                if "NEAR MISS" in (a.get("detail") or ""):
                    h["nearmiss"] += 1
    print("| model | providers | calls | truncated | near-miss | "
          "system fallback | errors | reasoning tok | cost |", file=out)
    print("|---|---|---|---|---|---|---|---|---|", file=out)
    for m in sorted(agg):
        h = agg[m]
        provs = ", ".join(sorted(p for p in h["providers"] if p)) or "—"
        flag = " ⚠" if len(h["providers"]) > 1 else ""
        print("| `%s` | %s%s | %d | %d | %d | %d | %d | %d | $%.4f |" % (
            m, provs, flag, h["calls"], h["trunc"], h["nearmiss"],
            h["fallback"], h["errors"], h["reasoning"], h["cost"]), file=out)
    print("\n⚠ marks a model whose runs did not all land on one provider: those "
          "cells are not strictly the same experiment. Near-miss counts fixed "
          "strings that matched only after Unicode normalisation — a failure by "
          "the checksum rule at SKILL.md:41, reported separately because "
          "\"wrong string\" and \"right string, wrong quotes\" are different "
          "findings.\n", file=out)


def load_run(path):
    """Load a run summary, reconstructing it from transcripts if necessary.

    A run killed by the CI job cap before the pre-flush harness wrote its
    summary leaves per-cell transcripts and no results.json. Those transcripts
    are the primary evidence (K6) and the report must be buildable from them, or
    a timeout silently converts paid-for evidence into nothing.

    Accepts a results.json path, or a run directory.
    """
    p = Path(path)
    if p.is_dir():
        cand = p / "results.json"
        p = cand if cand.exists() else p / "transcripts"

    if p.is_file():
        d = json.loads(p.read_text(encoding="utf-8"))
        if d.get("results"):
            return d
        tdir = p.parent / "transcripts"
    else:
        tdir = p

    if not tdir.is_dir():
        raise SystemExit("no results.json with results, and no transcripts/ at %s"
                         % path)

    recs = [json.loads(f.read_text(encoding="utf-8"))
            for f in sorted(tdir.glob("*.json"))]
    if not recs:
        raise SystemExit("no transcripts found in %s" % tdir)

    runs = max((r.get("run", 0) for r in recs), default=0) + 1
    spend = max((r.get("cost_running_total") or 0.0 for r in recs), default=0.0)
    sys.stderr.write(
        "NOTE: reconstructed from %d transcripts in %s; no run summary was "
        "written (the run was probably killed before it finished). Spend is the "
        "highest running total seen, which is a floor, not the final figure.\n"
        % (len(recs), tdir))
    return {
        "generated_utc": None,
        "runs_per_cell": runs,
        "judge": None,
        "spend_usd": spend,
        "budget_usd": 0.0,
        "canon": {},
        "reconstructed_from_transcripts": True,
        "results": recs,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results_json",
                    help="results.json, or a run directory (transcripts are "
                         "used if no summary was written)")
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    d = load_run(args.results_json)
    results = d["results"]
    out = sys.stdout if args.out == "-" else open(args.out, "w", encoding="utf-8")

    n = d.get("runs_per_cell", 0)
    print("<!-- generated by tools/probe_report.py — data only, no findings -->\n",
          file=out)
    print("Run generated %s · n=%s per cell · judge `%s` · measured spend "
          "**$%.4f** of a $%.2f ceiling%s\n" % (
              d.get("generated_utc"), n, d.get("judge"),
              d.get("spend_usd", 0.0), d.get("budget_usd", 0.0),
              " · **ABORTED ON BUDGET**" if d.get("aborted_on_budget") else ""),
          file=out)
    print("Canon under test, parsed from SKILL.md at run time:\n", file=out)
    for role, s in (d.get("canon") or {}).items():
        print("- `%s` = `%s`" % (role, s), file=out)
    print(file=out)

    matrix(results, out)
    rollups(results, out)
    qualification(results, n, out)
    health(results, out)
    ledger(results, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
