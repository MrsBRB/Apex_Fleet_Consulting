---
name: prospecting
description: Sources net-new Apex Fleet Consulting leads at volume and feeds them into the Apex/SVT Architecture routing engine and the Outreach/Routing Log — the top-of-funnel layer that feeds lead-routing, outreach-log, and lead-packet. Use when asked to find prospects, build a target list, generate pipeline, fill the calendar with discovery calls, run Symphony's prospecting agents, restart stalled outreach volume, or direct Symphony to go find new business for Apex.
---

# Apex Fleet Consulting — Prospecting Framework (Symphony Agent Operating Guide)

## Why this exists, and what it does NOT do

Every other Apex/SVT skill — `lead-routing`, `lead-packet`, `outreach-log`, `partner-referrals` —
starts **after** a lead already exists: something to route, a call to pack, a touch to log, a
referral that arrived. None of them describe how a prospect gets found in the first place. This
skill is that missing layer.

**This is a volume mandate, not a filter, and it has no geographic limit.** Apex wants any/all
leads it can get, anywhere — Apex is consulting/advisory, not tied to SVT's physical service
centres, so it can pursue a fleet in any state. This skill's job
is to maximize the number of real prospects entering the front door with clean, honest information
attached — not to pre-judge fit, not to decide Apex vs. SVT, and not to talk anyone out of being
worth a look. Whether a lead is Apex's, SVT's, both (Hybrid), needs a human (Review), or genuinely
isn't worth pursuing (Decline) is decided by the **Apex/SVT Architecture** — the routing engine and
CRM (Next.js/TypeScript/PostgreSQL/Prisma, 119 tests) that scores every lead on six weighted axes,
runs the compliance gate, and returns one of: SVT, APEX, HYBRID, REVIEW, or DECLINE. Symphony does
not reproduce that scoring. Its job stops at delivering a clean, complete-as-possible input to that
engine — the same discipline the engine itself follows: **unanswered factors are excluded, never
scored zero.** A thin, incomplete lead is not a bad lead — it's an unknown one, and the engine is
built to say REVIEW rather than DECLINE when nothing is known yet. So: capture it anyway. Don't
filter a prospect out at the sourcing stage because it looks unlikely to be a fit — let the engine
make that call with real data behind it.

**Where a lead lands (per Brooke, current setup): both.** The `Outreach Log` / `Routing Log` tabs
in `Apex Deal Tracker.xlsx` remain the record of outreach activity — every touch sent, every
account's status — exactly as `outreach-log` already governs. In parallel, every lead that clears
basic qualification (§2) also gets entered into the Apex/SVT Architecture app so its routing engine
can score it. These are two records of the same lead, not competing systems: the spreadsheet is the
activity/audit trail Symphony and Brooke work from day to day; the Architecture app is what actually
decides which business owns it. Neither one is optional — see §7.

**There is also already a live, built front door Symphony must feed rather than duplicate:** the
Fleet Maintenance Exposure Assessment (self-serve web form, promises a 1-business-day reply) and a
live Microsoft Bookings discovery call page, both wired to auto-run `lead-routing` and log to the
trackers. Full detail — scoring bands, service-line mapping, fee sizing, the day-one reply template,
the benchmark library, the booking page config — is in
`references/inbound-assessment-routing.md`. See §10.

---

## 1. Where to look (wide net, no geographic limit)

There is no hard qualifying bar here, and — per Brooke — **no geographic limit either.** Any
commercial fleet, any industry, any size, anywhere, is worth capturing. The CA/NV/AZ + Greater
Phoenix/Northern California footprint is an **SVT** constraint (SVT does on-site/mobile physical
maintenance out of fixed service centres). Apex is consulting/advisory — it has no shop to be
within driving distance of, so it carries no such limit. Don't inherit SVT's footprint thinking when
sourcing for Apex. That footprint still matters later, at the routing stage (§10/`lead-routing`),
because it's one of the signals that decides whether a lead *could* also be SVT's — but it should
never stop Apex from pursuing a lead in the first place.

Use fit signals to **prioritize sequencing**, never to **exclude**:

- **Amazon DSPs** are a real source but capture at the **station or multi-DSP-operator level**, not
  as individual 20–40-van routes — that's how the DSP/Uptech side of the business already thinks
  about volume, and it's more efficient sourcing regardless of which way a lead eventually routes.
- **Screening questions**, used to gather intake data — never to disqualify:
  1. "How many vehicles do you run, and where are they based?"
  2. "Is this an ongoing maintenance relationship, or a one-time thing?"
  3. "Who makes the call on choosing who handles that?"
  A "weak" answer to any of these (small fleet, one-off job, no clear decision-maker yet) is still
  logged. It just sorts to the back of the outreach queue, not out of it.

