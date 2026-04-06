### Community Automation

**Use when:** Setting up automated workflows for a new community, or reducing manual workload in an existing one. Automation handles the repetitive work so moderators can focus on humans.

**Gather:** Platform (Discord/Slack/Reddit/Circle/Discourse), current pain points (manual welcomes, repetitive questions, role management), existing bots/integrations, team technical capacity (can they write code or config-only?).

---

### Welcome Flow Design

A good welcome flow reduces lurker rate by 30-50%. The goal: get a new member to post their first message within 24 hours.

**Discord welcome flow (Carl-bot or custom bot):**

1. **Join trigger** → Bot assigns `@New` role (limited channel access)
2. **#rules channel** → Member reads rules, reacts with ✅
3. **Reaction trigger** → Bot removes `@New`, assigns `@Verified`, unlocks all channels
4. **Auto-DM** → Bot sends welcome message:

```
Welcome to [Community Name]! 👋

Here's how to get started:
1. Head to #introductions and tell us about yourself
2. Check out #resources for our top pinned content
3. Pick your interests in #role-select to see relevant channels

Questions? Ask in #help — someone will respond within a few hours.
```

5. **Auto-post in #mod-log** → "New verified member: @username — joined [date]"

**Slack welcome flow (Workflow Builder):**
- Trigger: member joins workspace → auto-post welcome message in #general → DM with workspace guide → prompt to post in #introductions
- Add a 48-hour follow-up DM: "Hey! Noticed you haven't posted yet — no pressure, but #introductions is a great place to start."

**Reddit:** No automated welcome for individual users. Instead: sticky a welcome post, configure AutoMod to comment on first-time posters' submissions with a welcome message and subreddit guide.

---

### FAQ Bot Setup

Stop answering the same questions manually. Identify the top 10-20 recurring questions and automate responses.

**Keyword trigger approach (Carl-bot / YAGPDB):**

```
Trigger: "how do I" + "join" OR "get started" OR "sign up"
Response: "Here's our getting started guide: [link]. If that doesn't answer your question, ask in #help!"

Trigger: "pricing" OR "how much" OR "cost"
Response: "Pricing info is here: [link]. For specific questions, reach out in #support."
```

**Forum/Discourse approach:** Create a FAQ category or knowledge base. Configure the "Search before posting" plugin to suggest existing answers when users type a new topic title.

**Rules for FAQ automation:**
- Always include a fallback: "If this didn't help, ask a human in #help"
- Review triggers monthly — questions change as the product/community evolves
- Don't automate nuanced questions — only clear-cut, factual answers
- Log which triggers fire most often — that's product/docs feedback

---

### Role Assignment Automation

**Reaction roles (Discord — Carl-bot):**
Create a #role-select channel with a message like:

```
React to get access to topic channels:
🎨 → #design
💻 → #engineering
📊 → #marketing
🎮 → #gaming
```

Carl-bot command: `!reactionrole create` → follow the setup wizard.

**Level-based roles (Discord — MEE6 or Arcane):**
- Level 5 (approx. 50 messages) → `@Active` role
- Level 15 (approx. 200 messages) → `@Regular` role
- Level 30 (approx. 500 messages) → `@Veteran` role

Attach perks to each level: @Active can post images, @Regular can use voice channels, @Veteran gets a custom colour. Perks must feel earned, not arbitrary.

**Verification automation:**
- Email-domain verification for company/org communities (Captcha.bot or custom)
- Phone verification for high-trust communities (Discord's built-in phone verification level)
- OAuth verification for product communities (link Discord account to product account)

---

### Alert and Notification Bots

**Mod alerts (high priority):**
- New member surge (10+ joins in 1 hour) → alert in #mod-chat — possible raid
- Spike in AutoMod actions (5+ in 10 minutes) → alert in #mod-chat
- User reported 3+ times in 24 hours → flag for immediate review

**Activity alerts (informational):**
- Daily summary: new members, messages sent, most active channels (Carl-bot or custom)
- Weekly digest: member growth, top contributors, engagement trend

**Platform setup:**
- Discord: Use Carl-bot logging or Dyno's modlog. Configure webhook-based alerts for custom events.
- Slack: Use Workflow Builder triggers or Zapier/Make for cross-platform alerts.
- Discourse: Built-in staff notifications handle most cases. Add webhooks for external alerting.

---

### Scheduled Messages

**Weekly recurring content:**
- Monday: Discussion prompt in #general ("What are you working on this week?")
- Wednesday: Resource share or tip of the week
- Friday: Open thread / casual chat / wins of the week

**Setup (Discord — Carl-bot):**
```
!autopost create #general
Interval: 7 days
Day: Monday
Time: 09:00 UTC
Message: "🧵 **Weekly check-in** — What are you working on this week? Drop a quick update below."
```

**Setup (Slack):** Workflow Builder → Scheduled trigger → Post message to channel.

**Setup (Discourse):** Use the Automation plugin to create recurring topics in specific categories.

---

### Integration Automation

Connect external tools to the community so information flows without manual copying.

| Integration | Source → Destination | Tool |
|---|---|---|
| GitHub notifications | New PR/issue → #dev channel | GitHub webhook or Zapier |
| Support tickets | New ticket created → #support-alerts | Zendesk/Intercom webhook |
| Blog posts | New post published → #announcements | RSS feed bot (MonitoRSS) |
| Social mentions | Brand mention on Twitter → #social-feed | Zapier + Twitter API |
| Calendar events | Upcoming event → #events reminder | Google Calendar bot |
| Form submissions | Application form → #applications | Google Forms + Zapier |

**Setup principle:** Every integration should post to a dedicated channel, never #general. Label automated messages clearly so members know what's bot-generated vs. human-posted.

---

### Bot Comparison Table

| Bot | Platform | Best For | Free Tier | Paid |
|---|---|---|---|---|
| Carl-bot | Discord | Reaction roles, automod, logging, embeds | Most features free | $5/mo premium |
| MEE6 | Discord | Levelling, auto-moderation, music | Basic features | $12/mo (aggressive upsell) |
| Dyno | Discord | Moderation, custom commands, auto-roles | Core features free | $5/mo premium |
| YAGPDB | Discord | Advanced automod, Reddit/YouTube feeds, custom commands | Fully free | Donation-based |
| Arcane | Discord | Levelling with XP curves, role rewards | Free | $5/mo premium |
| MonitoRSS | Discord | RSS feed delivery to channels | Fully free | Self-hosted option |
| Ticket Tool | Discord | Support ticket system with transcripts | Free for basic | $4/mo premium |

**Recommendation:** Start with Carl-bot for roles + automod + logging. Add YAGPDB if you need advanced custom commands. Avoid stacking multiple bots with overlapping functions — it creates conflicts and confuses members.

**Deliver:**
- Welcome flow configured and tested (join → verify → DM → first post)
- FAQ bot with 10-20 keyword triggers deployed
- Role assignment system (reaction or level-based) active
- Alert/notification system configured for mod team
- Scheduled messages set up for weekly content rhythm
- External integrations connected and posting to correct channels
- Documentation of all automation for handoff to other team members
