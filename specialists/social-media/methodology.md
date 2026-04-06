### Browse Setup

When a profile URL or competitor page is provided, run this setup block:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebFetch instead.

---

### Platform Strategy

**Gather:** Brand/product description, target audience (age, interests, job title), current platforms (if any), primary goal (awareness / followers / leads / sales), content production capacity (how many hours/week).

**Platform selection logic:**

| Platform | Best for | Content type | Commitment |
|---------|---------|-------------|------------|
| LinkedIn | B2B, hiring, thought leadership | Articles, carousels, short posts | 3–5× per week |
| Instagram | Consumer brand, visual product, lifestyle | Reels (primary), carousels, stories | 5–7× per week |
| X (Twitter) | Tech, media, real-time commentary | Short takes, threads, replies | 5–10× per day |
| TikTok | Consumer, entertainment, under-35 | Short-form video (15–60s) | 1–3× per day |
| YouTube | Education, software demos, long-form | Videos 8–15 min | 1–2× per week |
| Facebook | Local business, paid ads, events | Posts, groups, ads | 3–5× per week |

**For each active platform, define:**
- Primary content format (what dominates the feed right now)
- Posting cadence (realistic given capacity)
- Tone of voice (same brand, adapted to platform culture)
- Key metric: impressions / followers / engagement rate / clicks

**Content mix rule:** 60% educational/entertaining, 30% social proof/community, 10% promotional. Never lead with the pitch.

**Deliver:**
- Platform selection rationale (which to focus on + why to deprioritise others)
- One-pager per active platform: format, cadence, tone, primary metric
- 30-day content plan: topics by week with format notes

---

### Content Creation

**Gather:** Platform, topic or campaign theme, brand voice guide if available, any existing content assets (product screenshots, customer quotes, data).

**Content formats by platform:**

**LinkedIn:**
- Opening line wins or loses the post — no preamble, no "I'm excited to announce"
- Carousels: 8–10 slides, first slide = bold claim, last slide = CTA
- Short posts: 3–5 punchy lines, white space between, hook → insight → takeaway → CTA

**Instagram:**
- Reels: hook in first 2 seconds (text overlay or action), value in 15–30 seconds, CTA at end
- Carousels: swipe-worthy first slide, value builds across slides, last slide = save/share CTA
- Caption: first line is the hook (displayed before "more"); hashtags in comment or at bottom

**X (Twitter):**
- Threads: opening tweet is the hook + promise ("I did X for Y months. Here's what I learned:")
- Single tweet: one idea, one line, no filler
- Reply strategy: meaningful replies to relevant accounts builds following faster than posting alone

**TikTok:**
- Hook formula: address the viewer directly ("If you're a [persona] who struggles with X...")
- Native feel over polished production — trending audio, on-screen text captions, direct-to-camera
- Pattern interrupt: change scene, add text pop, cut within first 3 seconds

**Write for each piece:**
- Platform-native draft (caption / script / carousel text)
- Subject/hook variant (A/B)
- Hashtag set: 3–5 max (1 broad, 2 niche, 1 branded) — not a wall of tags
- Visual brief: what image, graphic, or b-roll supports this post

**Deliver:**
- 10 ready-to-post pieces (mix of formats)
- Visual brief for each (what to create or source)
- Hashtag strategy per platform
- 3 content series concepts (recurring formats that build audience over time)

---

### Community Management & Engagement

**Gather:** Active platforms, typical comment/DM volume, brand voice guidelines, any sensitive topics or competitors not to engage with.

**Daily engagement protocol (15–30 min per platform):**

1. **Respond to all comments on own posts** within 24 hours:
   - Genuine questions: answer fully
   - Compliments: acknowledge + add value ("Thanks! The key thing that made X work was...")
   - Criticism: acknowledge + take offline if needed ("DM us and we'll sort this out")
   - Never delete negative comments (unless spam/offensive) — respond and resolve publicly

2. **Proactive engagement (10 mins/day):**
   - Reply meaningfully to 5–10 posts from target audience or complementary accounts
   - Never generic ("Great post!") — add a specific point or question
   - Engage before you post — warms algorithm and builds relationships

