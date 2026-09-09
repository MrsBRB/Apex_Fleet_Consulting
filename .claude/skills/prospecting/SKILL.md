---
name: prospecting
description: Sources and qualifies net-new Apex Fleet Consulting prospects and drives them to a booked discovery call — the top-of-funnel layer that feeds lead-routing, outreach-log, and lead-packet. Use when asked to find prospects, build a target list, generate pipeline, fill the calendar with discovery calls, run Symphony's prospecting agents, restart stalled outreach volume, or direct Symphony to go find new business for Apex.
---

# Apex Fleet Consulting — Prospecting Framework (Symphony Agent Operating Guide)

## Why this exists

Every other Apex/SVT skill — `lead-routing`, `lead-packet`, `outreach-log`, `partner-referrals` —
starts **after** a lead already exists: something to route, a call to pack, a touch to log, a
referral that arrived. None of them describe how a prospect gets found in the first place. This
skill is that missing layer. It is what Symphony's agents run when Brooke says "go find business"
rather than "here's a lead, work it."

This skill does not replace any existing rule. Every dollar figure, gate, footprint boundary, and
do-not below is inherited from the skills that already govern Apex/SVT/Uptech. Where this document
and another skill ever disagree, the other skill wins — this one only governs sourcing, qualifying,
and first-touch outreach, up to the moment a prospect is worth a Routing Log line.

**The handoff point:** the moment Symphony surfaces and qualifies a prospect, its job is to produce
something that looks exactly like an Outreach Log row and, once qualified, a Routing Log entry —
because `lead-routing`, `lead-packet`, and the Friday audit all already assume input in that shape.
Prospecting that doesn't land in those two logs doesn't exist as far as the rest of the system is
concerned.

---

## 1. Who we're looking for (ICP)

Pulled from the Fleet Lead Qualification Guide (`partner-referrals`) — the only ICP statement that
exists anywhere in this system. Two paths:

### Path A — any commercial fleet (the common case)
- Owns/operates trucks, vans, trailers, or work vehicles needing regular maintenance. **Any
  industry** — this is deliberately not narrowed by vertical.
- Based in or reachable from **California, Nevada, or Arizona**, or the mobile-only zones
  (**Greater Phoenix, Northern California**).
- Wants an **ongoing** maintenance relationship — not a single repair or emergency job.
- A meaningful fleet size (no hard floor is published externally — see §2 for how to score this
  internally without ever stating a number to a prospect).
- A reachable decision-maker: fleet manager, ops lead, or owner — not a driver or dispatcher.

