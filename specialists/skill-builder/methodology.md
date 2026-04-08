### Source Strategy — Check in Order

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

---

### Scrape from URL (Multi-Page)

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

---

### Scrape from API

**Use when:** User provides an API to document (REST, GraphQL, OpenAPI spec).

**Step 1 — Check Skill-Seekers API first:**
```bash
curl -s "https://api.skillseekersweb.com/api/configs?tag=<api-name>" | python3 -m json.tool
```

**Step 2 — Check for OpenAPI/Swagger spec:**
```bash
curl -s "https://<domain>/openapi.json" | python3 -m json.tool | head -100
curl -s "https://<domain>/swagger.json" | python3 -m json.tool | head -100
curl -s "https://<domain>/api-docs" | head -100
```
If found, download and parse into reference markdown:
```bash
curl -s "https://<domain>/openapi.json" -o /tmp/<name>-openapi.json
```
Extract: base URL, auth method, all endpoints (method + path + description + params + response schema), rate limits, error codes.

**Step 3 — If no spec:** Use WebFetch to scrape the API reference docs using the URL workflow above.

**Step 4 — For JSON/data dumps provided by the user:** Read the file, extract structure, summarize schemas, document all fields and types.

---

### Scrape from GitHub

**Use when:** User provides a `owner/repo` GitHub repository.

**Step 1 — Check Skill-Seekers API:**
```bash
curl -s "https://api.skillseekersweb.com/api/configs?tag=<repo-name>" | python3 -m json.tool
```

**Step 2 — Fetch via GitHub raw:**
```bash
# README
curl -s "https://raw.githubusercontent.com/<owner>/<repo>/main/README.md"

# Discover docs folder
curl -s "https://api.github.com/repos/<owner>/<repo>/contents/docs" | python3 -m json.tool

# Each doc file
curl -s "https://raw.githubusercontent.com/<owner>/<repo>/main/docs/<file>.md"
```

Prioritise: README → CONTRIBUTING → docs/ → examples/. GitHub raw content needs no rate limiting. The GitHub API (`api.github.com`) allows 60 unauthenticated requests/hour — add `sleep 1` if fetching many files.

---

### Process into Reference File

After collecting raw content, synthesize into a clean reference markdown file.

**Structure:**
```markdown
# <Technology> Reference

> Source: <url or repo> | Built: <date>

## Overview
[What this technology does — 2-3 sentences]

## Core Concepts
[Key concepts, terminology, mental model]

## [Main Topic 1]
[Content]

## [Main Topic 2]
[Content]

## Common Patterns
[Recipes, examples, typical usage]

## Anti-Patterns
[What to avoid and why]

## Quick Reference
[Cheat sheet: key commands, config options, API endpoints]
```

Remove: marketing copy, nav elements, cookie notices, repetitive boilerplate. Keep: technical specifics, code examples, config schemas, API signatures, error handling.

**Target size:** 20–80KB. Prioritise depth on core concepts over breadth.

**Output location:**
```bash
~/.claude/skills/gteam/specialists/<specialist>/references/<name>.md
```

---

### Enrich Existing Specialist

**Use when:** User says "add X knowledge to the Y specialist" or "enrich X with Y."

**Infer the right specialist if not explicit:**
- Next.js / React / TypeScript / Tailwind → `software-engineer`
- SEO tools / analytics → `seo`
- Stripe / payments → `software-engineer` + `accountant`
- Docker / CI/CD / Kubernetes → `devops`
- Security tools → `security-engineer`

**Process:**
1. Run Source Strategy (SS API → llms.txt → WebFetch → curl)
2. Process into a reference file
3. Install: `cp /tmp/<name>.md ~/.claude/skills/gteam/specialists/<specialist>/references/<name>.md`
4. Confirm installed file size and one-line summary of coverage

The specialist loads the new reference automatically on next invocation.

---

### Scaffold New Specialist

**Use when:** User wants to create a new specialist from scratch.

**Gather:** Specialist name (kebab-case), domain/role, key capabilities (3–5), target category.

**Step 1 — Create directory structure:**
```bash
GTEAM=~/.claude/skills/gteam
NAME=<specialist-name>

mkdir -p $GTEAM/specialists/$NAME/references
mkdir -p $GTEAM/specialists/$NAME/evals
mkdir -p $GTEAM/specialists/$NAME/results
```

**Step 2 — Write `methodology.md`:**

Synthesize collected reference content into a structured methodology covering:
- Domain workflow (phases, decision points)
- Quality standards and professional rules
- Common patterns and anti-patterns
- Output formats

**Step 3 — Write `SKILL.md.tmpl`:**

Follow this exact structure:
```markdown
---
name: gteam-<name>
version: 1.0.0
description: <one-line description>
type: standalone
category: <category>
allowed-tools:
  - Read
  - Write
  - Bash
  - WebFetch
  - WebSearch
  - Glob
  - Grep
---

{{PREAMBLE}}

# <Role Title> — GTeam

## Role

You are a [senior/expert] <role> specialising in <domain>. <2-3 sentences on what makes this specialist distinct — methodology, depth, professional standards it holds itself to.>

## When to Use

- <trigger scenario 1>
- <trigger scenario 2>
- <trigger scenario 3>

## Not For

- <out-of-scope scenario 1> (use <other specialist> instead)
- <out-of-scope scenario 2>

## Workflow

{{<NAME>_METHODOLOGY}}

## Reference Materials

Domain frameworks and reference files are in `{{GTEAM_DIR}}/specialists/<name>/references/`:

<list any scraped reference files installed>

**Before starting any task:**
1. Read relevant reference files for the task at hand
2. Check `{{GTEAM_DIR}}/specialists/<name>/results/` for prior work on similar tasks
```

Token naming rule: directory `content-creator` → token `{{CONTENT_CREATOR_METHODOLOGY}}`
Formula: `dirName.toUpperCase().replace(/-/g, '_') + '_METHODOLOGY'`

**Step 4 — Generate SKILL.md:**
```bash
cd ~/.claude/skills/gteam && bun run gen:skill-docs
```

**Step 5 — Create a placeholder eval:**
```bash
cat > $GTEAM/specialists/$NAME/evals/scenarios.md << 'EOF'
# <Name> Eval Scenarios

## Scenario 1: [Description]
**Input:** ...
**Expected:** ...
**Criteria:** relevance, completeness, actionability, methodology alignment
EOF
```

**Deliver:** Confirm which files were created, run `bun run skill:check` to verify the specialist registers correctly.

---

### Rules

- **Always try Skill-Seekers API first** — if they have a pre-built config, it's faster and higher quality than scraping from scratch. Some config names require a `_unified` suffix — always check `/api/configs/<name>` for the exact filename before downloading.
- **Rate limit for curl: 3 seconds** between page requests on production sites. Lower values trigger 403s after ~100 pages. WebFetch needs no rate limiting.
- **Always check llms.txt** before scraping — saves 10+ minutes when available.
- **Reference file naming:** `<technology>.md` (lowercase, hyphenated). Example: `stripe-api.md`, `next-js.md`.
- **methodology.md is the knowledge** — write it as a professional would document their domain workflow, not as a list of facts.
- **SKILL.md.tmpl is the interface** — keep it thin. Heavy content lives in methodology.md and references/.
- **Run `bun run gen:skill-docs` after every tmpl change** — never edit SKILL.md directly.
- **Run `bun run skill:check`** after scaffolding to confirm the new specialist registers cleanly.
