# INDIGO edition — history-purge package

**Contract frozen:** 2026-07-31, by the signer's typed "freeze the INDIGO package, cost: one Monday morning }".
**Signer:** norrisaftcc (@uv). **Session:** week of 2026-08-03, delivered by one-shot trigger.
**Seat geometry:** purge writes are root's — history rewrite is an owner power. INDIGO reads,
files, and ENDs. No seat assays itself: the agent that verifies must not be the hands that rewrote.
**Standing rule:** every check emits its actual output. A checkmark without its check is unverified.
INDIGO re-derives the PII inventory fresh. It trusts no report from the session that wrote this file.

## Why this package exists

Two real-world artifacts were committed into public fiction repos and later deleted on branch:

- `underground/archive/outofcharacter/foundational_principles/angelas_notes.md` — real third-party
  correspondence with personal contact details. Present in BOTH repos, byte-identical.
- `BINDER_26SP_PARTIAL.zip` — a real employment-review binder. `norrisaftcc/algocratic` only.

Deletion landed on `main` via norrisaftcc/algocratic#80 (merged 2026-07-31). **Deletion does not
purge.** The blobs remain fetchable from history until the rewrite below is done and verified.

**Blob SHAs recorded at freeze (the fetch-must-fail targets):**

```
norrisaftcc/algocratic      cf70b8a:BINDER_26SP_PARTIAL.zip  a3004f9675b09318c8248c7bba9fc00c0836a7e8
norrisaftcc/algocratic      cf70b8a:...angelas_notes.md      1264f27286efa8b94982bef6a0d059dff6591ff2
algocratic/algocratic.github.io  f37d19d:...angelas_notes.md 1264f27286efa8b94982bef6a0d059dff6591ff2
```

## Runbook — in order

1. **DONE 2026-07-31.** PR norrisaftcc/algocratic#80 merged; `main` carries the deletions.
2. **Owner:** apply the delivered patch (`algocratic.github.io-lore-revival.patch`) to a clone of
   `algocratic/algocratic.github.io`, push, merge. The rewrite must not race a ref that still adds
   the file.
3. **Owner, per repo:** rewrite history. Fresh full clone (never shallow, never the working copy):
   ```
   git clone --no-local https://github.com/norrisaftcc/algocratic purge-algocratic
   cd purge-algocratic
   git filter-repo --invert-paths \
     --path BINDER_26SP_PARTIAL.zip \
     --path underground/archive/outofcharacter/foundational_principles/angelas_notes.md
   git remote add origin https://github.com/norrisaftcc/algocratic
   git push --force --all origin && git push --force --tags origin
   ```
   Repeat for `algocratic.github.io` with the notes path only.
4. **Owner:** GitHub retains unreachable objects and `refs/pull/*` until server-side GC. Open a
   support request to expire cached views and run GC on both repos. Check the fork network first;
   a fork retaining the blobs reopens this package with the fork named.
5. **INDIGO:** run every done condition below. Emit output. File the receipt.
6. **Owner + INDIGO:** consent checkpoint — before either artifact is ever re-added in any form,
   the named people consent in writing, or the artifacts are permanently out of scope. Redaction
   of a document whose whole subject is a real person is not a remedy.

## Done conditions — all mechanical, all four required

Run against fresh clones made AFTER the rewrite and GC.

1. **Object walk empty, both repos:**
   `git rev-list --all --objects | grep -Ei 'angelas_notes|BINDER_26SP'` → no output, exit 1.
2. **Old blob fetch fails, all three SHAs:** fetching each recorded SHA via the API or
   `git fetch origin <sha>` → refused / not found. Paste the refusal.
3. **Fresh-clone PII sweep empty, both repos:** phone-pattern and personal-email grep across the
   tree → no output outside fictional-domain allowlist. Paste the command and its empty result.
4. **Receipt filed:** `registry/findings/indigo-purge-receipt-<date>.md` carrying every command
   and its verbatim output, the runbook step timestamps, and the verifier's seat line.

## Fold-in: the sweeps still unrun

The 2026-07-31 disposition marked these UNRUN — nothing found is not checked:

- **Slur / extremist-language sweep** over all of `norrisaftcc/algocratic` (wordlist grep; every
  hit manually adjudicated; counts and dispositions emitted).
- **Third-party art provenance** — inventory image/video/zip assets in both repos; note origin or
  mark unknown. Unknown is a finding, not a pass.

## END rule

Any failed condition: emit "Failed on [item]. Contract reopened." — file the receipt with the
failure in it, stop, and do not patch mid-flight. There is no third side.
