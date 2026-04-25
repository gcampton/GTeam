## AI-Assisted Content Quality Control

**Use when:** Content is AI-generated or AI-assisted and must pass Google's quality standards, E-E-A-T signals, and avoid patterns that reduce credibility or ranking.

**The core problem:** AI-generated content is detectable by both humans and Google's quality systems — not necessarily because it's wrong, but because it lacks the markers of genuine firsthand experience. The fix is to add specificity, not to "humanise" the writing.

**Before reviewing or publishing:** `Grep {{GTEAM_DIR}}/specialists/content-creator/references/ai-writing-patterns.md` for the specific patterns you need to check. Work through all 5 categories below.

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
