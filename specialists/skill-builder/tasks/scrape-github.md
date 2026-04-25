## Scrape from GitHub

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
