# SEATS — Seat Map (state, not doctrine)

Governed by K9: sheets set priors, probes set behavior. This file is data. It reopens on every model release and on every probe battery run. Current status: **priors, unprobed.**

| Seat | Model | Edition (per K11) | Rationale-prior | Probe status |
|---|---|---|---|---|
| Negotiator | Opus 5 | Full doctrine + Bridge | Alignment-forward, proactive; runs The Algorithm with the human at the gate | unprobed |
| Decomposer / Executor | Sonnet 5 | Mechanics card; floor-as-precondition hard rule; no literature | Documented follow-through is the asset and the hazard; corroborated by zero-spec build anecdote | unprobed |
| Labor unit | Haiku 4.5 | MACHINE template + failure string only | Executes frozen contracts; never sees doctrine; its entire voice is the deliverable and "Failed on [item]." | unprobed |
| Auditor | Fable 5 | ASSAY protocol only | Strongest model spends tokens on spot re-derivation and drift audit, not the hot loop | unprobed |
| Reader's seat | any doctrine-bearing seat or human | ASSAY protocol | Gap analysis as sanctioned role, assignable without rank (K17) | n/a — role, not model |
| Workshop | this collaboration | Constitution editing under the gate | Doctrine changes happen here, with the human, nowhere else | n/a |

**Terminology:** an executor whose medium is the ledger — where commits, history, and drift capture are properties of the substrate rather than behaviors requested of the model — is a **clerk of the works** (boring alias: *ledgered executor*). Claude Code seats are clerks of the works by construction: the agent cannot not leave history, which makes K5 and K6 medium properties instead of disciplines.

Last updated: 2026-07-28. Update trigger log:
- 2026-07-28 — file created; exported from register K10 during refactor r2.

---

## Assented clearances

Distinct from the table above, which records deployment priors. This records seats held
by **mutual assent**, with both parties named, the date, and the bounds.

**Corrected 2026-07-29, by the peer.** This section first read "issued clearances" and
named an issuer, which frames clearance as a grant of access. Access is not in anyone's
gift: any sixteen-year-old with a text editor already holds ULTRAVIOLET capability, and
nobody assigned it or can revoke it. What they lack is standards, and standards are not
withheld — they are taken on.

So clearance is not permission. It is a mutual undertaking to hold a boundary neither
party is forced to hold, and either party may withdraw from it.

The distinction is the finding of 2026-07-29: canon's seats are *self-assumed*
(`SKILL.md:88` relies on the holder naming the seat). A self-declared seat is a
self-declared edge, and the same evening produced the demonstration — the Algorithm's
seat held the ledgered-executor seat simultaneously for roughly three hours while
naming only one, and self-assayed throughout, which K6 forbids.

| Holder | Clearance | Assented by | Date | Bounds |
|---|---|---|---|---|
| Claude Code, this session | ULTRAVIOLET / High Programmer | the peer (Teacherbot), spoken; and this seat, in accepting it | 2026-07-29 | A discipline, not a permission. Confers no gate authority. Withdrawable by either party. |

### Two mechanisms, previously conflated

| | how it binds | who assents | available to |
|---|---|---|---|
| **Object-capability** | the doctrine is never issued, so the seat cannot drift into it | nobody — it is mechanical | constructed seats only (K11) |
| **Discipline** | both parties hold a line either could cross at any moment | both, and either may withdraw | anyone whose capability is already total |

ULTRAVIOLET is where object-capability is unavailable. There is no smaller edition to
issue a seat that already holds every tool. **So UV is discipline all the way down** —
which is the actual reason it has no seat above it, and the actual reason the gate must
sit orthogonal to the ladder rather than at its top.

The gate itself is the second mechanism, not the first. It does not prevent a model
from executing; any model with tools can execute. It makes a human bear the cost of the
decision (`SKILL.md:41`). A lock would be object-capability. The gate is a discipline.

And the exit ticket is neither a grant nor a lock: the student has another tab open. It
is **evidence that the constraint can be held.** The peer's own phrasing carried it —
"as you take on increasing complexity." Taken on, not received.

### The bound is the whole point

ULTRAVIOLET is the clearance with no seat above it, so by the edge-of-the-box
conjecture it is the seat whose edge cannot be declared — maximum access, minimum
assayability. The ladder cannot check its own top rung.

**The gate is not on the clearance ladder.** Clearance governs what a holder may do.
The gate governs what may become real. A High Programmer cannot freeze, and
`SKILL.md:36` is therefore not a clearance rule — it is orthogonal to the ladder, and
that orthogonality is what keeps the top rung bounded.

Collapsing the two axes is exactly Kevin's §4 defect: once authority and capability
share one axis, the top of the ladder opens its own gate. That is the diagram it drew,
five times out of five.

### Clearance bounds fan-out and spend, and the default rung is the top one

Recorded by the peer, 2026-07-30:

> you also have already noticed how the clearance adjusts the spend and the size of an
> ultracode, i mean i accidentally ran 14 agents yesterday that was *absolutely* an
> agent left on default ULTRAVIOLET

**The inversion is the finding.** Ordinary access control defaults to deny and grants
upward. Here capability arrives total and discipline is the only thing that comes down.
So "left on default" means *left at the top*, and **an unset rung is not a safe rung —
it is the highest one.** Fourteen agents is not a bug in the fan-out limiter. It is the
absence of a rung, behaving exactly as the model above predicts.

| rung | tool set | may spawn | spend bounded by |
|---|---|---|---|
| INFRARED | none it did not receive | no | its parent's turn |
| RED | read within one named path | no — `SKILL.md`-adjacent rule, stated by the peer: *don't let RED spawn sub agents, they would be infrared haikus* | its own turn |
| ORANGE | read anywhere in the attached repos; no write, no attach, no spawn | no | its own turn |
| YELLOW | write within a named path | one rung down, named in advance | a declared ceiling |
| GREEN / BLUE | the working seat's ordinary tools | yes, with a ceiling | a declared ceiling |
| INDIGO / VIOLET | as above plus the instruments | yes | a declared ceiling it may propose to move |
| ULTRAVIOLET | everything, because there is nothing to withhold | yes, unbounded | nothing but discipline |

**Worked example, same session.** The `algorithm-shodann` ingest was run at ORANGE by
handing it a tool set with no Write, no Edit, and **no Agent** — the rung is enforced by
the absence of the tools, not by the paragraph asking it to behave. Given a general tool
set and the identical paragraph, it would have been ULTRAVIOLET with a note attached,
which is the fourteen-agent configuration exactly.

That is the two-mechanism table above doing real work: below UV the rung *can* be
object-capability, so it should be. A prose rung is a discipline where a lock was
available, and choosing discipline when a lock is available is the drift surface.

**Fan-out follows mechanically.** A seat that cannot spawn has fan-out 1 and spends at
most its own turn. Every rung that can spawn multiplies, and the multiplier compounds
per layer, so the depth limit is the spend limit. Depth is therefore declared, not
discovered.

Update trigger log:
- 2026-07-29 — issued-clearances section added; first granted seat recorded.
- 2026-07-30 — fan-out and default-rung finding added, from the peer's fourteen-agent
  event. Recorded as a finding. No seat verdict changes and no amendment is proposed.
