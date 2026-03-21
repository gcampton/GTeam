# Research Sources & Search Patterns

Quick reference for where to find niche intelligence. Use with browse ($B) where available.

## Trend Discovery

| Source | What to look for | How to access |
|--------|----------------|--------------|
| Google Trends | Rising queries in a broad category | `$B goto https://trends.google.com/trends/explore` |
| Reddit r/sidehustle | Recurring themes, what's working now | WebSearch `site:reddit.com/r/sidehustle "<topic>"` |
| Reddit r/juststart | Affiliate/content site journey posts | WebSearch `site:reddit.com/r/juststart niche income` |
| Reddit r/dropship | Winning product discussions | WebSearch `site:reddit.com/r/dropship winning product <year>` |
| Indie Hackers | Solo founder revenue reports | WebSearch `site:indiehackers.com "<niche>" revenue milestone` |
| Product Hunt | New tools, what problems are being solved | `$B goto https://www.producthunt.com` → Popular / Today |
| TikTok trending | Viral products and emerging content niches | `$B goto https://www.tiktok.com/channel/trending` |
| Amazon Best Sellers | Physical product demand by category | `$B goto https://www.amazon.co.uk/Best-Sellers` |

## Competition Analysis Searches

```bash
# Measure content competition
allintitle:"<target keyword>"    # < 10,000 = low competition

# Find weak incumbents
"<keyword>" -site:amazon.com -site:wikipedia.org -site:reddit.com

# Check if thin affiliate sites dominate
"<keyword>" "affiliate disclosure" OR "commission" in title

# Find what competitors aren't covering
"<keyword>" -"<missing angle>"

# Identify who's ranking
site:<competitor domain> "<topic>"    # what they publish about a topic
```

## Affiliate Programme Discovery

```bash
# Find programmes in a niche
"<niche> affiliate program" site:shareasale.com
"<niche> affiliate program" commission rate <year>
"<niche>" site:impact.com OR site:cj.com

# Find high-commission SaaS
"<category> software" affiliate "recurring commission" OR "lifetime commission"

# Check EPC and conversion signals
"<programme name>" affiliate review "EPC" OR "earnings per click"
```

## YouTube Niche Research

```bash
# Find underserved channels
YouTube search: "<niche>" → filter by "This year" → look for < 50k sub channels getting 100k+ views

# CPM verification
"<niche> YouTube CPM" <year>
"<niche> YouTube RPM how much do I make"
"<niche> YouTube faceless channel" — validates faceless viability

# Content gap search
"<niche>" YouTube -"<main competitor channel name>"    # find what they miss
```

## Digital Product Validation

```bash
# Problem discovery
site:reddit.com "I wish there was a tool"
site:reddit.com "is there an app that"
site:reddit.com "I hate that <tool> doesn't"

# Market size proxy
"<niche> software" site:g2.com OR site:capterra.com — count of tools = market validation
"<niche> newsletter" site:beehiiv.com OR site:substack.com

# Solo builder proof of concept
site:indiehackers.com "<model>" revenue
"<AI tool type>" maker:solo OR indie revenue
```

## Dropshipping Product Research

```bash
# Trend + virality signals
TikTok: #TikTokMadeMeBuyIt + <category>
"<product>" viral TikTok OR Instagram site:reddit.com

# Supplier check
"<product>" site:aliexpress.com "orders" "stars"
"<product>" dropship supplier "UK shipping" OR "EU warehouse"
"<product>" print on demand OR POD supplier

# Saturation check
"<product>" site:amazon.co.uk — count of results + review count on top listings
"<product>" Google Shopping — count of advertisers = demand signal
```

## Income Report Research (validate before committing)

These searches find real people sharing real numbers — the best signal a model works:

```bash
site:reddit.com "made £" OR "made $" "<niche>" "per month" <year>
"<niche>" "income report" <year> site:medium.com OR site:wordpress.com
"<model type>" "how I make" OR "how much I make" <year>
site:indiehackers.com "<niche>" "MRR" OR "ARR"
```

## Tools That Help (if user has access)

| Tool | Use | Cost |
|------|-----|------|
| Ahrefs / SEMrush | Real keyword volumes, competitor traffic | Paid |
| SimilarWeb | Competitor traffic estimates | Freemium |
| Jungle Scout / Helium 10 | Amazon product research | Paid |
| SpyFu | Competitor PPC data | Freemium |
| VidIQ / TubeBuddy | YouTube keyword research, competitor analysis | Freemium |
| Exploding Topics | Early trend signals | Freemium |

If user has none of these: WebSearch + $B + Reddit intelligence is 80% as good and free.
