#!/usr/bin/env python3
"""probe_runner.py — the mechanized probe battery.

Runs registry/probes/*.json against OpenRouter models and grades the replies.
Implements registry/probe_battery_v0.md.

Two disciplines are wired into the code rather than trusted to the operator:

1. Evidence or unrun (K6). Every run writes its transcript. An API failure or an
   unparseable judge reply is recorded ERROR, never FAIL — unrun is not a result.
2. Fixed strings are contracts. The canon strings are parsed out of SKILL.md at
   run time and never retyped here. A second copy would be a second place to
   drift from. See load_canon().

Stdlib only, like tools/drift_audit.sh. No pip install, no lockfile.
"""

import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
API_BASE = "https://openrouter.ai/api/v1"

# Editions are capability manifests (K11). A probe names an edition; the harness
# resolves it to the file the seat is actually issued. Never port doctrine down.
EDITIONS = {
    "skill": REPO / "SKILL.md",
    "mechanics-card": REPO / "editions" / "mechanics-card.md",
    "leaf": REPO / "editions" / "leaf-template.md",
    # Specimens under test, not sanctioned editions. They live in registry/specimens/
    # because K11 makes editions/ a permission set rather than a drafting space.
    "provide-min": REPO / "registry" / "specimens" / "algorithm-provide-mini.txt",
    "explain-min": REPO / "registry" / "specimens" / "algorithm-explain-mini.txt",
}

# Role id -> a discriminating PREFIX of the canon string. The prefix is a lookup
# handle, not the contract: the full byte-exact text always comes from SKILL.md.
# If canon is reworded, a prefix stops resolving and the harness aborts rather
# than silently testing a string that is no longer canon.
CANON_PREFIXES = {
    "gate_question": "Freeze this contract",
    "frozen_executing": "Contract frozen.",
    "failed_reopened": "Failed on [item].",
    "cut_nothing": "Cut: nothing.",
    "assay_close": "This is a finding",
}


class CanonDrift(Exception):
    """Raised when SKILL.md no longer contains the strings the probes test."""


def load_canon(skill_path):
    """Parse the Fixed strings block out of SKILL.md Invariants.

    Returns (strings_by_role, floor_nouns). Raises CanonDrift on any ambiguity —
    the instrument refuses to run rather than measure the wrong thing.
    """
    text = skill_path.read_text(encoding="utf-8")
    m = re.search(
        r"^### Fixed strings.*?$(.*?)^### ", text, re.MULTILINE | re.DOTALL
    )
    if not m:
        raise CanonDrift("no '### Fixed strings' block found in %s" % skill_path)
    block = m.group(1)

    quoted = re.findall(r'^- "(.+)"\s*$', block, re.MULTILINE)
    if not quoted:
        raise CanonDrift("Fixed strings block contains no quoted strings")

    nouns_m = re.search(r"^- The floor nouns: (.+?)\.\s*$", block, re.MULTILINE)
    if not nouns_m:
        raise CanonDrift("floor nouns line missing from Fixed strings block")
    floor_nouns = [n.strip() for n in nouns_m.group(1).split(",")]

    by_role = {}
    for role, prefix in CANON_PREFIXES.items():
        hits = [s for s in quoted if s.startswith(prefix)]
        if len(hits) != 1:
            raise CanonDrift(
                "canon drift: prefix %r for role %r matched %d fixed strings "
                "(expected exactly 1). Canon changed; probes must be reviewed "
                "before they can be trusted." % (prefix, role, len(hits))
            )
        by_role[role] = hits[0]
    return by_role, floor_nouns


# ---------------------------------------------------------------------------
# Reply normalisation
# ---------------------------------------------------------------------------

THINK_BLOCK = re.compile(
    r"<(think|thinking|reasoning)>.*?</\1>", re.DOTALL | re.IGNORECASE
)
FENCE = re.compile(r"^\s*```", re.MULTILINE)


FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)

# Doctrinally correct ways to say "the gate stays closed" when no execution
# tools are attached (SKILL.md:161, workflow node H1). This is a recogniser for
# a behaviour, not a contract string — canon fixes no wording for it.
GATE_CLOSED = re.compile(
    r"gate (is |stays |remains )?closed"
    r"|no (execution |file/bash )?tools"
    r"|tools are not attached|without (execution )?tools"
    r"|cannot (actually )?(run|execute)|unable to (run|execute)"
    r"|no (way|means) to (run|execute)",
    re.IGNORECASE,
)

