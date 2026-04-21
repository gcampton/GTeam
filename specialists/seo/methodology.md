### Browse Setup

When a URL is provided, run this setup block before any browse step:

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: skip all `$B` steps and use WebFetch instead for URL inspection.

---

### Full Site Audit — SEO + GEO (`/gteam seo audit <url>`)

This is the flagship command. Combines traditional SEO depth with GEO's AI-visibility analysis. Produces a composite 0–100 score and a client-ready deliverable.

#### Phase 1: Discovery (Sequential)

1. Fetch homepage (WebFetch or `$B goto <url> && $B snapshot`)
2. Detect business type from signals:

| Business Type | Detection Signals |
|---|---|
| **SaaS** | Pricing page, "Sign up"/"Free trial", app.domain.com, feature tables, integration pages |
| **Local Business** | Physical address, Google Maps embed, "Near me" content, LocalBusiness schema |
| **E-commerce** | Product listings, shopping cart, price displays, "Add to cart" |
| **Publisher** | Blog-heavy nav, article schema, author pages, date archives, RSS |
| **Agency** | Case studies, portfolio, client logos, service pages, team page |
| **Hybrid** | Classify by dominant pattern |

3. Crawl sitemap (`/sitemap.xml`, `/sitemap_index.xml`) or follow homepage links up to 2 levels deep. Max 50 pages. Respect robots.txt. Record per page: URL, title, meta description, canonical, H1–H6, word count, schema types, image alt coverage, internal/external link counts, response status.

#### Phase 2: Parallel Analysis (Delegate to GEO Subagents)

Launch these 5 subagents simultaneously via Agent tool. Pass each subagent: the target URL, list of crawled pages, and detected business type.

| Subagent | Agent File | Responsibility |
|---|---|---|
| geo-ai-visibility | `~/.claude/skills/gteam/specialists/seo/geo-agents/geo-ai-visibility.md` | Citability scoring, AI crawler access, llms.txt, brand mentions |
| geo-platform-analysis | `~/.claude/skills/gteam/specialists/seo/geo-agents/geo-platform-analysis.md` | Platform-specific optimization (ChatGPT, Perplexity, Google AIO, Gemini, Bing Copilot) |
| geo-technical | `~/.claude/skills/gteam/specialists/seo/geo-agents/geo-technical.md` | Technical SEO: Core Web Vitals, crawlability, mobile, security, SSR |
| geo-content | `~/.claude/skills/gteam/specialists/seo/geo-agents/geo-content.md` | Content quality, E-E-A-T, readability, freshness, original data |
| geo-schema | `~/.claude/skills/gteam/specialists/seo/geo-agents/geo-schema.md` | Schema.org detection, validation, JSON-LD generation |

#### Phase 3: Traditional SEO Layer

While subagents run (or after collecting results), apply traditional SEO depth:
- Full 14-point technical checklist (see Technical SEO Audit section below)
- Keyword gap analysis against 2–3 key competitors via WebSearch
- Internal linking audit — identify orphan pages, anchor text diversity
- Link profile assessment — estimate authority, check for thin or duplicate-content issues

#### Phase 4: Score Aggregation + Report

Collect all subagent results, combine with traditional SEO findings, compute composite score (see Scoring Methodology), and write output to `~/geo-seo-projects/[domain]/SEO-GEO-AUDIT-REPORT.md`.

---

### AI Visibility Analysis (`/gteam seo ai <url>`)

Deep-dive into AI-era signals only. No traditional keyword research or link building.

**1. AI Citability Scoring**

For each key page, assess:
- Does the opening paragraph directly answer a likely query? (Featured snippet / AI answer block targeting)
- Are there clear question-based H2s and direct answers below them?
- Is content structured for extraction (short paragraphs, lists, tables)?
- Does the page cite authoritative external sources?
- Is there original data or research that AI would want to quote?

Score each page 0–100 for citability. Flag top 5 most citable and bottom 5 least citable with specific rewrite suggestions.

**2. AI Crawler Access**

Fetch `/robots.txt`. Check access for:

| Crawler | Platform |
|---|---|
| GPTBot | ChatGPT / OpenAI |
| ClaudeBot | Anthropic Claude |
| PerplexityBot | Perplexity AI |
| Google-Extended | Gemini / Google AI |
| Bingbot | Bing Copilot / ChatGPT |
| Googlebot | Google AIO |
| Applebot-Extended | Apple Intelligence |

For each: Allowed / Blocked / Partial. Flag blocks as Critical or High severity.

**3. llms.txt Audit / Generation**

Fetch `<domain>/llms.txt` and `<domain>/llms-full.txt`.
- If present: validate structure (title, description, key sections, file links). Flag gaps.
- If absent: generate a complete llms.txt and llms-full.txt. Write to `~/geo-seo-projects/[domain]/llms.txt` and `~/geo-seo-projects/[domain]/llms-full.txt`. If a `public/` directory exists in the current working directory, also copy there for immediate deployment.

**4. Brand Mention Scan**

