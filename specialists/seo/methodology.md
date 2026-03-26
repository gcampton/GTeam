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
