### RevOps Discovery

**Gather before any recommendation:**

1. **GTM motion:** Product-led (PLG), sales-led, or hybrid? What's the ACV range?
2. **Current funnel:** How do leads enter? (inbound, outbound, partner, product-qualified) What CRM?
3. **Team structure:** How many AEs, SDRs, CSMs? Is there a dedicated RevOps function?
4. **Specific pain:** What's breaking? (leads falling through, no clear MQL definition, bad handoff, pipeline visibility, CRM hygiene, attribution)
5. **Tech stack:** CRM (Salesforce, HubSpot, Pipedrive, Close?), MAP (Marketo, HubSpot, ActiveCampaign?), enrichment (Apollo, Clay, Clearbit?), intent data?

Load lifecycle stage templates: Read `~/.claude/skills/gteam/specialists/revops/references/lifecycle-stages.md`

---

### Lead Lifecycle Design

The lifecycle is the spine of RevOps. Every other system (scoring, routing, reporting) depends on having clean, agreed-on stage definitions.

**Standard B2B lifecycle stages:**

| Stage | Owner | Definition | Entry criteria | Exit criteria |
|-------|-------|------------|----------------|---------------|
| Subscriber | Marketing | Opted into marketing communications | Email opt-in | Any qualifying activity |
| Lead | Marketing | Showed any interest signal | Form fill, content download, webinar registration | Meets MQL criteria |
| MQL | Marketing | Marketing-qualified, ready for sales review | Lead score threshold OR behaviour trigger | SDR accepts → SQL; SDR rejects → recycle |
| SAL (Sales Accepted Lead) | Sales | SDR has reviewed and accepted for outreach | SDR marks accepted within SLA | First meeting booked or disqualified |
| SQL | Sales | Sales-qualified: confirmed budget, authority, need, timeline (BANT or MEDDPICC subset) | Discovery call completed, qualified | Opportunity created |
| Opportunity | Sales | Active deal in pipeline | Opp created in CRM | Closed-won or closed-lost |
| Customer | CS | Paying | Payment received | Churn or expansion event |
| Churned | CS | Cancelled | Cancellation confirmed | Re-engage or archive |

**For PLG motions — product-qualified additions:**

| Stage | Definition | Entry |
|-------|------------|-------|
| PQL (Product-Qualified Lead) | Free/trial user who hit activation signal | Reached aha moment (product-defined) |
| PQA (Product-Qualified Account) | Account with multiple active users or usage spike | ≥3 seats active, or usage >80% of free tier limit |

**Stage definition rules:**
- Each stage must have unambiguous entry criteria (if two people would disagree, redefine)
- Each stage must have a single owner (marketing owns through MQL; sales owns from SAL)
- No stage can last more than 30 days without an escalation rule
- Disqualification must put the lead into a specific recycle stage, not limbo

Load: Read `~/.claude/skills/gteam/specialists/revops/references/lifecycle-stages.md`

---

### Lead Scoring Model

Lead scoring = fit score + engagement score. Both matter. A perfect-fit lead who never engages is less valuable than a strong-fit lead who's actively researching.

**Fit Scoring (firmographic / demographic)**

Score based on ICP match. Define ICP first, then assign points:

| Dimension | Strong fit (10 pts) | Moderate fit (5 pts) | Poor fit (0 pts) |
|-----------|---------------------|----------------------|------------------|
| Company size | [Your ICP range] | Adjacent range | Too small / too large |
| Industry | Target verticals | Adjacent verticals | Out-of-scope |
| Job title / seniority | Economic buyer or champion | Influencer | End user / intern |
| Geography | Target markets | Secondary markets | Excluded markets |
| Tech stack (if applicable) | Uses [complementary tool] | Neutral | Uses [competing tool] |

**Engagement Scoring (behavioural)**

Score based on recency-weighted engagement:

| Action | Points | Decay |
|--------|--------|-------|
| Pricing page visit | 15 | 50% after 14 days |
| Demo request | 25 | No decay |
| Trial signup | 20 | 50% after 30 days |
| Case study download | 10 | 50% after 30 days |
| Webinar attendance | 12 | 50% after 30 days |
| Email click (x3 in 7 days) | 8 | 50% after 14 days |
| Blog post view | 2 | 50% after 7 days |
| Unsubscribe | -20 | Permanent |
| Competitor page visit (if tracked) | 15 | 50% after 7 days |

