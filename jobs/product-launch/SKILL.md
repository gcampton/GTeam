---
name: gteam-product-launch
version: 1.0.0
description: Complete product launch package — SEO, content, social, and legal review. Provide product description and launch URL.
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
---

> GTeam update check: `cd ~/.claude/skills/gteam && git pull && bun run build`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.

# Product Launch — GTeam Job

This job runs four specialists. Estimated output: full launch package including content, social distribution, and legal checklist.

**Starting `product-launch` — running: SEO → Content Creator → Social Media → Lawyer**

---

## Step 1: SEO Foundation

Identify keyword targets and technical requirements for the launch page.

### Browse Setup

When a URL is provided, run this setup block before any browse step:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebFetch instead for URL inspection.

---

### Technical SEO Audit

**Gather:** URL of the site. Use `$B goto <url>` then `$B snapshot` to inspect rendering. If not browseable, ask user to paste page source or describe the stack.

**Technical audit checklist:**

1. **Title tags** — 50–60 chars, primary keyword near front, unique per page, no truncation
2. **Meta descriptions** — 150–160 chars, compelling copy with implicit CTA, unique per page
3. **Heading structure** — single H1, logical H2/H3 hierarchy, keywords in headings naturally
4. **Core Web Vitals** — LCP < 2.5s, CLS < 0.1, INP < 200ms. Search for PageSpeed report if URL available: `WebSearch "<url> PageSpeed Core Web Vitals"`
5. **Mobile** — viewport meta present, tap targets ≥ 48px, no horizontal scroll, readable font size
6. **Canonical tags** — self-referencing on primary pages, no conflicting canonicals, correct on paginated content
7. **Robots.txt** — accessible at /robots.txt, no accidentally blocked pages or critical assets (CSS/JS)
8. **XML sitemap** — present, submitted to Search Console, no 404s or noindex pages listed
9. **Internal linking** — orphan pages (≤ 1 inbound link), anchor text diversity, key pages linked from nav
10. **Duplicate content** — www vs non-www, HTTP vs HTTPS, trailing slash inconsistency — all 301 consolidated
11. **Schema markup** — structured data for page type (Article, Product, FAQ, LocalBusiness)
12. **HTTPS** — served over HTTPS, no mixed content warnings
13. **Redirect chains** — no chains longer than 1 hop; 301 (not 302) for permanent moves
14. **Hreflang** — if multi-language, hreflang tags correct and reciprocal

**Deliver:**
- Technical issues table (issue → priority: P1/P2/P3 → specific fix)
- Estimated effort per fix (< 1 hour / half day / sprint)
- Quick wins list: P1 issues fixable in under 1 hour

---

### Keyword Research & Content Gap Analysis

**Gather:** Domain, primary topic/niche, target audience, 3–5 competitor domains if known. Use WebSearch to research competitor content.

**Research process:**

1. **Seed keywords** — extract from: product/service names, ICP job titles, pain points, solution language
2. **Keyword classification by intent:**
   - Informational (how, what, why) → blog/guide content
   - Commercial investigation (best, vs, review, alternative) → comparison/landing pages
   - Transactional (buy, pricing, sign up, hire) → product/conversion pages
   - Navigational → branded terms (own and monitor)
3. **Gap analysis:**
   - Search top 3 competitors: `site:<competitor> <topic>` (WebSearch)
   - Identify topics they rank for that the site doesn't cover
   - Prioritise: high intent + moderate difficulty + evidence of existing traffic
4. **Prioritisation matrix:**
   | Priority | Intent | Signal | Action |
   |---------|--------|--------|--------|
   | Quick win | Any | Ranking 4–20 | Optimise existing page |
   | Build | Informational | Low competition, content gap | Create new content |
   | Compete | Commercial | High competition, high intent | Needs authority + links |
   | Own | Navigational | Branded | Protect + expand |
5. **Cannibalisation check** — flag 2+ pages targeting same keyword; consolidate or differentiate intent

