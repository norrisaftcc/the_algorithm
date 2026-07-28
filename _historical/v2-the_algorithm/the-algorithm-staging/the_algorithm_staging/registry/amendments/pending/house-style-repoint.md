# Pending amendment: house-style-repoint

**Target:** SKILL.md → Invariants → Language lock
**Status:** pending — unnumbered until frozen
**Resolves:** K16 — the supply-chain dependency on an external, licensed, versioned specification referenced by URL.

## Proposed change (full text)

Replace the line:

> Spec: https://www.asd-ste100.org/

with:

> House style: HOUSE-STYLE.md in this repository, vendored and hashed. ASD-STE100 is recorded there as upstream supplier; imports occur by diff and amendment.

All other Language lock rules are unchanged — they were already self-contained; only the pointer was the dependency.

## Rationale

No license was ever signed; the supplier can change terms; the URL can rot; the spec can revise underneath the invariant. Vendoring the enforced subset converts an external authority into an internal artifact under the repository's own hashing and amendment discipline.
