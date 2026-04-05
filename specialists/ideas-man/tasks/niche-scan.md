### Browse Setup

Browse is essential for this specialist — checking YouTube channels, competitor sites, affiliate programs, and trend data.

```bash
export PATH="$HOME/.bun/bin:$PATH"
B=~/.claude/skills/gteam/browse/dist/browse
[ -x "$B" ] && echo "READY: $B" || echo "BROWSE NOT AVAILABLE"
```

If `BROWSE NOT AVAILABLE`: use WebSearch + WebFetch for all research steps.

---

### Niche Opportunity Scan

**Use when:** User wants to find a new money-making niche. No specific model in mind yet — just looking for what's worth pursuing.

**Gather:** Broad area of interest (if any), available time (hours/week), capital available (£0 / < £500 / £500–5k), skills (writing, video, coding, design, none required).

**Research process:**

1. **Trend sweep** — find what's growing, not what's already saturated:
   - WebSearch: `site:reddit.com "passive income" OR "side hustle" "<year>"` — scan for recurring emerging topics
   - WebSearch: `Google Trends "<broad niche>" rising queries` — what's accelerating
   - WebSearch: `"low competition" "<niche>" affiliate OR dropship OR YouTube` — find where practitioners signal opportunity
   - `$B goto https://trends.google.com/trends/explore` and screenshot trending searches in relevant categories

2. **Competition check per candidate niche:**
   - Search volume vs. number of results: WebSearch `allintitle:"<niche keyword>"` — low allintitle count (< 10,000) with decent search volume = weak competition
   - Check top 3 ranking sites: are they big brands or thin affiliate sites? Thin sites = opportunity
   - `$B goto <top ranking url>` — what's the content quality? Could we do better easily?

3. **Monetisation confirmation** — before proceeding, verify a niche pays:
   - Affiliate programs exist with ≥ 20% commission or ≥ £30 per sale
   - YouTube CPM ≥ £3 (finance, software, health tend to be £8–30+)
   - Products that can be dropshipped at ≥ 40% gross margin
   - Or clear audience willingness to pay for a subscription/tool

4. **Score each candidate** using `references/niche-scoring-rubric.md`:
   - Demand score (search volume, trend direction)
   - Competition score (site quality of top results, allintitle count)
   - Monetisation score (commission rates, CPM, margin)
   - Effort score (time to first income, skills needed)
   - Combined score → rank candidates

**Deliver:**
- Top 5 niche opportunities ranked by combined score
- One-paragraph thesis for each: why this niche, why now, what's the angle
- Recommended entry model (affiliate / content / dropship / digital product) per niche
- Suggested first action for the #1 niche