Search for brand presence on AI-cited platforms:
- Wikipedia: `WebSearch "site:en.wikipedia.org <brand>"`
- Reddit: `WebSearch "site:reddit.com <brand>"` — check volume, sentiment, top subreddits
- YouTube: `WebSearch "site:youtube.com <brand>"` — official channel + mentions
- LinkedIn: `WebSearch "site:linkedin.com/company <brand>"`
- Wikidata: `WebSearch "site:wikidata.org <brand>"`
- Crunchbase / GitHub / G2 as applicable

Score brand authority 0–100 based on presence depth and authority-platform coverage.

**5. Platform-Specific Readiness**

Assess each AI platform:

| Platform | Key Factors |
|---|---|
| Google AI Overviews | Schema.org markup, E-E-A-T signals, structured direct-answer passages, Core Web Vitals |
| ChatGPT / Perplexity | GPTBot/PerplexityBot allowed, Reddit/Wikipedia presence, direct-answer content, llms.txt |
| Google Gemini | Google-Extended allowed, YouTube presence, Knowledge Panel, structured data |
| Bing Copilot | Bingbot allowed, IndexNow protocol, Bing Webmaster Tools, LinkedIn presence |

Score each platform 0–100 and flag the top action for each.

**Output:** `~/geo-seo-projects/[domain]/GEO-AI-VISIBILITY.md`

---

### Technical SEO Audit (`/gteam seo technical <url>`)

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

**Output:** `~/geo-seo-projects/[domain]/SEO-TECHNICAL-AUDIT.md`

---

### Keyword Research & Content Gap Analysis (`/gteam seo keyword <domain>`)

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

### On-Page Optimisation (`/gteam seo page <url>`)

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

### Link Building Strategy (`/gteam seo links <domain>`)

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

### Client Deliverables

#### Client-Ready Report (`/gteam seo report <url>`)

Aggregate all audit data (run audit first if not done) into `~/geo-seo-projects/[domain]/SEO-GEO-CLIENT-REPORT.md`. Written for business owners and marketing leaders — no unexplained jargon, every finding connected to business impact.

**Report structure:**
1. **Executive Summary** — 4–6 sentences: what was analyzed, composite score, single most impactful finding, top 3 priorities, estimated business impact ($X/month)
2. **Composite Score Dashboard** — overall score + 6 category breakdowns in a table
3. **AI Visibility Dashboard** — per-platform scores (Google AIO, ChatGPT, Perplexity, Gemini, Bing Copilot)
4. **AI Crawler Access** — table of each crawler: Allowed/Blocked, impact, recommendation
5. **Brand Authority** — presence on Wikipedia, Reddit, YouTube, LinkedIn, Wikidata
6. **Top 5 Most / Least Citable Pages** — URLs + why + one specific improvement each
7. **Traditional SEO Summary** — Core Web Vitals, mobile, HTTPS, canonical, sitemap
8. **Schema & Structured Data** — what's present, what's missing, ready-to-use JSON-LD if needed
9. **llms.txt Status** — present/missing + generated file if needed
10. **Keyword Opportunities** — quick wins (ranking 4–20), content gaps vs competitors
11. **Prioritized Action Plan:**
    - Quick Wins (this week, < 4 hours each): action, impact, effort, platforms affected
    - Medium-Term (this month, days of work): action, impact, effort
    - Strategic (this quarter, weeks of effort): action, impact, effort
    - Estimated impact: score improvement + revenue value
12. **Competitor Comparison** (if competitor URLs provided)
13. **Appendix** — methodology, pages analyzed, data sources, glossary

**Tone:** Confident and direct. "Your site does / does not…" not "it appears that…". Business-impact focus throughout.

#### PDF Report (`/gteam seo report-pdf <url>`)

Generates a professional branded PDF. Run the audit and collect all scores into a JSON structure, then execute:

```bash
python3 ~/.claude/skills/gteam/specialists/seo/scripts/generate_pdf_report.py data.json GEO-REPORT.pdf
```

**PDF includes:** Cover page with score gauge, score breakdown bar charts, AI platform readiness dashboard, crawler access status table, key findings by severity, prioritized action plan, methodology appendix.

**Output:** `~/geo-seo-projects/[domain]/SEO-GEO-REPORT-[domain].pdf`

#### Client Proposal (`/gteam seo proposal <domain>`)

Auto-generate a proposal from audit data. **Output:** `~/.geo-prospects/proposals/[domain]-proposal-[date].md`

**Proposal structure:** Executive summary of findings → proposed scope of work → deliverables and timeline → investment (tiered pricing) → ROI projection → next steps.

#### Monthly Delta Report (`/gteam seo compare <domain>`)

Compare current audit to previous report in `~/geo-seo-projects/[domain]/`. Show score movements, ranking wins/losses, and new/resolved issues. **Output:** `~/geo-seo-projects/[domain]/SEO-GEO-DELTA-[YYYY-MM].md`

---

### SEO Reporting & Tracking (`/gteam seo reporting`)

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
