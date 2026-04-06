# Community Metrics Framework

## Health Metrics Dashboard

| Metric | Healthy | Warning | Critical | Notes |
|---|---|---|---|---|
| DAU/MAU ratio | >20% | 10-20% | <10% | [TESTED] Industry standard for engaged communities |
| 7-day new member retention | >40% | 20-40% | <20% | [HYPOTHESIS] Based on SaaS onboarding benchmarks applied to communities |
| 30-day new member retention | >25% | 10-25% | <10% | [HYPOTHESIS] Extrapolated from 7-day with typical decay curves |
| 90-day retention | >15% | 5-15% | <5% | [HYPOTHESIS] Long-term engagement benchmark |
| Messages per active member per day | 2-10 | 1-2 or >15 | <1 or >20 | Too high may indicate spam or clique dominance |
| % members who ever post | >30% | 15-30% | <15% | [HYPOTHESIS] Lurker ratio varies by platform |
| Time to first message (new members) | <24 hours | 24-72 hours | >72 hours or never | Measures onboarding effectiveness |
| Moderator action rate | <2% of messages | 2-5% | >5% | High rate may indicate toxic culture or over-moderation |

## DAU/MAU Ratio Benchmarks by Community Type

| Community Type | Typical DAU/MAU | Notes |
|---|---|---|
| Developer tools (Discord) | 15-25% | [TESTED] Spikes around releases, lower between |
| Gaming communities | 25-40% | [TESTED] Highest engagement category |
| SaaS product community | 10-20% | [HYPOTHESIS] Users come when they need help |
| Course/membership | 20-35% | [HYPOTHESIS] Higher during cohort runs, drops between |
| Open source project | 8-15% | [HYPOTHESIS] Contributor base is small, users are transient |
| Brand community | 5-12% | [HYPOTHESIS] Lowest — members join but rarely return |

## Retention Curves

### Typical Retention Decay
```
Day 1:  100% (joined)
Day 7:  40-50% (healthy) / 20-30% (warning) / <20% (critical)
Day 30: 25-35% (healthy) / 10-20% (warning) / <10% (critical)
Day 90: 15-20% (healthy) / 5-10% (warning) / <5% (critical)
```

### Key Retention Levers
1. **First 24 hours** — Did the member get a welcome, read rules, and send a first message? [TESTED] Communities with structured onboarding see 2x retention at day 7
2. **First week** — Did the member find a conversation thread relevant to them? [HYPOTHESIS] Topic relevance is the #1 predictor of week-1 retention
3. **First month** — Did the member form at least one connection (reply thread, voice chat, DM)? [HYPOTHESIS] Social ties predict long-term retention better than content engagement

## Engagement Rate Calculation

```
Daily engagement rate = (messages sent today) / (members active today)

Weekly engagement rate = (messages sent this week) / (unique members active this week)

Contribution ratio = (members who posted at least once) / (total members)
```

**Benchmarks:**
- 2-5 messages/active member/day = healthy conversation [HYPOTHESIS]
- >10 messages/active member/day = check if a few power users are dominating [HYPOTHESIS]
- <1 message/active member/day = community feels dead, even if DAU is okay [HYPOTHESIS]

## Churn Signals

| Stage | Definition | Signal | Intervention |
|---|---|---|---|
| Active | Sent message in last 7 days | Normal activity | None needed |
| Declining | Active in last 30 days but not last 7 | Reduced frequency, shorter messages | Personal ping, ask for feedback |
| At-risk | Active in last 90 days but not last 30 | Stopped posting, may still lurk | Re-engagement campaign (event invite, content digest) |
| Churned | No activity in 90+ days | Gone | Win-back only if high-value member; otherwise accept natural churn |
| Zombie | Joined but never posted | Never activated | Improve onboarding; don't count as "members" in metrics |

**Power user churn is the most dangerous signal.** If your top 10% contributors start declining, investigate immediately — they often signal cultural problems before they become visible. [TESTED]

## Sentiment Indicators

### Quantitative Proxies
- Reaction ratio: positive reactions (thumbs up, hearts) vs negative (thumbs down, X) [HYPOTHESIS]
- Thread depth: longer threads suggest engagement; very short replies may signal dismissiveness
- Help channel resolution rate: questions that get answered vs ignored

### Qualitative Signals to Watch
- **Tone shift** — conversations becoming more sarcastic, passive-aggressive, or combative
- **"This community used to be better"** — nostalgia posts signal declining satisfaction
- **Mod criticism increasing** — may indicate over-moderation or inconsistent enforcement
- **Side channels forming** — members creating unofficial spaces suggests unmet needs
- **Introductions dropping off** — new members not introducing themselves suggests unwelcoming atmosphere
- **Event attendance declining** — people vote with their time

### Measurement Cadence

| Metric | Frequency | Tool |
|---|---|---|
| DAU/MAU | Weekly | Platform analytics or bot |
| Retention cohorts | Monthly | Custom tracking or analytics bot |
| Engagement rate | Weekly | Message count / active count |
| Sentiment | Monthly | Manual review + member survey quarterly |
| Churn analysis | Monthly | Export member activity data |
