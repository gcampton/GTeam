# Platform Algorithm Deep-Dive

## How Platform Algorithms Work

All social platforms use ML-based ranking systems that decide which content to show to which users. Understanding these systems is the difference between posting and being seen. Every platform is solving the same core problem: given thousands of candidate posts, predict which ones THIS user will engage with RIGHT NOW.

### Universal Ranking Signals

| Signal | What It Measures | Why It Matters | Platforms |
|---|---|---|---|
| Engagement velocity | Likes/comments/shares in first 30-60 mins | Early momentum triggers wider distribution | All |
| Completion rate | % of content consumed (video watch time, carousel swipes, text dwell) | Signals content quality to the algorithm | TikTok, YouTube, Instagram Reels, LinkedIn |
| Saves/bookmarks | User explicitly stores content for later | Strongest intent signal — user values it enough to return | Instagram, TikTok, X, YouTube |
| Shares | Content forwarded to others via DM, repost, or external | Social proof — user stakes their reputation on it | All |
| Dwell time | How long a user stops scrolling on your content | Passive quality signal, harder to game than clicks | LinkedIn, Instagram, X |
| Negative signals | Hide, unfollow, report, "not interested" | Algorithmically expensive — one report can outweigh dozens of likes | All |
| Session contribution | Does viewing your content lead to MORE platform usage? | Platforms reward creators who keep users on-platform | YouTube (strongest), TikTok, Instagram |

### The Universal Distribution Pattern

Nearly every platform follows the same cascade: **Small test batch -> Measure engagement -> Expand or kill**. The size of the initial batch and the metrics that trigger expansion differ, but the pattern is consistent. Your content is never shown to everyone at once — it earns its audience in waves. [TESTED]

---

## X (Twitter) Algorithm

### Core Models

- **Real-graph** — predicts interaction likelihood between pairs of users. Your followers' past engagement with your tweets determines how widely new tweets distribute. If your followers consistently ignore you, your reach shrinks even as follower count grows. [TESTED — open-sourced 2023]
- **SimClusters** — community detection using sparse embeddings. Content that resonates within a tight community (e.g., "Rust developers" or "NBA Twitter") gets pushed to similar communities. This is why niche accounts often outperform broad ones. [TESTED]
- **TwHIN** — knowledge graph mapping users to topics, interests, and entities. Staying in your niche strengthens your topical authority. Sudden topic pivots confuse the model and reduce distribution. [TESTED]
- **Tweepcred** — user reputation/authority score based on engagement consistency, follower quality, and account age. High-Tweepcred accounts get preferential ranking. [TESTED]

### Feed Pipeline

```
Candidate Retrieval (Search Index + UTEG + Tweet-mixer)
    → ML Ranking (predicted engagement per user)
    → Filtering (blocks, mutes, content policy)
    → Delivery (ranked feed)
```

### Signal Weights (Approximate Priority)

| Signal | Relative Weight | Notes |
|---|---|---|
| Retweet | Strongest | User stakes reputation by sharing |
| Reply | Very high | Indicates discussion-worthy content |
| Like | High | Direct positive feedback |
| Bookmark | Moderate-high | Strong intent signal, added 2023 |
| Profile visit | Moderate | Curiosity about the author |
| Time spent reading | Moderate | Passive quality indicator |
| Link click | Low-moderate | Useful but takes users off-platform |

### Optimisation Tactics

1. **Hook in the first line.** Twitter truncates after ~280 chars in feed. The first sentence determines whether users expand. Lead with a surprising claim, number, or question — not a preamble. [TESTED]
   - Before: "I've been thinking about AI lately and wanted to share some thoughts."
   - After: "Most AI startups will fail for the same reason most restaurants fail: unit economics."

2. **End with a question to trigger replies.** Replies are the second-strongest signal. A direct question ("What's your experience?" / "Agree or disagree?") reliably outperforms statements. [TESTED]