**MQL threshold:** typically 40–60 total points (fit + engagement). Set by looking at historical data: what was the average score of leads that converted to SQL? Set the threshold at ~80% of that average.

**Negative scoring:**
- Student/personal email domain: -15
- "Student" or "intern" in title: -10
- Country in exclusion list: disqualify entirely

Load: Read `~/.claude/skills/gteam/specialists/revops/references/scoring-models.md`

---

### Lead Routing Rules

Routing must be deterministic — no manual assignment queues for standard leads.

**Routing decision tree:**

```
Is the lead an existing customer account?
  → YES → Route to owning CSM (account-based routing)
  → NO:
    Does the lead have a company domain matching an existing opportunity?
      → YES → Route to owning AE (account-based routing)
      → NO:
        Is this an inbound demo request?
          → YES → Route round-robin to SDR pool (by territory if applicable)
          → NO:
            Does the lead meet MQL threshold?
              → YES → Route to SDR pool (round-robin or territory)
              → NO → Nurture sequence, no SDR assignment
```

**Territory-based routing:** If you have geographic or segment-based territories, routing must check:
1. Company HQ country/state → territory lookup table → assigned rep
2. If territory is open (no rep), route to manager or hold queue with SLA alert

**SLA rules (must be enforced via CRM automation):**
- Inbound demo request: first outreach within 5 minutes (speed-to-lead is the #1 conversion driver)
- MQL → SDR review: within 4 business hours
- SAL → discovery call: within 2 business days
- If SLA breached: auto-alert manager, re-route if no activity within 24h

---

### Pipeline Design & Hygiene

**Opportunity stage definitions (sales-led):**

| Stage | Definition | Probability | Exit criteria |
|-------|------------|-------------|---------------|
| Discovery | First meeting completed, need confirmed | 20% | Champion identified, problem defined |
| Qualification | MEDDPICC/BANT confirmed, decision process mapped | 35% | Economic buyer engaged, timeline confirmed |
| Proposal | Formal proposal or POC underway | 50% | Proposal sent, next step agreed |
| Negotiation | Legal/commercial terms being reviewed | 75% | Verbal agreement on terms |
| Closed-Won | Contract signed, payment initiated | 100% | — |
| Closed-Lost | Deal lost, reason logged | 0% | Loss reason required (mandatory field) |

**Hygiene rules (automate where possible):**
- No opportunity stays in the same stage for >21 days without a next-step date update → flag to manager
- Close date must be in the future — auto-alert if past due and still open
- Loss reason is a required field (no empty closed-lost records)
- Opportunity amount must be filled before moving past Discovery
- All opportunities must have a contact role (champion, economic buyer, etc.)

**Weekly pipeline review checklist:**
- [ ] Opps with no next-step activity in 14+ days
- [ ] Close dates in the past that are still open
- [ ] Opps stuck in the same stage for >21 days
- [ ] Opps with no amount set
- [ ] Opps without a contact role assigned

Load: Read `~/.claude/skills/gteam/specialists/revops/references/pipeline-design.md`

---

### Marketing-to-Sales Handoff

The handoff is the highest-leverage point in most revenue funnels. Most revenue leakage happens here.

**The perfect handoff record (what sales needs from marketing):**

```markdown
## Lead Handoff: [Name] at [Company]

**Contact:** [Name], [Title], [Email], [LinkedIn]
**Company:** [Name], [Size], [Industry], [HQ Location]
**ICP fit:** Strong / Moderate / Weak — [reason]

**What they did (engagement trail, most recent first):**
- [Date]: Requested a demo via [page]
- [Date]: Visited pricing page (3 times this week)
- [Date]: Downloaded [case study name] — [industry] use case
- [Date]: Attended [webinar name] (stayed 45 of 60 minutes)

**Intent signals:**
- Pricing page visits: 4 this month
- Time on site: 18 minutes average
- Pages viewed: /pricing, /case-studies/[company], /integrations/[tool]

**What they said (if any form data):**
- Pain point stated: "[verbatim from form]"
- Timeline stated: "[verbatim]"

**Recommended talk track:**
[1–2 sentences on what to lead with based on their engagement pattern]

**Do not pitch:**
[Any signals suggesting wrong persona or competing solution in play]
```

**SLA enforcement:** Marketing is responsible for data quality in the handoff record. Sales is responsible for reviewing and responding within the agreed SLA. Both sides must agree to the MQL definition in writing — disagreements about what counts as an MQL are the #1 RevOps failure mode.

---

### CRM Automation Patterns

Load: Read `~/.claude/skills/gteam/specialists/revops/references/crm-automation.md`

**Essential automation workflows:**

**1. MQL alert to SDR**
Trigger: Lead score crosses MQL threshold
Action: Create task for assigned SDR (due: same day), send Slack alert with lead summary, log "MQL created" activity

**2. Speed-to-lead for demo requests**
Trigger: "Request Demo" form submitted
Action: Immediately assign to next SDR in round-robin queue, create task (due: 5 minutes), send SDR mobile push notification, start 5-minute SLA timer

**3. Stage SLA escalation**
Trigger: Opportunity stage unchanged for 21 days
Action: Email manager + AE with link to the opp, flag opp with "At Risk" tag, if no activity in 48h → re-route

**4. Closed-lost feedback loop**
Trigger: Opportunity marked Closed-Lost
Action: Required: loss reason field. Then: if loss reason = "Chose Competitor X" → add to competitor re-engagement sequence in 90 days; if "Not ready" → add to 6-month nurture; if "Price" → notify product/pricing team

**5. Expansion trigger**
Trigger: Customer usage > 80% of plan limit for 14 consecutive days
Action: Alert CSM with expansion playbook link, log "Expansion Signal" in account, optionally trigger in-app upgrade prompt

**6. Churn risk detection**
Trigger: Usage drops >40% week-over-week for an account with >$5K ARR
Action: Alert CSM immediately, create "churn risk" task, log signal in account timeline

---

### RevOps Metrics Dashboard

Load: Read `~/.claude/skills/gteam/specialists/revops/references/revops-metrics.md`

**Tier 1 — Board-level (report monthly):**
- New ARR (by source: new logo, expansion, reactivation)
- Net Revenue Retention (NRR) — target: >110% for healthy SaaS
- CAC payback period — target: <18 months
- Pipeline coverage — target: 3–4× quarterly quota

**Tier 2 — Leadership (report weekly):**
- Leads created by source
- MQL volume and MQL→SQL conversion rate
- SQL→Opportunity conversion rate
- Opportunity→Close rate (by stage)
- Average sales cycle length (by segment)
- Open pipeline by stage and close date

**Tier 3 — Operational (report daily/real-time):**
- SLA compliance (% of MQLs reviewed within SLA)
- Speed-to-lead (minutes from demo request to first outreach)
- CRM hygiene score (% of opps with required fields complete)
- Overdue tasks (SDR and AE)

**Funnel conversion benchmarks (SaaS):**

| Conversion | Early-stage | Growth-stage | Mature |
|------------|-------------|--------------|--------|
| Visitor → Lead | 1–3% | 3–6% | 5–10% |
| Lead → MQL | 15–25% | 25–40% | 35–50% |
| MQL → SQL | 30–45% | 40–55% | 50–65% |
| SQL → Close | 20–30% | 25–35% | 30–45% |
| Overall visitor → close | 0.1–0.3% | 0.4–0.8% | 0.8–1.5% |

---

### Output Formats

**RevOps Audit Report:**

```markdown
# RevOps Audit: [Company]
Date: [YYYY-MM-DD]

## Current State
[Funnel conversion rates at each stage with benchmark comparison]

## Critical Issues
| Issue | Impact | Fix | Owner | Timeline |
|-------|--------|-----|-------|----------|
| [e.g. No MQL definition] | [Leads falling through] | [Define and implement] | [RevOps] | [2 weeks] |

## Recommended Stage Definitions
[Lifecycle stages table with entry/exit criteria]

## Lead Scoring Model
[Fit dimensions + points table] [Engagement actions + points table] [MQL threshold recommendation]

## Routing Rules
[Decision tree for lead assignment]

## Automation Backlog (prioritised)
1. [Automation name] — [trigger] → [action] — [expected impact]
2. ...

## Dashboard Spec
[Tier 1/2/3 metrics with targets]

## 30/60/90-Day Implementation Plan
- Week 1–2: [Quick wins — stage definitions, MQL criteria]
- Week 3–6: [Scoring + routing setup]
- Week 7–12: [Automation builds + dashboard]
```

Save output to `~/.claude/skills/gteam/specialists/revops/results/[company]-revops-[date].md`
