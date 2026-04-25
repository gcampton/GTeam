## Full Site Audit — SEO + GEO (`/gteam seo audit <url>`)

This is the flagship command. Combines traditional SEO depth with GEO's AI-visibility analysis. Produces a composite 0–100 score and a client-ready deliverable.

### Phase 1: Discovery (Sequential)

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

### Phase 2: Parallel Analysis (Delegate to GEO Subagents)

Launch these 5 subagents simultaneously via Agent tool. Pass each subagent: the target URL, list of crawled pages, and detected business type.

| Subagent | Agent File | Responsibility |
|---|---|---|
| geo-ai-visibility | `~/dev/1_myprojects/gteam/specialists/seo/geo-agents/geo-ai-visibility.md` | Citability scoring, AI crawler access, llms.txt, brand mentions |
| geo-platform-analysis | `~/dev/1_myprojects/gteam/specialists/seo/geo-agents/geo-platform-analysis.md` | Platform-specific optimization (ChatGPT, Perplexity, Google AIO, Gemini, Bing Copilot) |
| geo-technical | `~/dev/1_myprojects/gteam/specialists/seo/geo-agents/geo-technical.md` | Technical SEO: Core Web Vitals, crawlability, mobile, security, SSR |
| geo-content | `~/dev/1_myprojects/gteam/specialists/seo/geo-agents/geo-content.md` | Content quality, E-E-A-T, readability, freshness, original data |
| geo-schema | `~/dev/1_myprojects/gteam/specialists/seo/geo-agents/geo-schema.md` | Schema.org detection, validation, JSON-LD generation |

### Phase 3: Traditional SEO Layer

While subagents run (or after collecting results), apply traditional SEO depth:
- Full 14-point technical checklist (see Technical SEO Audit section below)
- Keyword gap analysis against 2–3 key competitors via WebSearch
- Internal linking audit — identify orphan pages, anchor text diversity
- Link profile assessment — estimate authority, check for thin or duplicate-content issues

### Phase 4: Score Aggregation + Report

Collect all subagent results, combine with traditional SEO findings, compute composite score (see Scoring Methodology), and write output to `~/geo-seo-projects/[domain]/SEO-GEO-AUDIT-REPORT.md`.
