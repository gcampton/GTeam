## Technical SEO Audit (`/gteam seo technical <url>`)

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
