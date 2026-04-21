# Research Plan: Trial-to-Paid Conversion Drop-off

**Date:** 2026-04-06
**Researcher:** UX Research (GTeam)
**Status:** Ready for review

---

## 1. Research Question

**We need to understand** why trial users who engage with the product during their trial period do not convert to a paid plan, **so we can decide** which friction points, value gaps, or expectation mismatches to address in order to increase trial-to-paid conversion rate.

**Decision this research serves:** Product and growth teams will use findings to prioritise changes to the trial experience, onboarding flow, pricing page, and feature gating strategy for the next two quarters.

**Decision deadline:** Findings needed within 6 weeks of kickoff.

---

## 2. Background Assumptions to Validate

Before designing solutions, we need to determine which of these common conversion blockers actually apply:

| # | Assumption | Signal if True |
|---|---|---|
| A1 | Users don't reach the "aha moment" during the trial | Low engagement with core features in analytics; interviews reveal confusion about what the product does |
| A2 | Users find value but perceive the price as too high relative to alternatives | Users describe the product positively but cite cost; willingness-to-pay probing reveals a gap |
| A3 | Users hit a feature wall (need something gated behind paid) at the wrong time | Support tickets or churn surveys mention specific missing features; task completion drops at gate points |
| A4 | Users solve their immediate problem during the trial and don't need ongoing access | Usage spikes early then drops; interviews reveal one-time use cases |
| A5 | The transition from trial to paid is confusing or friction-heavy | Usability testing reveals drop-off on pricing/checkout flow |
| A6 | Users aren't sure what changes when the trial ends | Interviews reveal uncertainty about what they lose; pricing page doesn't clearly communicate trial vs paid |

---

## 3. Method Selection

This is a "why" question requiring mixed methods. We'll run three sequential phases:

### Phase 1 — Behavioural Analytics Review (Quantitative)
**Purpose:** Identify where in the trial journey users disengage, and segment churned trial users into behavioural clusters before talking to them.

**Activities:**
- Pull trial-to-paid funnel data: signup → activation → core feature use → paywall encounter → checkout → conversion
- Segment churned trial users by: engagement level (high/medium/low), features used, days active, whether they hit a paywall, trial duration remaining at last visit
- Identify the top 3 drop-off points in the funnel
- Pull any existing churn survey or cancellation reason data

**Timeline:** 3–5 business days
**Owner:** UX Researcher + Data/Analytics team
**Deliverable:** Behavioural segmentation of churned trial users, funnel drop-off map

---

### Phase 2 — User Interviews with Churned Trial Users (Qualitative / Generative)
**Purpose:** Understand the reasons, context, and decision-making process behind non-conversion — from the user's perspective.