3. **Use threads for complex ideas.** Threaded tweets get compounding engagement — each reply in the thread triggers notification to everyone who engaged with earlier tweets. First tweet must stand alone as a hook. [TESTED]

4. **Post during your audience's active hours.** First-hour engagement velocity determines distribution tier. Use X Analytics to find when your followers are online. For global audiences, 8-10am ET is generally strongest. [HYPOTHESIS — varies by niche]

5. **Engage before and after posting.** Reply to others' tweets 15-30 minutes before posting your own. This warms up your Real-graph connections and puts you in followers' recent interaction history. [HYPOTHESIS — widely reported but not confirmed in source code]

6. **Avoid external links in tweets.** X deprioritises tweets with outbound links. Put the link in a reply or use the "link card" format. Posts without links get approximately 2x the impressions. [TESTED — confirmed by multiple A/B tests]

---

## LinkedIn Algorithm

### How It Works

LinkedIn's algorithm is built around **professional content quality** and **network-based distribution**. Unlike X or TikTok, LinkedIn heavily weights your 1st and 2nd-degree connections over pure content signals. [TESTED]

- **Dwell time** is the primary engagement signal — LinkedIn tracks how long users stop scrolling on your post, even if they don't react. Long-form posts that hold attention outperform short quips. [TESTED — confirmed by LinkedIn Engineering blog 2023]
- **Comments > Reactions > Shares** — comment engagement is weighted roughly 2x reactions. Shares are paradoxically weaker because they split engagement across two posts. [TESTED]
- **First-hour velocity** — posts that accumulate engagement in the first 60 minutes get pushed to 2nd-degree connections. After that window, distribution largely plateaus. [TESTED]
- **Creator Mode** — shifts profile from connections-first to followers-first, changes the follow/connect button, and enables LinkedIn Live and newsletters. Affects distribution algorithm. [TESTED]

### Content Ranking Tiers

1. **Spam filter** — automated removal of obvious spam, engagement bait, irrelevant content
2. **Low-quality test** — shown to a small slice of your network (~10% of connections)
3. **Quality assessment** — if engagement rate is strong, pushed to wider network + 2nd-degree
4. **Human review** — potential viral content flagged for editorial team review before massive distribution

[TESTED — LinkedIn has publicly described this pipeline]

### What LinkedIn Penalises