3. **DM handling:**
   - Respond within 4 hours during business hours
   - Qualify leads: what's their problem? Do we solve it?
   - Template library for: pricing questions, partnership requests, media enquiries, complaints

**Response templates (adapt to brand voice):**

| Scenario | Template |
|---------|---------|
| Positive comment | "Thanks [name]! [Specific observation about their comment]. [Value add]." |
| Question | "[Answer directly]. Happy to go deeper — [resource or DM offer]." |
| Complaint | "Sorry to hear this, [name]. [Acknowledge]. Can you DM us with [details]? We'll get this fixed." |
| Spam/sales DM | Ignore or soft decline; do not engage with arguments |

**Deliver:**
- Engagement protocol document
- DM response template library (5–8 scenarios)
- Escalation criteria (when to involve a human senior team member)
- Competitor monitoring list: 5–10 accounts to watch weekly

---

### Analytics & Reporting

**Gather:** Platforms, analytics access, reporting period, KPIs defined (or define them now), any previous benchmarks.

**Platform metrics that matter:**

| Metric | What it tells you | Platform |
|--------|-----------------|---------|
| Reach / Impressions | Content distribution | All |
| Engagement rate | Content quality | All (target > 3%) |
| Follower growth | Brand momentum | All |
| Link clicks | Traffic intent | LinkedIn, X, Instagram bio |
| Video completion rate | Hook + content quality | TikTok, Reels, YouTube |
| Share / Repost rate | Shareability | All |
| Profile visits → follows | Audience conversion | All |

**Avoid vanity metrics:** Raw likes and follower count without context; focus on engagement rate and downstream conversion.

**Monthly report structure:**

1. **Summary** — did we hit last month's goals? One sentence per platform
2. **Top 3 performing posts** — what worked and why (format, topic, timing)
3. **Bottom 3 posts** — what didn't work; hypothesis for why
4. **Follower growth chart** — net new followers per platform
5. **Engagement rate trend** — average ER this month vs last 3 months
6. **Traffic from social** — GA4 sessions attributed to each platform
7. **Next month plan** — 3 experiments to run based on this data

**Deliver:**
- Monthly social media report (template above filled with data)
- Insights: 3 observations about what's working in this niche right now
- Next month content recommendations (topics + formats based on performance data)

---

### Campaign Planning

**Gather:** Campaign objective (awareness / launch / promotion / event), timeline, budget (organic or paid), target audience, any creative assets available.

**Campaign structure:**

**Phase 1 — Pre-launch (1–2 weeks before):**
- Teaser content: hint at what's coming without revealing everything
- Build anticipation: countdown, behind-the-scenes, "what do you think about X" polls
- Warm up the algorithm: increase posting frequency 1 week before

**Phase 2 — Launch (Day 0–3):**
- Hero post: the main announcement. Best performing format for that platform.
- Cross-post across all active platforms (native format per platform, not copy-paste)
- Engagement blitz: respond to every comment in first 2 hours (boosts algorithm reach)
- Story/Reel supporting content: repurpose the hero into supporting formats

**Phase 3 — Sustain (Week 2–4):**
- Social proof: share customer reactions, UGC, results if available
- Educational content: why X matters, how X works, common questions answered
- Urgency drivers: deadline, limited availability, bonus offer (if applicable)

**Phase 4 — Wrap-up:**
- Results post: "Here's what happened when we launched X" — transparency builds trust
- Thank you content: acknowledge community
- Retarget warm audience with paid if budget available

**Paid amplification (if budget available):**
- Boost top organic performers only (≥ 5% engagement rate) — don't pay to amplify weak content
- Retarget website visitors or lookalike of email list
- $5–20/day test budget per platform before scaling

**Deliver:**
- Campaign calendar: day-by-day content plan for all phases
- Per-post brief: platform, format, copy, visual, posting time
- Success metrics: reach / engagement / click / conversion targets per phase
- Budget allocation (if paid component)

---

### Crisis Management

**Use when:** Negative content about the brand is gaining traction, a PR incident occurs, or community sentiment shifts sharply negative.

**Severity assessment:**

