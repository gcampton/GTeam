### Community Health Check

**Use when:** Monthly review of community health, or when something feels off (declining activity, rising toxicity, member complaints). Don't wait for a crisis — run this proactively.

**Gather:** Platform analytics access, time period for review (default: last 30 days), previous health report (if exists), any specific concerns from the team.

---

### Key Metrics Framework

Track these six metrics monthly. The numbers matter less than the trend — a DAU/MAU of 15% that's climbing is healthier than 30% that's falling.

**1. DAU/MAU Ratio (Daily Active / Monthly Active Users)**

| Range | Status | Interpretation |
|---|---|---|
| 30-50% | Healthy | Members return frequently, strong habit loop |
| 20-30% | Normal | Typical for topic-based communities |
| 15-20% | Concerning | Members drift away between visits |
| < 15% | Unhealthy | Community is a ghost town for most members |

Where to find it: Discord Server Insights, Slack Analytics, Discourse Admin Dashboard, Circle Analytics.

**2. Message Frequency Trend (week-over-week)**

| Trend | Status | Interpretation |
|---|---|---|
| +5% to +15% WoW | Healthy growth | Engagement increasing sustainably |
| -5% to +5% WoW | Stable | Normal for mature communities |
| -5% to -15% WoW | Concerning | Declining engagement, investigate cause |
| < -15% WoW | Urgent | Something is wrong — act immediately |

Exclude bot messages and automated posts from this count.

**3. New Member Retention**

| Metric | Healthy | Concerning | Unhealthy |
|---|---|---|---|
| Still active after 7 days | > 40% | 20-40% | < 20% |
| Still active after 30 days | > 25% | 10-25% | < 10% |
| Posted at least once (first 7 days) | > 50% | 30-50% | < 30% |

"Active" means sent at least one message. Lurking doesn't count — lurkers can't be measured and don't contribute to community health.

**4. Channel Activity Distribution**

Measure the percentage of total messages in each channel. A healthy community has activity spread across channels. If 80%+ of messages are in #general, your topic channels aren't working — either the topics are wrong or the channels aren't being seeded with content.

**Ideal distribution:**
- #general: 30-40%
- Topic channels (combined): 30-40%
- Support/help: 10-20%
- Off-topic/casual: 10-15%

**5. Moderator Action Frequency**

| Trend | Interpretation |
|---|---|
| Stable and low (1-3 actions/week per 1K members) | Healthy — rules are clear, culture is self-regulating |
| Rising steadily | Growing problems — review rules, check for new toxic members or external brigading |
| Spiking suddenly | Incident in progress — investigate immediately |
| Zero for 2+ weeks | Mods are inactive or disengaged — check in with the team |

**6. Sentiment Analysis (Qualitative)**

Read 50-100 recent messages across channels. Score the overall tone:
- **Positive:** Members help each other, share wins, express enthusiasm
- **Neutral:** Transactional exchanges, questions and answers, low emotion
- **Negative:** Complaints, arguments, passive-aggression, clique behaviour
- **Toxic:** Personal attacks, hostility toward newcomers, mod distrust

---

### Diagnostic Decision Tree

When a metric is concerning, use this tree to identify the likely cause and intervention.

**DAU/MAU declining:**
- Are new members joining but not returning? → Welcome flow is broken or first experience is poor → Fix onboarding
- Are established members leaving? → Content has gone stale or culture has shifted → Run a feedback survey, refresh content strategy
- Is it seasonal? → Check if the dip correlates with holidays or industry cycles → Wait and monitor

**Message frequency dropping:**
- Did a key contributor leave or go quiet? → Community was over-reliant on one person → Diversify content sources, recruit more contributors
- Did you change rules recently? → New rules may be chilling conversation → Revisit the rule, ask for feedback
- Is the product/topic losing relevance? → Broader market issue → Pivot community focus or acknowledge the shift

**New member retention low:**
- Are new members posting and getting no response? → Response time is too slow → Assign a "welcomer" role, seed responses to intro posts
- Are new members overwhelmed by channel count? → Too many channels → Consolidate channels, improve onboarding guide
- Are existing members hostile to newcomers? → Culture problem → Address directly, enforce welcoming behaviour

**Moderator actions spiking:**
- Is it one user or many? → One user: ban and move on. Many: systemic issue, check for external brigading or a controversial event
- Is it spam or toxicity? → Spam: tighten automod. Toxicity: review rules enforcement, check mod consistency

---

### Monthly Health Report Template

```markdown
# Community Health Report — [Month Year]

## Summary
- **Overall health:** [Healthy / Stable / Concerning / Urgent]
- **Key change:** [One sentence: what's different from last month]

## Metrics
| Metric | This Month | Last Month | Trend | Status |
|---|---|---|---|---|
| Total members | X | X | +X% | — |
| DAU/MAU | X% | X% | +/-X% | 🟢/🟡/🔴 |
| Messages/week (avg) | X | X | +/-X% | 🟢/🟡/🔴 |
| New members joined | X | X | +/-X% | — |
| New member 7-day retention | X% | X% | +/-X% | 🟢/🟡/🔴 |
| Mod actions | X | X | +/-X% | 🟢/🟡/🔴 |
| Sentiment | [Pos/Neu/Neg] | [Pos/Neu/Neg] | — | 🟢/🟡/🔴 |

## Channel Activity
| Channel | Messages | % of Total | Change |
|---|---|---|---|
| #general | X | X% | +/-X% |
| [other channels] | X | X% | +/-X% |

## Top Contributors (this month)
1. @user1 — X messages, helped in #support, started 3 discussions
2. @user2 — X messages, consistent presence in #topic-1
3. @user3 — X messages, welcomed 8 new members

## Issues & Actions
| Issue | Severity | Action Taken / Planned | Owner |
|---|---|---|---|
| [Issue description] | HIGH/MED/LOW | [What was done or will be done] | [Who] |

## Recommendations
- [1-3 specific, actionable recommendations for next month]
```

---

### Intervention Playbook

**Declining engagement:**
1. Post a "state of the community" message — transparency builds trust
2. Launch a time-limited event (challenge, AMA, collab project) to create urgency
3. DM 5-10 previously active members and ask what changed
4. Review content strategy — are discussion prompts stale?
5. Consider consolidating channels to concentrate activity

**Toxic culture developing:**
1. Identify the source — usually 2-3 individuals set the tone
2. Enforce rules consistently and visibly (public mod actions, not just DMs)
3. Recruit positive community members as moderators
4. Post a clear "community values" reminder
5. If toxicity is systemic, consider a culture reset: new rules, new channels, fresh start

**Moderator burnout:**
1. Reduce mod workload: automate more, restrict posting hours for mods
2. Rotate mod duties weekly instead of everyone doing everything
3. Recognise mod contributions publicly — they're volunteers
4. Recruit more mods — 1 per 500 active members minimum
5. Give mods a private space to vent and support each other

**Stale content:**
1. Introduce a content calendar with themed days
2. Invite guest experts for AMAs or workshops
3. Launch a member spotlight series
4. Create a challenge or project that generates organic content
5. Ask members what they want to discuss — don't guess

**Deliver:**
- Completed health report using the template above
- Diagnosis of any concerning metrics with root cause analysis
- Prioritised action plan (max 3 items) for the next 30 days
- Updated benchmarks if the community has matured past previous targets
