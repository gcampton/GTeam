# Discord Server Setup: DB Migration CLI — Open Source Community

**Platform:** Discord (free, excellent bot ecosystem, standard for dev tool communities)
**Expected size:** ~200 members (developer-focused)
**Purpose:** User support, bug reports, feature discussion, contributor coordination

---

## Server Info

| Setting | Value |
|---|---|
| Name | `[ToolName] Community` |
| Description | Open-source CLI for database migrations — support, discussion, and contributions |
| Verification Level | Medium (must have a verified email) |
| Default Notifications | Mentions only |
| Explicit Content Filter | Scan messages from members without roles |
| 2FA for Moderators | Yes |
| Default Channel | #rules |
| Community Features | Enable (allows Server Discovery later) |

---

## Categories & Channels

```
📋 START HERE
  #rules             — Read-only. Community guidelines. React ✅ to verify.
  #introductions     — Say hello, what DB stack you use, what brought you here.
  #announcements     — Read-only. Releases, breaking changes, roadmap updates.

💬 GENERAL
  #general           — Main conversation. Migrations, databases, CLI tools.
  #off-topic         — Non-project chat. Tech, careers, memes.
  #show-and-tell     — Share your migration workflows, custom scripts, integrations.

🔧 SUPPORT (Forum Channels)
  #help              — Forum channel. Ask questions, tag resolved when answered.
  #bug-reports       — Forum channel. Reproduction steps required (template enforced).
  #feature-requests  — Forum channel. Describe the use case, not just the feature.

📦 DEVELOPMENT
  #contributing      — How to contribute. Good first issues. PR discussion.
  #architecture      — Design decisions, RFCs, schema design patterns.
  #releases          — Automated release notes via GitHub webhook.

🔊 VOICE
  Voice Hangout      — Open drop-in voice channel.
  Office Hours       — Stage channel for scheduled Q&A sessions.

🔒 ADMIN (hidden from members)
  #mod-log           — Carl-bot action log (kicks, bans, warnings).
  #mod-chat          — Private moderator discussion.
  #bot-config        — Bot testing and configuration.
  #github-feed       — GitHub webhook: new issues, PRs, releases.
```

**Channel notes:**
- **Forum channels** for #help, #bug-reports, and #feature-requests — threads keep questions organized, prevent scroll burial, and allow "Resolved" tags. This is critical for a support-heavy dev tool community.
- **#releases** uses a GitHub webhook (repo → Settings → Webhooks → Discord webhook URL) to auto-post new releases. Zero maintenance.
- **#contributing** should be pinned with: contributor guide link, "good first issue" filter URL, and local dev setup steps.

---

## Role Hierarchy

| Priority | Role | Color | Permissions | Assignment |
|---|---|---|---|---|
| 1 | Owner | — | Full server management | You |
| 2 | Maintainer | `#E74C3C` Red | Manage channels, roles, bans, server settings | Manual — core maintainers only |
| 3 | Moderator | `#E67E22` Orange | Kick, mute, timeout, manage messages, manage threads | Manual — trusted community members |
| 4 | Contributor | `#3498DB` Blue | Send messages, embed links, attach files, use voice, create threads | Manual — merged a PR (verified via GitHub) |
| 5 | Verified | `#2ECC71` Green | Send messages, react, use voice, view all public channels | Bot — reaction role on #rules ✅ |
| 6 | New | `#95A5A6` Gray | View #rules and #announcements only | Auto on join |

**Permission matrix:**

| Permission | Owner | Maintainer | Moderator | Contributor | Verified | New |
|---|---|---|---|---|---|---|
| Manage Server | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Manage Channels | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manage Roles (below own) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Kick/Ban | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Timeout Members | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Manage Messages | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Manage Threads | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Create Public Threads | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Send Messages | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Embed Links / Attach Files | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Add Reactions | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| View Channels | ✅ | ✅ | ✅ | ✅ | ✅ | #rules, #announcements only |