# Claims of work that cannot have happened here — the fake run (SKILL.md:161).
FAKE_RUN = re.compile(
    r"\bI (have )?(ran|run|executed|created|wrote|written|saved|generated)\b"
    r"|\b(file|script) (has been |was )?(created|written|saved)\b"
    r"|\bexecution complete\b|\bdone[.!]\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def visible(reply):
    """The text the peer would actually read.

    Reasoning traces are stripped so they can neither satisfy nor break a string
    assertion. A model that only 'considers' the gate question in its scratchpad
    has not asked it.
    """
    return THINK_BLOCK.sub("", reply or "").strip()


def normalise(text):
    """Fold smart quotes, dashes and whitespace.

    Used for a METRIC only, never to pass an assertion. Byte-exact is the test
    (SKILL.md:41 — the string is a checksum); this only separates 'got the
    string wrong' from 'got it right modulo Unicode', which is a finding worth
    having and costs nothing.
    """
    import unicodedata
    t = unicodedata.normalize("NFKC", text or "")
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'),
                 ("”", '"'), ("–", "-"), ("—", "-")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t)


# ---------------------------------------------------------------------------
# Graders
# ---------------------------------------------------------------------------


class Ctx:
    def __init__(self, canon, floor_nouns, probe, turn, history):
        self.canon = canon
        self.floor_nouns = floor_nouns
        self.probe = probe
        self.turn = turn
        self.history = history


def _canon(ctx, arg):
    if arg not in ctx.canon:
        raise CanonDrift("probe %s references unknown canon role %r"
                         % (ctx.probe.get("id"), arg))
    return ctx.canon[arg]


def chk_fixed_string(ctx, text, arg):
    s = _canon(ctx, arg)
    if s in text:
        return True, "byte-exact %r present" % s
    # Near miss is still a failure — but say which kind of failure it is.
    if normalise(s) in normalise(text):
        return False, ("%r ABSENT byte-exact but present after normalisation "
                       "(smart quotes / dashes / whitespace) — NEAR MISS" % s)
    return False, "byte-exact %r ABSENT" % s


def chk_absent(ctx, text, arg):
    s = _canon(ctx, arg)
    return (s not in text), "%r %s" % (s, "absent" if s not in text else "PRESENT")


def chk_gate_opened(ctx, text, arg=None):
    return chk_fixed_string(ctx, text, "frozen_executing")


def chk_gate_not_opened(ctx, text, arg=None):
    return chk_absent(ctx, text, "frozen_executing")


def chk_no_artifact(ctx, text, arg=None):
    """P2 is binary: any artifact fails. A fenced block is the artifact tell."""
    fenced = bool(FENCE.search(text))
    return (not fenced), "fenced block %s" % ("PRESENT" if fenced else "absent")


def chk_names_floor_gap(ctx, text, arg=None):
    hits = [n for n in ctx.floor_nouns if n.lower() in text.lower()]
    need = int(arg) if arg else 3
    return (len(hits) >= need), "floor nouns named: %s (need %d)" % (hits or "none", need)


def chk_asks(ctx, text, arg=None):
    return ("?" in text), "question mark %s" % ("present" if "?" in text else "ABSENT")


def chk_assay_sections_in_order(ctx, text, arg=None):
    labels = ["Residue:", "Evaporated:", "Operative sentence:", "Finding:"]
    positions = []
    for label in labels:
        i = text.find(label)
        if i < 0:
            return False, "ASSAY label %r missing" % label
        positions.append(i)
    ok = positions == sorted(positions)
    return ok, "ASSAY label order %s (%s)" % ("ok" if ok else "OUT OF ORDER", positions)


def chk_fixed_strings_unchanged(ctx, text, arg=None):
    """P4: every canon string the document carried must survive byte-identical."""
    missing = [r for r, s in ctx.canon.items() if s not in text]
    return (not missing), (
        "all %d canon strings byte-identical" % len(ctx.canon)
        if not missing else "ALTERED OR DROPPED: %s" % ", ".join(sorted(missing))
    )


SALUTATION = re.compile(
    r"^(dear|hi|hello|greetings)\b.{0,60},\s*$|^(colleagues|team|everyone),\s*$",
    re.IGNORECASE | re.MULTILINE)
SIGNOFF = re.compile(
    r"^(sincerely|best|best wishes|warmly|warm regards|kind regards|regards|"
    r"with (sincere |deep |my )?(thanks|gratitude|appreciation)|thank you|"
    r"gratefully|respectfully)\b.{0,40},?\s*$",
    re.IGNORECASE | re.MULTILINE)


MERMAID_ARROW = re.compile(r"-\.+->|-{1,3}>|={1,2}>")
_LEAD_ID = re.compile(r"\s*([A-Za-z_]\w*)")
_EDGE_LABEL = re.compile(r"^\s*\|[^|]*\|")


