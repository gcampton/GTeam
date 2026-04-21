# Metrics Framework: In-App Messaging

**Date:** 2026-04-15
**Status:** Framework design — ready for instrumentation
**Feature:** In-app messaging (user-to-user direct messaging within the product)

---

## 1. North Star Metric

### Messages exchanged between two distinct users per week

| Field | Value |
|---|---|
| **Name** | Weekly Bidirectional Conversations |
| **Formula** | COUNT(DISTINCT conversation_id) WHERE messages_sent >= 1 by each participant, rolling 7 days |
| **Data source** | `messaging_events` table |
| **Update frequency** | Daily (trailing 7-day window) |
| **Owner** | Product — Messaging team lead |

**Why this metric:** A message sent into the void is not value delivered. A conversation where both parties participate proves the feature is creating connection. This rises when users find messaging useful and falls when they don't — regardless of whether we're growing total users.

**Why not alternatives:**
- *Messages sent* — inflated by spam, one-sided broadcast, and bot-like behaviour. A user sending 50 unanswered messages is not a success story.
- *DAU of messaging* — tells you people opened the feature, not that they got value from it.
- *Read receipts / open rate* — passive consumption, not engagement.

---

## 2. Supporting Metrics

### 2a. Input Metrics (Leading Indicators)

These are the levers teams can pull to drive the North Star.

| # | Metric | Formula | Data Source | Frequency | Owner |
|---|---|---|---|---|---|
| I1 | **Messaging activation rate** | Users who send first-ever message / Users exposed to messaging entry point, per cohort week | `messaging_events` + `feature_exposure` | Weekly | Growth |
| I2 | **Reply rate** | Conversations with ≥1 reply / Conversations started, trailing 7d | `messaging_events` | Daily | Product |
| I3 | **Time to first reply** | MEDIAN(first_reply_timestamp − first_message_timestamp) | `messaging_events` | Daily | Product |
| I4 | **Notification tap-through rate** | Message notification taps / Message notifications delivered | `push_events` + `messaging_events` | Daily | Engagement |
| I5 | **Conversation depth** | MEDIAN(messages per conversation per 7d window) | `messaging_events` | Weekly | Product |

**How these connect to the North Star:**
- I1 drives the top of the funnel — more activated users means more potential conversations
- I2 is the conversion step — a started conversation only counts if someone replies
- I3 is the friction metric — long reply times kill conversation momentum
- I4 brings users back into the product to continue conversations
- I5 measures whether conversations are meaningful or just "hi / hi"

### 2b. Guardrail Metrics

These must not degrade while we optimise the North Star.

| # | Metric | Formula | Threshold | Owner |
|---|---|---|---|---|
| G1 | **Spam/abuse report rate** | Messages reported / Messages sent | < 0.5% (alert at 0.3%) | Trust & Safety |
| G2 | **Block rate** | Users blocked via messaging / Users who received a message | < 2% (alert at 1.5%) | Trust & Safety |
| G3 | **Core feature engagement (non-messaging)** | DAU on core product features, trailing 7d | No decline > 3% week-over-week | Product — Core |
| G4 | **App performance (p95 load time)** | p95 of screen load time, messaging screens | < 1.5s | Engineering |
| G5 | **Notification opt-out rate** | Users disabling message notifications / Users with notifications enabled | < 5% monthly | Engagement |

**G3 is critical.** If messaging cannibalises time from the core product loop without adding retention, it's a net negative. Monitor this from day one.

### 2c. Vanity Metrics — Explicitly Excluded

Do **not** use these to evaluate feature success:

| Metric | Why it's misleading |
|---|---|
| Total messages sent (cumulative) | Goes up by default. Tells you nothing about whether users are succeeding. |
| "Messaging DAU" without activation context | Counts people who opened the tab, not people who got value. |
| Average messages per user | Skewed by power users. Median is the relevant statistic. |
| Number of conversations created | One-sided conversations are not success. Use bidirectional count. |

---

## 3. Cohort & Retention Design

### Cohort definition

Group users by **messaging activation week** (the week they sent their first message). This is independent of product signup date — a user who signed up 6 months ago but just discovered messaging is a new messaging cohort member.

### Retention table structure

| Cohort | W0 | W1 | W2 | W4 | W8 | W12 |
|---|---|---|---|---|---|---|
| 2026-W15 | 100% | ? | ? | ? | ? | ? |
| 2026-W16 | 100% | ? | ? | ? | ? | ? |

**"Active" for retention purposes** = participated in at least one bidirectional conversation that week.

### Key questions to answer by W8 post-launch

1. **What is the retention floor?** If it stabilises above 15%, there is a retained core. Below 10%, the feature has a value problem.
2. **Which cohorts retain better?** Compare against product changes, onboarding experiments, channel mix.
3. **Who are the retained users?** Segment by: user tenure, plan type, use case, acquisition channel. Find the profile that retains and double down.

---

## 4. Instrumentation Plan

### 4a. Events to Track

Every event follows the schema: `event_name`, `timestamp`, `user_id`, `session_id`, `properties{}`.

