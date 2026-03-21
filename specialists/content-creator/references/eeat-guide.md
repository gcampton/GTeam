# Google E-E-A-T Implementation Guide

> **Confidence:** All recommendations are `[HYPOTHESIS]` (untested best-practice) unless marked `[TESTED: date]` or `[REVISED: date]`. Check `../results/` for empirical outcomes before applying advice.

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is Google's quality evaluator framework, used by human Quality Raters and increasingly inferred algorithmically. It is not a direct ranking factor — it is a proxy signal correlated with content quality. Treat it as a content quality standard, not an SEO trick.

---

## Experience — Signals of Firsthand Knowledge

Experience is the newest addition (2022). It distinguishes content written by someone who has done the thing from content synthesised from other sources.

**What firsthand experience looks like:**

- Specific dates: "In March 2024, we ran this test on 1,200 subscribers..."
- Actual outcomes with numbers: "Response rate increased from 1.8% to 4.3%"
- Named people and places: "Our account manager at [Vendor] told us..."
- Original photos: screenshots, real product images, process photos — not stock
- Failure disclosure: "This didn't work. Here's what we tried next."
- Decisions with context: "We chose X over Y because of Z constraint"

**What AI cannot fake:**

`[HYPOTHESIS]` Google's quality raters are specifically trained to flag content that describes processes correctly but at a surface level — the pattern of a textbook, not a practitioner. The signal is specificity of failure, not just specificity of success.

- Unexpected outcomes that contradict the "best practice"
- Named counterparties (vendor, client, colleague)
- Time-bound context (what the market / tool / situation was at the time)
- Costs, timelines, constraints — the friction of real execution

**Experience checklist:**
- [ ] Does the article name a specific time period when events occurred?
- [ ] Are outcomes expressed as real numbers (not ranges or estimates)?
- [ ] Are there original images, screenshots, or data tables from actual work?
- [ ] Is there at least one disclosure of what went wrong or what was tried and failed?

---

## Expertise — Author Credentials

Expertise is demonstrated through credentials, depth of knowledge, and author attribution. Anonymous or vague authorship is a red flag.

**Required byline format:**

```
Written by [Full Name], [Relevant Title or Role]
[Short bio — 1–2 sentences connecting credentials to the topic]
[LinkedIn URL or professional profile link]
Last updated: [Month YYYY]
```

Example:
```
Written by Sarah Chen, Head of Demand Generation at Acme Corp
Sarah has run email campaigns for 7 years across SaaS and fintech,
managing lists of up to 400k subscribers.
linkedin.com/in/sarahchen
Last updated: February 2025
```

**Expertise signals by content type:**

| Content type | Minimum expertise signal |
|---|---|
| General how-to | Named author with 2+ years relevant experience |
| Product review | Author has used the product; states how long |
| Industry analysis | Author works in the industry or cites primary interviews |
| Opinion / commentary | Author's background makes opinion credible |
| YMYL content (health/finance/legal) | Named expert with professional credentials (MD, CPA, JD) |

`[HYPOTHESIS]` A brief, specific credential sentence outperforms a long bio. "Maria spent 12 years as a tax attorney specialising in small business formation" signals more expertise than a 200-word biography.

---

## Authoritativeness — Source Credibility

Authoritativeness is about what others say about you — and what you cite.

**Citation standards:**

- Cite primary sources: government reports, peer-reviewed research, official statistics
- Link to `.gov`, `.edu`, `.org` where applicable — these carry citation weight
- Avoid citing blog-to-blog: if Source A cites Source B, go find Source B and cite it directly
- Include publication date for every statistic cited: "per the CDC's 2023 report"

**Do not cite:**
- Other blogs without checking their original source
- Wikipedia as a final source (acceptable as a starting point)
- Paywalled sources readers cannot verify
- Your own older articles as "proof" of a claim

**Internal authoritativeness signals:**
- [ ] The site has a clear topical focus (not a general "lifestyle" blog with one finance article)
- [ ] The article links to related content on the same site that demonstrates depth
- [ ] Other credible sites have linked to this site or author (earns authority, not built in a day)

`[HYPOTHESIS]` A page that cites 3–5 primary sources (government data, academic research, official industry reports) with links will be evaluated as more authoritative than a page with 15 citations all pointing to other blogs.