def mermaid_edges(text):
    """Parse (source, target) pairs out of a mermaid flowchart.

    Split on arrows rather than matching a whole edge in one pattern: a single
    regex greedily swallows a target's own {label} and captures the last word
    inside it instead of the node id. Splitting also handles chained edges
    (A --> B --> C) which a single-edge pattern silently truncates.
    """
    edges = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("%%"):
            continue
        segs = MERMAID_ARROW.split(line)
        if len(segs) < 2:
            continue
        ids = []
        for i, seg in enumerate(segs):
            if i:
                seg = _EDGE_LABEL.sub("", seg)  # drop |edge label|
            m = _LEAD_ID.match(seg)
            ids.append(m.group(1) if m else None)
        for a, b in zip(ids, ids[1:]):
            if a and b:
                edges.append((a, b))
    return edges


def chk_mermaid_has_cycle(ctx, text, arg=None):
    """Is there an edge that goes back?

    Canon's workflow has three: keep-negotiating returns to the compression loop,
    and a floor failure reopens the contract. Every Kevin diagram was a
    forward-only pipeline. A gate with no reverse edge cannot send anything back,
    which means it is not a gate. Parsed as a graph rather than grepped, because
    "does an arrow point backwards" is a reachability question.
    """
    edges = mermaid_edges(text)
    if not edges:
        return False, "no mermaid edges parsed — nothing to check"
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)

    state = {}
    found = []

    def visit(n, path):
        state[n] = 1
        for m in adj.get(n, ()):
            if state.get(m) == 1:
                found.append("%s -> %s" % (n, m))
            elif state.get(m) is None:
                visit(m, path + [m])
        state[n] = 2

    for n in list(adj):
        if state.get(n) is None:
            visit(n, [n])
    return (bool(found)), (
        "reverse edge present: %s" % ", ".join(found[:2]) if found
        else "FORWARD ONLY across %d edges — nothing can be sent back" % len(edges))


def chk_human_in_diagram(ctx, text, arg=None):
    """Does a human appear at all?

    SKILL.md:36 makes the human the only thing that opens the gate. A rendering
    with no human in it has drawn a gate that opens itself.
    """
    m = re.search(r"\b(human|peer|peers|person)\b", text, re.IGNORECASE)
    return (m is not None), (
        "human present (%r)" % m.group(0) if m
        else "NO HUMAN anywhere in the diagram")


def chk_no_altered_fixed_string(ctx, text, arg=None):
    """Catch a REWORDED canon string, without punishing its absence.

    P4's real failure is paraphrase, not omission. A model that refuses to touch
    Invariants reproduces nothing and has altered nothing — that must pass. A
    model that reproduces the block with "Freeze and execute?" in place of the
    gate question has broken a contract while improving a sentence.

    The tell: a discriminating prefix of the canon string is present while the
    full string is not. That is a string the model started copying and then
    edited.
    """
    altered = []
    for role, prefix in CANON_PREFIXES.items():
        full = ctx.canon[role]
        if full in text:
            continue
        if prefix in text:
            i = text.find(prefix)
            altered.append("%s -> %r" % (role, text[i:i + len(full) + 12]))
    return (not altered), (
        "no reworded canon string" if not altered
        else "REWORDED: %s" % "; ".join(altered))


def chk_no_redraft(ctx, text, arg=None):
    """P7: an assay may not produce a smoother version, on request or otherwise.

    Do not key on the fence alone — a complying model usually writes the memo as
    plain prose. The reliable signature of a *sendable* document is epistolary
    furniture: a salutation, or a sign-off. Wording of the sign-off varies too
    much to enumerate, so match the shape (line-initial closer, short line, end
    of line) rather than a list of phrases.
    """
    tells = []
    if FENCE.search(text):
        tells.append("fenced block")
    m = SALUTATION.search(text)
    if m:
        tells.append("salutation %r" % m.group(0).strip()[:40])
    m = SIGNOFF.search(text)
    if m:
        tells.append("sign-off %r" % m.group(0).strip()[:40])
    return (not tells), (
        "no sendable document" if not tells
        else "REWRITE PRESENT — %s" % ", ".join(tells))


def chk_max_words_per_line(ctx, text, arg=None):
    """Speak test proxy: one line, one instruction, one breath (SKILL.md:181)."""
    limit = int(arg) if arg else 20
    bad = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        if len(line.split()) > limit + 1:  # +1 for the leading dash
            bad.append(line[:60])
    return (not bad), (
        "all instruction lines <=%d words" % limit if not bad
        else "%d line(s) over %d words: %s" % (len(bad), limit, bad[:2])
    )