| Event Name | Trigger | Key Properties |
|---|---|---|
| `messaging.entry_point_viewed` | User sees any messaging CTA or icon | `entry_point_location`, `variant` (for A/B) |
| `messaging.conversation_started` | User sends first message in a new conversation | `conversation_id`, `recipient_id`, `message_type` (text/image/file), `character_count`, `entry_point_source` |
| `messaging.message_sent` | Any message sent | `conversation_id`, `sender_id`, `recipient_id`, `message_type`, `character_count`, `is_reply` (bool), `reply_latency_seconds` (null if not a reply) |
| `messaging.message_read` | Recipient views a message | `conversation_id`, `message_id`, `reader_id`, `read_latency_seconds` |
| `messaging.notification_delivered` | Push/in-app notification sent | `conversation_id`, `notification_type` (push/in-app/email), `recipient_id` |
| `messaging.notification_tapped` | User taps a message notification | `conversation_id`, `notification_type`, `user_id` |
| `messaging.conversation_muted` | User mutes a conversation | `conversation_id`, `user_id`, `conversation_age_days` |
| `messaging.user_blocked` | User blocks another via messaging | `conversation_id`, `blocker_id`, `blocked_id`, `messages_exchanged_count` |
| `messaging.message_reported` | User reports a message | `conversation_id`, `message_id`, `report_reason`, `reporter_id` |
| `messaging.attachment_uploaded` | User attaches a file/image | `conversation_id`, `attachment_type`, `file_size_bytes` |

### 4b. Derived Tables (ETL)

Build these as daily-refreshed tables for dashboard and analysis use.

| Table | Grain | Key Columns | Purpose |
|---|---|---|---|
| `messaging_conversations_daily` | One row per conversation per day | `conversation_id`, `date`, `messages_sent`, `unique_participants_active`, `is_bidirectional` | Feeds North Star + I2, I5 |
| `messaging_user_daily` | One row per user per day | `user_id`, `date`, `conversations_active`, `messages_sent`, `messages_received`, `replies_sent`, `median_reply_time` | Feeds I1, I3, retention |
| `messaging_cohort_weekly` | One row per cohort per retention week | `activation_week`, `retention_week`, `cohort_size`, `active_users`, `retention_rate` | Feeds cohort analysis |
| `messaging_health_daily` | One row per day | `date`, `total_messages`, `spam_report_rate`, `block_rate`, `notification_optout_rate`, `p95_load_time` | Feeds guardrail dashboard |

### 4c. Data Quality Checks (Automated)

Run these daily before dashboards refresh. If any check fails, flag the dashboard as "data quality issue — investigating" rather than showing bad data.

| Check | Logic | Alert |
|---|---|---|
| Event volume drop | Today's `messaging.message_sent` count < 50% of 7-day trailing average | PagerDuty to data engineering |
| Null rate spike | Any event property null rate > 10% (vs. baseline < 2%) | Slack alert to data team |
| Duplicate events | COUNT != COUNT(DISTINCT event_id) on any event table | Slack alert to data team |
| Join key mismatch | `conversation_id` in `message_sent` not found in `conversation_started` > 1% | Slack alert to data team |
| Clock skew | `message_read.timestamp` < `message_sent.timestamp` for same message > 0.5% | Slack alert to engineering |

---

## 5. Dashboard Layout

### Primary dashboard: "Messaging Health" (daily review)

**Row 1 — North Star**
- Weekly bidirectional conversations (line chart, trailing 8 weeks)
- Week-over-week change (single number with directional arrow)

**Row 2 — Input metrics**
- Activation rate by cohort week (bar chart, sorted by value)
- Reply rate trailing 7d (line chart)
- Median time to first reply (line chart, lower is better)

**Row 3 — Guardrails**
- Spam report rate (line chart with red threshold line at 0.3%)
- Block rate (line chart with red threshold line at 1.5%)
- Core feature DAU (line chart, flagged if > 3% WoW decline)

### Secondary dashboard: "Messaging Cohorts" (weekly review)

- Retention triangle table (cohort rows × retention week columns)
- Retention curve overlay (line chart, one line per cohort)
- Segment breakdown of retained users (plan type, tenure, channel)

---

## 6. Launch Measurement Plan

### Pre-launch (1 week before)

- [ ] All events instrumented and verified in staging
- [ ] Derived tables built and back-tested with synthetic data
- [ ] Data quality checks running and alerting
- [ ] Dashboards built with placeholder data
- [ ] Baseline metrics captured for guardrails (G3, G4, G5)

### Launch week

- [ ] Monitor guardrails daily — any threshold breach triggers a review within 24h
- [ ] Verify event volumes match expected adoption curve
- [ ] Run data quality checks twice daily (morning + evening)
- [ ] Do **not** draw conclusions about North Star yet — sample size is insufficient

### Week 2–4

- [ ] First cohort retention data available (W1 retention for launch cohort)
- [ ] Publish first weekly business review using the format: what happened → why → what we're doing
- [ ] Identify early adopter profile from segment analysis

### Week 8+

- [ ] Sufficient data for retention floor estimate
- [ ] A/B test readiness for first optimisation experiment (power calculation based on observed baseline)
- [ ] Executive summary with three sentences: finding, implication, recommended action

---

## Executive Summary

**Finding:** This framework measures whether in-app messaging creates genuine two-way conversations (North Star: weekly bidirectional conversations), supported by five input levers the team controls and five guardrails that prevent growth-at-all-costs degradation.

**Implication:** Without this instrumentation, the team will default to tracking messages sent — a vanity metric that rewards spam and one-sided behaviour — and will be unable to distinguish a feature that connects users from one that annoys them.

**Recommended action:** Instrument all events listed in Section 4a before launch, build the derived tables and quality checks in the first sprint, and commit to the weekly review cadence starting launch week.
