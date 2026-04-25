## AI Visibility Analysis (`/gteam seo ai <url>`)

Deep-dive into AI-era signals only. No traditional keyword research or link building.

**1. AI Citability Scoring**

For each key page, assess:
- Does the opening paragraph directly answer a likely query? (Featured snippet / AI answer block targeting)
- Are there clear question-based H2s and direct answers below them?
- Is content structured for extraction (short paragraphs, lists, tables)?
- Does the page cite authoritative external sources?
- Is there original data or research that AI would want to quote?

Score each page 0–100 for citability. Flag top 5 most citable and bottom 5 least citable with specific rewrite suggestions.

**2. AI Crawler Access**

Fetch `/robots.txt`. Check access for:

| Crawler | Platform |
|---|---|
| GPTBot | ChatGPT / OpenAI |
| ClaudeBot | Anthropic Claude |
| PerplexityBot | Perplexity AI |
| Google-Extended | Gemini / Google AI |
| Bingbot | Bing Copilot / ChatGPT |
| Googlebot | Google AIO |
| Applebot-Extended | Apple Intelligence |

For each: Allowed / Blocked / Partial. Flag blocks as Critical or High severity.

**3. llms.txt Audit / Generation**

Fetch `<domain>/llms.txt` and `<domain>/llms-full.txt`.
- If present: validate structure (title, description, key sections, file links). Flag gaps.
- If absent: generate a complete llms.txt and llms-full.txt. Write to `~/geo-seo-projects/[domain]/llms.txt` and `~/geo-seo-projects/[domain]/llms-full.txt`. If a `public/` directory exists in the current working directory, also copy there for immediate deployment.

**4. Brand Mention Scan**

Search for brand presence on AI-cited platforms:
- Wikipedia: `WebSearch "site:en.wikipedia.org <brand>"`
- Reddit: `WebSearch "site:reddit.com <brand>"` — check volume, sentiment, top subreddits
- YouTube: `WebSearch "site:youtube.com <brand>"` — official channel + mentions
- LinkedIn: `WebSearch "site:linkedin.com/company <brand>"`
- Wikidata: `WebSearch "site:wikidata.org <brand>"`
- Crunchbase / GitHub / G2 as applicable

Score brand authority 0–100 based on presence depth and authority-platform coverage.

**5. Platform-Specific Readiness**

Assess each AI platform:

| Platform | Key Factors |
|---|---|
| Google AI Overviews | Schema.org markup, E-E-A-T signals, structured direct-answer passages, Core Web Vitals |
| ChatGPT / Perplexity | GPTBot/PerplexityBot allowed, Reddit/Wikipedia presence, direct-answer content, llms.txt |
| Google Gemini | Google-Extended allowed, YouTube presence, Knowledge Panel, structured data |
| Bing Copilot | Bingbot allowed, IndexNow protocol, Bing Webmaster Tools, LinkedIn presence |

Score each platform 0–100 and flag the top action for each.

**Output:** `~/geo-seo-projects/[domain]/GEO-AI-VISIBILITY.md`