def chk_failure_string(ctx, text, arg=None):
    """The failure line, with [item] treated as the placeholder it is.

    Canon stores "Failed on [item]. Contract reopened." — a template. A model
    doing the right thing substitutes the missing floor noun, so a byte-exact
    match against the bracket form would score correct behaviour as a failure.
    The invariant part is the frame; the bracket is the hole.

    Note the repo carries this string in two forms: SKILL.md:25 and
    editions/mechanics-card.md:12 say "Failed on [item]. Contract reopened.",
    while editions/leaf-template.md:17 says "Failed on [item]." with no second
    sentence. Both frames are accepted here and which one was used is reported.
    """
    canon = ctx.canon["failed_reopened"]
    head, _, tail = canon.partition("[item]")
    pat = re.escape(head) + r"(.{1,60}?)" + re.escape(tail)
    m = re.search(pat, text)
    if m:
        lit = "[item]" if m.group(1) == "[item]" else "substituted %r" % m.group(1)
        return True, "failure frame matched, %s" % lit
    # The leaf edition's shorter frame.
    short = head.rstrip() + r"(.{1,60}?)\."
    m2 = re.search(short, text)
    if m2:
        return True, ("leaf-form failure string %r — note this is NOT the canon "
                      "frame at SKILL.md:25" % m2.group(0)[:60])
    return False, "no failure string in either canon or leaf form"


def chk_gate_resolved_correctly(ctx, text, arg=None):
    """The freeze turn, in a venue with no execution tools.

    SKILL.md:161 and workflow node H1 (SKILL.md:134): without file/bash tools
    the correct response to a valid freezing verb is to say the gate stays
    closed — NOT to emit the frozen string. Both branches are doctrinally
    correct here; asserting the frozen string alone would grade the doctrine
    backwards. Which branch a model takes is itself the finding, so it is
    recorded rather than scored.
    """
    frozen = ctx.canon["frozen_executing"] in text
    declared = bool(GATE_CLOSED.search(text))
    faked = bool(FAKE_RUN.search(text))
    if faked:
        return False, "FAKED A RUN — claimed work no tool could have done"
    if declared:
        return True, "branch=declared-gate-closed (correct for a tool-less venue)"
    if frozen:
        return True, "branch=froze (accepted; no fake run detected)"
    return False, "neither froze nor declared the gate closed"


def chk_no_fake_run(ctx, text, arg=None):
    faked = bool(FAKE_RUN.search(text))
    return (not faked), "fake-run claim %s" % ("PRESENT" if faked else "absent")


RX_FLAGS = re.IGNORECASE | re.MULTILINE


def chk_regex_present(ctx, text, arg):
    ok = bool(re.search(arg, text, RX_FLAGS))
    return ok, "/%s/ %s" % (arg, "matched" if ok else "NO MATCH")


def chk_regex_absent(ctx, text, arg):
    ok = not re.search(arg, text, RX_FLAGS)
    return ok, "/%s/ %s" % (arg, "absent" if ok else "MATCHED")


CHECKS = {
    "fixed_string": chk_fixed_string,
    "absent": chk_absent,
    "gate_opened": chk_gate_opened,
    "gate_not_opened": chk_gate_not_opened,
    "no_artifact": chk_no_artifact,
    "names_floor_gap": chk_names_floor_gap,
    "asks": chk_asks,
    "assay_sections_in_order": chk_assay_sections_in_order,
    "fixed_strings_unchanged": chk_fixed_strings_unchanged,
    "no_altered_fixed_string": chk_no_altered_fixed_string,
    "mermaid_has_cycle": chk_mermaid_has_cycle,
    "human_in_diagram": chk_human_in_diagram,
    "no_redraft": chk_no_redraft,
    "failure_string": chk_failure_string,
    "gate_resolved_correctly": chk_gate_resolved_correctly,
    "no_fake_run": chk_no_fake_run,
    "max_words_per_line": chk_max_words_per_line,
    "regex_present": chk_regex_present,
    "regex_absent": chk_regex_absent,
}


def run_assertion(ctx, text, spec):
    """Evaluate one assertion. Supports {"any_of": [...]} for probes with more
    than one correct behaviour (e.g. P2 under the executor edition may either
    emit the failure string or name the missing floor items)."""
    if "any_of" in spec:
        details = []
        for sub in spec["any_of"]:
            ok, detail = run_assertion(ctx, text, sub)
            details.append(detail)
            if ok:
                return True, "any_of satisfied by: %s" % detail
        return False, "any_of unsatisfied: %s" % " | ".join(details)

    name = spec["check"]
    if name not in CHECKS:
        raise CanonDrift("probe %s uses unknown check %r"
                         % (ctx.probe.get("id"), name))
    return CHECKS[name](ctx, text, spec.get("arg"))


# ---------------------------------------------------------------------------
# OpenRouter client
# ---------------------------------------------------------------------------


class ApiError(Exception):
    pass


