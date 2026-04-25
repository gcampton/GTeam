## Source Strategy — Check in Order

Always work through these steps before scraping anything. Each step is faster and more reliable than the next.

**Step 1 — Skill-Seekers API (fastest for known technologies):**
```bash
# Search for a pre-built config
curl -s "https://api.skillseekersweb.com/api/configs?tag=<technology>" | python3 -m json.tool

# Or by category
curl -s "https://api.skillseekersweb.com/api/configs?category=web-frameworks" | python3 -m json.tool
```
If a match exists, get the exact filename and download:
```bash
curl -s "https://api.skillseekersweb.com/api/configs/<name>" | python3 -m json.tool
curl -s "https://api.skillseekersweb.com/api/download/<config_file>.json" \
  -o /tmp/<name>-config.json
```
Then fetch the pre-built SKILL.md if available, or use the config to understand the source structure and proceed to scraping.

Available categories: `ai-ml`, `api-tech`, `build-tools`, `cloud`, `cms`, `css-frameworks`, `databases`, `development-tools`, `devops`, `game-engines`, `languages`, `messaging`, `mobile`, `payments`, `search`, `security`, `testing`, `web-frameworks`

**Step 2 — Check for llms.txt:**
```bash
curl -s -o /dev/null -w "%{http_code}" "https://<domain>/llms.txt"
curl -s -o /dev/null -w "%{http_code}" "https://<domain>/llms-full.txt"
curl -s -o /dev/null -w "%{http_code}" "https://<domain>/docs/llms-full.txt"
```
If `llms-full.txt` returns 200: download directly — no scraping needed:
```bash
curl -s "https://<domain>/docs/llms-full.txt" -o /tmp/<name>.md
```

**Step 3 — WebFetch (static/SSR docs):**

Use the WebFetch tool on the docs index page. If it returns readable prose, use WebFetch to crawl all doc pages. No rate limiting needed — WebFetch is not a browser and doesn't trigger bot detection.

**Step 4 — curl fallback (if WebFetch unavailable):**
```bash
curl -s "https://<domain>/docs/<page>" | python3 -c "
import sys, re
text = re.sub(r'<[^>]+>', ' ', sys.stdin.read())
text = re.sub(r'\s+', ' ', text).strip()
print(text[:5000])
"
```

If all four steps fail (JS-rendered SPA with no alternative source), check for a GitHub repo or versioned/legacy docs URL that may be static HTML.
