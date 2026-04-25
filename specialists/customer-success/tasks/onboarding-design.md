## Onboarding Design

**Gather:** Customer tier (high-touch / low-touch / self-serve), contract value, product purchased, assigned CSM (if any), target go-live date.

**Onboarding checklist by tier:**
- High-touch (enterprise): dedicated CSM, kickoff call within 3 business days of signing, custom implementation plan, weekly check-ins for 90 days, executive sponsor identified
- Low-touch (mid-market): kickoff call within 5 business days, templated 30/60/90 plan sent on day 1, bi-weekly check-in for 60 days
- Self-serve (SMB): automated onboarding email sequence, in-product checklists, first-use milestone triggers, human touchpoint only at day 14 and day 30

**Kickoff call agenda (45–60 min):**
1. Customer goals — what does success look like in 90 days? (10 min)
2. Success metrics — how will they measure it? (5 min)
3. Stakeholders — who needs to be involved? Who is the day-to-day contact? (5 min)
4. Timeline — key milestones and dependencies (10 min)
5. Product walkthrough focused on their specific use case (15 min)
6. Next steps — assign actions with owners and dates (5 min)

**30/60/90 day plan milestones:**
- Day 30: product configured, first team members active, first core workflow completed
- Day 60: full team onboarded, initial results visible, integration with other tools live
- Day 90: time-to-value milestone hit, expansion use case identified, QBR scheduled

**Time-to-value tracking:** Define the product's "aha moment" (e.g. first report run, first automation triggered). Track days from contract sign to first aha moment. Flag any account >14 days without hitting it.

#### Activation Metric Discovery

**How to identify the aha moment:**
1. List all actions a user can take in first 7 days
2. Correlate each action with 30-day retention — the action with highest retention correlation is the activation metric
3. Set activation target: users who complete this action within X days retain at Y% vs Z% for those who don't

**Real-world examples:**
- Slack: team sends 2,000 messages → retained
- Dropbox: uploads first file → retained
- HubSpot: imports contacts + sends first email → retained

#### Friction Mapping

Before designing any onboarding flow, map friction points:

| Step | Action Required | Avg Time | Drop-off % | Fix |
|---|---|---|---|---|
| Signup | Email + password only | 30s | 5% | Defer all other fields |
| First value | [product-specific] | ? | ? | Guided walkthrough |
| Integration | Connect data source | ? | ? | Pre-built templates |

Rule: every step must complete in < 2 minutes. If not, split it.

#### Onboarding Email Sequence

5-email sequence template:
1. **Welcome** (immediate): Confirm account, single CTA to first-value action
2. **Quick win** (Day 1): Show easiest path to activation metric, include 60-second video
3. **Social proof** (Day 3): Customer story similar to their segment/use-case
4. **Feature spotlight** (Day 5): One feature they haven't used yet, tied to their stated goal
5. **Check-in** (Day 7): "How's it going?" with calendar link for 15-min call if stuck

Personalisation triggers: segment (enterprise/SMB), stated use-case, features used/not-used.

#### Measurement Benchmarks

| Metric | Healthy Range | Action if Below |
|---|---|---|
| Activation rate (Day 7) | 30-60% | Simplify first-value path |
| Time-to-first-value | < 24 hours | Add guided setup wizard |
| Onboarding email opens | 40-60% | Improve subject lines, send timing |
| Day 7 retention | 40-60% | Audit friction map |
| Day 30 retention | 25-40% | Review feature adoption depth |
| NPS (Day 30) | > 30 | Investigate detractors by segment |

#### Monthly Onboarding Review

Cadence: first Monday of each month
1. Pull funnel metrics (signup → activation → Day 7 → Day 30)
2. Identify biggest drop-off stage
3. Hypothesise one fix, A/B test it
4. Review previous month's test results
5. Update friction map with new data