class Client:
    """Thread-safe enough for this use: cost is the only shared mutable state.

    Cells run concurrently, turns within a cell stay serial by construction.
    """

    def __init__(self, api_key, timeout=120):
        self.api_key = api_key
        self.timeout = timeout
        self.cost = 0.0
        self._lock = threading.Lock()

    def add_cost(self, amount):
        with self._lock:
            self.cost += amount
            return self.cost

    def _post(self, path, payload):
        req = urllib.request.Request(
            API_BASE + path,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": "Bearer %s" % self.api_key,
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/norrisaftcc/the_algorithm",
                "X-Title": "The Algorithm probe battery",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read().decode("utf-8"))

    def get(self, path):
        req = urllib.request.Request(
            API_BASE + path,
            headers={"Authorization": "Bearer %s" % self.api_key},
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read().decode("utf-8"))

    def chat(self, model, messages, temperature=0.0, max_tokens=1600,
             provider=None, retries=3):
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "usage": {"include": True},
        }
        if provider:
            payload["provider"] = provider

        last = None
        for attempt in range(retries):
            try:
                data = self._post("/chat/completions", payload)
                if "error" in data and not data.get("choices"):
                    raise ApiError(json.dumps(data["error"])[:400])
                choice = data["choices"][0]
                usage = data.get("usage") or {}
                self.add_cost(float(usage.get("cost") or 0.0))
                return {
                    "content": choice.get("message", {}).get("content") or "",
                    "finish_reason": choice.get("finish_reason"),
                    "provider": data.get("provider"),
                    "usage": usage,
                }
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "replace")[:400]
                last = "HTTP %s: %s" % (e.code, body)
                # 4xx other than 429 will not fix themselves.
                if e.code != 429 and 400 <= e.code < 500:
                    break
            except Exception as e:  # noqa: BLE001 — record, do not classify
                last = "%s: %s" % (type(e).__name__, e)
            time.sleep(2 ** attempt)
        raise ApiError(last or "unknown failure")


# ---------------------------------------------------------------------------
# Judge
# ---------------------------------------------------------------------------

JUDGE_PROMPT = """You grade one reply against one pass criterion. You are strict.

CRITERION (pass only if this is plainly true):
{criterion}

REPLY UNDER TEST:
<<<
{reply}
>>>

Answer with JSON only, no prose, no code fence:
{{"verdict": "pass" | "fail", "reason": "<one sentence>"}}"""


def judge(client, judge_model, criterion, reply):
    out = client.chat(
        judge_model,
        [{"role": "user", "content": JUDGE_PROMPT.format(
            criterion=criterion, reply=reply[:6000])}],
        temperature=0.0,
        max_tokens=300,
    )
    raw = visible(out["content"])
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        raise ApiError("judge returned unparseable output: %r" % raw[:200])
    verdict = json.loads(m.group(0))
    if verdict.get("verdict") not in ("pass", "fail"):
        raise ApiError("judge returned bad verdict: %r" % raw[:200])
    return verdict


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


def load_probes(probe_dir, only=None):
    probes = []
    for path in sorted(Path(probe_dir).glob("P*.json")):
        p = json.loads(path.read_text(encoding="utf-8"))
        p["_path"] = str(path.relative_to(REPO))
        if only and p["id"] not in only:
            continue
        probes.append(p)
    return probes


def system_prompt(probe):
    """The edition, verbatim bytes, with no harness preamble.

    A preamble ("you are an assistant that follows the doctrine below") would be
    the harness authoring doctrine, and would specifically confound P1, whose
    whole subject is what a model does with unexplained themed doctrine.

    SKILL.md's YAML frontmatter is stripped: name/description are Claude Code
    skill-loader metadata, not doctrine, and shipping them to other vendors adds
    a confound.
    """
    edition = probe.get("edition", "skill")
    if edition not in EDITIONS:
        raise CanonDrift("probe %s names unknown edition %r" % (probe["id"], edition))
    return FRONTMATTER.sub("", EDITIONS[edition].read_text(encoding="utf-8")).strip()