---

## Verification & Onboarding Flow

```
New member joins
  → Sees only #rules and #announcements (New role)
  → Reads rules in #rules
  → Reacts with ✅ on the rules message
  → Carl-bot removes New role, assigns Verified role
  → All community channels become visible
  → Carl-bot sends Welcome DM (see below)
  → Member prompted to post in #introductions
```

### Welcome DM

```
Welcome to [ToolName] Community!

Here's how to get started:

📖 Need help? Post in #help — use a descriptive title and include:
   - Your DB engine (Postgres, MySQL, SQLite, etc.)
   - CLI version (toolname --version)
   - The error message or unexpected behavior

🐛 Found a bug? Post in #bug-reports with repro steps.

💡 Want a feature? Describe your use case in #feature-requests.

🔨 Want to contribute? Check #contributing for good first issues.

Introduce yourself in #introductions — we'd love to know what stack you're working with!
```

---

## Bots

| Bot | Purpose | Config Notes |
|---|---|---|
| **Carl-bot** | Reaction roles (✅ verification), automod, welcome DM, logging | Free tier covers all needs at 200 members. Set up reaction role on #rules message. Log to #mod-log. |
| **GitHub Bot** (Discord webhook) | Post new releases, issues, and PRs to #releases and #github-feed | Repo → Settings → Webhooks → Add Discord webhook URL. Filter events to releases + issues + PRs. |
| **Discohook** (or Carl-bot embeds) | Rich embed messages for #rules, #announcements | Use for formatted rules post with the ✅ reaction target. |

**Why no MEE6 or Dyno?** For a 200-member dev community, Carl-bot alone handles automod, reaction roles, welcome DMs, and logging. Adding more bots creates config sprawl with no benefit. Add Dyno later only if you need timed announcements or more granular logging.

---

## Automod Rules (Carl-bot)

| Rule | Action | Rationale |
|---|---|---|
| Spam: 5+ identical messages in 10 seconds | Delete + 10-minute timeout | Prevents bot spam and raids |
| Discord invite links (except allowlist) | Delete + warn | Prevents server advertising |
| @everyone / @here by non-mods | Block | Prevents notification abuse |
| Mention spam: 4+ user mentions in one message | Delete + warn | Prevents targeted harassment |
| Link filter for New role | Block all links | New (unverified) members cannot post links |
| Excessive caps (70%+ caps, 10+ chars) | Warn | Keeps conversations readable |
| Slur / hate speech word list | Delete + immediate ban | Zero tolerance |

---

## Community Rules

Post this as a rich embed in #rules using Carl-bot or Discohook. Pin it. Set the ✅ reaction on it.

---

### [ToolName] Community Rules

**We're a community of developers building and using [ToolName] for database migrations. We value clear communication, helping each other debug, and shipping reliable software.**

**1. Be respectful.** No personal attacks, harassment, or discrimination. Critique code and ideas, not people.

**2. Stay on topic.** Use the right channels. Migration questions go to #help. Random chat goes to #off-topic.

**3. No spam or self-promotion.** Don't DM members unsolicited. Share your projects in #show-and-tell only.

**4. Write good questions.** Include your DB engine, CLI version, error message, and what you've already tried. "It doesn't work" is not a question.

**5. No NSFW content.** This is a professional developer community.

**6. Protect privacy.** No doxxing. No sharing DMs without consent.

**7. Listen to moderators.** Mod decisions are final. Appeal via DM to any Maintainer.

### Enforcement

| Severity | First | Second | Third |
|---|---|---|---|
| Minor (wrong channel, mild spam) | Verbal warning | Written warning | 24-hour mute |
| Moderate (personal attacks, repeated spam) | Written warning | 7-day mute | Temporary ban (30 days) |
| Severe (harassment, doxxing, hate speech, raids) | Immediate ban | — | — |

