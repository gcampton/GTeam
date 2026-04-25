## CRM Automation Patterns

Load: Read `~/dev/1_myprojects/gteam/specialists/revops/references/crm-automation.md`

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