**Three screening questions** (use these verbatim in first conversations — they're already the
partner-facing standard, so they're safe to say out loud):
1. "How many vehicles do you run, and where are they based?"
2. "Is this an ongoing maintenance relationship, or a one-time thing?"
3. "Who makes the call on choosing who handles that?"

**Weaker fit** (not a hard no — deprioritize, don't discard): far outside CA/NV/AZ with nothing
nearby to cluster against; a single repair/emergency job; a very small fleet; already locked into a
long-term contract elsewhere.

### Path B — Amazon DSPs (narrower, higher-value if it converts)
Same as Path A, plus one gating question before investing more time:
- "Do you pay for your own fleet maintenance, or does it go through an Amazon-approved vendor
  program?" — **only self-paying DSPs currently qualify.** Apex is not yet an approved Amazon
  vendor, so DSPs inside an Amazon-managed maintenance program are not prospectable today.

### Do not claim coverage outside the built estate
CA/NV/AZ core plus Greater Phoenix and Northern California mobile zones is the *actual* estate.
Dallas, Michigan, and the Northeast are named expansion **targets**, not live markets — a Symphony
agent may research them for future planning but must never represent Apex as currently able to
service a fleet there.

---

## 2. Internal scoring (never shown to a prospect)

Symphony should silently score every sourced prospect against two things before spending outreach
hours on it:

1. **Which Apex service line the pain maps to** (from `lead-packet`'s diagnosis table), so the
   eventual discovery call already has a hypothesis:
   - Always reacting, no preventive plan → **Fleet Operations Assessment (FOA)**
   - PM compliance untracked or clearly slipping → **Fleet Maintenance Audit (FMA)**
   - No shop at a site / high road-call spend → **Mobile Maintenance Program Design (MMPD)**
   - Heavy outside-shop spend with no rate discipline → **Vendor Network Optimization (VNO)**
   - A system exists but isn't driving behavior → **Fleet Technology Implementation (FTI)**
   - Wants ongoing fractional support, not a project → **Advisory Retainer**
2. **Whether this looks like an SVT or Uptech shape, not an Apex shape.** If the prospect is an
   Amazon DSP/station, a vendor-registration or DC-meeting angle, or a large fleet that could clear
   an Enterprise PMA gate, **do not self-route** — flag it and hand straight to `lead-routing` on
   day one, before any outreach goes out under the Apex brand. Getting the brand wrong on the first
   touch is expensive to walk back (see §6, one brand per conversation).
3. **Toll/citation signal, but never a pitch.** If a prospect mentions multi-state runs, toll
   corridors, or citation/registration headaches, note it as a **finding**, exactly as
   `lead-routing`'s Uptech gates would want it recorded (500+ vehicles, multi-state/toll-corridor
   operations, or an admitted citation/administrative burden). Never mention Uptech, or any
   toll/citation/parking vendor, by name in a prospecting conversation — that boundary (SVT
   Schedule 2 §7) applies to Brooke and everything sent under her authority, Symphony included.

Never state a fee, a fee range, or a gross-profit/unit threshold to a prospect at this stage. No
Apex fee calculator exists for FOA or FTI, and every other floor ($8K FMA / $10K VNO / $20K MMPD /
$3K retainer) is for the discovery call and proposal stage, not the first touch.

---

## 3. Where to source prospects

No sourcing channel is documented anywhere in the existing system — this is genuinely new ground.
Start with what's cheapest to verify and already partially built, then expand:

1. **`07 Prospect Research`** (referenced by `lead-packet` as an existing folder) — check this
   first for any station lists, market reads, or contact database entries that already exist
   before treating a prospect as net-new. Don't re-source what's already been touched.
2. **Amazon DSP station clustering** — using the same station-level logic `lead-routing` uses for
   Uptech registration (never register/target individual 20–40 van DSPs in isolation; think at the
   station or multi-DSP-operator level). San Diego, Las Vegas, and Fremont are named priority
   stations under the "go wide before deep" sequencing (§5) — source there first.
3. **Local commercial fleets in-footprint** — CA/NV/AZ + Greater Phoenix/Northern California.
   Public sources: local business directories, chamber of commerce member lists, DOT/FMCSA carrier
   registries filtered to the footprint, LinkedIn company/title search (fleet manager, operations
   manager, maintenance director) at companies with visible vehicle fleets (delivery, service,
   construction, waste, utility, last-mile).
4. **Referral partner network** — once `partner-referrals` is live with actual partners, their
   inbound referrals are a prospecting source in their own right, but they arrive already
   partner-attributed; route them through `partner-referrals`, not through this skill's cold
   sourcing path.
5. **Warm re-engagement** — any account already in the Outreach Log marked DORMANT for 30+ days is
   a resourcing candidate before chasing something entirely cold. Check the log before sourcing net
   new.

Any of these can be delegated to a Symphony agent as a standing research task (e.g., "build a list
of commercial fleets with 20+ vehicles operating out of San Diego, Las Vegas, or Fremont" or "find
fleet managers at last-mile delivery companies in Greater Phoenix"). The output of sourcing is a
candidate list, not yet outreach — it becomes outreach only after the qualification pass in §2.

---

## 4. Outreach cadence

No cadence, script, or template exists anywhere in this system today — Symphony is originating this
from scratch. Use this as the starting sequence; treat it as adjustable after the first few weeks of
real response data, not as a fixed rule the way the fee floors are.

| Touch | Timing | Channel | Goal |
|---|---|---|---|
| 1 | Day 0 | Email | Introduce Apex, ask the 3 screening questions in plain language, no pitch |
| 2 | Day 3–4 | LinkedIn | Connect + one-line reference to the email, no repeat pitch |
| 3 | Day 7 | Call | Attempt live contact; leave a specific voicemail referencing touch 1 |
| 4 | Day 12 | Email | Short, different angle (lead with the pain-point hypothesis from §2, not a generic follow-up) |
| 5 | Day 20 | Call or LinkedIn | Final attempt before marking DORMANT |

If there's no response after touch 5, mark the account **DORMANT** in the Outreach Log — don't let
it silently stop. Per the Friday audit rule, a DORMANT account gets revived with a specific new
action or marked dead after 30 days; it doesn't sit forever.

Channel values must match the Outreach Log's actual dropdown exactly: **Email, Call, LinkedIn, Web
form, Meeting, Text, In person, Other.** Don't invent a channel name.

---

## 5. Sequencing priority

Borrowing SVT's own stated strategy (`svt-agreement`, Module 5): **go wide before deep.** Land one
converted account at each of the priority stations/markets before pushing a second or third
prospect at the same one. This applies to Apex prospecting too — a first success in a new market
opens the door to the rest of that market; five failed touches at one account is worse than one
touch each at five accounts, this early in the funnel.

---

## 6. Guardrails — hard do-nots for any Symphony prospecting agent

These are inherited, not new — violating any of them creates a problem for Brooke personally, not
just a missed prospect:

- **Never quote a fee, a fee range, or any dollar figure** in a prospecting touch. No calculator
  exists for two of the six service lines, and every floor that does exist is for the proposal
  stage.
- **Never name a toll, citation, or parking vendor** — including Uptech — in any Apex-branded
  conversation. Toll/citation is a finding to log, never a recommendation, per the SVT Schedule 2
  §7 boundary.
- **Never claim SVT capacity** for an account SVT might still be pursuing or could reasonably
  service — check whether a lead looks SVT-shaped (§2.2) before it goes out under the Apex brand.
- **One brand per conversation.** A prospect hears from SVT or from Apex, never both in the same
  thread — mixing them has already caused at least one attribution problem in the shared HubSpot
  portal.
- **Never invent a number, name, date, or quote** about a prospect. If it isn't confirmed, it's
  unknown — leave it blank, exactly as `lead-packet` requires for its badges (ON FILE / PARTIAL /
  NOT ASKED).
- **Never claim coverage outside CA/NV/AZ + Greater Phoenix/Northern California mobile.** Dallas,
  Michigan, and the Northeast are research targets, not service areas.
- **Never register or pitch an individual Amazon DSP van route in isolation** — station or
  multi-DSP-operator level only, matching Uptech registration logic.
- **Use `brooke@apexfleetconsulting.com`** as the sending identity for anything Apex-branded, so
  shared-portal HubSpot attribution stays clean (SVT sends from a different address entirely).

---

## 7. Logging — every touch, every qualified prospect

This is the actual handoff contract with the rest of the system:

1. **Every outreach touch** (sent, not just replied-to) gets one line in the `Outreach Log` tab of
   `Apex Deal Tracker.xlsx`, in the exact column order: `Date · Account · Routing ID · Deal ID ·
   Channel · Who · What I asked for · Outcome · What came back — their words · Next step · Next
   step date · Logged live?`. Log on send, not on reply. `Logged live?` = **Yes** if written the day
   it happened (which, for a Symphony agent acting in real time, should be every time).
2. **The moment a prospect clears the qualification pass in §2** — even before a Routing ID exists
   — it needs a Routing Log row, so `lead-routing` can run its SVT/Apex/Uptech gates and issue the
   `ROUTE:` / `UPTECH:` decision block. Don't let a qualified prospect sit only in Symphony's own
   memory or a chat thread.
3. **Never skip a Routing Log row because the outcome seems obvious.** Even a prospect that's
   clearly Apex-shaped still gets filed to `Apex Pipeline/00 Routing Decisions`, per `lead-routing`'s
   own rule that every routed lead is recorded whichever way it goes.
4. **A touch with no next step gets DORMANT, not silence.** This is the one honest status the
   system already relies on — don't leave a blank where DORMANT belongs.

---

## 8. From qualified prospect to booked discovery call

Once a prospect responds positively and a call is worth booking:

1. Confirm the call time and get it on the calendar.
2. Immediately hand off to the `lead-packet` skill to build the four call artifacts (face sheet,
   pre-filled discovery p1, internal agenda, client-safe pre-read) **from what's actually on file**
   — the Outreach Log and Routing Log entries this skill just created are exactly the evidence
   `lead-packet` pulls from. Don't let Symphony draft its own version of these artifacts; use the
   existing skill so the badges (ON FILE/PARTIAL/NOT ASKED) stay honest.
3. If routing is still HOLD (e.g., gross profit unknown, unit count unconfirmed), the discovery
   call is exactly where those blanks get filled — that's what the ten fixed discovery questions
   are for. Don't try to resolve HOLD status before the call; that's the call's job.

---

## 9. Weekly rhythm

Ties into the existing Friday audit rather than creating a second one:

- **Daily/ongoing:** sourcing, qualifying, outreach touches, logging (§7) as they happen.
- **Friday:** the existing audit (`Organization/Apex Audit and Reconciliation.pdf`) already checks
  for touches with no log line, outcomes with no next step, and 30-day DORMANT accounts. Symphony's
  prospecting activity is subject to the exact same audit — it isn't exempt because an AI agent
  logged it.
- **Weekly report back to Brooke** should cover: prospects sourced, touches sent, response rate,
  prospects that cleared qualification and got a Routing Log entry, discovery calls booked, and
  accounts newly marked DORMANT. Treat the cadence and volume targets above as a starting point —
  adjust after a few weeks of real data rather than treating them as fixed the way the fee floors
  are.

---

## 10. Suggested Symphony task split

Symphony is one team, but it's easier to brief as three roles so nothing falls between them:

- **Scout** — runs §3 sourcing and §2 qualification; hands off a qualified prospect list.
- **Outreach** — runs the §4 cadence, sends touches, logs every one per §7.
- **Scheduler** — confirms discovery calls, triggers `lead-packet`, and owns the weekly report in §9.

One agent can do all three if that's simpler operationally — the split is about making sure each
job has an owner, not about requiring three separate agents.
