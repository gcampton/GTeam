# CRM Automation Patterns

## Principles Before Patterns

1. **Define before you automate.** Automating a broken process at scale breaks it faster. Get stage definitions and scoring criteria agreed first.
2. **Every automation needs an owner.** Who monitors it? Who fixes it when it breaks?
3. **Build in escape hatches.** Every automation should have a manual override. SDRs and AEs need to be able to flag edge cases.
4. **Log everything.** Every automation action should write to the CRM activity timeline. "Automated: MQL alert sent to Jane, 2:34pm" — this is how you debug issues.
5. **Test with real data before activating.** Run the automation on 10 historical records and check the output before enabling for live leads.

---

## The 8 Essential Revenue Automation Workflows

### 1. Speed-to-Lead (Demo Request)

**The most impactful automation in revenue operations.** Research shows:
- Contact within 5 minutes: 9× more likely to qualify than contact after 30 minutes
- Contact within 1 hour: 7× more likely to qualify than contact after 2 hours

**Trigger:** "Request Demo" or "Contact Sales" form submitted

**Actions (sequential, all within 60 seconds):**
1. Create lead record (if not existing) with all form data
2. Enrich company data via Clay/Apollo/Clearbit (async — don't wait for enrichment before routing)
3. Assign to next SDR in round-robin queue (by territory if configured)
4. Create task for assigned SDR: "Call [Name] — Demo request — Due: 5 minutes" (high priority)
5. Send SDR mobile push notification via Slack/Teams: "🔥 New demo request: [Name] at [Company]"
6. Start 5-minute SLA timer
7. If SDR does not log activity within 5 minutes: escalate to SDR manager via Slack
8. Send prospect confirmation email: "Your demo request is confirmed — [SDR Name] will reach out shortly"

**Log:** "Demo request automation triggered at [timestamp]. Assigned to [SDR]. SLA timer started."

---

### 2. MQL Alert and Assignment

**Trigger:** Lead score crosses MQL threshold (or specific behaviour trigger: pricing page 3× in 7 days, etc.)

**Actions:**
1. Update lifecycle stage to "MQL" in CRM
2. Assign to SDR (round-robin or territory logic)
3. Create task for SDR: "Review MQL: [Name]" — Due: 4 business hours
4. Send SDR Slack alert: "New MQL: [Name] at [Company] — Score: [X] — Top signals: [Pricing page ×3, Case study download]"
5. If SDR does not mark SAL or recycle within 4 business hours: send manager escalation alert
6. Log automation action in lead activity timeline

**Handoff record format for the alert:**
```
Company: [Name] | Size: [N] employees | Industry: [industry]
Contact: [Name], [Title]
Top scoring actions: [list top 3 engagement signals with dates]
ICP fit: Strong / Moderate / Weak
Recommended talk track: [1 sentence based on top signal]
```

---

### 3. Stage SLA Escalation

**Trigger:** Opportunity stage field unchanged for 21 consecutive days

**Actions:**
1. Tag opportunity with "Stuck Deal" label in CRM
2. Send email to AE and manager with: opp name, current stage, days since last stage change, link to opp
3. Add manager task: "Review stuck deal: [Opp Name] — [days] days in [Stage]"
4. If no stage change in 48 hours after alert: re-alert with "CRITICAL: Deal may need re-forecast" tag

**Exception:** Do not trigger during legal review stage (negotiation can legitimately take >21 days). Configure stage exclusions.

---

### 4. Close Date Past-Due Alert

**Trigger:** Opportunity close date = today (run daily at 6am)

**Actions:**
1. Send AE email: "Close date passed: [Opp Name] — update close date or status"
2. Add task to AE: "Update close date or close this deal"
3. If not updated within 48h: tag with "Past Due" and alert manager
4. Weekly: generate report of all past-due opps for manager pipeline review

---

### 5. Closed-Lost Follow-Up and Recycle

**Trigger:** Opportunity marked Closed-Lost

**Required pre-action (block without this):** Loss reason field must be completed. If empty, pop-up prompt prevents stage save.

**Actions based on loss reason:**
| Loss Reason | Automation |
|-------------|-----------|
| "Chose Competitor: [Name]" | Tag lead "Competitor - [Name]"; add to win-back sequence in 180 days |
| "No budget / wrong timing" | Add to 6-month re-engage nurture sequence |
| "Not ready / status quo" | Add to 90-day educational nurture sequence |
| "Product gap" | Create task for Product team member: "[Company] lost due to: [reason]" |
| "Price" | Notify RevOps for pricing model review tracking |

**All closed-lost:** Set lifecycle stage back to "Lead" (not deleted — they may return); set re-engage date.

---

### 6. Expansion Signal Detection

**Trigger:** Account usage metrics cross threshold (from product analytics via webhook or integration)

Thresholds to configure:
- Usage > 80% of plan limit for 14 consecutive days
- Seat count at plan maximum for 7 days
- Key feature usage spike: 3× normal volume in one week
- Multiple team members accessing product (for individual-plan account)

**Actions:**
1. Add "Expansion Signal" tag to account in CRM
2. Create task for CSM: "Expansion opportunity: [Account] — [Trigger: over seat limit / usage spike]"
3. Send CSM Slack alert with account details
4. Add to "Expansion Shortlist" CRM view
5. Optional: trigger in-app upgrade prompt (coordinate with product team)

---

### 7. Churn Risk Detection

**Trigger:** Any of:
- Login frequency drops >40% week-over-week for accounts with ARR > $5K
- No login for 14 days (for accounts with 30-day prior active streak)
- NPS response submitted with score 0–6
- Support ticket: category = "Cancellation enquiry" OR "Considering alternatives"

**Actions:**
1. Add "Churn Risk" tag to account
2. Create urgent task for CSM: "Churn risk: [Account] — [Trigger: usage drop / detractor NPS]"
3. Slack alert to CSM + CS Manager: "⚠️ Churn signal: [Account Name] ($[ARR] ARR)"
4. If no CSM outreach logged within 24h: escalate to CS Manager
5. Log trigger in account timeline

**NPS detractor-specific:**
- Auto-send internal alert to CS Manager with verbatim comment
- Block marketing emails to this contact (don't add fuel to the fire)
- CSM task: "Personal outreach within 24h — do not use automated sequences"

---

### 8. Renewal Preparation

**Trigger:** 90 days before contract end date (for annual contracts)

**Actions:**
1. Create renewal opportunity in CRM (linked to original)
2. Create CS task: "Start renewal conversation: [Account] — Contract ends [date]"
3. Slack alert to CSM and their manager
4. At 60 days: if no renewal activity logged, escalate to CS Manager
5. At 30 days: if renewal not confirmed, escalate to CS Director

**Renewal prep checklist (generate as task list for CSM):**
- [ ] Review usage data — is customer getting full value?
- [ ] Review all open support tickets — resolve before renewal conversation
- [ ] Check expansion potential — any upsell opportunities?
- [ ] Review NPS/CSAT score from last 90 days
- [ ] Identify any new stakeholders who joined this account
- [ ] Prepare business review deck with ROI data

---

## Automation Maintenance

| Check | Frequency | How |
|-------|-----------|-----|
| Failed automation count | Weekly | CRM automation error log |
| False positive rate (wrong alerts) | Monthly | SDR/AE feedback form |
| SLA compliance (measured vs. target) | Weekly | CRM report |
| Lead assignment balance (round-robin drift) | Monthly | Check distribution across SDR team |
| Trigger condition accuracy | Quarterly | Spot-check 20 random automations |
| Enrichment quality | Monthly | Check % of records with company size, industry filled |
