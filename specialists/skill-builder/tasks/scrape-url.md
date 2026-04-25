## Scrape from URL (Multi-Page)

**Use when:** User provides a documentation URL to build a reference file from.

**Always run Source Strategy first.** If Skill-Seekers API or llms.txt resolves it, skip scraping.

**WebFetch crawl (preferred):**

1. Fetch the docs index page with WebFetch
2. Extract all doc page links from the content
3. Fetch each page with WebFetch, collecting content
4. Stop when content exceeds 200KB — enough for a strong reference file

No delays needed between WebFetch calls.

**curl crawl (fallback):**
```bash
# Fetch index and extract links
curl -s "https://<domain>/docs/" | python3 -c "
import sys, re
links = re.findall(r'href=[\"\'](/docs/[^\"\']+)[\"\'\ ]', sys.stdin.read())
for l in sorted(set(links)): print(l)
"

# Fetch each page — add sleep 3 between requests on production sites
sleep 3
curl -s "https://<domain>/docs/<page>"
```

Rate limit for curl: **3 seconds between requests** on production doc sites. Lower values trigger 403s after ~100 pages.
