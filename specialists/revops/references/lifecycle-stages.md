# Lead Lifecycle Stage Templates

## PLG (Product-Led Growth) Lifecycle

For products with a free tier, self-serve trial, or freemium model.

```
Visitor → Subscriber → Lead → PQL → PQA → [Sales Touch] → Customer → Expanded Customer
```

| Stage | Owner | Entry criteria | Exit criteria | Max duration |
|-------|-------|----------------|---------------|--------------|
| **Visitor** | Marketing | Any site visit | Any form fill, signup, or content engagement | — |
| **Subscriber** | Marketing | Email opt-in (newsletter, content download) | Any qualifying product or behavioural signal | 90 days |
| **Lead** | Marketing | Free signup / trial start | Reaches activation milestone | 14 days |
| **PQL (Product-Qualified Lead)** | Marketing/Sales | Hits activation signal (defined per product — see below) | Assigned to sales (if sales-assisted) or self-converts | 30 days |
| **PQA (Product-Qualified Account)** | Sales | ≥3 users active in account OR usage > 80% of free tier limits | Opportunity created or expansion confirmed | 21 days |
| **Opportunity** | Sales | Sales conversation started | Closed-won or closed-lost | 60 days |
| **Customer** | CS | Payment confirmed | — | — |
| **Expanded** | CS | Upsell/cross-sell completed | — | — |

### Defining Your Activation Signal (PQL threshold)

The activation signal is the specific in-product action that predicts long-term retention. Find it by analysing which early actions correlate most strongly with 90-day retention.

Common patterns:
| Product type | Activation signal |
|-------------|-----------------|
| Collaboration tool | Invited ≥1 teammate AND sent ≥1 message |
| Analytics | Connected ≥1 data source AND viewed ≥1 report |
| Email marketing | Created AND sent first campaign |
| Project management | Created ≥3 tasks AND added ≥1 teammate |
| Developer tool | Made first successful API call OR deployed to production |

If you don't know your activation signal yet: proxy with "Returned to the app within 7 days of signup AND completed onboarding flow."

---

## Sales-Led Lifecycle

For products with a predominantly inbound or outbound sales motion.

```
Visitor → Lead → MQL → SAL → SQL → Opportunity → Customer
```

| Stage | Owner | Entry criteria | Exit criteria | SLA |
|-------|-------|----------------|---------------|-----|
| **Lead** | Marketing | Any contact record created (form fill, event, webinar, referral) | Lead score threshold reached OR manual MQL | 24h to score |
| **MQL** | Marketing | Lead score ≥ [threshold] OR manual override by marketing | SDR accepts (→ SAL) or rejects with reason (→ Recycle) | SDR review: 4 business hours |
| **SAL (Sales Accepted Lead)** | Sales | SDR has reviewed and accepted for outreach | Discovery call booked or lead disqualified | First outreach: 5 min for demo requests; 4h for other MQLs |
| **SQL (Sales Qualified Lead)** | Sales | Discovery completed, BANT or MEDDPICC subset confirmed | Opportunity created in CRM | Opportunity creation: 24h after qualifying call |
| **Opportunity** | Sales | Formal deal record created | Closed-won or closed-lost | Per stage SLAs (see pipeline-design.md) |
| **Customer** | CS | Contract signed AND payment received | — | Onboarding initiated: 24h |

### MQL Definition Options

Choose ONE of these approaches. Hybrid approaches cause arguments.

**Option A: Score-based MQL**
Lead score ≥ [X] (fit score + engagement score combined). Clear, objective, automatable. Requires clean scoring model.

**Option B: Behaviour-triggered MQL**
Specific actions auto-qualify as MQL regardless of score:
- Demo request: always MQL
- Pricing page viewed ≥ 3 times in 7 days: MQL
- Free trial started: MQL after day 7 if still active
- Attended live demo webinar: MQL

**Option C: Marketing-manual MQL**
Marketing team reviews and manually promotes leads based on judgment. No automation. Scales poorly; only for teams generating <20 leads/month.

**Best practice:** Use Option B for high-intent signals (demo request, trial) + Option A for nurture-qualified leads. Never use Option C at scale.

---

## Hybrid (PLG + Sales-Assisted) Lifecycle

Most modern SaaS companies operate a hybrid: self-serve for SMB, sales-assisted for mid-market and enterprise.

```
[Self-serve path]: Visitor → Signup → PQL → Self-converts → Customer → PQA for expansion
[Sales-assisted path]: Visitor → Lead → MQL → SAL → SQL → Opportunity → Customer
[PLG-to-sales bridge]: PQA → Sales identifies and creates Opportunity
```

**Routing rule for hybrid:**
- ACV < $[threshold]: self-serve only, no SDR outreach
- ACV $[threshold]–$[upper bound]: SDR reaches out to offer assisted onboarding (not a hard sell)
- ACV > $[upper bound]: full sales-assisted motion required

**PLG-to-sales hand-off triggers (PQA → Opportunity):**
- Account has ≥[N] seats active
- Account usage > 90% of free tier for 14 consecutive days
- Champion requests a demo or contacts sales
- Champion's company matches enterprise ICP (size, industry, tech stack signal)

---

## Recycle and Re-engagement

All lifecycles need a recycle state — otherwise rejected or stalled leads become data garbage.

| Recycle reason | Recycle action | Re-engage after |
|---------------|----------------|-----------------|
| Not ready / wrong timing | Add to 3-month nurture sequence | 90 days |
| Wrong persona (not the buyer) | Route to the right contact at same company | 14 days (if right contact found) |
| Lost to competitor | Add to win-back sequence in 6 months | 180 days |
| No budget this cycle | Add to 6-month re-engage | 180 days |
| Bad data (wrong contact, bounced email) | Enrich and re-qualify | After enrichment |
| Unsubscribed | Do not contact | Never (GDPR/CAN-SPAM) |

**Recycle is not archive.** A recycled lead should re-enter the scoring model as new activity occurs. Set up re-scoring rules: if a recycled lead visits the pricing page or starts a trial, they should auto-promote back to MQL status.
