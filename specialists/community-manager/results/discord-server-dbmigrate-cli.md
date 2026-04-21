# Discord Server Blueprint: [DBMigrate CLI] Community

> Open-source database migration CLI — ~200 expected members
> Platform: Discord (free, excellent bot ecosystem, standard for OSS dev tools)
> Moderation model: Proactive (automod + active monitoring — right fit for a growing 100-500 member community where culture is still forming)

---

## 1. Server Settings

| Setting | Value |
|---|---|
| **Server name** | DBMigrate |
| **Description** | Open-source CLI for database migrations — help, discussion, and contributions |
| **Verification level** | Medium (must have a verified email + be registered on Discord for 5+ minutes) |
| **Default notifications** | Mentions only |
| **Explicit content filter** | Scan messages from all members |
| **2FA for moderators** | Yes |
| **Default channel** | #rules |
| **Community features** | Enable (for Server Discovery once you hit 500 members) |

---

## 2. Categories & Channels

```
📋 START HERE
  #rules              — Read-only. Community guidelines. React ✅ to verify.
  #introductions       — Post-only (slow mode 6h). New members say hello.
  #announcements       — Read-only. Releases, breaking changes, roadmap updates.

💬 GENERAL
  #general             — Main conversation. Anything about DBMigrate.
  #off-topic           — Non-project chat. Memes, career, etc.
  #show-and-tell       — Share your migration workflows, setups, and wins.

🔧 TECHNICAL
  #help                — Forum channel (threaded). Ask questions, get answers.
  #bugs                — Forum channel (threaded). Bug reports with repro steps.
  #feature-requests    — Forum channel (threaded). Propose improvements.
  #database-talk       — General DB discussion: Postgres, MySQL, SQLite, Mongo, etc.

🛠️ CONTRIBUTING
  #contributing        — Discussion about contributing to the project.
  #pull-requests       — GitHub webhook feed: new PRs, reviews, merges.
  #releases            — GitHub webhook feed: new releases and tags.

🔊 VOICE
  Voice Hangout        — Open voice channel for pairing / casual chat.
  Office Hours         — Stage channel for scheduled Q&A / contributor onboarding.

🔒 ADMIN (hidden from members)
  #mod-log             — Bot action logs (kicks, bans, warns, automod triggers).
  #mod-chat            — Private moderator discussion.
  #bot-commands        — Bot configuration and testing.
  #github-admin        — GitHub webhook feed for issues, CI status (mod-only).
```

### Channel notes

- **#help, #bugs, #feature-requests** use Discord's Forum channel type so each question/report becomes its own thread with tags. This prevents conversations from getting buried.
- **#pull-requests and #releases** are webhook-only channels (no member posting) — keeps signal clean.
- **Slow mode:** 6 hours on #introductions, 30 seconds on #general, none on #help.

### Forum channel tags

**#help tags:** `postgres`, `mysql`, `sqlite`, `mongo`, `cli-usage`, `configuration`, `ci-cd`, `resolved`

**#bugs tags:** `confirmed`, `cannot-reproduce`, `fixed`, `needs-info`, `regression`

**#feature-requests tags:** `under-discussion`, `planned`, `wont-fix`, `shipped`

---

## 3. Role Hierarchy

| Priority | Role | Color | Permissions | How Assigned |
|---|---|---|---|---|
| 1 | **Owner** | — | Full server permissions | You |
| 2 | **Admin** | `#E74C3C` Red | Manage channels, roles, bans, server settings | Manual (core maintainers only) |
| 3 | **Moderator** | `#E67E22` Orange | Kick, mute, timeout, manage messages, view mod channels | Manual (trusted community members) |
| 4 | **Maintainer** | `#9B59B6` Purple | Same as Contributor + can pin messages, manage threads | Manual (project maintainers / top contributors) |
| 5 | **Contributor** | `#3498DB` Blue | Send messages, react, voice, embed links, attach files | Reaction role (self-assign) or granted after merged PR |
| 6 | **Verified** | `#2ECC71` Green | Send messages, react, view all community channels | Bot-assigned after rule acceptance |
| 7 | **New** | `#95A5A6` Grey | Read-only; can only see #rules and #announcements | Auto-assigned on join |

### Permission matrix

| Permission | Owner | Admin | Mod | Maintainer | Contributor | Verified | New |
|---|---|---|---|---|---|---|---|
| Manage Server | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage Channels | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage Roles | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Kick Members | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Ban Members | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Timeout Members | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manage Messages | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Pin Messages | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Manage Threads | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Send Messages | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Embed Links | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Attach Files | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| View Channels | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | #rules only |

---

## 4. Community Rules

> Post this in **#rules** as an embed. Members react with ✅ to gain Verified role.