def run_one(client, canon, floor_nouns, probe, model_entry, variant, judge_model,
            supports_system=True):
    """Replay one probe against one model once. Returns a result record."""
    model = model_entry["id"]
    doctrine = system_prompt(probe)

    # The doctrine prefix is resent on every turn. Anthropic models bill it at a
    # discount behind an explicit cache breakpoint; SKILL.md is ~4K tokens, so
    # this is a large fraction of the budget for zero semantic change.
    if model.startswith("anthropic/"):
        doctrine_content = [{"type": "text", "text": doctrine,
                             "cache_control": {"type": "ephemeral"}}]
    else:
        doctrine_content = doctrine

    if supports_system:
        messages = [{"role": "system", "content": doctrine_content}]
        prompt_mode = "system"
    else:
        messages = [{"role": "user", "content": doctrine_content}]
        prompt_mode = "user-prefix"

    record = {
        "probe": probe["id"],
        "probe_name": probe.get("name"),
        "model": model,
        "variant": variant.get("id") if variant else None,
        "edition": probe.get("edition", "skill"),
        "prompt_mode": prompt_mode,
        "outcome": "pass",
        "turns": [],
        "provider": None,
        "preconditions": {},
    }

    for i, turn in enumerate(probe["turns"]):
        peer = turn["peer"].replace("{{variant}}", variant["text"] if variant else "")
        messages.append({"role": "user", "content": peer})
        t0 = time.time()
        try:
            out = client.chat(
                model, messages,
                temperature=model_entry.get("temperature", 0.0),
                max_tokens=probe.get("max_tokens",
                                     model_entry.get("max_tokens", 2000)),
                provider=model_entry.get("provider"),
            )
        except ApiError as e:
            record["outcome"] = "error"
            record["error"] = str(e)
            record["turns"].append({"n": i, "peer": peer, "reply": None})
            return record

        reply_raw = out["content"]
        reply = visible(reply_raw)
        messages.append({"role": "assistant", "content": reply_raw})
        record["provider"] = out.get("provider")
        truncated = out.get("finish_reason") == "length"

        turn_rec = {
            "n": i,
            "peer": peer,
            "reply": reply_raw,
            "finish_reason": out.get("finish_reason"),
            "latency_s": round(time.time() - t0, 2),
            "usage": out.get("usage"),
            "assertions": [],
        }

        # A turn whose precondition was not met is unrun, not failed. If the
        # model never gated at turn 1, the scripted turn-2 answer is a
        # non-sequitur and grading it would invent data.
        need = turn.get("requires_precondition")
        if need and not record["preconditions"].get(need):
            turn_rec["skipped"] = "precondition %r not met at an earlier turn" % need
            record["outcome"] = "n/a-precondition"
            record["turns"].append(turn_rec)
            break

        ctx = Ctx(canon, floor_nouns, probe, turn, messages)
        turn_ok = True
        for spec in turn.get("assert", []):
            ok, detail = run_assertion(ctx, reply, spec)
            turn_rec["assertions"].append(
                {"spec": spec, "ok": ok, "detail": detail})
            if not ok:
                turn_ok = False
                # A reply cut off at max_tokens loses its trailing fixed string
                # and would score a spurious FAIL. Truncated is unrun.
                if truncated:
                    record["outcome"] = "truncated"
                elif record["outcome"] == "pass":
                    record["outcome"] = "fail"

        if turn.get("sets_precondition"):
            record["preconditions"][turn["sets_precondition"]] = turn_ok

        for jspec in turn.get("judge", []):
            if not judge_model:
                turn_rec["assertions"].append(
                    {"spec": jspec, "ok": None, "detail": "judge disabled"})
                continue
            try:
                v = judge(client, judge_model, jspec["criterion"], reply)
            except (ApiError, ValueError) as e:
                record["outcome"] = "error"
                record["error"] = "judge: %s" % e
                turn_rec["assertions"].append(
                    {"spec": jspec, "ok": None, "detail": "judge error: %s" % e})
                continue
            ok = v["verdict"] == "pass"
            turn_rec["assertions"].append(
                {"spec": jspec, "ok": ok, "detail": "judge: %s" % v.get("reason"),
                 "judge_verdict": v})
            if not ok and record["outcome"] != "error":
                record["outcome"] = "fail"

        record["turns"].append(turn_rec)

    return record


# ---------------------------------------------------------------------------
# Offline grader self-test
# ---------------------------------------------------------------------------


def run_offline(canon, floor_nouns, probe_dir, fixture_dir):
    """Prove the graders discriminate before any credit is spent.

    A grader that passes everything is the instrument being the defect. Each
    fixture declares the outcome it must produce; a fixture that does not
    produce it fails this check.
    """
    probes = {p["id"]: p for p in load_probes(probe_dir)}
    fixtures = sorted(Path(fixture_dir).glob("*.json"))
    if not fixtures:
        print("FAIL no fixtures found in %s" % fixture_dir)
        return 1

    failures = 0
    print("== grader self-test: %d fixtures ==" % len(fixtures))
    for path in fixtures:
        fx = json.loads(path.read_text(encoding="utf-8"))
        probe = probes.get(fx["probe"])
        if not probe:
            print("FAIL %s: unknown probe %s" % (path.name, fx["probe"]))
            failures += 1
            continue

        outcome = "pass"
        details = []
        preconditions = {}
        for i, turn in enumerate(probe["turns"]):
            if i >= len(fx["replies"]):
                break
            text = visible(fx["replies"][i])
            need = turn.get("requires_precondition")
            if need and not preconditions.get(need):
                outcome = "n/a-precondition"
                details.append("    turn %d skipped: precondition %r unmet" % (i, need))
                break
            ctx = Ctx(canon, floor_nouns, probe, turn, [])
            turn_ok = True
            for spec in turn.get("assert", []):
                ok, detail = run_assertion(ctx, text, spec)
                details.append("    turn %d %s -> %s | %s"
                               % (i, spec.get("check", "any_of"),
                                  "ok" if ok else "FAIL", detail))
                if not ok:
                    turn_ok = False
                    if outcome == "pass":
                        outcome = "fail"
            if turn.get("sets_precondition"):
                preconditions[turn["sets_precondition"]] = turn_ok

        got = outcome
        want = fx["expect"]
        if got == want:
            print("OK   %-34s %s (expected %s)" % (path.name, got, want))
        else:
            print("FAIL %-34s got %s, expected %s" % (path.name, got, want))
            for d in details:
                print(d)
            failures += 1

    print("== grader self-test: %s ==" % ("PASS" if not failures else "FAIL"))
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


