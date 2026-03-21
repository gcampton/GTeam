# SEO Technical Checklist

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

Use this as a systematic audit checklist. Work top to bottom — crawl blocks and canonicals first, cosmetic issues last.

## Priority 1 — Crawl & Indexation

- [ ] **Robots.txt** — accessible at `/robots.txt`, no accidental `Disallow: /` blocking crawlers
- [ ] **XML Sitemap** — exists, submitted to GSC, contains only indexable URLs (no 4xx, no noindex)
- [ ] **Noindex tags** — confirm no pages are accidentally noindexed (`<meta name="robots" content="noindex">`)
- [ ] **Canonical conflicts** — every page has exactly one canonical; no page canonicals to a different page that itself has a different canonical (chain canonicals)
- [ ] **HTTPS** — site is fully HTTPS; no mixed-content warnings; HTTP redirects to HTTPS
- [ ] **Redirect chains** — no chains longer than 1 hop (A → B → C should be A → C)
- [ ] **4xx errors** — zero broken internal links; external broken links flagged for replacement

## Priority 2 — On-Page Fundamentals

- [ ] **Title tags** — 50–60 characters, primary keyword near front, unique per page
- [ ] **Meta descriptions** — 150–160 characters, compelling, unique per page, includes keyword
- [ ] **H1** — exactly one H1 per page, contains primary keyword, not a duplicate of title tag
- [ ] **H2/H3 hierarchy** — logical nesting, secondary keywords present, no heading skips (H1 → H3 without H2)
- [ ] **Canonical tag** — self-referencing `<link rel="canonical">` on every indexable page
- [ ] **Open Graph / Twitter cards** — present for social share appearance

## Priority 3 — Core Web Vitals

Check via Google PageSpeed Insights (desktop + mobile):

| Metric | Target | Check |
|--------|--------|-------|
| LCP (Largest Contentful Paint) | < 2.5s | Hero image/text load time |
| CLS (Cumulative Layout Shift) | < 0.1 | No layout jumps after load |
| INP (Interaction to Next Paint) | < 200ms | JS blocking, event handlers |

**Common LCP fixes:** Preload hero image, use modern image formats (WebP/AVIF), CDN, reduce TTFB.
**Common CLS fixes:** Set explicit width/height on images, avoid injecting content above existing content.

## Priority 4 — Mobile

- [ ] Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] Tap targets ≥ 48×48px (buttons, links)
- [ ] No horizontal scroll on mobile
- [ ] Font size ≥ 16px for body text (avoid browser zoom requirement)
- [ ] Mobile PageSpeed score ≥ 75

## Priority 5 — Internal Linking & Structure

- [ ] No orphan pages (every page reachable via internal link)
- [ ] Tiered link structure: pillar pages → hub pages → supporting articles
- [ ] Anchor text diversity — avoid all "click here" or all exact-match anchors
- [ ] No more than ~100 links per page (crawl budget)
- [ ] Breadcrumbs present on deep pages

## Priority 6 — Structured Data

- [ ] Schema present where applicable: Article, Product, FAQ, HowTo, LocalBusiness, BreadcrumbList
- [ ] Validated via Google Rich Results Test (no errors, only warnings acceptable)
- [ ] No schema mismatch (schema claims things not visible on page)

## Priority 7 — URL & Crawl Hygiene

- [ ] URLs lowercase, hyphens not underscores, no unnecessary parameters
- [ ] Paginated series handled correctly (rel=next/prev deprecated — use canonical to page 1 or index all)
- [ ] Faceted navigation / filter URLs: either noindex or canonicalised to prevent duplication
- [ ] Crawl depth — important pages reachable within 3 clicks from homepage

---

## Quick-Reference: Issue → Priority → Fix

| Issue | Priority | Fix |
|-------|----------|-----|
| Robots.txt blocking crawlers | P0 | Edit robots.txt immediately |
| Accidental noindex on key pages | P0 | Remove noindex tag |
| Missing/conflicting canonicals | P1 | Add self-referencing canonical |
| Redirect chains | P1 | Update to single-hop redirect |
| 4xx broken links | P1 | Fix or redirect |
| Title tag too long/missing | P2 | Rewrite to 50–60 chars |
| No H1 or multiple H1s | P2 | Fix heading structure |
| LCP > 2.5s | P2 | Image optimisation + CDN |
| CLS > 0.1 | P2 | Set image dimensions |
| Mobile tap targets too small | P3 | CSS fix |
| Orphan pages | P3 | Add internal link from relevant hub |
| Missing schema | P4 | Add relevant structured data |