---

## Trustworthiness — The Trust Stack

Trustworthiness is the baseline. Without it, E-E-A-T fails regardless of expertise level.

**Required trust infrastructure:**

| Element | Minimum requirement |
|---|---|
| **Privacy policy** | Exists, is linked in footer, covers data collection |
| **Contact page** | Has a real email or contact form, not just a social media link |
| **About page** | Features real people with names and roles, not corporate-speak |
| **HTTPS** | Site is fully HTTPS — no exceptions |
| **Business signals** | Physical address (if applicable), phone number, business registration |

**Trust stack — ordered by impact:**

1. HTTPS + no security warnings (foundational — all else fails without this)
2. Privacy policy visible in footer
3. Named authors on every article (not "Editorial Team")
4. Contact page with real details
5. About page with real bios and photos
6. Editorial or review policy published
7. Corrections policy: "If we get something wrong, we update the article and note what changed"

`[HYPOTHESIS]` A corrections policy — even a simple sentence at the bottom of the About page — is one of the most underused trust signals. It demonstrates intellectual honesty and is specifically cited in Google's Quality Rater Guidelines.

---

## YMYL Content Checklist

YMYL (Your Money or Your Life) content covers health, finance, legal, and safety topics. Google applies stricter E-E-A-T standards here because bad advice can cause real harm.

**YMYL content categories:**
- Health and medical advice
- Financial decisions (investments, taxes, insurance)
- Legal guidance
- Safety information

**Before publishing YMYL content:**
- [ ] Named author has verifiable professional credentials in the subject area (MD, RN, CPA, JD, CFP)
- [ ] Content reviewed by a second credentialed expert
- [ ] Review date is visible on the page
- [ ] Disclaimer is present and accurate (e.g., "This is not financial advice — consult a licensed advisor")
- [ ] Sources are primary: peer-reviewed journals, official government guidance, professional body standards
- [ ] No claims that exceed what the evidence supports

`[HYPOTHESIS]` For YMYL content, the expert review step is non-negotiable. A page written by a generalist with a medical review is significantly safer than a page written by a doctor without any structural disclosure — because the disclosure signals process, not just credentials.

---

## Red Flags That Fail E-E-A-T

If any of these are present, fix them before optimising anything else.

| Red flag | Why it fails | Fix |
|---|---|---|
| "Editorial Team" byline | No accountable human, no credentials | Replace with named author + bio |
| No publish date or update date | Signals stale content, no quality maintenance | Add "Published: [date] / Updated: [date]" |
| AI-generated stock photos | No firsthand experience signal | Replace with real photos, screenshots, or remove images |
| No citations | Claims without evidence | Add primary source links |
| Zero external links | Signals insularity, fear of "link leaking" | Link out to authoritative sources — it builds trust |
| No About page | No entity identity | Build a real About page with named people |
| Contact form only, no email | Low trust for sensitive content | Add a real email address |
| Affiliate content with no disclosure | Legal requirement (FTC), trust signal | Add affiliate disclosure above the fold |

---

## Adding E-E-A-T Post-Hoc

For existing content that lacks E-E-A-T signals, use this review workflow.

**Step 1 — Audit each article:**
Add an internal comment or doc note: `[OWNER INPUT NEEDED]` wherever the article makes a specific claim that requires firsthand knowledge to validate.

**Step 2 — Owner input session:**
Schedule 30 minutes with the person who has done the work (the subject matter expert, not the writer). Ask:
- "What actually happened? Give me dates and numbers."
- "What went wrong that we didn't include?"
- "What would you have done differently?"

**Step 3 — Writer revision:**
Replace generic claims with specifics from the owner input session. Add original data where possible.

**Step 4 — Add the author block:**
Create a named author byline for the subject matter expert, even if they didn't write the article. Use: "Written by [Writer] in collaboration with [Expert], [Title]."

**Step 5 — Update date and add review note:**
Change the article date to the revision date and add: "Updated [Month YYYY] to add [specific information from review]."

`[HYPOTHESIS]` Post-hoc E-E-A-T upgrades are more effective when they add specific numbers and failure disclosures than when they add author bios alone. The signal Google is looking for is specificity of experience, not credentials.
