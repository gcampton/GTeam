### Source Reachability — Check First

Before running anything, determine if the target is scrapeable:

**Step 1 — Check for llms.txt (fastest, always try first):**
```bash
curl -s -o /dev/null -w "%{http_code}" "https://<domain>/llms.txt"
curl -s -o /dev/null -w "%{http_code}" "https://<domain>/llms-full.txt"
curl -s -o /dev/null -w "%{http_code}" "https://<domain>/docs/llms-full.txt"
```
If `llms-full.txt` returns 200: download it directly — no scraping needed:
```bash
curl -s "https://<domain>/docs/llms-full.txt" \
  -o ~/.claude/skills/gteam/specialists/<specialist>/references/<name>.md
```

**Step 2 — Check if the site is server-side rendered (scrapeable):**
```bash
curl -s "https://<domain>/docs/<any-page>" | python3 -c "
import sys, re
text = re.findall(r'>([A-Z][^<]{50,})<', sys.stdin.read())
print(f'Text chunks: {len(text)}')
"
```
- **Text chunks > 0** → static/SSR, scrapeable. Use `skill-seekers scrape`.
- **Text chunks = 0** → JS-rendered (React/Next.js SPA). Find an alternative source:
  - Check for versioned/legacy docs (e.g. `v2.example.com/docs`) — often static HTML
  - Check GitBook mirrors (`<name>.gitbook.io`)
  - Check GitHub raw markdown (public repos, no auth needed for raw content)

**Step 3 — Rate limit:**
Use `--rate-limit 5` as the default minimum. Lower values (0.3–0.5) cause 403s on most production doc sites.

---

### Setup Check

Before any skill-seekers operation, verify the environment:

```bash
source ~/dev/skill-seekers/Skill_Seekers/.venv/bin/activate
skill-seekers --version
```

If the command fails, the venv may need rebuilding:
```bash
cd ~/dev/skill-seekers/Skill_Seekers
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[mcp,docx,epub]"
```

---

### Enrich a GTeam Specialist

**Use when:** The user says "enrich X specialist with Y" or "add Y knowledge to X".

**Gather:** Specialist name, technology/topic. Infer the right specialist if not explicit:
- Next.js / React / TypeScript / Tailwind → `software-engineer`
- SEO tools / analytics → `seo`
- Stripe / payments → `software-engineer` + `accountant`
- Docker / CI/CD → `devops`

**Process:**

1. **Find the best config** — check the API first:
   ```bash
   curl -s "https://api.skillseekersweb.com/api/configs?tag=<technology>" | python3 -m json.tool
   ```
   If a match exists, use it. If not, build a custom config (see "Build from URL" or "Build from GitHub").

2. **Get the exact download filename** — some configs use `_unified` suffix:
   ```bash
   curl -s "https://api.skillseekersweb.com/api/configs/<name>" | python3 -m json.tool
   ```

3. **Download the config:**
   ```bash
   curl -s "https://api.skillseekersweb.com/api/download/<config_file>.json" \
     -o ~/dev/skill-seekers/Skill_Seekers/configs/gteam/<name>.json
   ```

4. **Run skill-seekers:**
   ```bash
   source ~/dev/skill-seekers/Skill_Seekers/.venv/bin/activate
   cd ~/dev/skill-seekers/Skill_Seekers
   skill-seekers create configs/gteam/<name>.json -p standard --enhance-level 0
   ```
   Preset guide: `-p quick` (1-2 min, shallow) / `-p standard` (5-10 min, default) / `-p comprehensive` (20-60 min, deep)

5. **Install into the specialist:**
   ```bash
   cp ~/dev/skill-seekers/Skill_Seekers/output/<name>/SKILL.md \
      ~/.claude/skills/gteam/specialists/<specialist>/references/<name>.md
   ```

6. **Register in the specialist's SKILL.md** — add a bullet to the Reference Materials section if it isn't already listed.

**Deliver:** Confirmation of which file was installed, its size, and a one-line summary of what it covers.

---

### Build from URL

**Use when:** The user provides a documentation URL and wants a skill built from it.

**Gather:** URL, skill name (default: domain name), target specialist (optional).

**Always run Source Reachability check first** (see above).

**Process — use `scrape` directly, not `create`:**
```bash
source ~/dev/skill-seekers/Skill_Seekers/.venv/bin/activate
cd ~/dev/skill-seekers/Skill_Seekers
skill-seekers scrape "<url>" --name <name> --rate-limit 5 --enhance-level 0
```

> **Note:** `skill-seekers create <url>` routes through the unified config system which has a known `KeyError: 'base_url'` bug when calling the doc scraper. Use `skill-seekers scrape` directly for single documentation sources.

If the output SKILL.md is thin (< 50KB), retry with `--max-pages 500`.

Install output:
```bash
cp output/<name>/SKILL.md ~/.claude/skills/gteam/specialists/<specialist>/references/<name>.md
```

---

### Build from GitHub

**Use when:** The user provides a `owner/repo` and wants a skill built from it.

**Gather:** Repo, skill name, target specialist (optional), analysis depth.

```bash
source ~/dev/skill-seekers/Skill_Seekers/.venv/bin/activate
cd ~/dev/skill-seekers/Skill_Seekers
skill-seekers create <owner/repo> --name <name> -p standard --enhance-level 0
```

For codebases: add `--local-repo-path ./path` if the repo is already cloned locally.

---

### Discover Configs

**Use when:** The user asks what configs are available, or you need to find a config for a technology.

```bash
# List all configs
curl -s "https://api.skillseekersweb.com/api/configs" | python3 -c "
import json,sys
data = json.load(sys.stdin)
configs = data if isinstance(data, list) else data.get('configs', [])
for c in configs:
    print(f\"{c.get('name','?'):<30} {c.get('category','?'):<20} {c.get('description','')[:60]}\")
"

# Filter by category
curl -s "https://api.skillseekersweb.com/api/configs?category=web-frameworks"

# Filter by tag
curl -s "https://api.skillseekersweb.com/api/configs?tag=javascript"
```

**Available categories:** ai-ml, api-tech, build-tools, cloud, cms, css-frameworks, databases, development-tools, devops, game-engines, languages, messaging, mobile, payments, search, security, testing, web-frameworks

---

### Batch Enrich

**Use when:** The user wants to enrich a specialist with multiple technologies at once.

Run each config sequentially (not in parallel — disk I/O contention):

```bash
source ~/dev/skill-seekers/Skill_Seekers/.venv/bin/activate
cd ~/dev/skill-seekers/Skill_Seekers
for cfg in <config1> <config2> <config3>; do
  echo "=== Building $cfg ==="
  skill-seekers create configs/gteam/$cfg.json -p standard --enhance-level 0
done
```

---

### Refresh a Skill

**Use when:** The user wants to update an existing reference file with fresh documentation.

Re-run the original config or source, compare size before overwriting, only overwrite if the new file is larger or the user confirms.

---

### Rules

- Always use `-p standard --enhance-level 0` as the default.
- Some config names on the API require a `_unified` suffix for the download — always check `/api/configs/<name>` for the exact filename before downloading.
- Output lands in `output/<name>/SKILL.md`. If the run produces no output or errors, check `output/<name>/` for partial results.
- GTeam specialist reference files should be named `<technology>.md` (lowercase, hyphenated) for consistency.
- After installing a reference file, remind the user that the specialist will load it automatically on the next invocation.