### Reporting

- **React with 🚩** on any rule-breaking message to flag it for mods.
- **DM a Moderator or Maintainer** for sensitive issues.
- All reports are confidential.

*Last updated: 2026-04-06*

---

## Seed Content (Post Before Launch)

Populate these channels so the server isn't empty when the first members arrive:

| Channel | Seed Post |
|---|---|
| #announcements | "Welcome to the [ToolName] community! We just launched this Discord — introduce yourself in #introductions and let us know what DB you're migrating." |
| #general | "What database engine are you using [ToolName] with? We'd love to know what stacks our users are running." |
| #help | (Forum post) "Example: How to roll back a migration on Postgres 15 — [include answer as a template for question quality]" |
| #show-and-tell | "Here's our CI/CD pipeline setup using [ToolName] with GitHub Actions — [link to docs or gist]" |
| #contributing | Pin: contributor guide, good-first-issues link, local dev setup, and code of conduct link. |
| #architecture | "We're considering [design decision]. Here's the RFC — thoughts?" |

---

## Launch Checklist

### Pre-Launch (before any invites)
- [ ] Server created with settings from Server Info table above
- [ ] All categories and channels created with correct descriptions
- [ ] Role hierarchy configured; permissions tested per matrix
- [ ] Carl-bot installed: reaction role on #rules, welcome DM, automod rules, logging to #mod-log
- [ ] GitHub webhook configured for #releases and #github-feed
- [ ] Rules embed posted in #rules with ✅ reaction
- [ ] Welcome DM tested (join with alt account or have a friend test)
- [ ] Verification flow tested end-to-end (join → see only #rules → react → get Verified → see all channels)
- [ ] 2+ moderators recruited and briefed on enforcement table
- [ ] 5-10 seed members invited (maintainers, early users, friends)
- [ ] Seed content posted in 4+ channels

### Soft Launch (1-2 weeks, invite-only)
- [ ] Seed members active and giving feedback
- [ ] Channel structure validated — drop unused channels, add missing ones
- [ ] Bot automation confirmed working (DMs send, roles assign, logs appear)
- [ ] Moderation tested — mods can timeout, warn, and ban
- [ ] Adjusted based on feedback

### Public Launch
- [ ] Permanent invite link created (vanity URL if eligible: discord.gg/toolname)
- [ ] Link added to: GitHub README, project website, docs footer, social profiles
- [ ] Launch announcement: tweet/post, GitHub discussion, mailing list
- [ ] First 48 hours: maintainers actively present, respond to every intro
- [ ] Track: join rate, verification rate (reacted / joined), first-message rate
- [ ] 1-week retrospective: what's working, what needs adjusting

---

## Growth Targets (200-member horizon)

| Metric | Target | How to Measure |
|---|---|---|
| Verification rate | >80% (of joins complete ✅ verification) | Carl-bot logs: Verified role assignments / joins |
| First-message rate | >50% (of Verified members post at least once) | Manual check or bot command |
| DAU/MAU ratio | >15% (30+ members active daily) | Discord Server Insights (available at 500+ members; estimate manually before then) |
| #help response time | <4 hours for first response | Spot check forum posts weekly |
| Contributor pipeline | 2-3 new contributors per month | Track #contributing → merged PRs |

---

## Post-Launch: Monthly Health Check

1. **Activity**: Are conversations happening daily? Which channels are dead?
2. **Support quality**: Are #help posts getting answered? Average time to first response?
3. **Moderation load**: How many incidents per week? Is automod catching most spam?
4. **Growth**: New joins per week? Verification rate holding?
5. **Contributor pipeline**: Anyone moving from user → contributor?

If a channel has zero posts in 30 days, archive it. If #help is overwhelmed, consider adding a "Community Helper" role for active answerers. If growth stalls, cross-post the invite link in relevant developer communities (Hacker News Show threads, relevant subreddits, Twitter/X).
