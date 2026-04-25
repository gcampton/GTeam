## Tracking & Measurement

**Conversion tracking verification checklist (before scaling any spend):**

- [ ] GTM firing correctly on all conversion events — verify in GTM Preview mode and Tag Assistant
- [ ] Google Ads conversion actions using the correct tag or imported from GA4
- [ ] Enhanced conversions configured (hashed email/phone for better match rates)
- [ ] Meta Pixel firing on all key events (PageView, ViewContent, AddToCart, Purchase)
- [ ] Meta Conversions API (CAPI) implemented server-side — deduplication via `event_id` matching between browser Pixel and CAPI
- [ ] Attribution windows set intentionally: 7-day click / 1-day view for social (default); 30-day click for B2B longer sales cycles
- [ ] GA4 events verified in DebugView — event names, parameters, and values correct
- [ ] No double-counting: confirm deduplication logic between server-side and client-side events

**Platform vs. GA4 discrepancy root causes:**

| Cause | Typical discrepancy size |
|-------|--------------------------|
| Attribution window difference | 10–30% |
| Cross-device (platform claims, GA4 misses) | 5–20% |
| iOS privacy (SKAN, modelled conversions) | 10–40% for Meta |
| Bot traffic / click fraud | 2–15% |
| CAPI double-counting (no deduplication) | Can be 2× reported conversions |

**ROAS vs. MER (Media Efficiency Ratio):**
- **ROAS** (platform-reported) is channel-level, subject to attribution bias and platform self-reporting
- **MER** = Total Revenue / Total Ad Spend (blended, all channels). More reliable for understanding true return on overall spend.
- Use MER for budget allocation decisions across channels. Use ROAS for intra-channel optimisation (which campaigns/ad groups to scale or cut).
- Track MER weekly. Rising MER with flat ROAS → organic is helping. Falling MER with stable ROAS → paid is cannibalising organic.

**Weekly reporting format:**

| Metric | This week | Last week | WoW change | vs. target |
|--------|-----------|-----------|------------|------------|
| Spend | | | | |
| Impressions | | | | |
| Clicks | | | | |
| CTR | | | | |
| CPC | | | | |
| Conversions | | | | |
| CPA | | | | |
| ROAS | | | | |
| MER (blended) | | | | |

Include one "insight" per channel: what changed, why (if known), and what action is being taken. Reporting without recommended action is just noise.
