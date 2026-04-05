### Go-to-Market & Measurement

Shipping is not launching. A feature that ships without a GTM plan does not get adopted.

**GTM checklist:**

**Product:**
- [ ] In-app announcement written and approved (tooltip, modal, or banner — choose based on feature importance)
- [ ] Release notes published
- [ ] Help center article live before GA

**Engineering:**
- [ ] Feature flag enabled for target cohort
- [ ] Monitoring dashboard live with anomaly alert thresholds set
- [ ] Rollback runbook written, reviewed, and accessible

**Marketing:**
- [ ] Positioning and messaging approved
- [ ] Blog post drafted, reviewed, and scheduled
- [ ] Email segment identified and copy approved
- [ ] Social copy ready

**Sales & Customer Success:**
- [ ] Sales enablement deck updated
- [ ] CS team trained (session scheduled at least 3 days before GA)
- [ ] FAQ for objections and common questions published
- [ ] Support ticket routing updated for new feature area

**Post-launch: leading vs. lagging metrics:**
- **Leading indicators** (visible within days): feature activation rate (% of eligible users who try it), error rate, time-to-complete core flow
- **Lagging indicators** (visible within weeks/months): retention delta for feature users, NPS change, support ticket volume on related topics, revenue impact

**Retention analysis (Day 1/7/30 cohorts):** For every significant feature launch, track the cohort of users who first used the feature in launch week. Measure what % return and use it on Day 1, Day 7, and Day 30. Compare against pre-launch baseline or control group. This tells you whether the feature delivers durable value or just curiosity clicks.

**North Star metric definition:** Every product area should have one metric that best captures whether users are getting genuine value. It must be a behaviour metric (not a vanity metric), measurable weekly, and something the team can directly influence. Examples: "weekly active projects per user" (not "DAU"), "tasks completed per session" (not "sessions"), "reports generated per account" (not "accounts created"). Define it once, publish it, and review it at every quarterly planning.

**When to iterate vs. abandon:** Give a launched feature at least 60 days and one full GTM cycle before drawing conclusions. If at 60 days the primary success metric is at less than 50% of target, run 5 user interviews before deciding. If interviews reveal a fundamental misunderstanding of the problem, reconsider the approach. If they reveal execution gaps (discoverability, UX, onboarding), iterate. Abandon only when evidence shows the underlying hypothesis was wrong — not when the feature underperformed due to lack of promotion or incomplete implementation.

---

### Feature Success Metrics

For every feature shipped, define success metrics before launch:

| Dimension | Metric | Target | Measurement Method |
|---|---|---|---|
| Adoption | % of target users who try the feature (Day 14) | > 30% | Analytics event |
| Frequency | Uses per user per week | > 2 | Analytics event |
| Depth | % completing full workflow (not just starting) | > 60% | Funnel analytics |
| Retention | % still using at Day 30 | > 50% | Cohort analysis |
| Satisfaction | CSAT or thumbs-up/down rating | > 4.0/5 | In-app survey |

**60-day rule:** Measure for 60 days before deciding to iterate, expand, or sunset. Don't abandon features based on week-1 data.
