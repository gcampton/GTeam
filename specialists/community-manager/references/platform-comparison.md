# Community Platform Comparison

## Feature Matrix

| Feature | Discord | Slack | Reddit | Circle | Discourse |
|---|---|---|---|---|---|
| Real-time chat | Yes (primary) | Yes (primary) | No (async) | Partial | No (forum) |
| Threaded discussion | Limited | Yes | Yes (primary) | Yes | Yes (primary) |
| Voice/video | Yes (built-in) | Huddles | No | No | No |
| Bot ecosystem | Huge (open API) | Large (App Directory) | Automod only | Limited | Plugins |
| Mobile experience | Good | Good | Good | Fair | Fair |
| Search | Poor | Good (paid) | Good | Fair | Excellent |
| Free tier limits | Unlimited members | 90-day message history | Unlimited | None (paid only) | Self-host free |
| Content persistence | Messages scroll away | 90-day free / full paid | Permanent (indexed) | Permanent | Permanent (indexed) |
| SEO value | None (gated) | None (gated) | High (public, indexed) | Optional (gated/public) | High (public, indexed) |
| Onboarding flow | Server welcome screen | Slackbot intro | Subreddit sidebar | Spaces + welcome | Categories + pinned |
| Analytics | Server Insights (basic) | Analytics (paid) | Subreddit stats | Built-in dashboard | Admin dashboard |
| Custom branding | Limited (boost tiers) | Paid plans | Subreddit CSS/flairs | Full branding | Full branding |
| Moderation tools | Automod, bots, roles | Channel permissions | Automod, mod queue | Basic | Flags, review queue |
| API access | Full REST + Gateway | Full REST + Events | Read-heavy, rate-limited | REST API | Full REST API |
| Self-hosting | No | No | No | No | Yes (free) |
| Best audience | Developers, gamers, crypto, creators | Professionals, B2B, teams | General public, niche interests | Course creators, memberships | Open source, documentation |

## Decision Framework

**Choose Discord when:**
- Audience is developers, gamers, or crypto/web3
- Real-time interaction and voice channels matter
- You want rich bot integrations (welcome flows, reaction roles, moderation)
- Community is synchronous and chat-first

**Choose Slack when:**
- Audience is professional or B2B
- Community is tied to a paid product or service
- Threaded discussions and integrations with work tools matter
- You can afford paid plans (free tier 90-day limit is a dealbreaker for knowledge preservation)

**Choose Reddit when:**
- You want SEO value from community discussions
- Community is async and content-first
- You want to tap into Reddit's existing discovery engine
- Low maintenance overhead is important (community self-moderates at scale)

**Choose Circle when:**
- Community is part of a paid course, membership, or SaaS product
- You need branded experience with your own domain
- Gated access and payment integration matter
- You want spaces (sub-communities) with different access levels

**Choose Discourse when:**
- Long-form discussion and knowledge base are primary goals
- SEO and public discoverability matter
- You want full control (self-hosted option)
- Community is for open-source project or documentation support

## Migration Guidance

### When to Migrate
- Platform limits are blocking growth (e.g., Slack 90-day history loss)
- Audience mismatch (professional community stuck on Discord)
- Feature needs changed (need async knowledge base but using chat-first platform)
- Cost scaling issues (Slack per-seat pricing at 1,000+ members)

### Migration Checklist
1. **Announce early** — 4-6 weeks notice minimum
2. **Run dual platforms** — 2-4 weeks overlap where both are active
3. **Export what you can** — Discord: no native export (use DiscordChatExporter), Slack: Workspace Export (paid), Reddit: pushshift/API, Discourse: full SQL export
4. **Migrate key content first** — pin top discussions, FAQs, rules in new platform
5. **Move moderators first** — they seed activity and handle early issues
6. **Set a hard cutoff date** — archive old platform (read-only) after overlap period

### Data Export Options

| Platform | Native Export | Third-Party Tools | What You Lose |
|---|---|---|---|
| Discord | None | DiscordChatExporter, Ditto | Reactions, thread context |
| Slack | JSON export (paid) | Slack-export-viewer | Formatting, integrations |
| Reddit | API / pushshift | Arctic Shift | Deleted content, DMs |
| Circle | CSV export | None | Media attachments |
| Discourse | Full SQL + API | Built-in backup | Nothing (best export story) |
