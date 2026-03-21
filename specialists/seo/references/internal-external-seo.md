# SEO Strategy: Internal & External

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

## Internal SEO

### Website Audit

A full audit identifies structural issues before any content work begins. Check in this order:

1. **Broken links** — crawl with a tool (Screaming Frog, Ahrefs Site Audit) or `$B` and fix all 4xx/5xx links. Broken internal links waste crawl budget and hurt UX.
2. **Canonical tags** — every page should have a self-referencing canonical. Paginated series, filtered URLs, and HTTPS/HTTP variants must all point to the correct canonical. Conflicting canonicals cause index confusion.
3. **Interlinking (tiered structure)** — structure pages in a clear hierarchy:
   - Tier 1: Homepage / pillar pages
   - Tier 2: Category / topic hub pages
   - Tier 3: Supporting articles / product pages
   Each tier links down to support and up to authority. Orphan pages (no inbound internal links) should be linked from a relevant tier.
4. **Above the fold content** — the most important content (H1, value prop, primary keyword) should appear before the fold on both desktop and mobile. Google weights above-the-fold content more heavily.

**Audit output:** Prioritised issue list with fix, page affected, and estimated impact.

---

### Page Planning

Before writing new content, audit existing pages first — rewriting an existing ranking page is almost always faster than writing from scratch.

**Evaluate existing pages for rewrites:**
- Pages ranking 4–20 for target keyword (quick-win candidates)
- Pages with thin content (<600 words) for a competitive keyword
- Pages with high impressions but low CTR (title/meta problem)
- Pages cannibalising the same keyword across multiple URLs

**Planning new pages:**
- Identify keyword gaps: topics competitors rank for that you don't cover
- Group keywords by intent cluster — one page per intent, not one page per keyword
- Map each new page to a tier in the site structure before writing
- Confirm search volume justifies effort (≥100 monthly searches for niche, ≥500 for broader)

---

### Rewriting Pages (SEO Optimisation)

When rewriting an existing page:

1. Pull current rankings and impressions from Google Search Console
2. Identify the primary keyword and 2–4 secondary/LSI keywords
3. Review top 3 SERP competitors — match or exceed their content depth
4. Rewrite with: keyword in H1, keyword in first 100 words, keyword in at least one H2, natural keyword density (~1–2%)
5. Add structured data (FAQ schema for Q&A content, HowTo schema for tutorials)
6. Improve internal links: add 2–4 relevant internal links from and to this page
7. Update meta title and description with keyword and a clear CTA/benefit
8. **Apply E-E-A-T signals** — see `eeat.md`. At minimum: named author with bio, firsthand specifics that generic content wouldn't contain, sources cited for all factual claims, publish/update date visible

---

### Creating New SEO Pages

1. Confirm keyword cluster and search intent (informational / commercial / transactional)
2. Write a content brief: target keyword, secondary keywords, required headings, word count target, competitor reference URLs
3. **Plan E-E-A-T before writing** — see `eeat.md`. Decide upfront: who is the author, what firsthand experience will be included, what sources will be cited, is this YMYL (if so, requires expert review before publishing)
4. Publish with: unique title tag, unique meta description, self-referencing canonical, proper schema markup, named author with bio, visible publish date
5. Submit URL to Google Search Console after publishing
6. Add internal links from at least 2 existing pages

---

## External SEO

### Link Building — High Quality, Low Volume

Focus on fewer, higher-authority links rather than volume. A single DA 60 link outweighs 50 DA 20 links.

**Quality thresholds (minimum):**
- Page Authority (PA): ≥ 25
- Domain Authority (DA): ≥ 30
- Spam score: ≤ 5% (Moz)
- Organic traffic: page should have real traffic (verify via Ahrefs/Semrush if available)

**Link placement rules:**
- Link must appear in the body content, not footer/sidebar
- Anchor text should be varied: branded, keyword, partial-match, and generic ("click here") mix
- The linking page should be topically relevant to your target page

---

### Email Outreach for Guest Posting

**Prospecting:**
- Search: `[niche] "write for us"` / `[niche] "guest post"` / `[niche] "contributor"`
- Filter results: DA ≥ 30, not a link farm (check for too-many outbound links, thin editorial standards)

**Outreach email structure:**
1. Personalised opener — reference a specific post on their site
2. One-line intro — who you are, relevant credential
3. 2–3 specific headline ideas tailored to their audience
4. Short close — no pressure, happy to send full outline first

**Follow-up:** One follow-up after 5–7 days, then move on. Do not spam.

---

### Guest Posting with Links

**Before accepting a guest post slot:**
- Confirm DA/PA meets threshold
- Confirm the post will be indexed (not noindex)
- Confirm link will be dofollow (or note nofollow — still has referral value)
- Agree on anchor text in advance

**Writing the post:**
- Match the host site's tone and content depth
- Link naturally — contextual placement, not forced
- Include only one link to your site per post (unless more are editorially justified)
- Deliver on time, formatted per their guidelines

**Tracking:**
- Record every live link: source URL, target URL, anchor text, DA, date live
- Check links monthly (Ahrefs alerts or manual check) — links can disappear or go nofollow
