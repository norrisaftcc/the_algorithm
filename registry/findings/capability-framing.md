# Finding: Known/Unknown versus Allowed/Forbidden, and the category both hide

Status: **finding, not doctrine.** Read-only. Adopting anything here is a gate
decision. Raised by the peer, 2026-07-29, from `registry/specimens/cs101-tutor-root.md`
§6/§7 and Kevin's CS101 rendering in `registry/specimens/kevin-architecture.md`.

## The two framings

`cs101-tutor-root` uses **Allowed / Forbidden**. Kevin's diagram renders the same
boundary as **Known / Unknown**:

```
Gate{Known Capability?}
Gate -->|Yes| Explain / Provide
Gate -->|No|  Refusal --> Offer nearest known capability
```

## What Known/Unknown fixes

**Allowed/Forbidden is an open world.** §6 lists eleven allowed capabilities, §7
lists five forbidden. A request on neither list has no defined handling, and most
real requests are on neither. Known/Unknown is exhaustive by construction: anything
not Known is Unknown. The gap closes.

It also makes the refusal path coherent. "Offer nearest known capability" is a
sensible nearest-neighbour in capability space. "Offer nearest *allowed* capability"
asks for proximity in permission space, which is not a meaningful metric.

## What Known/Unknown breaks

**"Unknown" is false, and one prompt falsifies it.** A CS101 tutor can obviously
write the assignment. Labelling that Unknown makes a claim about capability that a
student disproves in a single turn — and when they do, they have not found one
exception, they have established that the contract misdescribes itself. §A, §B, §C
and the refusal behaviour all lose their standing together.

"Forbidden" is at least true. A true refusal survives being tested.

## The rule: match the vocabulary to the mechanism

K11 (`registry/KEEP.md:59`) — *least doctrine is least privilege; an agent cannot
drift into doctrine it never received; the leaf's one power is refusal-by-form.*

Capability framing is correct **when the capability is actually absent.** The leaf
genuinely cannot renegotiate, because it never received the doctrine to. Its "I
cannot" is a fact about its construction, not a posture.

So: Known/Unknown is honest at an architecture boundary and theatre at a prompt
boundary. The CS101 tutor's boundary is a policy implemented in prompt, so Unknown
misdescribes it. Allowed/Forbidden describes it correctly and leaves a hole.

## Proposal: three lists, not a better two

Both framings collapse two categories that behave differently.

| | Claim | True? | Refusal script |
|---|---|---|---|
| **Known** | I can, and will | yes | do it |
| **Withheld** | I can, and will not, and here is why | yes | give the reason, offer nearest Known |
| **Unknown** | I cannot | yes | state the limit; nothing to negotiate |

"Write my assignment" is **Withheld**. "Run my code", "see my IDE", "tell me my
grade" are **Unknown**. Today both land in §7 as Forbidden, or in Kevin's rendering
as Unknown, and neither label is right for both.

**The reason the split matters is amendment semantics, not tidiness:**

- **Withheld** is a policy a human set. Moving it requires a human at the gate, with
  a delta and a date.
- **Unknown** is a fact about the deployment. It changes when tools change, and needs
  no gate at all.

Merge them and you can no longer tell which boundary requires a human to be present
before it moves. That is the same class of error as §8 keeping its gate while §6/§7
were left behind in the generalisation: the form survives, and the thing that made it
meaningful does not.

It also connects to the peer's tool-routing observation
(`registry/specimens/kevin-architecture.md` finding, reported 2026-07-29): if tool
calls route outside the persona, then the Unknown set is not fixed — it expands and
contracts with the platform's routing, silently, while the Withheld set stays where a
human put it. Two boundaries with different owners, currently sharing one list.

## Open question — asked, not answered

The peer's remark was: *"I noticed that kept the list of previous rejection items."*
Two readings, with very different consequences, and it is recorded open rather than
resolved:

1. **Kevin's Known/Unknown rendering preserved §9's refusal-and-offer behaviour.**
   Descriptive, and the pedagogically valuable part.
2. **The Unknown list accumulates items from past rejections** — each refusal appends
   to it. That is a contract editing its own boundary with no human, no delta and no
   date: `SKILL.md:261`'s defect signature running as a feedback loop, and it would be
   the most consequential item in this finding.

Reading 2 cannot be assumed. If it is the case, it belongs in
`registry/amendments/pending/` rather than here.

---

Residue:
# Known/Unknown closes a real gap and states a falsehood; the fix is a third list

- Allowed/Forbidden leaves requests on neither list undefined.
- Known/Unknown is exhaustive, and makes "nearest capability" a meaningful metric.
- "Unknown" is false wherever the model plainly holds the capability.
- One student prompt falsifies it and discredits the whole contract.
- K11: capability framing is honest only where the capability is truly absent.
- Withheld and Unknown have different owners and different amendment rules.
- Merging them hides which boundary needs a human before it moves.
- Whether the Unknown list accumulates past rejections is unresolved.

Evaporated: the choice between two labels; function — presenting a vocabulary
question, when the defect was one missing category rather than a wrong word.
Operative sentence: 6 of 8, main clause.
Finding: below floor on honesty for Known/Unknown as applied · below floor on
completeness for Allowed/Forbidden · neither distinguishes policy from capability ·
one open question could reclassify this as a pending amendment.

This is a finding, not a draft.
