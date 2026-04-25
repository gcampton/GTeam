## Paid Search (Google/Microsoft)

**Account architecture (hierarchy):**
Campaign (budget + bid strategy + network settings) → Ad Group (theme/intent cluster) → Keywords → Ads (RSAs). Each level controls different variables — don't mix unrelated themes in one ad group.

**Recommended campaign tiers:**
1. Brand (exact + phrase) — protect own brand terms, usually highest ROAS
2. Non-brand (core product/service terms) — main volume driver
3. Competitor (conquest) — separate budget, lower ROAS expectation, test messaging
4. Remarketing / RLSA — past visitors, often higher intent

**Match type strategy:**
- **Broad match + Smart Bidding (tCPA/tROAS):** Best for accounts with ≥30 conversions/month per campaign. Google's algorithm uses broad match signals effectively with sufficient data. Run alongside negatives to limit waste.
- **Phrase/Exact for control:** Use when conversion volume is low (algorithm learning is unreliable), brand terms (protect exact intent), or high-CPC terms where waste is expensive.
- **Never run broad match without smart bidding** — manual CPC + broad = uncontrolled spend.

**Negative keyword management:**
- Account-level negatives: irrelevant industries, competitor brand terms (unless running conquest), obviously off-topic queries
- Campaign-level negatives: cross-campaign isolation (non-brand campaign excludes brand terms, etc.)
- Review search term report weekly (new accounts) or monthly (mature accounts). Add converting queries as exact/phrase; add waste as negatives.

**Search term analysis workflow:**
1. Pull 90-day search term report, sort by cost descending
2. Flag: (a) high-spend / zero-conversion terms → add as negatives; (b) high-conversion terms not in keyword list → add as exact/phrase
3. Identify themes of waste — often reveals match type settings to tighten

**Ad copy structure (RSAs):**
- 15 headlines: 3–4 brand/trust, 3–4 benefit-focused, 3–4 feature-specific, 2–3 CTA variants, 1–2 social proof
- 4 descriptions: 2 benefit/value-led, 1 CTA-focused, 1 social proof or urgency
- Pin only when necessary (headline 1 for brand name or legal). Pinning reduces combination testing.
- Assets (formerly extensions): sitelinks (4 minimum), callouts (4 minimum), structured snippets, image extensions, call extension. 100% asset utilisation is a baseline, not a bonus.

**Smart bidding setup and learning period:**
- tCPA: set target at current CPA or 10–15% above — don't start aggressive. Allow 2–4 week learning period (50+ conversions). Avoid budget changes >20% or target changes >15% during learning.
- tROAS: requires higher conversion volume (≥50/month recommended). Set initial target at actual recent ROAS, not aspirational ROAS.
- Exiting learning period: stable conversion volume, consistent CPA/ROAS within 20% of target over 2+ weeks.
