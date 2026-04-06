### Affiliate Marketing Research

**Use when:** User wants to find affiliate opportunities in a specific niche, or find the best affiliate niches to enter.

**Gather:** Niche or topic area. Budget for content/SEO (if any). Preferred content type (blog, YouTube, newsletter, social).

**Step 1 — Find affiliate programs:**

Search across multiple networks:
```
WebSearch: "<niche> affiliate program site:shareasale.com OR site:cj.com OR site:impact.com"
WebSearch: "<niche> affiliate program commission rate"
WebSearch: "<niche> best affiliate programs <year>"
```

For each program found, check:
- Commission rate: digital products target ≥ 30%, physical ≥ 8%, SaaS ≥ 20% recurring
- Cookie window: 30 days minimum; 90 days ideal
- EPC (earnings per click) if published — higher = better converting offer
- Payout threshold and method (PayPal, bank transfer, cheque)
- Brand quality: would you recommend this to a friend?

**Step 2 — Keyword opportunity within the niche:**

For each top affiliate program, find content keywords that can rank:
- WebSearch: `"best <product type>" OR "<product> review" OR "<product> vs"` — commercial intent keywords
- Check top results: are they authoritative domains (DA 60+) or thin affiliate sites?
- Identify the 5 keywords where thin sites are ranking — those are the entry points

**Step 3 — Competitor affiliate site analysis:**
- `$B goto <competitor affiliate site>` — what pages get the most links? (check their top content)
- What affiliate disclosure patterns do they use?
- What's their content volume and publishing cadence?
- Could a more thorough, better-designed site outrank them within 6–12 months?

**Step 4 — Traffic and earnings estimate:**
- Estimate traffic: ranking position × search volume × average CTR (pos 1 = 28%, pos 3 = 11%, pos 5 = 7%)
- Earnings estimate: monthly visits × 2% conversion × average commission
- Example: 5,000 visits/month × 2% conversion × £40 commission = £4,000/month at scale

**Deliver:**
- Top 5 affiliate programs with commission rates, cookie windows, and brand quality assessment
- Top 10 keywords to target (keyword → search vol estimate → competition → affiliate angle)
- Competitor gap: what the top site is missing that you could own
- 90-day content plan to start building affiliate revenue
- Earnings potential estimate (conservative / realistic / optimistic)

---

### Content Channel Research (YouTube / TikTok)

**Use when:** User wants to build a YouTube or TikTok channel for ad revenue, sponsorships, or affiliate traffic.

**Gather:** Broad topic interest (or ask for none — find what works), available equipment (phone only / basic setup / full setup), time per week for video.

**Step 1 — Find underserved YouTube niches:**

```
WebSearch: "YouTube niche low competition high CPM <year>"
WebSearch: site:reddit.com/r/youtubers OR /r/NewTubers "low competition niche"
```

For each candidate niche, check:
- `$B goto https://www.youtube.com/results?search_query=<niche>` — scroll through results
  - How many channels have < 10k subs but 100k+ views on individual videos? (= underserved)
  - What's the average view count on top videos from channels under 50k subs?
  - Are recent videos (< 6 months) getting traction, or is it all old content?

**Step 2 — CPM/RPM data by niche:**

Check `references/monetisation-models.md` for CPM benchmarks, then verify with:
```
WebSearch: "<niche> YouTube CPM <year>"
WebSearch: "<niche> YouTube RPM how much"
```

High-CPM niches (typically £8–30+ CPM): personal finance, software/SaaS reviews, B2B tools, legal, insurance, investing, AI tools
Low-CPM niches (typically £1–4 CPM): gaming (exceptions exist), general entertainment, memes

**Step 3 — Competitor channel deep-dive:**

Pick 3–5 channels with 5k–100k subs that are growing in the niche:
- `$B goto <channel url>` — check: upload frequency, average views per video, engagement (likes/comments)
- What video formats are they using? (talking head, screen record, faceless, animation)
- What video topics get 2× their average views? (that's the sweet spot)
- What are they NOT covering? (content gaps = your opportunity)

**Transcript extraction for deeper analysis:**
Extract transcripts from competitors' top 3-5 videos to understand their content strategy at depth:
```bash
# Extract YouTube subtitles (no video download needed)
pip install yt-dlp 2>/dev/null
yt-dlp --write-auto-sub --sub-lang en --skip-download -o "%(title)s" "VIDEO_URL"

# Or use the YouTube transcript API for clean text
pip install youtube-transcript-api 2>/dev/null
python3 -c "from youtube_transcript_api import YouTubeTranscriptApi; print('\n'.join(e['text'] for e in YouTubeTranscriptApi.get_transcript('VIDEO_ID')))"
```
Analyse transcripts for: pain points addressed, frameworks taught, language patterns, CTAs used, questions left unanswered (= your content gaps). For full transcript analysis methodology, see `content-creator/references/transcript-analysis.md`.

**Step 4 — Faceless channel viability check:**

If user wants faceless (AI voiceover, stock footage, or screen recordings):
- Is the niche viable without a personal brand? (tutorials, reviews, and finance often work; vlogging doesn't)
- WebSearch: `"faceless YouTube channel" "<niche>" success` — find proof of concept
- Tools needed: ElevenLabs (voice), Canva/Adobe (thumbnails), CapCut/DaVinci (editing)

**Step 5 — TikTok angle (if relevant):**

TikTok works differently — discoverability is algorithm-driven, not search-driven:
- Find trending sounds + topics: WebSearch `TikTok trending "<niche>" <month year>`
- Hook formats that work: "POV:", "Things I wish I knew about X", "Day in the life of X"
- Monetisation path: TikTok Creator Fund (low RPM) → sponsorships → affiliate links in bio → own product

**Deliver:**
- Top 3 channel concepts with niche, format, CPM estimate, and competition level
- Content gap analysis: 10 video ideas the top channels haven't covered well
- Monetisation timeline: when to expect first AdSense payment, first sponsorship inquiry
- First 10 video titles (optimised for both SEO and click-through)
- Channel setup checklist (name, branding, SEO description, first upload strategy)
