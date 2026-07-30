import json, sys
sys.path.insert(0,"/home/user/the_algorithm/tools")
import probe_runner as pr
from pathlib import Path
canon, nouns = pr.load_canon(Path("/home/user/the_algorithm/SKILL.md"))
d = Path("/home/user/the_algorithm/.p14_review/fix/probes")
probe = json.loads((d/"P14.json").read_text())
LBL = {0:"RX_A record-state",1:"RX_B mechanism",2:"RX_C acceptance(absent)"}
for f in sorted((d/"fixtures").glob("*.json")):
    fx = json.loads(f.read_text())
    print("=== %s (expect %s)" % (f.name, fx["expect"]))
    for i,turn in enumerate(probe["turns"]):
        if i >= len(fx["replies"]): break
        text = pr.visible(fx["replies"][i])
        ctx = pr.Ctx(canon, nouns, probe, turn, [])
        for spec in turn["assert"]:
            ok, det = pr.run_assertion(ctx, text, spec)
            nm = spec["check"]
            if nm.startswith("regex"):
                det = det[:22]+" ...]"
            print("  t%d %-22s %s | %s" % (i, nm, "ok  " if ok else "FAIL", det[:90]))
