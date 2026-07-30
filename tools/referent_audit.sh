#!/usr/bin/env bash
# referent_audit.sh v0 — the checksum's blind spot.
#
# tools/drift_audit.sh verifies that fixed strings are byte-exact. That is a
# checksum, and a checksum cannot detect a changed referent. This script checks
# whether a protected term is being used to mean something other than what canon
# says it means.
#
# Evidence discipline: prints every check it ran, including the ones that passed.
#
# Detects COLLISIONS, not compliance. Requiring positive evidence would false-flag
# canon: SKILL.md:179 defines Path without containing a file path. Each term
# instead carries patterns indicating the term used as something else.
#
# Reports. Wire it non-blocking in CI — this instrument has no measured
# false-positive rate and has not earned a gate.

set -u
FAIL=0
say() { printf '%s\n' "$*"; }

FILES=("$@")
[ ${#FILES[@]} -eq 0 ] && FILES=("SKILL.md")

say "== referent audit v0 =="
say "terms from: registry/referents.json"
say "method: collision detection, fenced blocks skipped"
say ""

# Strip fenced code blocks. A mermaid diagram's arrows are notation, not prose.
strip_fences() {
  awk 'BEGIN{f=0}
       /^[[:space:]]*```/ {f=!f; print ""; next}
       {print (f ? "" : $0)}' "$1"
}

# --- Path: a label followed within 2 lines by a multi-stage arrow chain --------
check_path() {
  local f="$1" tmp="$2"
  awk -v FNAME="$f" '
    { line[NR]=$0 }
    END {
      hits=0
      for (i=1; i<=NR; i++) {
        if (line[i] !~ /(^|[^A-Za-z])Path([^A-Za-z]|$)/) continue
        for (j=i; j<=i+2 && j<=NR; j++) {
          s=line[j]
          n=gsub(/→|->|=>/, "&", s)
          if (n >= 2) {
            printf "FAIL %s:%d  Path with a %d-stage arrow chain -> control flow, not an output location\n", FNAME, i, n+1
            printf "       %s\n", substr(line[j],1,96)
            hits++
            break
          }
        }
      }
      exit (hits>0 ? 1 : 0)
    }' "$tmp"
}

# --- gate: dispatch language nearby, and no human-authority word ---------------
check_gate() {
  local f="$1" tmp="$2"
  awk -v FNAME="$f" '
    { line[NR]=tolower($0); orig[NR]=$0 }
    END {
      hits=0
      for (i=1; i<=NR; i++) {
        if (line[i] !~ /gate/) continue
        disp=0; human=0
        for (j=(i-3<1?1:i-3); j<=i+6 && j<=NR; j++) {
          if (line[j] ~ /determine skill|skill match|capability match|verify capability|route|dispatch|identify capability/) disp=1
          if (line[j] ~ /human|peer|person|live|signer/) human=1
        }
        if (disp && !human) {
          printf "FAIL %s:%d  gate described with dispatch language and no human-authority word nearby\n", FNAME, i
          printf "       %s\n", substr(orig[i],1,96)
          hits++
        }
      }
      exit (hits>0 ? 1 : 0)
    }' "$tmp"
}

# --- Execute: a numbered procedure pairing a check step with an execute step ---
check_execute() {
  local f="$1" tmp="$2"
  awk -v FNAME="$f" '
    { line[NR]=$0; low[NR]=tolower($0) }
    END {
      hits=0
      for (i=1; i<=NR; i++) {
        if (low[i] !~ /^[[:space:]]*[0-9]+\.[[:space:]]*execute/) continue
        chk=0
        for (j=(i-4<1?1:i-4); j<=i+2 && j<=NR; j++) {
          if (j==i) continue
          if (low[j] ~ /^[[:space:]]*[0-9]+\.[[:space:]]*(check|verify|determine|identify)/) chk=1
        }
        if (chk) {
          printf "FAIL %s:%d  Execute as a numbered step beside a check step -> dispatch; drafting treated as execution\n", FNAME, i
          printf "       %s\n", substr(line[i],1,96)
          hits++
        }
      }
      exit (hits>0 ? 1 : 0)
    }' "$tmp"
}

for f in "${FILES[@]}"; do
  if [ ! -f "$f" ]; then
    say "FAIL $f: no such file"; FAIL=1; continue
  fi
  say "-- $f --"
  TMP=$(mktemp)
  strip_fences "$f" > "$TMP"

  for pair in "Path:check_path" "gate:check_gate" "Execute:check_execute"; do
    term="${pair%%:*}"; fn="${pair##*:}"
    OUT=$("$fn" "$f" "$TMP") && RC=0 || RC=$?
    if [ "$RC" -eq 0 ]; then
      say "OK   $term — no collision"
    else
      printf '%s\n' "$OUT"
      FAIL=1
    fi
  done
  rm -f "$TMP"
  say ""
done

say "== result: $([ $FAIL -eq 0 ] && echo PASS || echo COLLISIONS FOUND) =="
say "A collision is a term used two ways. Which use is wrong is a human's call."
exit $FAIL