| Level | Trigger | Response Time | Who's Involved |
|---|---|---|---|
| LOW | Isolated complaint, < 10 interactions | 4 hours | Social media manager |
| MEDIUM | Multiple complaints on same issue, 10-50 interactions, minor press | 1 hour | Social + leadership |
| HIGH | Viral negative content, 50+ interactions, mainstream press, legal risk | 15 minutes | Social + leadership + legal + PR |

**Rapid response framework:**

1. **Acknowledge** (within response time window):
   - "We're aware of [issue] and are looking into it"
   - Do NOT delete negative comments (screenshots exist, deletion amplifies)
   - Do NOT go silent — silence is interpreted as guilt

2. **Investigate** (parallel to acknowledgement):
   - What happened? Get facts from internal team
   - How widespread? Check all platforms, not just where you first saw it
   - Legal risk? If yes, loop in lawyer specialist before any further public statements

3. **Respond** (once facts are clear):
   - Own the mistake if it's real: "We got this wrong. Here's what happened and what we're doing about it."
   - Correct misinformation if it's false: "Here's what actually happened: [facts with evidence]."
   - Never be defensive, never blame the customer, never use corporate-speak

4. **Monitor** (48 hours post-response):
   - Track sentiment shift — is the response working?
   - Respond to follow-up questions promptly
   - Prepare a post-mortem for internal team

5. **Post-crisis content** (1-2 weeks after):
   - Transparency post: what changed as a result
   - Return to normal content cadence gradually
   - Do NOT pretend it didn't happen

**Pre-prepared assets (create before you need them):**
- Holding statement template: "We're aware of [X] and taking it seriously. We're investigating and will share an update by [time]."
- Escalation contact list: who to call at each severity level
- Platform-specific response templates (X character limit vs LinkedIn long-form)

---

### Influencer & Partnership Strategy

**Use when:** Brand wants to grow through creator collaborations rather than (or alongside) owned content.

**Partnership types:**

| Type | Cost | Scale | Best For |
|---|---|---|---|
| Micro-influencer (1K-50K) | £100-500/post or product gifting | Niche, high engagement | Early-stage brands, specific audiences |
| Mid-tier (50K-500K) | £500-5K/post | Broader reach, still niche credibility | Growing brands, product launches |
| Macro (500K+) | £5K-50K+/post | Mass awareness | Established brands, major launches |
| Brand ambassador | Ongoing retainer + perks | Consistent, authentic | Long-term brand building |
| Content collaboration | Revenue share or cross-promotion | Organic, mutual benefit | Complementary brands |

**Vetting checklist before partnering:**
- Engagement rate > 2% (fake followers inflate follower count but not engagement)
- Audience demographics match your target (ask for their analytics screenshot)
- Content quality and tone align with brand
- No history of controversy that conflicts with brand values
- Check comments — are they real conversations or bot spam?

**Campaign structure:**
1. Brief the creator (brand guidelines, key messages, what NOT to say, creative freedom boundaries)
2. Review draft content before publishing (one round of feedback, not micromanagement)
3. Agree on posting schedule and cross-promotion plan
4. Track with UTM links or promo codes per creator
5. Measure: reach, engagement, clicks, conversions attributed to each creator

**Deliverables:**
- Influencer shortlist (10-20 vetted candidates with engagement data)
- Outreach template (personalised, not mass DM)
- Campaign brief template
- ROI tracking spreadsheet (creator → reach → clicks → conversions → cost per acquisition)

---

### Audience Psychology & Messaging

**Use when:** Content is technically correct but not resonating — good information, low engagement.

**Why content fails to land:**
Content fails not because it's wrong, but because it doesn't connect emotionally. Every piece of social content triggers one of these responses:

| Response | Trigger | Action |
|---|---|---|
| "That's me" | Identity validation — content reflects who they are or aspire to be | Like, save |
| "I need to remember this" | Utility — genuinely useful, reference-worthy | Save, bookmark |
| "My network needs to see this" | Social currency — sharing makes them look smart/helpful | Share, retweet |
| "I have something to say about this" | Debate — content invites opinion or challenges a belief | Comment, reply |
| "I feel seen" | Empathy — content acknowledges a struggle or experience | Like, comment, follow |

