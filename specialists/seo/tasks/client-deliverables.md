## Client Deliverables

### Client-Ready Report (`/gteam seo report <url>`)

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

### PDF Report (`/gteam seo report-pdf <url>`)

Generates a professional branded PDF. Run the audit and collect all scores into a JSON structure, then execute:

```bash
python3 ~/dev/1_myprojects/gteam/specialists/seo/scripts/generate_pdf_report.py data.json GEO-REPORT.pdf
```

**PDF includes:** Cover page with score gauge, score breakdown bar charts, AI platform readiness dashboard, crawler access status table, key findings by severity, prioritized action plan, methodology appendix.

**Output:** `~/geo-seo-projects/[domain]/SEO-GEO-REPORT-[domain].pdf`

### Client Proposal (`/gteam seo proposal <domain>`)

Auto-generate a proposal from audit data. **Output:** `~/.geo-prospects/proposals/[domain]-proposal-[date].md`

**Proposal structure:** Executive summary of findings → proposed scope of work → deliverables and timeline → investment (tiered pricing) → ROI projection → next steps.

### Monthly Delta Report (`/gteam seo compare <domain>`)

Compare current audit to previous report in `~/geo-seo-projects/[domain]/`. Show score movements, ranking wins/losses, and new/resolved issues. **Output:** `~/geo-seo-projects/[domain]/SEO-GEO-DELTA-[YYYY-MM].md`