- **External links in posts** — reduces reach by 50%+ compared to text-only posts. Put links in the first comment instead. [TESTED — widely confirmed]
- **Engagement pods** — LinkedIn actively detects coordinated engagement and penalises participants [TESTED — LinkedIn announced crackdown 2023]
- **Hashtag stuffing** — use 3-5 max, choose niche hashtags over broad ones (#SaaSGrowth over #Business) [HYPOTHESIS — commonly reported]
- **Editing within first hour** — reported to reset distribution momentum [HYPOTHESIS — anecdotal]
- **Tagging people who don't engage** — if tagged users ignore the post, it signals low relevance [HYPOTHESIS]

### Optimisation Tactics

1. **Write "scroll-stopping" first lines.** LinkedIn shows ~3 lines before the "see more" fold. That first line must compel clicks. Use a bold claim, counterintuitive insight, or personal vulnerability. [TESTED]
   - Before: "Excited to share that our team hit a milestone this quarter."
   - After: "We almost shut down the company last quarter. Here's what saved us."

2. **Optimise for dwell time with formatting.** Use line breaks, white space, and numbered lists. Dense paragraphs get scrolled past. Each line should be 1-2 sentences max. [TESTED]

3. **Reply to every comment within the first 2 hours.** Each reply counts as additional engagement AND restarts the distribution cycle. Your own replies to comments on your post trigger re-ranking. [TESTED]

4. **Post Tuesday-Thursday, 7-9am local time.** LinkedIn engagement peaks during the work-commute and morning-coffee window. Weekends see 50-70% less engagement. [TESTED — consistent across multiple studies]

5. **Use document/carousel posts for highest reach.** PDF carousel posts consistently outperform text, image, and video posts on LinkedIn because they maximise dwell time (users swipe through multiple pages). [TESTED — 2023-2024 data]

6. **Lead with expertise, not self-promotion.** Posts that teach something get 3-5x the engagement of announcements. Frame wins as lessons: "Here's what I learned" not "Here's what I achieved." [HYPOTHESIS — strong anecdotal support]

---

## Instagram Algorithm

### Multiple Algorithms

Instagram uses DIFFERENT algorithms for each surface — there is no single "Instagram algorithm." [TESTED — confirmed by Adam Mosseri, Head of Instagram]

- **Feed** — relationship signals (who you interact with most), interest prediction based on past behaviour, recency. Heavy bias toward accounts you DM, comment on, or search for.
- **Stories** — prioritises close connections and viewing history. Users who consistently watch your stories see them first. Completion rate matters.
- **Reels** — content-based signals dominate over follower signals. Watch time, replays, and shares determine distribution. Audio popularity acts as a boost.
- **Explore** — pure interest-based discovery. Looks at content similar to what you've recently engaged with. Follower count is less relevant here.

### Key Signals by Surface

| Signal | Feed | Stories | Reels | Explore |
|---|---|---|---|---|
| Relationship strength | Primary | Primary | Low | None |
| Interest/topic match | High | Moderate | Moderate | Primary |
| Recency | High | High | Low | Moderate |
| Watch time / completion | Moderate | High | Primary | High |
| Shares via DM | High | Moderate | Very high | High |
| Saves | High | N/A | High | High |
| Comments | High | Moderate | Moderate | High |
| Audio/trend usage | N/A | Low | High | Moderate |

### What Instagram Penalises

- **Recycled TikTok content** with visible watermarks — Instagram has confirmed they deprioritise this [TESTED]
- **Low-resolution images/video** — Instagram favours high-quality visual content [TESTED]
- **Engagement bait** ("tag a friend who...", "like for X, comment for Y") — classified as spam [TESTED — Instagram guidelines]
- **Posting more than 3x per day on feed** — diminishing returns, can hurt per-post engagement rate [HYPOTHESIS]
- **Shadowban triggers** — using banned hashtags, repeated community guideline violations [TESTED]

### Optimisation Tactics

1. **For Reels: hook in the first 1-2 seconds.** The algorithm measures how many viewers make it past the 3-second mark. Open with movement, text overlay, or a surprising visual — never a slow intro. [TESTED]
   - Before: 3-second logo animation followed by talking head
   - After: Text overlay "This changed everything" + immediate visual payoff

2. **Maximise saves by creating reference content.** Infographics, step-by-step guides, and "save for later" content triggers the strongest algorithmic signal on Feed and Explore. [TESTED]

3. **Use Instagram Stories to boost Feed ranking.** Regular story posting strengthens your relationship signal with viewers, which directly improves where your feed posts appear in their timeline. [TESTED]

4. **Share Reels to Stories for double-surface exposure.** This creates two entry points and the story view counts toward the Reel's engagement metrics. [HYPOTHESIS — widely reported]

5. **Post Reels with trending audio.** Instagram's Reels algorithm includes an audio popularity signal. Using trending sounds (even at low volume under a voiceover) can boost initial distribution. [TESTED — but effect size is debated]

6. **Write long captions for Feed posts.** Captions up to 2,200 characters increase dwell time. Ask a question at the end to trigger comments. The algorithm measures time spent on the full post, not just the image. [HYPOTHESIS — strong anecdotal support]

---

## TikTok Algorithm (For You Page)

### How FYP Works

TikTok's algorithm is fundamentally different from other platforms: **content signals dominate over social signals**. A video from an account with zero followers can reach millions if the content performs. [TESTED — TikTok has publicly confirmed this]

Each video goes through a batch-testing cascade:
1. **Initial batch** — shown to 300-500 users (mix of followers + interest-matched non-followers)
2. **If engagement is strong** — expanded to 1K-5K users
3. **If engagement holds** — expanded to 10K-50K
4. **Viral pool** — 100K+ views, shown broadly across the platform

The key metric at each stage is **watch time ratio** — what percentage of viewers watch to the end, or rewatch. A 7-second video watched twice by most viewers will outperform a 60-second video abandoned at the 10-second mark. [TESTED]

### Ranking Signals (Priority Order)

| Rank | Signal | Why It Matters |
|---|---|---|
| 1 | Watch time / completion rate | Strongest signal — did users find it worth their time? |
| 2 | Replays | Users chose to watch again — very strong quality signal |
| 3 | Shares | Users sent it to friends — strongest social signal |
| 4 | Comments | Users had something to say — engagement depth |
| 5 | Likes | Positive but passive — weakest engagement signal |
| 6 | Profile visits after viewing | User wants to see more from this creator |

[TESTED — TikTok's 2023 transparency report confirms this hierarchy]

### What TikTok Penalises

- **Duplicate content** — same video reposted gets flagged and suppressed [TESTED]
- **QR codes or watermarks** from other platforms — similar to Instagram's policy [TESTED]
- **Violence, hate speech, misinformation** — flagged by automated classifiers [TESTED]
- **Unoriginal sounds** — using another creator's original audio without the duet/stitch mechanism [HYPOTHESIS]
- **Long periods of inactivity** followed by posting — account "warm-up" may be needed [HYPOTHESIS]

### Optimisation Tactics

1. **Hook in the first 1-2 seconds.** TikTok measures the 1-second and 3-second retention rates. If users swipe away before 2 seconds, the video dies in batch 1. Start with movement, a bold text overlay, or a surprising statement. [TESTED]
   - Before: "Hey guys, so today I wanted to talk about..."
   - After: "Nobody talks about this $0 marketing hack." (text on screen, immediate visual)

2. **Create loop endings.** Videos that loop seamlessly (the end flows into the beginning) trick the algorithm into counting replays. This is one of the most effective tactics for short-form content. [TESTED — widely documented]
   - Structure: Start mid-action, end at a point that makes viewers want to re-watch from the start

3. **Use trending audio strategically.** Trending sounds get a distribution boost, but the audio must feel natural. Use trending audio as background with a text overlay or voiceover for best results. [TESTED]

4. **Optimise video length for your content type.** Short (7-15 seconds) works for quick tips and humour. Medium (30-60 seconds) for tutorials. TikTok now supports 10-minute videos but completion rate drops sharply after 60 seconds — only go long if retention data supports it. [HYPOTHESIS — optimal length varies by niche]

5. **Post 1-3 times per day consistently.** TikTok rewards posting frequency more than any other platform. Each video gets its own algorithmic evaluation, so volume increases your odds of hitting the viral cascade. [TESTED — TikTok creator portal recommends this]

6. **Engage in the first 30 minutes after posting.** Reply to every comment quickly — each reply counts as additional engagement and TikTok's algorithm weighs early comment velocity heavily. Pin a controversial or question-prompting comment to spark more replies. [HYPOTHESIS — widely reported by top creators]

---

## YouTube Algorithm

### Discovery Surfaces

YouTube has four distinct discovery surfaces, each with its own ranking logic:

- **Home** — personalised recommendations based on watch history, topic clustering, and what similar users watched. This is where most views come from for established channels. [TESTED]
- **Search** — keyword relevance + engagement metrics (CTR, watch time). YouTube Search functions more like a search engine than a social feed. [TESTED]
- **Suggested** — shown alongside and after related videos. Based on co-watch patterns (users who watched X also watched Y). This is the primary growth driver for new channels. [TESTED]
- **Shorts** — YouTube's TikTok competitor. Uses a batch-test model similar to TikTok's FYP. Shorts and long-form have SEPARATE algorithmic evaluation. [TESTED]

### Key Metrics

| Metric | Target | Why It Matters |
|---|---|---|
| Click-Through Rate (CTR) | 5-10% | Thumbnail + title effectiveness — determines if users choose YOUR video from a list |
| Average View Duration (AVD) | 50%+ of video length | How much of the video people actually watch — the single strongest ranking signal |
| Session time | Positive contribution | Does your video lead to MORE YouTube watching? YouTube rewards creators who keep users on-platform |
| Subscriber conversion | Varies | % of viewers who subscribe after watching — signals long-term channel value |
| Likes-to-views ratio | 4%+ | Quick quality signal, but much weaker than AVD |

[TESTED — YouTube has publicly discussed these metrics in Creator Insider videos]

### What YouTube Penalises

- **Clickbait with poor retention** — high CTR + low AVD is the worst combination. YouTube interprets this as misleading and reduces future impressions. [TESTED]
- **Inconsistent upload schedule** — the algorithm favours channels that post predictably. Long gaps between uploads reduce Home page recommendations. [HYPOTHESIS — strong anecdotal support]
- **Engagement bait in Shorts** — "follow for part 2" without delivering erodes trust signals [HYPOTHESIS]
- **Misleading metadata** — titles/tags that don't match content get penalised after enough negative signals [TESTED]

### Optimisation Tactics

1. **Thumbnail and title are 80% of the battle.** YouTube's algorithm can only recommend your video — the thumbnail and title determine whether anyone clicks. Use high-contrast images, readable text (3-4 words max), and emotional faces. A/B test thumbnails using YouTube's built-in testing tool. [TESTED]
   - Before: Screenshot of code editor with small text
   - After: Split image — confused face on left, celebration on right — "This Bug Cost Me $10,000"

2. **Front-load value in the first 30 seconds.** YouTube tracks the audience retention curve. A steep drop-off in the first 30 seconds tells the algorithm the content doesn't deliver on the title's promise. Preview what viewers will learn, then deliver immediately. [TESTED]

3. **Optimise for session time with end screens and playlists.** YouTube rewards videos that lead to more watching. Use end screens pointing to related videos, create playlists, and verbally suggest the next video. "If you liked this, you'll love my video on X." [TESTED]

4. **Use chapters (timestamps) for Search ranking.** Chapters improve Search visibility because YouTube can match individual sections to search queries. They also improve user experience metrics by reducing abandonment. [TESTED]

5. **Publish Shorts and long-form separately.** Shorts subscribers and long-form subscribers behave differently. YouTube now allows channels to separate Shorts from the main feed. Use Shorts for discovery and long-form for depth. [TESTED — YouTube confirmed separate algorithmic paths]

6. **Study your Analytics > Audience tab.** YouTube tells you exactly when your audience is online. Post 1-2 hours before peak activity so the video accumulates early engagement before the surge. [TESTED — available in YouTube Studio]

---

## Cross-Platform Strategy Notes

### Platform Selection by Content Type

| Content Type | Best Platform | Why |
|---|---|---|
| Long-form educational | YouTube | Watch time + evergreen search traffic |
| Quick tips / entertainment | TikTok + Reels | Completion rate rewards short, punchy content |
| Professional thought leadership | LinkedIn | Dwell time + network-based distribution |
| Real-time commentary / debate | X | Reply-driven engagement + SimCluster communities |
| Visual storytelling / lifestyle | Instagram Feed + Stories | Relationship-based ranking favours consistent visual brands |

### Repurposing Hierarchy

When repurposing content across platforms, adapt for each algorithm — never cross-post identical content:

1. **Create the long-form version first** (YouTube or blog post)
2. **Extract 3-5 short clips** for TikTok and Reels (remove watermarks between platforms)
3. **Write a LinkedIn post** teaching the key insight (text-first, no link)
4. **Create an X thread** with the most provocative angles
5. **Use Instagram Stories** for behind-the-scenes of the creation process

Each piece should feel native to its platform. The algorithm on every platform can detect low-effort reposts and deprioritises them. [HYPOTHESIS — mechanism varies, but the pattern is consistent]
