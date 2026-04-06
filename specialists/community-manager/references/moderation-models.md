# Moderation Models

## Three Approaches

### 1. Reactive Moderation
**How it works:** Moderators respond to user reports and flagged content. No proactive monitoring.

**Pros:**
- Low effort — only act when problems surface
- Respects member autonomy — community self-polices
- Works for small, mature, high-trust communities

**Cons:**
- Problems fester before reports come in
- Toxic culture can establish before you notice
- Silent members leave rather than report — survivorship bias
- Creates perception that "anything goes" until someone complains

**Best for:** Small communities (<100 members) with established norms and high trust.

### 2. Proactive Moderation
**How it works:** Automod filters + active moderator monitoring of channels. Moderators read channels regularly and intervene early.

**Pros:**
- Catches issues before they escalate
- Sets clear tone from day one
- Automod handles high-volume, low-judgment tasks (spam, slurs, invite links)
- Consistent enforcement builds trust

**Cons:**
- Requires moderator time investment (1-2 hours/day for active communities)
- Automod false positives can frustrate members
- Risk of over-moderation creating a "walking on eggshells" atmosphere

**Best for:** Growing communities (100-5,000 members) where culture is still forming.

### 3. Community-Led Moderation
**How it works:** Trained volunteer moderators drawn from the community. Mod team has guidelines, escalation paths, and regular syncs. Core team handles appeals and policy.

**Pros:**
- Scales with community growth
- Mods understand community culture from the inside
- Members feel ownership and investment
- Distributes workload across time zones

**Cons:**
- Requires investment in mod recruitment, training, and retention
- Volunteer burnout is real — plan for rotation
- Inconsistent enforcement if training gaps exist
- Power dynamics can create cliques or mod abuse

**Best for:** Large communities (5,000+ members) that need 24/7 coverage.

## Escalation Tier Table

| Level | Action | Criteria | Duration | Who Decides | Reversible |
|---|---|---|---|---|---|
| 0 | Verbal warning | First minor offence, clearly unintentional | N/A | Any mod | N/A |
| 1 | Written warning | Repeated minor offence or first moderate offence | Logged permanently | Any mod | N/A |
| 2 | Mute / timeout | Continued behaviour after warning, heated argument | 1-24 hours | Any mod | Auto-expires |
| 3 | Extended mute | Pattern of moderate offences (3+ warnings) | 7 days | Senior mod | On appeal |
| 4 | Temporary ban | Severe single offence or chronic moderate offences | 14-30 days | Senior mod + admin | On appeal |
| 5 | Permanent ban | Harassment, doxxing, hate speech, illegal content, or return after temp ban with same behaviour | Indefinite | Admin only | Appeal after 6 months |

**Key principles:**
- Always DM the member explaining the action and citing the specific rule violated
- Log every action in #mod-log with: member, action, reason, evidence (screenshot/link), mod who acted
- Two-mod rule for Level 4+: a second moderator must confirm before temp/perm bans
- Appeals go to someone other than the mod who took the action

## Automod Pattern Library

### Spam Detection
```
# Repeated messages (flood)
Trigger: Same message posted 3+ times in 60 seconds
Action: Delete + mute 10 minutes

# Invite links
Trigger: discord.gg/, invite.gg/, dsc.gg/ (except allowlisted servers)
Action: Delete + warn

# Mass mentions
Trigger: @everyone, @here, or 5+ user mentions in one message
Action: Delete + warn (unless role has permission)
```

### Content Filtering
```
# Slur filter
Trigger: Regex word-boundary match against slur list
Action: Delete + log + auto-warn
Note: Maintain and review list quarterly. Include common evasions (leetspeak, zero-width chars)

# NSFW detection
Trigger: Known NSFW domain list + image scanning bot (if available)
Action: Delete + warn

# Excessive caps
Trigger: >70% uppercase in messages >20 characters
Action: Soft warning (bot reply, no delete)

# Excessive emoji
Trigger: >10 emoji in a single message
Action: Soft warning (bot reply, no delete)
```

### Scam Protection
```
# Crypto/NFT scam patterns
Trigger: "airdrop", "free mint", "DM me for", "guaranteed returns", wallet address patterns
Action: Delete + mute + flag for review

# Phishing links
Trigger: URL shorteners (bit.ly, tinyurl) + lookalike domains
Action: Delete + warn. Allowlist known safe short URLs.
```

## Moderator Guidelines

### What to enforce
- Rule violations (as written in community rules)
- Behaviour that makes others uncomfortable even if not explicitly against a rule
- Patterns of low-level negativity that individually seem minor

### What NOT to moderate
- Disagreements where both sides are respectful
- Unpopular opinions expressed civilly
- Criticism of the product, project, or community direction
- Messages you personally dislike but that break no rules