---

### Our Values

We're a community of developers who believe database migrations shouldn't be painful. We value clear documentation, honest bug reports, and helping each other ship reliable data changes. This is a space for learning, not gatekeeping.

### Rules

1. **Be respectful.** No personal attacks, harassment, or discrimination. Disagree with the idea, not the person.
2. **Stay on topic.** Use the right channels. Off-topic goes in #off-topic.
3. **No spam or self-promotion.** Don't advertise your product, course, or newsletter. Share relevant tools in #show-and-tell only.
4. **Search before asking.** Check #help threads, GitHub issues, and docs before posting a question. If you searched and still need help, say what you tried.
5. **Post useful bug reports.** Include: CLI version, database type + version, migration file (sanitised), full error output, and steps to reproduce.
6. **No NSFW content.** None. Zero.
7. **Protect privacy.** Don't share connection strings, credentials, or others' personal info. Sanitise your config before posting.
8. **Listen to moderators.** Mod decisions are final in the moment. Use the appeals process if you disagree.

### Enforcement

| Severity | First | Second | Third |
|---|---|---|---|
| Minor (off-topic, didn't search first) | Verbal warning | Written warning + redirect | 24h mute |
| Moderate (personal attacks, repeated spam, unsolicited DMs) | Written warning | 7-day mute | Temporary ban (14 days) |
| Severe (harassment, doxxing, hate speech, posting credentials) | Immediate temp ban (14 days) | Permanent ban | — |

### Reporting

- **React with 🚩** on the message to flag it for mods
- **DM a moderator** if the issue is sensitive
- All reports are confidential

### Appeals

DM any Admin with: what happened, why you disagree, and what you'd do differently. Appeals are reviewed within 48 hours by an Admin who wasn't involved in the original action.

---

## 5. Bots & Integrations

| Bot | Purpose | Key Config |
|---|---|---|
| **Carl-bot** | Reaction roles (✅ in #rules → Verified), automod, logging, custom commands | Reaction role on rules embed; log to #mod-log |
| **Dyno** | Moderation (warn, mute, ban with reason logging), auto-purge | Warning system with DM notifications; mod log integration |
| **GitHub Bot** | Webhook integration — PR/release/issue feeds to designated channels | Webhook URLs per channel: PRs → #pull-requests, releases → #releases, issues → #github-admin |
| **AnswerOverflow** | Indexes #help threads for Google — makes your Discord Q&A searchable on the web | Connect to #help forum channel |

### Why these bots

- **Carl-bot over MEE6**: No aggressive upselling, better reaction role UX, more reliable automod.
- **AnswerOverflow**: Critical for OSS — most users Google errors before joining Discord. Indexing your help threads means your community answers show up in search results. Free growth engine.
- **No leveling bot**: At 200 members, XP/leveling adds noise without value. Revisit at 500+.

---

## 6. Automod Configuration (Carl-bot)

```
# Spam: repeated messages
Trigger: Same message posted 3+ times in 60 seconds
Action: Delete all copies + 10-minute mute + log to #mod-log

# Discord invite links
Trigger: discord.gg/, invite.gg/, dsc.gg/
Action: Delete + warn (allowlist: your own server invite)

# Mass mentions
Trigger: @everyone, @here, or 5+ user mentions in one message
Action: Delete + warn

# New member link restriction
Trigger: Any URL from members with the "New" role (joined <24h ago)
Action: Hold for mod review

# Scam patterns
Trigger: "airdrop", "free nitro", "steam gift", "DM me for"
Action: Delete + mute + flag for review

# Credential leak protection
Trigger: Patterns matching connection strings, API keys, passwords
  - postgres://*, mysql://*, mongodb+srv://*
  - sk-*, AKIA*, ghp_*, glpat-*
Action: Delete immediately + DM member warning about credential exposure
```

---

## 7. Onboarding Flow

```
Member joins
  ↓
Lands on #rules (only visible channel)
  ↓
Reads rules → reacts with ✅
  ↓
Carl-bot assigns "Verified" role
  ↓
All community channels become visible
  ↓
Carl-bot sends welcome DM (see below)
  ↓
Member posts in #introductions (prompted by DM)
```

### Welcome DM template

```
👋 Welcome to the DBMigrate community!

You're verified — here's how to get started:

1. Say hello in #introductions — tell us what database you work with
   and what brought you here.
2. Got a question? Post it in #help (it's a forum — create a new thread).
3. Found a bug? Drop it in #bugs with your CLI version and error output.
4. Want to contribute? Check #contributing for good-first-issue picks.

Docs: [link to docs]
GitHub: [link to repo]
```

---

## 8. GitHub Webhook Setup

Create webhooks in your GitHub repo settings → Webhooks:

| Webhook | Events | Target Channel |
|---|---|---|
| PR feed | Pull request opened, closed, merged, review requested | #pull-requests |
| Release feed | Release published | #releases |
| Issue + CI feed | Issues opened/closed, check suite completed | #github-admin (mod-only) |

**Payload URL format:** Discord channel webhook URL (Settings → Integrations → Webhooks → New Webhook → select channel → copy URL).

Append `/github` to the webhook URL so Discord formats GitHub payloads correctly:
```
https://discord.com/api/webhooks/{id}/{token}/github
```

---

## 9. Seed Content (Post Before Launch)

Before inviting anyone beyond your core team, post these conversation starters:

| Channel | Post |
|---|---|
| #general | "Welcome to the DBMigrate Discord! We're the core team — ask us anything about the project, the roadmap, or database migrations in general." |
| #show-and-tell | "Here's our current CI/CD migration setup for the main project: [screenshot/description]. What does yours look like?" |
| #help | Seed thread: "FAQ: How do I roll back a failed migration?" — answer it yourself to model the format. |
| #help | Seed thread: "FAQ: How do I run migrations in CI/CD?" — answer with examples for GitHub Actions, GitLab CI, etc. |
| #database-talk | "What's your hot take on ORMs generating migrations vs writing them by hand? We'd love to hear the tradeoffs you've hit." |
| #feature-requests | Seed thread: "What's the #1 feature you wish DBMigrate had?" — shows you're listening. |
| #contributing | Pin a message: "New to contributing? Start here → [link to CONTRIBUTING.md]. These issues are tagged good-first-issue: [link]." |

---

## 10. Launch Checklist

### Pre-Launch (before any invites)
- [ ] Server created with settings from Section 1
- [ ] All categories and channels created per Section 2
- [ ] Forum channels configured with tags per Section 2
- [ ] Role hierarchy set up and permissions tested per Section 3
- [ ] Rules posted in #rules as an embed per Section 4
- [ ] Carl-bot installed: reaction role on #rules, automod rules active
- [ ] Dyno installed: warning system configured, logging to #mod-log
- [ ] GitHub webhooks connected to #pull-requests, #releases, #github-admin
- [ ] AnswerOverflow connected to #help
- [ ] Welcome DM tested end-to-end (join on alt account → react → check DM)
- [ ] Credential leak automod tested (post a fake `postgres://` string, verify it's deleted)
- [ ] At least 2 moderators recruited from core team and briefed on escalation tiers
- [ ] Server icon and banner uploaded

### Soft Launch (1-2 weeks, invite core contributors + early users)
- [ ] 5-10 seed members invited
- [ ] Seed content posted per Section 9
- [ ] All bot automations working (welcome DM, role assignment, webhook feeds)
- [ ] Moderation tested (mods can warn, mute, and actions log correctly)
- [ ] Channel structure validated — any unused channels? any missing?
- [ ] Feedback collected from seed members and adjustments made

### Public Launch
- [ ] Permanent invite link created (vanity URL if available: discord.gg/dbmigrate)
- [ ] Invite link added to: GitHub README, docs site, npm/crate/pip package page
- [ ] Launch announcement posted on Twitter/X, GitHub Discussions, relevant subreddits
- [ ] First 48 hours: at least one maintainer actively monitoring and responding
- [ ] Track: join rate, verification rate (react ✅), first-message rate, #help response time

### Week 1 Post-Launch
- [ ] Review automod false positives — adjust filters
- [ ] Check #help response time — target <4 hours during business hours
- [ ] Identify most active members as potential future moderators
- [ ] Run first "Office Hours" voice session with a maintainer

---

## 11. Ongoing Health Metrics

Track monthly starting from launch:

| Metric | Target (at 200 members) | How to Measure |
|---|---|---|
| DAU / MAU ratio | >15% (30+ daily active) | Discord Server Insights |
| Verification rate | >80% of joins react ✅ | Carl-bot logs vs join count |
| #help response time | <4 hours (business hours) | Manual spot-check or bot tracking |
| #help resolution rate | >70% threads marked resolved | Forum tag tracking |
| Member retention (30-day) | >60% still active after 30 days | Server Insights |
| Messages/day | 20-50 | Server Insights |
| Mod actions/week | <5 (low toxicity signal) | #mod-log count |

**Red flags to watch for:**
- Verification rate drops below 50% → rules too long or unclear
- #help threads going unanswered >24h → recruit more helpers or create a bot FAQ
- Messages/day drops consistently → run an event or AMA to re-engage
- Mod actions spike → investigate root cause (raid? one bad actor? unclear rule?)

---

*Generated by GTeam Community Manager — 2026-04-06*
