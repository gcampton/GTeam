### Platform Selection

**Use when:** Launching a new community or migrating an existing one. The platform decision is hard to reverse — get it right first.

**Gather:** Community purpose (support, learning, networking, product feedback), target audience, expected member count (0-100, 100-1K, 1K-10K, 10K+), budget, team capacity (dedicated community manager vs. part-time).

**Platform decision matrix:**

| Platform | Best For | Max Scale | Cost | Moderation Tools |
|---|---|---|---|---|
| Discord | Gaming, tech, crypto, dev communities | 10K-100K+ | Free (Nitro optional) | Excellent (bots, automod, roles) |
| Slack | B2B, professional, internal teams | 100-5K | Free tier limited; paid $7.25/user/mo | Basic (channels, apps) |
| Reddit | Public discussion, topical communities | Unlimited | Free | Good (automod, community mods) |
| Circle | Paid communities, courses, memberships | 100-10K | $39-399/mo | Moderate (spaces, member tiers) |
| Discourse | Open-source, technical docs, long-form | 1K-100K+ | Self-hosted free; hosted $50-300/mo | Excellent (trust levels, plugins) |

**Selection rules:**
- If the community monetises directly (courses, memberships) → Circle or Discourse
- If the audience is developers or gamers → Discord
- If you need real-time chat for a B2B product → Slack
- If discoverability matters more than depth → Reddit
- If you need threaded long-form discussions → Discourse
- If budget is zero and scale is unknown → Discord

---

### Discord Server Setup

**Category and channel structure:**

```
📋 START HERE
  #rules (read-only — members must react ✅ to get Verified role)
  #introductions (post-only, no replies — keeps it clean)
  #announcements (read-only, admin-posted)

💬 COMMUNITY
  #general
  #off-topic
  #show-and-tell (members share what they're working on)

📚 TOPICS (adapt to your domain)
  #topic-1
  #topic-2
  #resources (curated links, pinned messages)

❓ SUPPORT
  #help (or use forum channel for threaded questions)
  #feedback

🔊 VOICE
  #voice-hangout
  #events (stage channel for AMAs)

🔒 ADMIN (hidden from members)
  #mod-chat
  #mod-log
  #bot-config
```

**Channel naming:** All lowercase, hyphens between words, no special characters. Prefix with emoji only at category level.

**Role hierarchy (top to bottom):**
1. **Owner** — full permissions, server settings
2. **Admin** — manage channels, roles, bans; cannot delete server
3. **Moderator** — kick, mute, timeout, manage messages; cannot manage roles
4. **Verified** — full access to all community channels
5. **New** — default role on join; can only see #rules and #announcements

**Permission matrix:**

| Permission | Owner | Admin | Mod | Verified | New |
|---|---|---|---|---|---|
| Manage Server | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manage Channels | ✅ | ✅ | ❌ | ❌ | ❌ |
| Manage Roles | ✅ | ✅ | ❌ | ❌ | ❌ |
| Kick/Ban Members | ✅ | ✅ | ✅ | ❌ | ❌ |
| Timeout Members | ✅ | ✅ | ✅ | ❌ | ❌ |
| Manage Messages | ✅ | ✅ | ✅ | ❌ | ❌ |
| Send Messages | ✅ | ✅ | ✅ | ✅ | ❌ |
| View Channels | ✅ | ✅ | ✅ | ✅ | #rules only |

**Verification flow:** New member joins → lands in #rules (only visible channel) → reads rules → reacts with ✅ → bot assigns Verified role → full access unlocked → bot DMs welcome message with intro prompt.

**Essential bots:**
- **Carl-bot** — reaction roles, automod, logging, custom commands. Preferred over MEE6 (less aggressive upselling).
- **Dyno** — moderation (warnings, mutes, bans with reason logging), auto-purge, announcements.
- **Ticket Tool** — support ticket system if the community handles user issues.

---

### Slack Workspace Setup

**Channel structure:** `#general`, `#introductions`, `#random`, `#announcements` (admin-post-only), topic channels prefixed with `topic-` (e.g., `#topic-engineering`), `#help`, `#feedback`. Use `#admin-` prefix for internal channels.

**Naming convention:** Lowercase, hyphens, verb or noun prefix: `help-billing`, `topic-frontend`, `announce-releases`.

**Onboarding:** Use Slackbot custom responses for common questions. Set up a Workflow Builder flow: new member joins → auto-post welcome message in #general → DM with workspace guide → prompt to post in #introductions.

---

### Reddit Subreddit Setup

**Creation checklist:** Subreddit name (short, memorable, no hyphens), description (160 chars), sidebar rules (5-7 rules max), post flair (at least: Discussion, Question, Resource, Meta), user flair (optional role indicators), wiki page with FAQ and resources.

**AutoMod essentials:** Minimum account age filter (7 days), minimum karma filter (10 comment karma), banned domain list, self-promotion ratio enforcement (9:1 rule), new-user comment hold for manual approval.

---

### Forum Setup (Circle / Discourse)

**Circle:** Create spaces by topic, not by content type. Enable member tiers if monetising. Set notification defaults to "weekly digest" — daily is too aggressive for forums. Pin an introductions thread in the main space.

**Discourse:** Use trust levels (0-4) as-is — they're well-designed. Categories map to topics. Enable Solved plugin for Q&A categories. Set up "New User of the Month" badge. Configure digest emails: weekly for active users, monthly for lurkers.

**Deliver:**
- Fully configured server/workspace/subreddit/forum (or setup instructions if you lack admin access)
- Channel/category structure documented in a pinned message or wiki
- Role hierarchy and permissions documented for future moderators
- Verification or onboarding flow tested end-to-end
- Bot/integration list with purpose of each