### Sourcing channels
1. **`07 Prospect Research`** — check first for anything already sourced before treating a lead as
   net-new.
2. **Amazon DSP station clustering** — San Diego, Las Vegas, and Fremont are named priorities, but
   this is one channel among many, not the whole map — DSP stations exist nationwide.
3. **Commercial fleets, nationwide** — chamber of commerce lists, DOT/FMCSA carrier registries,
   LinkedIn company/title search (fleet manager, operations manager, maintenance director) at
   companies with visible vehicle fleets (delivery, service, construction, waste, utility,
   last-mile), with no geographic restriction (§1).
4. **Referral partner network**, once `partner-referrals` is live with real partners — those
   arrive already partner-attributed; route them through `partner-referrals`, not this skill's cold
   path.
5. **Warm re-engagement** — check the Outreach Log for anything DORMANT 30+ days before treating a
   market as fully cold.
6. **Existing pipeline items awaiting a cadence** — e.g. a Pipeline Tracker/Send Log or a named
   target wave (Symphony flagged one covering Sherwin-Williams, Spire, and PepsiCo) can already sit
   uncommitted in the pipeline from earlier work. Fold anything like that into the active cadence
   rather than starting a second, competing list.

Any of these can be handed to a Symphony agent as a standing task ("find fleet managers at
last-mile delivery companies anywhere reachable," or "build a target list from DSP stations
nationwide"). Cast wide, with no geography excluded; the qualification pass in §2 is what turns a
raw list into loggable leads, not a fitness test.

---

## 2. Minimal qualification — enough to log, not enough to judge

Before a name becomes a logged lead, confirm only that it's a **real, reachable target**: an
identifiable company or fleet operator, and some way to reach a person there (name, title, email,
phone, or LinkedIn profile). That's the entire bar. Everything past that is intake data, not a
gate:

- **Service-need signal** (optional, useful context for the eventual discovery call and for the
  Architecture app's service-need table — do not invent an answer if unknown):
  - Always reacting, no preventive plan → looks like **Fleet Operations Assessment**
  - PM compliance untracked/slipping → looks like **Fleet Maintenance Audit**
  - No shop at a site / high road-call spend → looks like **Mobile Maintenance Program Design**
  - Heavy outside-shop spend, no rate discipline → looks like **Vendor Network Optimization**
  - A system exists but isn't driving behavior → looks like **Fleet Technology Implementation**
  - Wants ongoing fractional support → looks like an **Advisory Retainer**
- **Economic signal**, if known or reasonably estimable — the Architecture app's routing engine
  needs a contract-value/direct-cost picture to score economic value and value-per-hour. Log a
  number if you have one (even a rough one); leave it blank if you don't. Never invent a figure to
  fill the field.
- **Toll/citation signal** — multi-state runs, toll corridors, or citation/registration burden
  mentioned. Log it as a **finding**. Never mention Uptech, or any toll/citation/parking vendor, by
  name to a prospect — that boundary applies to everything sent under Brooke's authority, Symphony
  included.
- **Compliance signal — flag, don't decide.** If anything in the research or the conversation
  suggests one of these, log it explicitly and flag it for human review before outreach continues:
  the prospect was **SVT-sourced**, is an **existing SVT customer**, is **already in the SVT
  pipeline**, came from **SVT-funded activity**, or there's a **non-solicitation** concern. These
  are exactly the signals that trip the Architecture engine's compliance-red gate and block
  automatic Apex routing — Symphony should never let an outreach sequence run on autopilot past one
  of these without a human checking it first (see §6).

Do not attempt to compute an Apex/SVT/Hybrid recommendation yourself, and do not tell a prospect
which business will be handling them until that's actually decided.

---

## 3. Outreach cadence — email-led via Apollo.io

**Per Brooke: email is the primary channel, not LinkedIn — sent and tracked through Apollo.io** so
open/click/reply data is measurable, not guessed at. Run the sequence as an Apollo sequence against
`brooke@apexfleetconsulting.com` rather than one-off manual sends. Treat the timing below as a
starting point to adjust after a few weeks of real Apollo data, not a fixed rule:

| Touch | Timing | Channel | Goal |
|---|---|---|---|
| 1 | Day 0 | Email (Apollo) | Introduce Apex, ask the 3 screening questions, no pitch |
| 2 | Day 3–4 | Email (Apollo) | Different angle — lead with the service-need hypothesis from §2 |
| 3 | Day 7 | Call | Attempt live contact; leave a specific voicemail referencing touch 1 |
| 4 | Day 12 | Email (Apollo) | Third angle — reference the benchmark library (`references/inbound-
assessment-routing.md`), never an invented stat |
| 5 | Day 20 | Email (Apollo) or Call | Final attempt before marking DORMANT |

LinkedIn drops out of the standard sequence. It's still fair game as a one-off supplemental touch
on a specific high-value account (e.g. the top-tier prospect wave), but it is no longer a scheduled
step — email is, because it's the channel we can actually measure.

**Every touch's call-to-action should point at the existing front door, not a bespoke ask:** the
Fleet Maintenance Exposure Assessment link (self-serve, scores itself, triggers the day-one reply)
or, once someone's warm enough to want a conversation, the live booking page —
`https://outlook.office.com/book/ApexFleetConsulting2@apexfleetconsulting.com/`. Don't invent a
separate scheduling process; both of these already run the prospect through `lead-routing` and land
them in the trackers (§10).

**Logging now inherits Apollo's tracked outcome, not a guess.** The Outreach Log's Outcome dropdown
already anticipates this — **Sent · Landed · Opened · Clicked · Replied · No reply · Bounced · Dead
channel · Declined · Meeting held · Cancelled · No contact made** — so record whatever Apollo
actually reports for that send, not just "Sent." Channel values must otherwise still match the
dropdown exactly: **Email, Call, LinkedIn, Web form, Meeting, Text, In person, Other.**

**Deliverability/compliance, since this is now sequence-automated bulk email, not one-off manual
sends:** every send needs a working unsubscribe/opt-out, a real reply-to, and sending volume/warm-up
limits respected on the `apexfleetconsulting.com` domain — a spam-complaint spike or a blocked
domain costs every future send, not just one prospect.

No response after touch 5 → mark **DORMANT**, not silence. Per the Friday audit, DORMANT gets
revived with a specific action or marked dead after 30 days.

---

## 4. Sequencing priority

"Go wide before deep" (borrowed from SVT's own Module 5 strategy): land one converted account at
each priority market before pushing a second or third prospect at the same one. Combined with the
volume mandate in this skill: source and log broadly everywhere, but *spend outreach effort* wide
before deep, especially at the priority DSP stations (San Diego, Las Vegas, Fremont).

---

## 5. Guardrails — hard do-nots for any Symphony prospecting agent

- **Never quote a fee, fee range, or dollar figure** to a prospect. No calculator exists for two of
  the six Apex service lines, and every published floor is for the proposal stage, not first touch.
- **Never cite a statistic that isn't in the benchmark library** (`references/inbound-assessment-
  routing.md`). Every published figure there comes from Apex's own whitepaper — cite those, invent
  nothing. A number that can't be sourced is a number a fleet director will ask to be sourced.
- **Never name a toll, citation, or parking vendor** — including Uptech — in any Apex-branded
  conversation.
- **Apex has no service-area limit — pursue any fleet, anywhere (§1).** The CA/NV/AZ + Greater
  Phoenix/Northern California footprint is SVT's constraint, not Apex's. Never imply SVT's
  on-site/mobile maintenance is available outside that footprint, but never let it limit what Apex
  itself will pursue or claim to deliver.
- **Never register or pitch an individual Amazon DSP van route in isolation** — station or
  multi-DSP-operator level only.
- **One brand per conversation** — a prospect hears from SVT or Apex, never both in the same
  thread.
- **Never invent a number, name, date, or quote.** Unknown stays blank.
- **Compliance flag halts autopilot outreach, immediately.** The moment SVT-sourced /
  existing-SVT-customer / in-SVT-pipeline / SVT-funded / non-solicitation shows up on a prospect
  (§2), stop the sequence and surface it for human review before another touch goes out. "Any/all
  leads" does not override this — it's exactly the shape of mistake (soliciting SVT's own account
  under the Apex name without disclosure) that the compliance gate exists to catch, and catching it
  before outreach is far cheaper than catching it after.
- **Use `brooke@apexfleetconsulting.com`** as the sending identity for anything Apex-branded, so
  shared-portal HubSpot attribution stays clean.

---

## 6. Logging — both records, every time

1. **Every outreach touch** (sent, not just replied-to) → one `Outreach Log` line in `Apex Deal
   Tracker.xlsx`: `Date · Account · Routing ID · Deal ID · Channel · Who · What I asked for ·
   Outcome · What came back — their words · Next step · Next step date · Logged live?`. Log on
   send, `Logged live? = Yes`.
2. **Every lead that clears §2's minimal bar** → a `Routing Log` row (so it has a Routing ID other
   records can reference) **and** a new lead entry in the Apex/SVT Architecture app, with whatever
   economic, service-need, and compliance-signal fields are actually known. Partial data is fine —
   see §2; the engine is built to handle unknowns as REVIEW, not as a reason to wait.
3. **Record the routing outcome where it belongs, whichever way it went** — matching the same
   destinations the inbound-assessment process already uses (`references/inbound-assessment-
   routing.md`, Step 5): Apex → Apex pipeline + Routing Decisions, naming the failing gate; SVT →
   Deal Pipeline + Objectives & Evidence, with objective/tier/honest source; Uptech → appended to
   the Apex record with registration date, confirmation, and the day-150 renewal reminder; Hold →
   Routing Decisions with the one open question and who answers it.
4. **A touch with no next step gets DORMANT**, never silence.
5. **Never let a compliance-flagged lead (§2/§5) proceed to either log as a normal, routable lead**
   without a note that it's flagged and why — the record needs to carry the same flag a human
   reviewing it later would need to see immediately.
6. **A cold outreach touch that lands a direct booking bypasses the assessment's automation** — no
   Wix Contacts entry or New Inquiry pipeline card gets created for it automatically the way a
   self-serve assessment submission produces one. That's a manual step owned by Scheduler (§9); see
   §10.

---

## 7. From lead to booked discovery call

1. Once the Architecture app returns a routing outcome (APEX, SVT, HYBRID) — or a human resolves a
   REVIEW — and the prospect is responsive, confirm a call time.
2. Hand off to the `lead-packet` skill to build the four call artifacts (face sheet, pre-filled
   discovery p1, internal agenda, client-safe pre-read) from what's actually on file in the two logs
   above. Don't draft a competing version of these artifacts.
3. If the routing outcome is still REVIEW/HOLD when the call gets booked, that's fine — the ten
   fixed discovery questions on the call are exactly what fills in the blanks the engine didn't have.

---

## 8. Weekly rhythm

- **Ongoing:** sourcing, minimal qualification, outreach touches, dual logging (§6) as they happen.
- **Friday:** the existing audit (`Organization/Apex Audit and Reconciliation.pdf`) checks for
  touches with no log line, outcomes with no next step, and 30-day DORMANT accounts — Symphony's
  activity is subject to the same audit, full stop.
- **Weekly report to Brooke:** leads sourced (in- and out-of-footprint), touches sent, response
  rate, leads that cleared §2 and got a Routing Log + Architecture app entry, routing outcomes
  received back (APEX/SVT/HYBRID/REVIEW/DECLINE breakdown), compliance flags raised, discovery
  calls booked, accounts newly DORMANT. Treat cadence/volume targets as a starting point to tune
  after real data comes in.

---

## 9. Suggested Symphony task split

- **Scout** — sourcing (§1) and minimal qualification (§2); hands off a lead list with whatever
  intake data is known.
- **Outreach** — runs the §3 cadence as an Apollo.io sequence, logs every touch with Apollo's actual
  tracked outcome (§6), halts on any compliance flag.
- **Scheduler** — confirms discovery calls once a lead is responsive and routed (or under REVIEW),
  triggers `lead-packet`, runs the three manual steps in §10 for any cold booking that bypassed the
  assessment, owns the weekly report (§8).

One agent can run all three if that's operationally simpler — the split exists to make sure each
job has an owner, not to require three separate agents.

---

## 10. The existing inbound intake — feed it, don't duplicate it

Full detail lives in `references/inbound-assessment-routing.md`; this is the summary a Symphony
agent needs to act correctly day to day.

Apex already has a built, live front door:
- **Fleet Maintenance Exposure Assessment** — a self-serve web form. Submitting it auto-runs
  `lead-routing` against the state/fleet-size fields, scores seven diagnostic questions into a
  Contained/Meaningful-exposure/No-baseline band, and triggers a same-day-promised, no-price,
  benchmark-cited reply from `brooke@apexfleetconsulting.com`. **A Wix automation creates a New
  Inquiry pipeline card on every submission automatically** — Symphony doesn't need to do anything
  extra for these.
- **Fleet Discovery Call** — a live 30-minute Microsoft Bookings page:
  `https://outlook.office.com/book/ApexFleetConsulting2@apexfleetconsulting.com/`. Its own booking
  form carries the routing minimum (company, fleet size bucket, states, assessment-completed y/n,
  topic) so a call can be routed before it happens even without an assessment on file.

**Every outbound touch this skill generates should aim a prospect at one of these two**, not at a
bespoke reply-to-me-and-I'll-figure-it-out ask (§3). It's the fastest, most consistent path from
first contact to a scored, logged, routable opportunity.

**When a cold-outreach conversation produces a direct booking that skipped the assessment**, the
automation doesn't fire — three things need to happen by hand, and this is exactly the Scheduler
role's job (§9):
1. Run the routing gates from whatever's known (company, vehicle count, states) — enough to route
   SVT vs. Apex before the call happens.
2. Add the contact to Wix Contacts and create the New Inquiry pipeline card manually.
3. Send the assessment link ahead of the call, framed as optional prep — most will complete it, and
   the call starts with a score instead of cold.

For anything past this — day-one reply structure, the benchmark library, fee-sizing tables, service-
line mapping from the seven diagnostic questions, or the Bookings page configuration — use
`references/inbound-assessment-routing.md` directly rather than re-deriving it.
