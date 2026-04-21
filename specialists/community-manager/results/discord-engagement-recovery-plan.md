# Discord Community Health Diagnosis & Recovery Plan

**Date:** 2026-04-06
**Community size:** ~2,000 members
**Platform:** Discord

---

## Current Health Assessment: URGENT

| Metric | 3 Months Ago | Now | Change | Status |
|---|---|---|---|---|
| Messages/day | 500 | 300 | -40% | RED |
| New member 7-day retention | 45% | 20% | -56% relative | RED |
| Implied DAU/MAU | ~25% (est.) | ~15% (est.) | Declining | RED |

Both headline metrics have crossed from "healthy" into "unhealthy" territory simultaneously. This is not a single-cause problem — it's a compounding failure loop:

**Fewer active members → less content → slower response to newcomers → newcomers leave → fewer active members.**

---

## Root Cause Diagnosis

### 1. Onboarding Failure (Primary — drives retention collapse)

7-day retention dropping from 45% to 20% means **4 out of 5 new members leave within a week**. The most likely causes:

- **No response to first posts.** With engagement down 40%, new members posting intros or questions are hitting silence. A first message that gets no reply within 2 hours is effectively a "this community is dead" signal.
- **Broken or absent welcome flow.** If there's no automated onboarding (welcome DM, intro channel prompt, guided first steps), new members don't know what to do or where to go.
- **Channel overwhelm.** Too many channels with low activity make the server look like a ghost town. New members see 20+ empty channels and leave.

### 2. Power User Disengagement (Secondary — drives message volume drop)

A 200 message/day drop doesn't come from casual members leaving. In most 2,000-member communities, **10-15 power users generate 30-50% of all messages.** If 3-5 of those people went quiet, that alone accounts for the volume drop.

Likely causes:
- **Key contributors churned** — left the community, got busy, or moved to a competitor community
- **Content fatigue** — same discussions repeating, no fresh topics or events to drive engagement
- **Culture shift** — if moderation became inconsistent or a few toxic members drove good people out

### 3. No Engagement System (Structural)

Communities without a content cadence (scheduled events, themed days, discussion prompts) are entirely dependent on organic conversation. When organic conversation dips — for any reason — there's nothing to catch the fall.

---

## 30-Day Recovery Plan

### Week 1: Stop the Bleeding (Days 1-7)

**Goal:** Fix onboarding and consolidate activity so the server feels alive.

| Action | Owner | Detail |
|---|---|---|
| **Audit channels** | Admin | Identify every channel with <5 messages/week. Archive or merge them. Goal: cut channel count by 30-50%. Concentrate activity into fewer, busier channels. |
| **Fix welcome flow** | Admin | Set up Carl-bot or equivalent: auto-role on join → welcome channel ping → DM with 3 steps (read rules, post intro, join one topic channel). Add 48-hour follow-up DM for silent members. |
| **Assign Welcomer role** | Admin | Recruit 3-5 active members. Their job: reply to every intro post within 2 hours, react to new member messages, pull them into conversations. Give them a visible role colour. |
| **DM 10 churned power users** | Admin | Personal, non-templated DMs to your most active members from 3 months ago who've gone quiet. Ask: "Hey — noticed you've been quiet. What changed? Anything we could do better?" Listen to the answers. |
| **Post "State of the Community"** | Admin | Transparent message in #announcements: "We've noticed things have been quieter. Here's what we're doing about it. We want your input." Honesty builds trust. |

### Week 2: Inject Energy (Days 8-14)

**Goal:** Create reasons to come back. Break the cycle of "nothing's happening so why visit."

| Action | Owner | Detail |
|---|---|---|
| **Launch themed days** | Mod team | Pick 2-3 days/week with consistent prompts. Examples: "Show & Tell Monday" (share what you're working on), "Question Wednesday" (ask anything), "Feedback Friday" (get feedback from the community). Post prompts at the same time each day. |
| **Schedule first event** | Admin | One AMA or workshop within 14 days. Invite an expert the community respects. Promote it 7 days in advance. Create a dedicated event thread. |
| **Seed conversations daily** | Mod team | Every day, at least 2 team members post genuine discussion starters in topic channels. Not "How's your day?" — specific, opinion-provoking questions relevant to the community's focus. |
| **Launch a time-limited challenge** | Admin | 7-day challenge related to the community's topic. Leaderboard resets after the week. Low barrier to entry (e.g., "share one tip per day"). Small prize for top 3 (role badge, shoutout, gift card). |

### Week 3: Build Systems (Days 15-21)

**Goal:** Move from manual effort to sustainable automation.

| Action | Owner | Detail |
|---|---|---|
| **Set up FAQ bot** | Admin | Identify the 10 most-asked questions from the past 3 months. Configure a bot (Carl-bot tags, or a custom slash command) to answer them instantly. Reduces unanswered-question frustration. |
| **Implement engagement tracking** | Admin | Set up Statbot or Server Insights dashboard tracking: daily messages, active users, new joins, retention. Review weekly. |
| **Create content calendar** | Mod team | Plan 4 weeks of content: 2-3 themed days/week, 2 events/month, 1 member spotlight/week. Assign owners for each item. |
| **Launch contributor recognition** | Admin | Monthly contributor spotlight in #announcements. Identify top 5 helpers and give them public thanks + a special role. Achievement-based, not volume-based. |

### Week 4: Measure & Adjust (Days 22-30)

**Goal:** Check what's working, kill what isn't, double down on wins.

| Action | Owner | Detail |
|---|---|---|
| **Run first health report** | Admin | Full metrics review using the health report template. Compare all metrics to Day 0 baseline. |
| **Collect member feedback** | Admin | Post a 3-question survey: (1) What do you enjoy most here? (2) What would you change? (3) What content/events do you want? |
| **Review themed days** | Mod team | Which themed days got engagement? Keep those, replace the ones that flopped. |
| **Adjust channel structure** | Admin | Based on 3 weeks of data, further consolidate or split channels as needed. |
| **Plan Month 2** | Admin | Based on results, create next month's content calendar and event schedule. |

---

## Success Targets (30 Days)

| Metric | Current | 30-Day Target | Stretch |
|---|---|---|---|
| Messages/day | 300 | 400 | 450 |
| 7-day new member retention | 20% | 35% | 40% |
| Welcomer response time (intros) | Unknown | <2 hours | <1 hour |
| Events held | 0/month | 2 | 3 |
| Channels archived | — | 30-50% of inactive | — |

---

## Critical Watch Items

1. **Power user responses.** If DMs to churned power users reveal a culture problem (toxicity, cliques, mod inconsistency), that must be addressed before engagement tactics will work. No amount of events fixes a hostile environment.

2. **Don't over-program.** The goal is 2-3 structured touchpoints per week, not a schedule so packed it feels corporate. Leave room for organic conversation.

3. **Mod capacity.** This plan requires consistent effort from 3-5 people for 30 days. If the mod team is burned out or understaffed, recruit before executing. One mod per 500 active members minimum.

4. **Avoid vanity metrics.** Member count doesn't matter. Don't run a "invite your friends" campaign to inflate numbers. Focus entirely on activating the 2,000 you already have.

---

## If This Doesn't Work After 30 Days

If retention hasn't improved by Week 4, escalate to a deeper intervention:

- **Run 1:1 calls with 5 members** (mix of active, semi-active, churned) to understand the qualitative experience
- **Consider a community reset**: rename channels, refresh rules, relaunch with a "new era" framing
- **Evaluate platform fit**: if the audience has moved to another platform (e.g., a competing Discord, a subreddit, a Telegram group), follow them rather than fighting the migration
