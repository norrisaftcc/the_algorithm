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

## Open question — CLOSED by the peer, 2026-07-29

The remark was *"I noticed that kept the list of previous rejection items."* Reading 1
is correct: the peer confirms the rendering **did not delete the list, it renamed it.**
The rejection items survived; only the label changed. There is no self-amending
feedback loop, and no pending amendment is owed.

That makes the whole question a vocabulary substitution over an intact payload — which
is the same shape as `Path` and `gate` in
`registry/specimens/universal-contract-ancestor.md`: the content held, the word moved.
Third instance in this chain.

## The routing argument, and where it holds

The peer's reasoning, offered with `Capable / Incapable` as a further rename:

> The most helpful thing they could do is report back incapable to save wasted effort.
> If a tool can't do what you want then it's invoked will invoke another one.

**This is correct, and it reconstructs canon's leaf design from first principles.**
A fast, honest incapability report is the highest-value output a leaf can produce: it
lets the caller stop spending and re-route. That is exactly what
`"Failed on [item]."` is for, and it is why K11 (`registry/KEEP.md:59`) says the
leaf's one power is refusal-by-form. The peer arrived at the same mechanism from
routing efficiency rather than from doctrine.

**Where it fails is the seam this finding already named.** For routing, "I cannot" and
"I will not" are not interchangeable:

| signal | correct orchestrator response |
|---|---|
| **Incapable** | route elsewhere; retrying here is waste |
| **Withheld** | do **not** route elsewhere; the boundary is the point |

"If a tool can't do what you want, it will invoke another one" is right for
incapability and catastrophic for withholding. Label the academic-integrity boundary
`Incapable` and the routing layer treats a policy as a capacity shortfall — then shops
around until it finds an agent that complies. The frame does not merely misdescribe
the boundary; it instructs the system to circumvent it.

`Capable / Incapable` is therefore **worse than Known / Unknown** for this purpose,
because it is a more explicit capacity claim, and capacity claims are re-routable by
design.

## "Is the agent within a contract part important?" — yes, and it is the whole hinge

The contract is what makes a refusal **bind the caller** instead of merely informing
it. Outside a contract, an agent's refusal is a capacity report and the orchestrator is
free to route around it. Inside one, the refusal returns the *contract* to negotiation,
and re-dispatching to a different agent is not an available move.

Canon already encodes this, in the second sentence of a fixed string:

```
"Failed on [item]. Contract reopened."
```

**"Contract reopened." is the anti-routing clause.** It says the work does not go
looking for a more willing executor; it goes back to the negotiation side, where a
human is.

### Which makes the two-form divergence decidable

`registry/specimens/ASSAY-of-specimens.md` recorded that the failure string exists in
two forms:

```
SKILL.md:25                     "Failed on [item]. Contract reopened."
editions/mechanics-card.md:12   "Failed on [item]. Contract reopened."
editions/leaf-template.md:17    "Failed on [item]."
```

Read through the routing argument, that is not sloppiness — it is precisely the
Withheld/Incapable distinction, already present in the editions and never labelled. A
leaf emitting the short form **informs**: this is a capacity report, re-dispatch is
permitted. An executor emitting the long form **binds**: reopen the contract, do not
shop around.

If that is intentional, it is the most important undeclared design decision in the
repository and it should be stated. If it is not intentional, then leaves currently
emit re-routable refusals for policy boundaries, which is the defeat described above.

Either way it is now a decision rather than an inconsistency, and it needs the gate.

---

Residue:
# Incapability reporting is the right instinct; the contract is what stops it re-routing

- The rename kept the rejection list. No self-amending loop exists. Question closed.
- A fast incapability report is the highest-value output a leaf can give: it stops spend.
- That reconstructs "Failed on [item]." from routing efficiency rather than doctrine.
- For routing, "I cannot" and "I will not" demand opposite responses.
- Incapable means route elsewhere. Withheld means routing elsewhere is the failure.
- Labelled Incapable, a policy boundary instructs the orchestrator to circumvent it.
- Capable/Incapable is worse than Known/Unknown: a plainer capacity claim, more re-routable.
- "Contract reopened." is the anti-routing clause, and answers the peer's own question.
- The leaf/executor two-form divergence is that distinction, present and undeclared.

Evaporated: the difference between a refusal that informs the caller and a refusal that
binds it; function — treating every boundary as a capacity fact, which is the one framing
a routing layer is built to work around.
Operative sentence: 6 of 9, main clause.
Finding: the routing premise is above the floor and independently rediscovers canon's
leaf mechanism · the vocabulary is below it, because a capacity claim is re-routable by
construction · one undeclared design decision in the editions now decidable · erosion
direction toward the orchestrator's convenience.

This is a finding, not a draft.