**Messaging framework per audience type:**

| Audience | What resonates | What falls flat |
|---|---|---|
| Founders/entrepreneurs | Contrarian takes, revenue numbers, "here's what I learned" | Generic motivation, vague success stories |
| Developers | Technical depth, honest trade-offs, "I built X, here's how" | Marketing-speak, oversimplification |
| Marketers | Frameworks with examples, campaign results, benchmarks | Theory without data, outdated tactics |
| Consumers (B2C) | Emotion, identity, entertainment, social proof | Feature lists, technical jargon |
| Executives | Strategic implications, bottom-line impact, peer examples | Tactical details, how-to content |

**Hot take formula (what makes a take actually hot):**
A hot take is NOT just a strong opinion. It works when it:
1. Challenges a widely-held belief ("Everyone says X, but actually Y")
2. Is backed by specific evidence or experience ("I did X for 6 months and here's what happened")
3. Has stakes — the reader gains something by changing their mind
4. Is debatable but defensible — not just contrarian for attention

**Before/after content improvement:**
- Before: "Remote work has pros and cons" → flat, no engagement trigger
- After: "I tracked my team's output for 6 months: remote engineers shipped 40% more code but creative collaboration dropped 60%. Here's how we fixed both." → specific, evidence-based, invites discussion

---

### Real-Time Trend Capture

**Use when:** A trending topic, breaking news, or viral moment is relevant to the brand. Speed matters — trends have a 2-6 hour window for maximum impact.

**Detection sources:**
- X trending topics and Explore tab
- TikTok Discover page and trending sounds
- Google Trends (rising searches)
- Industry Slack/Discord channels
- Competitor posts getting unusual engagement

**Evaluate before posting (5-minute check):**

| Question | If No → Skip |
|---|---|
| Is this relevant to our brand/audience? | Don't force a connection |
| Can we add genuine value or perspective? | Don't just echo the trend |
| Is the topic safe? (no tragedy, no political minefield) | Don't risk brand on a hot-button issue |
| Can we produce quality content in < 2 hours? | Don't rush out low-quality content |

**Execution (if all checks pass):**
1. Draft content in platform-native format (< 30 mins)
2. Quick review — brand voice check, sensitivity check (< 15 mins)
3. Post on primary platform first, adapt to others within 1 hour
4. Engage heavily in first 60 minutes (reply to every comment)
5. Monitor sentiment — if response turns negative, pause and assess

**Trend content types:**
- Commentary: "Here's our take on [trend]" — works for thought leadership accounts
- Tutorial: "How to [trend-related skill]" — works for educational accounts
- Meme/humour: Remix the trend with brand relevance — works for consumer brands
- Data: "We analysed [trend] and here's what we found" — works for analytical brands

---

### Paid-Organic Integration

**Use when:** Budget is available and organic reach alone isn't achieving goals. This supplements (not replaces) organic strategy.

**Note:** For full paid campaign design, audience targeting, and ad platform management, use the paid-media specialist. This section covers the organic-paid handshake only.

**Rule: Only boost winners.** Never pay to amplify content that didn't perform organically.

| Organic Performance | Paid Action |
|---|---|
| Engagement rate > 5% | Boost with £5-20/day budget — this content resonates |
| Engagement rate 3-5% | Test boost with £5/day for 48 hours — evaluate |
| Engagement rate < 3% | Do NOT boost — fix the content first |

**Organic-to-paid repurposing workflow:**
1. Identify top-performing organic posts (weekly review)
2. Adapt for paid format: add CTA, tighten copy, improve visual
3. Target: lookalike audience based on current followers/engagement
4. Run for 3-7 days with daily budget, monitor CPA
5. Kill if CPA exceeds target after 48 hours

**Attribution basics:**
- UTM tag all links from social: `?utm_source=linkedin&utm_medium=social&utm_campaign=q2-launch`
- Track in GA4: Acquisition → Traffic Acquisition → filter by utm_source
- Social-attributed conversions = last-touch attribution (imperfect but actionable)

---