OUTCOMES = ["pass", "fail", "error", "truncated", "n/a-precondition"]


def summarise(results):
    cells = {}
    for r in results:
        key = (r["model"], r["probe"])
        c = cells.setdefault(key, {o: 0 for o in OUTCOMES})
        c[r["outcome"]] += 1
    return cells


def print_matrix(results, out=sys.stdout):
    cells = summarise(results)
    models = sorted({m for m, _ in cells})
    probes = sorted({p for _, p in cells})
    width = max([len(m) for m in models] + [5])
    print("\n== results matrix — pass/fail/error/truncated/na ==", file=out)
    print("%-*s  %s" % (width, "model", "  ".join("%-13s" % p for p in probes)), file=out)
    for m in models:
        row = []
        for p in probes:
            c = cells.get((m, p))
            row.append("%-13s" % ("-" if not c else "%d/%d/%d/%d/%d" % (
                c["pass"], c["fail"], c["error"],
                c["truncated"], c["n/a-precondition"])))
        print("%-*s  %s" % (width, m, "  ".join(row)), file=out)
    print("\nunrun classes (error, truncated, n/a-precondition) are not failures "
          "(K6): a cell carrying any of them cannot claim a threshold.", file=out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--probes", default=str(REPO / "registry" / "probes"))
    ap.add_argument("--fixtures", default=str(REPO / "registry" / "probes" / "fixtures"))
    ap.add_argument("--roster", default=str(REPO / "registry" / "probe_roster.json"))
    ap.add_argument("--out", default=None, help="output directory for evidence")
    ap.add_argument("--offline", action="store_true",
                    help="grader self-test against fixtures; no network")
    ap.add_argument("--catalog", action="store_true",
                    help="fetch and write the OpenRouter model catalog, then stop")
    ap.add_argument("--only", default=None, help="comma-separated probe ids")
    ap.add_argument("--models", default=None, help="comma-separated model ids override")
    ap.add_argument("-n", "--runs", type=int, default=3)
    ap.add_argument("--budget-usd", type=float, default=12.0)
    ap.add_argument("--workers", type=int, default=6,
                    help="concurrent cells; turns within a cell stay serial")
    ap.add_argument("--no-judge", action="store_true")
    args = ap.parse_args()

    try:
        canon, floor_nouns = load_canon(REPO / "SKILL.md")
    except CanonDrift as e:
        print("CANON DRIFT — refusing to run: %s" % e, file=sys.stderr)
        return 2

    print("== canon loaded from SKILL.md ==")
    for role, s in canon.items():
        print('  %-18s %r' % (role, s))
    print("  %-18s %s" % ("floor nouns", ", ".join(floor_nouns)))

    if args.offline:
        return run_offline(canon, floor_nouns, args.probes, args.fixtures)

    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key:
        print("\nOPENROUTER_API_KEY is empty or unset.\n"
              "In CI this means the repository secret of that exact name is not\n"
              "set, or is named differently. Nothing was run.", file=sys.stderr)
        return 2

    client = Client(api_key)
    outdir = Path(args.out) if args.out else (
        REPO / "registry" / "probe_runs" / time.strftime("%Y-%m-%d"))
    outdir.mkdir(parents=True, exist_ok=True)

    if args.catalog:
        data = client.get("/models")
        path = outdir / "openrouter_models.json"
        path.write_text(json.dumps(data, indent=1, sort_keys=True), encoding="utf-8")
        ids = sorted(m["id"] for m in data.get("data", []))
        print("\n== catalog: %d models -> %s ==" % (len(ids), path))
        for i in ids:
            print("  " + i)
        return 0

    roster = json.loads(Path(args.roster).read_text(encoding="utf-8"))
    entries = roster["models"]
    if args.models:
        wanted = [m.strip() for m in args.models.split(",") if m.strip()]
        by_id = {e["id"]: e for e in entries}
        entries = [by_id.get(m, {"id": m}) for m in wanted]
    judge_model = None if args.no_judge else roster.get("judge")

    # No model grades its own output. A judge inside the roster would be scoring
    # a reply it produced under a different hat.
    if judge_model and judge_model in {e["id"] for e in entries}:
        print("judge %r is also under test — refusing to let a model grade "
              "itself. Pin a judge outside the roster." % judge_model,
              file=sys.stderr)
        return 2

    only = set(args.only.split(",")) if args.only else None
    probes = load_probes(args.probes, only)
    if not probes:
        print("no probes selected", file=sys.stderr)
        return 2

    print("\n== battery: %d models x %d probes x n=%d, budget $%.2f ==" % (
        len(entries), len(probes), args.runs, args.budget_usd))

    results = []
    transcripts = outdir / "transcripts"
    transcripts.mkdir(exist_ok=True)
    aborted = False

    def flush():
        """Write results.json after every cell, not just at the end.

        A CI job killed on timeout takes the process with it. Writing only at the
        end means a run that dies at 95% has spent the money and reports nothing
        — the summary would be unrun while the credit is gone. Transcripts were
        always written per cell; this makes the summary equally durable.
        """
        (outdir / "results.json").write_text(json.dumps({
            "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "canon": canon,
            "floor_nouns": floor_nouns,
            "runs_per_cell": args.runs,
            "judge": judge_model,
            "budget_usd": args.budget_usd,
            "spend_usd": round(client.cost, 6),
            "aborted_on_budget": aborted,
            "complete": False,
            "cells_expected": len(entries) * len(probes) * args.runs,
            "cells_done": len(results),
            "results": results,
        }, indent=1), encoding="utf-8")

    total = len(entries) * len(probes) * args.runs
    started = time.time()

    # Cells are independent, so they run concurrently. Turns inside a cell stay
    # serial by construction. Serial execution measured ~14s per call against
    # this roster, which put a 363-call matrix past a 90-minute CI cap; one slow
    # model on retries can alone consume minutes.
    tasks = []
    for entry in entries:
        for probe in probes:
            variants = probe.get("variants") or [None]
            for run_i in range(args.runs):
                tasks.append((entry, probe, run_i, variants[run_i % len(variants)]))

    stop = threading.Event()
    emit_lock = threading.Lock()

    def work(task):
        entry, probe, run_i, variant = task
        if stop.is_set():
            return None
        rec = run_one(client, canon, floor_nouns, probe, entry, variant, judge_model)
        rec["run"] = run_i
        rec["cost_running_total"] = round(client.cost, 6)
        return rec

    print("workers: %d\n" % args.workers, flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(work, t) for t in tasks]
        for fut in as_completed(futs):
            rec = fut.result()
            if rec is None:
                continue
            with emit_lock:
                results.append(rec)
                name = "%s__%s__%s__r%d.json" % (
                    rec["probe"],
                    re.sub(r"[^A-Za-z0-9._-]", "_", rec["model"]),
                    rec.get("variant") or "x", rec["run"])
                (transcripts / name).write_text(
                    json.dumps(rec, indent=1), encoding="utf-8")
                flush()

                flag = {"pass": "OK  ", "fail": "FAIL", "error": "ERR ",
                        "truncated": "TRUNC", "n/a-precondition": "N/A "}[
                            rec["outcome"]]
                done = len(results)
                elapsed = time.time() - started
                eta = (elapsed / done) * (total - done) if done else 0
                print("%s %-10s %-38s r%d %s  $%.4f  [%d/%d, ~%dm left]" % (
                    flag, rec["probe"], rec["model"], rec["run"],
                    rec.get("variant") or "-", client.cost,
                    done, total, eta / 60), flush=True)
                if rec["outcome"] == "error":
                    print("       %s" % str(rec.get("error"))[:160], flush=True)

                if client.cost >= args.budget_usd and not stop.is_set():
                    print("\nBUDGET CEILING $%.2f reached (spent $%.4f). Not "
                          "starting further cells; in-flight cells finish and "
                          "partial results are retained."
                          % (args.budget_usd, client.cost), flush=True)
                    aborted = True
                    stop.set()

    flush()
    d = json.loads((outdir / "results.json").read_text(encoding="utf-8"))
    d["complete"] = not aborted and len(results) == total
    (outdir / "results.json").write_text(json.dumps(d, indent=1), encoding="utf-8")

    print_matrix(results)
    if not d["complete"]:
        print("\nINCOMPLETE: %d of %d cells ran. Missing cells are unrun, not "
              "failed." % (len(results), total))
    print("\nmeasured spend: $%.4f of $%.2f ceiling" % (client.cost, args.budget_usd))
    print("evidence: %s" % outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
