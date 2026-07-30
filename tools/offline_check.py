#!/usr/bin/env python3
"""Offline discrimination check for a probe + its two-sided fixtures.

Usage: python3 tools/offline_check.py <probe_dir> P17 [P18 ...]
Runs each probe's programmatic assertions against its pass/fail fixtures and
reports whether the graders discriminate. Judge assertions are skipped (no
network) and listed so their coverage is not silently assumed. Zero spend.
"""
import json, sys, pathlib
sys.path.insert(0, "tools")
import probe_runner as pr

REPO = pathlib.Path(__file__).resolve().parent.parent
canon, nouns = pr.load_canon(REPO / "SKILL.md")


def check(probe_dir, pid):
    d = pathlib.Path(probe_dir)
    probe = json.loads((d / f"{pid}.json").read_text())
    fixtures = sorted((d / "fixtures").glob(f"{pid}.*.json"))
    if not fixtures:
        print(f"  {pid}: NO FIXTURES"); return False
    all_ok = True
    judge_ids = []
    for fx_path in fixtures:
        fx = json.loads(fx_path.read_text())
        prog_fail = []
        for i, turn in enumerate(probe["turns"]):
            if i >= len(fx["replies"]):
                break
            text = pr.visible(fx["replies"][i])
            ctx = pr.Ctx(canon, nouns, probe, turn, [])
            for spec in turn.get("assert", []):
                ok, det = pr.run_assertion(ctx, text, spec)
                if not ok:
                    prog_fail.append((i, spec.get("check", "any_of"), det[:70]))
            for j in turn.get("judge", []):
                if j["id"] not in judge_ids:
                    judge_ids.append(j["id"])
        prog_pass = (len(prog_fail) == 0)
        discriminates = (prog_pass == (fx["expect"] == "pass"))
        all_ok &= discriminates
        tag = "DISCRIMINATES" if discriminates else "*** WRONG WAY ***"
        print(f"  {fx_path.name:<22} expect={fx['expect']:<5} prog_fails={len(prog_fail):<2} {tag}")
        if not discriminates:
            for f in prog_fail[:6]:
                print("        t%d %-24s %s" % f)
    if judge_ids:
        print(f"  {pid}: judge assertions NOT run offline: {judge_ids}")
    return all_ok


if __name__ == "__main__":
    pdir = sys.argv[1]
    ok = True
    for pid in sys.argv[2:]:
        print(f"=== {pid} ===")
        ok &= check(pdir, pid)
    print("\nALL DISCRIMINATE:", ok)
    sys.exit(0 if ok else 1)
