#!/usr/bin/env bash
# drift_audit.sh v0 — the mechanized archivist.
# Checks the canon for the defect signatures we know. Exit nonzero on any failure.
# Evidence discipline: this script prints what it actually tested.

set -u
CANON="${1:-SKILL.md}"
FAIL=0

say() { printf '%s\n' "$*"; }

say "== drift audit v0 on: $CANON =="

# 1. Fixed strings, byte-exact (grep -F, correct case — the instrument has been the defect twice).
declare -a STRINGS=(
"Freeze this contract and execute, or keep negotiating?"
"Contract frozen. Executing."
"Failed on [item]. Contract reopened."
"Cut: nothing."
"This is a finding, not a draft."
)
say "-- fixed strings --"
for s in "${STRINGS[@]}"; do
  c=$(grep -cF -- "$s" "$CANON")
  if [ "$c" -ge 1 ]; then say "OK  [$c] $s"; else say "FAIL [0] $s"; FAIL=1; fi
done

# 2. Floor nouns present as the canonical quartet.
say "-- floor nouns --"
if grep -qF "Audience, Scope, Format, Path" "$CANON"; then
  say "OK  floor quartet present"
else
  say "FAIL floor quartet missing or reworded"; FAIL=1
fi

# 3. Superseded liturgy contained: old gate family may appear only in the Amendment record.
say "-- superseded liturgy containment --"
HITS=$(grep -n "Through the gate" "$CANON" | grep -v "Amendment record" | grep -cv "family" || true)
TOTAL=$(grep -c "Through the gate" "$CANON" || true)
say "occurrences: $TOTAL total; outside amendment-record context: $HITS"
if [ "$HITS" -gt 0 ]; then say "FAIL ghost liturgy outside the record"; FAIL=1; else say "OK  contained"; fi

# 4. Amendment record exists and is non-empty.
say "-- amendment record --"
if grep -qF "### Amendment record" "$CANON" && grep -qE '^\- \*\*v[0-9]+' "$CANON"; then
  say "OK  record present with versioned entries"
else
  say "FAIL amendment record missing or empty — the defect signature"; FAIL=1
fi

# 5. Invariants-change discipline (only meaningful inside a git repo with history).
if git rev-parse --git-dir >/dev/null 2>&1 && git rev-parse HEAD~1 >/dev/null 2>&1; then
  say "-- invariants change discipline (HEAD~1..HEAD) --"
  INV_CHANGED=$(git diff HEAD~1..HEAD -- "$CANON" | grep -cE '^[+-].*' || true)
  if git diff HEAD~1..HEAD -- "$CANON" | grep -q "Gate integrity\|Fixed strings\|Language lock"; then
    if git diff HEAD~1..HEAD -- "$CANON" | grep -q "Amendment record\|frozen"; then
      say "OK  invariants touched with record touched"
    else
      say "FAIL invariants touched without amendment record change"; FAIL=1
    fi
  else
    say "OK  invariants untouched this commit"
  fi
  # 6. Mass report — not error, gradient.
  say "-- mass report (words, HEAD~1 -> HEAD) --"
  for f in $(git diff --name-only HEAD~1..HEAD -- '*.md'); do
    OLD=$(git show HEAD~1:"$f" 2>/dev/null | wc -w || echo 0)
    NEW=$(wc -w < "$f" 2>/dev/null || echo 0)
    say "  $f: $OLD -> $NEW ($((NEW-OLD)))"
  done
else
  say "-- git history unavailable: skipping change-discipline and mass report --"
fi

say "== result: $([ $FAIL -eq 0 ] && echo PASS || echo FAIL) =="
exit $FAIL