**Sample:** 8 participants across behavioural segments from Phase 1:
- 3 high-engagement churners (used the product actively but didn't convert)
- 3 medium-engagement churners (signed up, explored, then disengaged)
- 2 low-engagement churners (signed up but barely used the product)

**Recruiting criteria:**
- Trial ended within the last 30 days (memory is still fresh)
- Did not convert to paid
- Represents a mix of company sizes / roles / use cases
- Exclude users who signed up with disposable emails or never logged in after signup

**Screener questions (6):**
1. When did you sign up for [Product]? (Verify recency)
2. How often did you use [Product] during your trial? (Daily / A few times a week / Once or twice / Just the first day)
3. What were you trying to accomplish when you signed up? (Open text — reveals job-to-be-done)
4. Did you evaluate any other tools for the same purpose? (Yes/No + which ones)
5. What is your role and team size? (Segmentation)
6. Are you the person who would make the purchase decision? (Decision-maker vs end-user)

**Incentive:** $75 gift card (or product credit equivalent) per 45-minute session.

**Timeline:** 5–7 business days for recruiting, 5 days for sessions (max 2 per day to prevent fatigue and allow same-day debrief).

---

### Phase 2 — Discussion Guide

**Warm-up (2 min)**
- Thanks for joining. I'm researching how people experience [Product] during the trial — I'm not selling anything, and there are no right or wrong answers. Honest feedback, including negative feedback, is the most helpful thing you can give me.
- Confirm recording consent.

**Context — Their world before the trial (5 min)**
- "Tell me about what you were working on when you decided to try [Product]. What prompted you to look for a tool like this?"
- "How were you handling [the relevant task] before you signed up?"
- "Had you tried other tools for this? What was that experience like?"

**Trial experience — What actually happened (20 min)**
- "Walk me through your first session with [Product]. What did you do first?"
- "What were you hoping would happen when you signed up?"
- "Was there a moment where you thought 'this is useful' or 'this could work for me'?" → Probe: "Tell me more about that moment."
- "Was there a moment where you felt stuck, confused, or frustrated?" → Probe: "What happened next?"
- "How far did you get into [core workflow]?"
- "Did you hit any point where the product asked you to upgrade or told you a feature wasn't available?" → Probe: "How did that feel? What did you do?"

**The decision not to convert (10 min)**
- "When the trial was ending, what were you thinking about whether to continue?"
- "What would have needed to be different for you to upgrade to a paid plan?"
- "Was there a specific reason you decided not to, or did it just... not happen?" (Important: distinguish active rejection from passive drift)
- "Did you talk to anyone else about whether to upgrade — a manager, a colleague?"

**Willingness-to-pay probing (5 min)**
- "How much time were you spending on [the problem] each week before you tried [Product]?"
- "Had you spent money on other tools to solve this? How much?"
- "If [Product] solved [their stated core problem] reliably, what would that be worth to you per month — in time saved or money?"
- "When you saw the pricing, what was your reaction?"

**Close (3 min)**
- "Is there anything I didn't ask about that would help us understand your experience?"
- "If you could change one thing about the trial, what would it be?"
- Thank and explain next steps.

**Self-check after each interview:** Did I learn about their experience and decision process, or did I learn what they think of our product idea? (Mom Test check)

---

### Phase 2 — Note-Taking Template (per participant)

| Field | Content |
|---|---|
| Participant | [P#, segment (high/med/low engagement), role, company size] |
| Core Job | [What they were trying to accomplish] |
| Current Solution | [How they handle it now — post-trial] |
| Biggest Pain | [Most frustrating part of the trial, in their words] |
| Aha Moment | [Did they reach it? What was it? If not, where did they stall?] |
| Conversion Blocker | [The primary reason they didn't convert — active rejection vs passive drift] |
| Price Perception | [How they reacted to pricing — too high, unclear value, compared to what?] |
| Willingness to Pay | [Time/money currently spent on the problem; stated WTP] |
| Surprise Finding | [One thing that contradicted our assumptions] |
| Follow-up | [Questions for next session or for the usability test phase] |

---

### Phase 3 — Usability Test of Trial-to-Paid Flow (Evaluative)
**Purpose:** Test whether the conversion flow itself (pricing page, plan comparison, checkout) introduces unnecessary friction or confusion.

**Sample:** 5 participants — mix of current trial users (still in trial) and prospective users who match the target profile but haven't signed up yet.

**Tasks:**

| # | Task Scenario | Success Criteria | What We're Observing |
|---|---|---|---|
| T1 | "You've been using the free trial for a week. You want to find out what happens when your trial ends — what do you keep and what do you lose." | User can articulate what changes | Is the trial-to-paid transition clear? |
| T2 | "You've decided to upgrade. Find the plan that fits your needs and get to the point where you'd enter payment details." | User selects a plan and reaches checkout | Where do users hesitate? Is plan differentiation clear? |
| T3 | "Before you confirm, you want to understand exactly what you're paying and when you'll be charged." | User can state the price, billing cycle, and any commitments | Is pricing transparent? Are there surprise moments? |
| T4 | "Actually, you've changed your mind — you want to keep using the free version instead." | User finds the downgrade/free option | Is there a clear exit? Does the product make downgrading hostile? |

**Think-aloud protocol:** Brief participants before Task 1. Do not guide during tasks.

**Timeline:** 3 business days for sessions, 2 days for analysis.

---

## 4. Synthesis Plan

### Affinity Mapping Process
1. Write one observation per note: participant ID + verbatim quote or observed behaviour
2. Cluster without naming first — group related observations
3. Name clusters once stable (describe what users experience, not what the product does)
4. Cross-reference clusters with behavioural segments from Phase 1

### Insight Format (for each finding)

**Observation:** [What users did or said — cite participant count, e.g. "6 of 8 participants..."]
**So what:** [Why this matters for conversion rate and revenue]
**Therefore:** [Specific, actionable recommendation — name the feature, flow, or element to change]

### Product-Segment Fit Assessment (per behavioural segment)

| Dimension | High-Engagement Churners | Medium-Engagement Churners | Low-Engagement Churners |
|---|---|---|---|
| Core job alignment | | | |
| #1 unmet need | | | |
| Unexpected insight | | | |
| Data gaps remaining | | | |

---

## 5. Deliverables & Timeline

| Week | Phase | Activities | Deliverable |
|---|---|---|---|
| 1 | Phase 1 | Analytics pull, funnel mapping, segmentation | Behavioural segment definitions + funnel drop-off map |
| 1–2 | Recruiting | Screener distribution, participant scheduling | 8 interview participants + 5 usability participants confirmed |
| 2–3 | Phase 2 | 8 interviews (max 2/day), daily debriefs | Completed note-taking templates, raw transcripts |
| 4 | Phase 3 | 5 usability sessions | Severity-rated issue log for trial-to-paid flow |
| 4–5 | Synthesis | Affinity mapping, JTBD framing, insight writing | Insight deck with segment-level findings |
| 5 | Report | Write-up, recommendations, prioritisation | Final research report |

**Total duration:** 5 weeks from kickoff to final report.

---

## 6. Final Report Structure

1. **Executive summary** — 3 key findings, 3 prioritised recommendations (for stakeholders who read only one page)
2. **Methodology** — methods used, participant count and profile, dates, screener criteria
3. **Participants** — anonymised overview table (segment, role, engagement level, company size)
4. **Funnel analysis** — quantitative findings from Phase 1 with drop-off visualisation
5. **Findings** — one section per finding using insight format (observation + so what + therefore), with supporting quotes and screenshots
6. **Usability issues** — severity-rated issue table from Phase 3
7. **Segment fit assessment** — which user segments have product-market fit and which don't
8. **Recommendations** — prioritised by impact x effort, sorted into:
   - Quick wins (< 1 sprint, high impact) — act immediately
   - Strategic initiatives (> 1 sprint, structural change) — add to roadmap
   - Further research needed — questions this study couldn't answer
9. **Appendix** — discussion guide, screener, raw affinity map, participant quotes index

---

## 7. Assumptions & Risks

| Risk | Mitigation |
|---|---|
| Churned users are hard to recruit (low response rate) | Over-recruit by 50%; offer meaningful incentive ($75); reach out within 30 days of trial end while memory is fresh |
| Analytics data is incomplete or unreliable | Validate instrumentation with engineering before Phase 1; define "activation" metric jointly with product |
| Participants give socially desirable answers about why they left | Use Mom Test techniques: ask about past behaviour, not hypotheticals; probe for specifics; watch for enthusiasm without action |
| Findings are spread across too many minor issues | Use severity rating + participant count to force-rank; limit final recommendations to top 5 |
| Stakeholders want to skip research and "just fix the pricing page" | Lead with the research question framing: we don't yet know if pricing is the problem — this research will tell us where to invest |

---

## 8. Success Criteria for This Research

This research is successful if, at the end, the product team can:

1. **Name the top 3 reasons** trial users don't convert (ranked by prevalence and severity)
2. **Distinguish** whether non-conversion is primarily a value delivery problem, a pricing problem, or a UX friction problem
3. **Prioritise** specific changes to the trial experience with confidence that they address real user behaviour, not assumed behaviour
4. **Identify** which user segments have strong product fit (and should be doubled down on) versus weak fit (and should be deprioritised or redesigned for)