**Deliver:**
- Keyword opportunity table: keyword → intent → difficulty → recommended page
- 10 quick-win keywords (currently ranking 4–20)
- Content gap list (topics competitors cover that the site doesn't)
- Cannibalisation issues (pages to merge or differentiate)

---

### On-Page Optimisation

**Gather:** URL(s) to optimise, target keyword per page, existing content. Load with `$B goto <url>` if available.

**For each page:**

1. **Title tag** — keyword in first 60 chars; power word (ultimate, complete, guide); year if time-sensitive
2. **Meta description** — include keyword naturally; add a benefit; soft CTA ("Learn more", "See examples")
3. **H1** — matches page intent; contains primary keyword; one H1 only
4. **Content structure:**
   - Opening paragraph: answer the query directly in first 100 words (featured snippet targeting)
   - H2s: cover related questions and subtopics (check People Also Ask: WebSearch `"<keyword>" people also ask`)
   - Word count: match top-ranking pages ± 20% — don't pad, don't under-serve
5. **Keyword placement:** title, H1, first 100 words, one H2, image alt text, naturally throughout
6. **Internal links:** 2–4 contextual links to related content; descriptive anchor text (not "click here")
7. **External links:** 1–2 outbound links to authoritative sources (supports E-E-A-T)
8. **Images:** descriptive alt text, compressed (WebP), filename includes keyword
9. **Schema:** FAQ schema for Q&A sections; HowTo for step-by-step content
10. **E-E-A-T signals:** author byline with credentials, publication date, last-reviewed date, cited sources

**Deliver:**
- Copy-ready title tag and meta description
- Suggested H2 structure (outline) for the page
- Specific optimisation actions per element (with file:line if code is provided)

---

### Link Building Strategy

**Gather:** Domain, niche, current authority level if known, content assets available (tools, studies, guides), budget (organic only vs outreach).

**Link building tiers:**

**Tier 1 — No-cost foundations (always do first):**
- Google Business Profile — complete and verified (if local)
- Industry directories — niche-specific only (not generic link farms)
- Podcast appearances — WebSearch `"<niche>" podcast "guest" OR "apply"` for 10 targets
- HARO / Connectively — respond to journalist queries in the niche daily
- Partner / supplier links — reciprocal mentions from existing business relationships
- Unlinked mentions — find brand mentions without links; request link addition

**Tier 2 — Content-driven (requires good content assets):**
- Original research / data studies — survey audience; pitch findings to industry publications
- Free tools — calculators, templates, generators that attract natural links
- Ultimate guides — comprehensive resources that become industry reference material
- Guest posts — 3–5 high-authority publications; pitch original angles, not rehashes

**Tier 3 — Proactive outreach:**
- Skyscraper — find top-linked content on a topic; create something objectively better; outreach to same linkers
- Digital PR — newsworthy angles (funding, data, product launches); target trade press
- Niche edits — reach out to existing articles; request contextual link insertions

**Google Search Operator Prospecting:**

Use these search patterns to surface link opportunities at scale. Run in Google (not AI search).

| Pattern | Example | Finds |
|---------|---------|-------|
| `"brand name" -site:domain.com` | `"Stonehill Dental" -site:stonehilldental.com` | All brand mentions on other sites — outreach to request link |
| `"business type" inurl:business-directory` | `"Electrician Brisbane" inurl:business-directory` | Business directories accepting submissions |
| `"keyword" inurl:resources` | `"dental implants" inurl:resources` | Resource pages that curate links in the niche |
| `"keyword" intitle:"useful links" OR intitle:"recommended links"` | `"accounting software" intitle:"useful links"` | Links/resources pages to pitch for inclusion |
| `"keyword" "write for us" OR "guest post"` | `"digital marketing" "write for us"` | Sites accepting guest contributions |
| `"keyword" "sponsored by" OR "proud sponsor"` | `"Brisbane dentist" "proud sponsor"` | Sponsorship opportunities with link credit |
| `site:edu "keyword" "resources" OR "links"` | `site:edu "orthodontics" "resources"` | Educational resource pages (high authority) |
| `"keyword" inurl:directory -site:yelp.com -site:yellowpages.com` | `"plumber Sydney" inurl:directory` | Niche directories excluding generic giants |
| `"[competitor]" "review" OR "vs" -site:[competitor].com` | `"Ahrefs" "review" -site:ahrefs.com` | Review sites and comparison pages linking to competitor — pitch them yours |
| `"[niche]" "best tools" OR "top resources" OR "roundup"` | `"SEO" "best tools 2025"` | Roundup posts that list tools/resources in the niche |

**Workflow:** Run the pattern → extract domain list → filter for DA > 20 and relevance → add to outreach queue.

**Anchor text distribution target:**
- Branded (domain/brand name): 40%
- Naked URL: 20%
- Exact match keyword: 5% max (over-optimisation risk)
- Partial match / generic ("learn more", "this article"): 35%

**Deliver:**
- Link building plan by tier with timeline
- 10 specific target domains for outreach (found via WebSearch)
- Pitch template for guest post or niche edit outreach
- Anchor text guidance for the domain

---

### SEO Reporting & Tracking

**Gather:** Tools in use (Google Search Console, GA4, Ahrefs, SEMrush, etc.), reporting period, KPIs the team cares about.

**Core metrics to track:**

| Metric | Source | Target |
|--------|--------|--------|
| Organic sessions | GA4 | Month-over-month growth % |
| Impressions | GSC | Upward trend |
| Average position | GSC | Trending down (= improving) |
| Click-through rate | GSC | > 3% overall average |
| Pages in top 10 | GSC | Count growing |
| Organic conversions | GA4 | Tied to business KPI |
| Referring domains | Ahrefs/Moz | Steady growth month-on-month |

**Monthly report structure:**

1. **Executive summary** — one paragraph: what moved, what caused it, what's next
2. **Traffic snapshot** — organic sessions vs prior period, vs same period last year
3. **Ranking wins / losses** — new keywords entering top 10; material drops
4. **Technical health** — crawl errors, index coverage, Core Web Vitals status
5. **Content performance** — top 5 pages by organic traffic; new pages gaining traction
6. **Link acquisition** — new backlinks and referring domains this month
7. **Action items** — 3 specific things to do next month, tied to the data

**Deliver:**
- Completed monthly report (template above, filled with available data)
- Priority action list for next 30 days
- Anomalies flagged with probable cause (algorithm update, technical issue, competitor movement)


---

## Step 2: Launch Content

Produce launch announcement, landing page copy, and blog post using Step 1 keyword targets.

### Browse Setup

When researching competitors or checking live content, run this setup block:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebSearch + WebFetch instead.

---

### Content Creation

**Gather:** Topic, target audience, content goal (inform/convert/rank/entertain), target keywords if known, preferred format (blog post, landing page, newsletter, long-form guide).

**Research phase:**
1. Identify search intent for the primary keyword
2. Review top 3 ranking pages: WebSearch `"<keyword>"` and browse/fetch the top results
3. Find angles those pages miss — specific data, a contrarian view, a more practical how-to — that's the differentiation

**Structure:**
- **Hook:** first sentence earns the second. Open with a specific claim, surprising fact, or vivid scenario — not "In today's world..."
- **Subheadings:** every H2 is a complete thought, not a label. "Why Conversion Rates Drop at Checkout" not "Conversion Issues"
- **Proof points:** data, examples, case studies — one per major claim
- **CTA:** single, clear, matches reader intent at this point in the funnel

**Writing checklist:**
- Flesch reading ease ≥ 60 (conversational, not academic)
- No paragraph longer than 4 lines
- Internal linking: 2–4 links to related content (placeholder links if URLs unknown)
- Keyword density: primary keyword in title, H1, first 100 words, one H2, naturally throughout
- Meta title (50–60 chars) and meta description (150–160 chars) included

**E-E-A-T checklist** (Google Experience, Expertise, Authoritativeness, Trustworthiness):
- Named author with credentials relevant to the topic — not "Editorial Team"
- Firsthand experience signals: original examples, specific unexpected details, real outcomes/numbers
- All factual claims cited with primary source link
- Publish date and last-reviewed date visible on the page
- For YMYL topics (health, finance, legal, safety): flag as "needs expert review before publishing"
- If AI-assisted: mark sections needing firsthand specifics as "needs owner input"

**Deliver:**
- Full content piece (publish-ready)
- Meta title and description
- Social media pull-quotes (3 × tweet-length excerpts)
- E-E-A-T notes: sections where firsthand sourcing is thin

---

### Content Audit & Gap Analysis

**Gather:** Domain or list of existing content URLs. If browseable, load the site and crawl key content pages. Otherwise work from a spreadsheet or list the user provides.

**Audit each piece:**

1. **Traffic performance:** is it getting organic traffic? (ask user for GA4 data, or estimate from ranking position)
2. **Ranking position:** what keyword is it ranking for? Position 1–10 / 11–20 / not ranking
3. **Search intent match:** does the content format match the intent? (informational keyword → how-to article ✓; transactional keyword → product page ✓; mismatch → fix)
4. **Age:** last updated? Content > 18 months old in fast-moving topics needs a refresh
5. **Quality score (1–5):**
   - 5: comprehensive, well-cited, distinctive angle, E-E-A-T signals present
   - 3: covers the topic but generic, no differentiation
   - 1: thin, stub, no real value
6. **Action:** Keep / Update / Merge / Delete / Redirect

**Decision rules:**
- Ranking 1–10 + quality 4–5 → Keep, minor refresh only
- Ranking 11–20 + quality 3+ → Update to push into top 10 (quick win)
- Ranking 20+ + quality 1–2 → Merge with a stronger related piece, or delete + redirect
- Cannibalisation (2+ pieces targeting same keyword) → Consolidate into one authoritative page
- Zero traffic + zero ranking + thin content → Delete + 301 redirect to nearest relevant page

**Deliver:**
- Content audit spreadsheet: URL → keyword → position → quality score → action
- Priority update list: top 5 pieces to refresh for quick ranking gains
- Consolidation plan: pages to merge with redirect mapping
- Gap list: topics needed based on keyword research that don't exist yet

---

### Pillar & Cluster Content Strategy

**Gather:** Primary topic area, existing content inventory (from audit above), target audience job-to-be-done, domain authority level (rough estimate).

**Topic cluster model:**

```
Pillar page (broad topic, 3,000–5,000 words)
├── Cluster article 1 (specific subtopic, 1,000–2,000 words)
├── Cluster article 2 (specific subtopic)
├── Cluster article 3 (related question / comparison)
└── Cluster article 4 (use case or example)
```

**Step 1 — Choose pillar topics:**
- High search volume + high business relevance
- Broad enough to spawn 8–15 cluster articles
- Example pillar: "Email Marketing" spawns clusters: deliverability, subject lines, segmentation, welcome sequences, A/B testing, list building...

**Step 2 — Map cluster articles:**
- Each cluster targets a specific long-tail keyword
- Cluster articles link back to the pillar page
- Pillar page links out to all cluster articles
- Internal link anchor text must use the cluster article's target keyword

**Step 3 — Build in priority order:**
1. Create or upgrade the pillar page first (signals topic authority)
2. Publish cluster articles one at a time (each strengthens the pillar)
3. Add internal links from existing content to new cluster articles

**Pillar page anatomy:**
- Comprehensive overview of the topic (not a deep dive — clusters do that)
- Table of contents (improves dwell time + featured snippet eligibility)
- Links to all cluster articles as "deep dives"
- Clear target keyword + related terms throughout

**Deliver:**
- Pillar + cluster map (topic → pillar → list of 8–12 cluster articles with keywords)
- Content brief for the pillar page
- Publication roadmap: order to create content + estimated effort per piece
- Internal linking plan: which existing pages to update with new links

---

### Content Repurposing

**Gather:** Source content (blog post, guide, webinar transcript, podcast episode, research report), target platforms, content production capacity.

**Repurposing hierarchy (one long-form piece → many formats):**

```
Long-form article / Guide (source of truth)
├── LinkedIn carousel (10 slides: one insight per slide)
├── Twitter/X thread (10 tweets: one point per tweet)
├── Email newsletter (key insight + link back to full article)
├── Short video script (60–90 second "key takeaway" video)
├── Infographic brief (3–5 statistics or steps visualised)
├── Podcast talking points (if the brand has a podcast)
└── FAQ page (extract Q&A pairs for schema + featured snippets)
```

**Repurposing principles:**
- Each format needs a native rewrite — not copy-paste from the blog post
- Lead with the best insight for that platform's audience; they may not read the original
- Always link back to the source article (drives traffic + internal linking)
- Update the source article with embeds of the repurposed content (adds media richness)

**LinkedIn carousel formula:**
- Slide 1: bold contrarian claim or surprising stat (the hook)
- Slides 2–8: one actionable insight per slide; short sentence + supporting detail
- Slide 9: the "what most people miss" slide
- Slide 10: CTA (follow for more, link in bio, comment your question)

**Email newsletter from long-form:**
- Subject line: the most surprising insight from the article
- 150–200 words max: context → key insight → why it matters → link to read more
- Don't give everything away — make the click worth it

**Deliver:**
- Repurposing plan: source piece → list of formats with brief per format
- Copy-ready versions for 3 formats (chosen based on active platforms)
- Visual brief for any graphics needed (carousel, infographic)
- Publishing schedule across channels

---

### AI-Assisted Content Quality Control

**Use when:** Content is AI-generated or AI-assisted and must pass Google's quality standards, E-E-A-T signals, and avoid patterns that reduce credibility or ranking.

**The core problem:** AI-generated content is detectable by both humans and Google's quality systems — not necessarily because it's wrong, but because it lacks the markers of genuine firsthand experience. The fix is to add specificity, not to "humanise" the writing.

**Check `references/ai-writing-patterns.md` before reviewing or publishing any AI-assisted piece.** Work through all 5 categories.

**Category 1 — Remove hollow opener patterns:**

These phrases signal AI generation and reduce credibility:
- "In today's fast-paced world..."
- "In the ever-evolving landscape of..."
- "It goes without saying that..."
- "As we navigate [topic]..."
- "Whether you're a beginner or expert..."
- "In this article, we will explore..."
- Any opening that restates the title

Fix: Start with a specific claim, data point, or scenario that proves firsthand knowledge.

**Category 2 — Replace vague generalities with specifics:**

| Vague (AI pattern) | Specific (human signal) |
|-------------------|------------------------|
| "Many businesses struggle with X" | "According to [source], 67% of SaaS companies lose >20% of revenue to X" |
| "There are several approaches to consider" | "Three approaches work: [A], [B], [C] — here's when each applies" |
| "It's important to understand that..." | Delete — state the thing directly |
| "X can be challenging" | "X fails at [specific point] because [mechanism]" |

**Category 3 — Add E-E-A-T signals:**

For every major claim, one of the following must be present:
- **Primary source citation:** link to the study, data, or official guidance
- **Firsthand example:** "When we ran this for [client type], we saw [specific result]"
- **Named expert quote:** Name, title, organisation — not "experts say"
- **Original data:** survey results, internal analysis, novel calculation

Flag sections that have none of these as `[NEEDS OWNER INPUT]` — these need a human with experience to add the specifics before publishing.

**Category 4 — Sentence structure variation:**

AI-generated text tends to: all sentences similar length, all paragraphs similar length, heavy use of "Additionally" / "Furthermore" / "Moreover" / "In conclusion".

Fix checklist:
- [ ] At least 30% of sentences are short (under 15 words)
- [ ] At least 1 sentence fragment used for emphasis (intentional, not error)
- [ ] Transition words ("Additionally", "Furthermore") replaced with direct connectives or sentence restructure
- [ ] No paragraph that is exactly the same structure as the one before it

**Category 5 — YMYL and sensitive topics:**

For health, finance, legal, or safety content:
- Every claim requires a primary source link — no exceptions
- Add "last reviewed" date
- Add appropriate disclaimer (not legal/medical advice language)
- Flag for expert review before publishing — this is non-negotiable

**Delivery checklist:**
- [ ] All hollow openers removed
- [ ] All vague generalities replaced with specifics or flagged `[NEEDS DATA]`
- [ ] E-E-A-T signals present in every major section or flagged `[NEEDS OWNER INPUT]`
- [ ] Sentence variation check passed
- [ ] YMYL check completed (if applicable)
- [ ] Author byline with relevant credentials added


---

## Step 3: Social Launch Campaign

Produce launch-day social posts, pre-launch teasers, and post-launch content calendar.

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


---

## Step 4: Legal Checklist

Review any terms of service, privacy policy, or partner contracts associated with the launch.

### Browse Setup

When a URL is provided (legislation, case law, regulatory guidance), run this setup block:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebFetch instead.

---

### Contract Review

**Gather:** Document (file path or paste). Identify: contract type, parties, governing jurisdiction if visible.

**Use Grep to search `references/contract-review-checklist.md` for relevant clause types as needed.** Work through every clause:

1. Liability & indemnification — who bears risk, any unlimited liability exposure?
2. IP ownership — who owns work product, licenses, background IP?
3. Termination — notice periods, termination for convenience vs cause, post-termination obligations
4. Governing law & jurisdiction — which courts, which law? Favourable to client?
5. Payment terms — amounts, milestones, late payment penalties, currency, invoicing requirements
6. Confidentiality — scope, duration, carve-outs, return/destruction obligations
7. Warranties & representations — what's promised, what's disclaimed?
8. Dispute resolution — arbitration, mediation, litigation? Seat and rules?
9. Force majeure — what events excuse performance?
10. Assignment & change of control — can either party assign without consent?
11. Entire agreement / variation — are verbal agreements excluded?
12. Notices — method, address, deemed receipt timing

**Risk rating per clause:** HIGH / MEDIUM / LOW / OK

Check `references/redline-patterns.md` for standard problematic clauses and suggested replacements.
Check `references/jurisdiction-notes.md` for jurisdiction-specific traps (UK, US, EU, AU).

**Surface to user only when:** a clause presents HIGH risk that could be deal-breaking, or two equally valid interpretations exist and the choice has material consequences.

**Deliver:**
- Risk summary table (clause → risk level → one-line explanation)
- Redlined document with `[SUGGESTED: ...]` inline edits
- Recommended next steps (negotiate, accept, reject, seek specialist counsel)

---

### Contract Drafting

**Gather:** Contract type (services, employment, SaaS, NDA, partnership, licensing, etc.), parties and their roles, key commercial terms (price, duration, deliverables, jurisdiction), specific protections required.

**Structure a complete draft:**

1. **Parties & recitals** — full legal names, registered addresses, role definitions
2. **Definitions block** — defined terms for everything used more than once
3. **Core commercial clauses** — scope of work, deliverables, acceptance criteria, timelines
4. **Payment** — amounts, milestones, invoicing process, late payment (statutory rate default)
5. **IP** — ownership of outputs, licence grants, background IP carve-out
6. **Confidentiality** — mutual NDA clause; duration 2–5 years standard
7. **Termination** — for convenience (30-day notice), for cause (material breach, insolvency)
8. **Liability cap** — standard: 12 months' fees; exclusion for consequential loss
9. **Governing law** — match client's jurisdiction; dispute resolution method
10. **Boilerplate** — entire agreement, waiver, severability, notices, counterparts

**Drafting principles:**
- Plain English — avoid archaic legalese unless jurisdiction requires it
- Short sentences; one obligation per clause
- Use "must" (obligation) not "shall"; use "will" for statements of fact
- Number every clause; sub-clauses in (a)(b)(c) format

**Deliver:**
- Full draft contract (clean version)
- Negotiation notes: which clauses client can concede, which are non-negotiable
- Summary of key commercial terms (one page, non-legalese)

---

### Risk Assessment

**Gather:** Business activity, jurisdiction(s) of operation, proposed transaction or action, any regulatory context mentioned.

**Risk categories to assess:**

1. **Contractual risk** — exposure from existing agreements (non-competes, exclusivity, IP assignments)
2. **Regulatory risk** — sector-specific regulation (GDPR/data, FCA/financial, employment law, consumer protection)
3. **IP risk** — infringement of third-party IP, ownership gaps, open source licence conflicts
4. **Employment risk** — contractor vs employee misclassification, restrictive covenants, TUPE/WARN triggers
5. **Corporate risk** — director duties, shareholder agreements, minority protection, change of control
6. **Data & privacy risk** — lawful basis, data transfers, breach notification, DPA compliance
7. **Commercial risk** — payment default, insolvency of counterparty, jurisdiction enforcement

**For each risk identified:**
- Probability: HIGH / MEDIUM / LOW
- Impact: SEVERE / MATERIAL / MINOR
- Mitigation: specific contractual or operational action

**Deliver:**
- Risk matrix (category → probability → impact → mitigation)
- Top 3 immediate actions (ranked by risk × impact)
- Questions requiring specialist input (flag jurisdiction-specific grey areas)

---

### NDA & Standard Document Review (Fast Track)

**Use for:** NDAs, simple service agreements, terms of service, privacy policies, standard form contracts. Goal is speed — flag blockers, pass everything else.

**Fast-track checklist (target 15 minutes):**
- Mutual vs one-way — appropriate for the relationship?
- Definition of confidential information — too broad or too narrow?
- Exclusions present (already public, independently developed, compelled disclosure)?
- Duration — 2–5 years standard; perpetual is unusual and worth flagging
- Return/destruction obligation on termination?
- Non-solicitation or non-compete buried in NDA — flag immediately if present
- Governing law clause present?

**For ToS / Privacy Policy:**
- GDPR/CCPA: lawful basis, data subject rights, DPO contact, retention periods
- Acceptable use policy present?
- Limitation of liability clause present?

**Output:**
- GREEN (sign as-is) / AMBER (negotiate these points) / RED (do not sign without changes)
- Bullet list of specific redlines for AMBER/RED items only
- Estimated negotiation effort: 1 hour / half day / full legal engagement

---

### Regulatory & Compliance Check

**Gather:** Business type, jurisdiction(s), specific activity or product being assessed, any existing compliance framework.

**Core regimes to check (filter to relevant):**

| Regime | Trigger | Key obligation |
|--------|---------|----------------|
| GDPR / UK GDPR | Processing EU/UK personal data | Lawful basis, DPA, breach notification 72h |
| CCPA | California consumers | Right to opt out, privacy notice, data deletion |
| FCA / SEC | Financial services, investment, lending | Authorisation, suitability, disclosure |
| Employment law | Hiring in jurisdiction | Contracts, right to work, payroll, benefits |
| Consumer protection | Selling to consumers | 14-day cooling off, unfair terms, refund rights |
| AML / KYC | Financial transactions | Customer due diligence, suspicious activity reports |
| Open source licences | Using OSS in commercial product | Copyleft vs permissive; GPL contamination risk |
| Export controls | Software/tech sales cross-border | US EAR, EU dual-use, OFAC sanctions |

**Deliver:**
- Applicable regimes table (regime → status: compliant / gap / unknown)
- Gap remediation plan: specific actions, estimated effort, priority order
- Referrals needed (flag where analysis requires a qualified practitioner)


---

## Final Delivery

1. SEO targets + technical checklist
2. Landing page copy + launch blog post
3. Social media launch kit (pre/launch/post content)
4. Legal risk summary + any flagged items
