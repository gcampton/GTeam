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

### SEO Audit

**Gather:** URL of the site or page. Use $B to load and inspect if available.

**Technical audit checklist:**
1. Title tags — length (50–60 chars), keyword inclusion, uniqueness across pages
2. Meta descriptions — length (150–160 chars), compelling copy, uniqueness
3. Heading structure — single H1, logical H2/H3 hierarchy
4. Core Web Vitals — LCP, CLS, FID/INP (check via PageSpeed Insights if browseable)
5. Mobile friendliness — viewport meta, tap target sizes
6. Canonical tags — self-referencing, no conflicting canonicals
7. Robots.txt + sitemap — accessible, no accidentally blocked pages
8. Internal linking — orphan pages, anchor text diversity
9. Keyword cannibalisation — multiple pages targeting same keyword
10. Backlink profile — assess via available data (Ahrefs, Moz if user provides)
11. Schema markup — structured data present and valid

**Keyword strategy:**
- Primary keyword: search intent (informational/commercial/transactional/navigational)
- Keyword gap opportunities from top 3 competitors (if URL provided)
- Quick-win keywords: ranking 4–20 with decent volume

**On-page recommendations:** Title, meta, H1, content additions — specific and copy-ready.

**Deliver:**
- Technical issues table (issue → priority → fix)
- Keyword opportunities table (keyword → intent → difficulty → recommended page)
- Copy-ready title tag and meta description for the primary page


---

## Step 2: Launch Content

Produce launch announcement, landing page copy, and blog post using Step 1 keyword targets.

### Content Creation

**Gather:** Topic, target audience, content goal (inform/convert/rank/entertain), target keywords if known, preferred format (blog post, landing page, newsletter, long-form guide).

**Research phase:**
1. Identify search intent for the primary keyword
2. Review top 3 ranking pages for this topic (WebSearch)
3. Find angles those pages miss — that's the differentiation

**Structure:**
- Hook: first sentence earns the second. Open with a specific claim, surprising fact, or vivid scenario.
- Subheadings: every H2 should be a complete thought, not a label
- Proof points: data, examples, case studies — one per major claim
- CTA: single, clear, matches reader intent at that point in the funnel

**Writing checklist:**
- Flesch reading ease ≥ 60 (conversational, not academic)
- No paragraph longer than 4 lines
- Internal linking: 2–4 links to related content (placeholder links if URLs unknown)
- Keyword density: primary keyword in title, H1, first 100 words, one H2, naturally throughout
- Meta title (50–60 chars) and meta description (150–160 chars) included

**Deliver:**
- Full content piece (publish-ready)
- Meta title and description
- Social media pull-quotes (3 × tweet-length excerpts)


---

## Step 3: Social Launch Campaign

Produce launch-day social posts, pre-launch teasers, and post-launch content calendar.

### Social Media Strategy

**Gather:** Brand/product description, target audience, current platforms (if any), content goals.

**Platform strategy (for each relevant platform):**
- Format requirements (image ratios, video length, character limits)
- Optimal posting cadence (based on platform algorithm norms)
- Content mix: educational / entertaining / promotional (80/20 rule guidance)
- Platform-specific hooks: carousels on LinkedIn, reels on Instagram, threads on X

**Content creation:**
1. Write 5 ready-to-post captions with hashtags (platform-specific)
2. Propose 3 content series ideas (recurring themes that build audience)
3. Draft 1 engagement post (question, poll, or interactive format)

**Engagement playbook:**
- Response templates for common comment types
- Hashtag strategy: 3 tiers (broad/niche/branded)
- Optimal posting times by platform

**Deliver:**
- Platform strategy one-pager per active platform
- 5 ready-to-post captions
- Content calendar template (2 weeks)
- Engagement playbook


---

## Step 4: Legal Checklist

Review any terms of service, privacy policy, or partner contracts associated with the launch.

### Legal Review

**Gather:** Ask for the document (file path or paste). Identify: contract type, parties, governing jurisdiction if visible.

**Review checklist — work through every clause:**
1. Liability & indemnification — who bears risk, any unlimited liability exposure?
2. IP ownership — who owns work product, licenses, background IP?
3. Termination — notice periods, termination for convenience vs cause, post-termination obligations
4. Governing law & jurisdiction — which courts, which law?
5. Payment terms — amounts, milestones, late payment, currency
6. Confidentiality — scope, duration, carve-outs
7. Warranties & representations — what's promised, what's disclaimed?
8. Dispute resolution — arbitration, mediation, litigation?
9. Force majeure — what events excuse performance?
10. Assignment — can either party assign without consent?

**Risk rating per clause:** HIGH / MEDIUM / LOW / OK

**Redline:** Produce a redlined version with suggested edits inline using `[SUGGESTED: ...]` markers.

**Surface to user only when:** a clause presents HIGH risk that could be deal-breaking, or when two equally valid interpretations exist and the choice has material consequences.

**Deliver:**
- Risk summary table (clause → risk level → one-line explanation)
- Redlined document with `[SUGGESTED: ...]` inline edits
- Recommended next steps (negotiate, accept, reject, seek specialist counsel)


---

## Final Delivery

1. SEO targets + technical checklist
2. Landing page copy + launch blog post
3. Social media launch kit (pre/launch/post content)
4. Legal risk summary + any flagged items
