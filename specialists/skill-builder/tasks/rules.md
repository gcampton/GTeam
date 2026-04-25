## Rules

- **Always try Skill-Seekers API first** — if they have a pre-built config, it's faster and higher quality than scraping from scratch. Some config names require a `_unified` suffix — always check `/api/configs/<name>` for the exact filename before downloading.
- **Rate limit for curl: 3 seconds** between page requests on production sites. Lower values trigger 403s after ~100 pages. WebFetch needs no rate limiting.
- **Always check llms.txt** before scraping — saves 10+ minutes when available.
- **Reference file naming:** `<technology>.md` (lowercase, hyphenated). Example: `stripe-api.md`, `next-js.md`.
- **methodology.md is the knowledge** — write it as a professional would document their domain workflow, not as a list of facts.
- **SKILL.md.tmpl is the interface** — keep it thin. Heavy content lives in methodology.md and references/.
- **Run `bun run gen:skill-docs` after every tmpl change** — never edit SKILL.md directly.
- **Run `bun run skill:check`** after scaffolding to confirm the new specialist registers cleanly.
