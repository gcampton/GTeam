### Moderation Framework

**Use when:** Setting up moderation for a new community, or when an existing community has inconsistent enforcement, rising toxicity, or moderator burnout.

**Gather:** Community platform, current member count, existing rules (if any), moderation team size, recurring problem types (spam, toxicity, self-promo, off-topic), any legal or compliance requirements (GDPR, COPPA if minors present).

---

### Rule Writing

Rules must be clear, specific, and enforceable. Vague rules like "be nice" or "use common sense" create inconsistent enforcement and invite arguments.

**Rule structure:** Each rule needs a name, a one-sentence definition, an example of a violation, and the consequence.

```markdown
**Rule 3: No unsolicited self-promotion**
Posting links to your own product, service, blog, or YouTube channel outside of #show-and-tell is not allowed. This includes indirect promotion ("I wrote a tool that does X, DM me").
*First offence: message removed + warning. Second offence: 24h mute. Third: 7-day ban.*
```

**Essential rules (adapt to your community):**
1. **Be respectful** — No personal attacks, slurs, or harassment. Disagreement is fine; insults are not.
2. **Stay on topic** — Use the right channel/category. Off-topic posts will be moved or removed.
3. **No spam** — No repeated messages, excessive emoji, or bot-like behaviour.
4. **No unsolicited self-promotion** — Share your work in designated channels only.
5. **No NSFW content** — Unless the community explicitly allows it in age-gated channels.
6. **No doxxing** — Never share someone's personal information without consent.
7. **Follow platform ToS** — Anything that violates the platform's terms violates ours.

Keep rules to 5-7. More than 10 and nobody reads them. Fewer than 4 and you lack enforcement basis.

---

### Escalation Tiers

Consistent escalation prevents favouritism and protects moderators from accusations of bias.

| Tier | Action | When | Duration | Reversible |
|---|---|---|---|---|
| 0 | Verbal nudge | First minor offence, clearly unintentional | N/A | N/A |
| 1 | Written warning | First clear rule violation, or repeated minor offence | Permanent record | N/A |
| 2 | Mute/timeout | Second violation within 30 days, or disruptive behaviour | 1-24 hours | Auto-expires |
| 3 | Temporary ban | Third violation within 60 days, or serious single offence | 7-30 days | Manual review |
| 4 | Permanent ban | Doxxing, threats, illegal content, or 3+ temp bans | Permanent | Appeal only |

**Immediate Tier 4 offences (no escalation):** Doxxing, credible threats of violence, sharing illegal content (CSAM, piracy of community content), brigading/raiding.

---

### Automod Configuration

**Discord (built-in AutoMod + Carl-bot):**
- Block messages containing slurs (use a maintained keyword list, not just the obvious ones)
- Flag messages with 3+ links for moderator review
- Auto-delete messages from accounts younger than 24 hours in non-welcome channels
- Rate-limit: max 5 messages per 10 seconds per user
- Carl-bot: log all deleted messages and edits to #mod-log

**Reddit AutoMod (YAML):**
```yaml
# Remove posts from new/low-karma accounts
type: submission
author:
  account_age: "< 7 days"
  combined_karma: "< 10"
action: remove
action_reason: "New/low-karma account"
comment: "Your post was removed because your account is too new. Please participate in comments first."

# Flag self-promotion
type: submission
domain+body: [youtu.be, youtube.com, medium.com, substack.com]
action: filter
action_reason: "Potential self-promotion — mod review"
```

**Slack:** Install the Slack Moderation app or configure custom Workflow Builder rules to flag messages with banned keywords and route them to an admin channel.

---

### Moderator Recruitment and Training

**Recruitment criteria:** Active for 3+ months, consistently helpful, calm under pressure, no history of warnings. Never recruit someone who asks to be a mod unprompted — look for people who are already moderating informally.

**Training checklist:**
- [ ] Read all community rules and escalation tiers
- [ ] Shadow an existing mod for 1 week (observe, don't act)
- [ ] Handle 5 mock scenarios (spam, argument, self-promo, edge case, appeal)
- [ ] Learn the moderation tools (bot commands, platform admin panel)
- [ ] Understand what to escalate (threats, legal issues, doxxing → admin immediately)

**Mod team size rule of thumb:** 1 active moderator per 500 active members. "Active" means checking in daily and handling reports within 4 hours during waking hours.

---

### Appeals Process

Every permanent ban and contested action should have an appeal path. This protects the community from mod mistakes and gives banned members a fair hearing.

**Appeal flow:**
1. Banned user submits appeal via a Google Form or dedicated email (not DM — DMs create pressure on individual mods)
2. Appeal reviewed by a mod who was not involved in the original action
3. Decision within 72 hours: uphold, reduce, or reverse
4. Outcome communicated to the user with a one-sentence explanation
5. All appeals logged regardless of outcome

---

### Handling Specific Situations

**Spam:** Delete and ban immediately. No warnings for bot spam. For human spam (persistent self-promo), follow escalation tiers.

**Harassment:** Remove the content, mute the harasser, DM the target to check in. If the harassment includes threats or doxxing, permanent ban immediately and screenshot evidence before deletion.

**Doxxing:** Delete immediately, permanent ban, notify the affected person, report to the platform. Do not engage with the doxxer.

**Brigading:** Lock affected channels temporarily, enable slow mode, ban obvious raiders, post a mod message acknowledging the situation. Contact platform trust & safety if it's organised.

**NSFW content:** Remove immediately from non-designated channels. If the community has no NSFW channels, warn → ban. If it involves minors, permanent ban and report to the platform and relevant authorities.

**Self-promotion:** Move to the appropriate channel with a note. If repeated, escalate per tiers.

---

### Moderation Log Template

Every action should be logged. Use a spreadsheet, Notion database, or bot logging channel.

```markdown
| Date | Moderator | User | Action | Rule Violated | Context | Notes |
|---|---|---|---|---|---|---|
| 2025-01-15 | @mod1 | @user123 | Written warning | Rule 4 (self-promo) | Posted YouTube link in #general | First offence, redirected to #show-and-tell |
```

**Deliver:**
- Complete rule set (publish-ready for your platform)
- Escalation tier document for moderator reference
- Automod configuration (platform-specific, ready to deploy)
- Moderator recruitment criteria and training checklist
- Appeals process document
- Moderation log template (spreadsheet or database)
