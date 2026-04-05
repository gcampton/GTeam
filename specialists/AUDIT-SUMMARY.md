# GTeam Structural Audit -- Skillsmith Comparison

**Date:** 2026-04-05
**Scope:** All 25 specialists in `/home/garratt/dev/gteam/specialists/`
**Method:** Automated scan of SKILL.md frontmatter, directory contents, XML section presence, and spot-check of reference file quality.

---

## 1. Summary Table

| Specialist | Lines | Frontmatter Fields | type | category | XML Sections | refs/ | methodology | tmpl | evals | Thickness |
|---|---|---|---|---|---|---|---|---|---|---|
| accountant | 211 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 6 files | yes | yes | yes | THICK |
| brand-strategist | 166 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| content-creator | 275 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 13 files | yes | yes | yes | THICK |
| copywriter | 353 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 7 files | yes | yes | yes | THICK |
| cro-specialist | 341 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 11 files | yes | yes | yes | THICK |
| customer-success | 224 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| data-analyst | 113 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| devops | 268 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 6 files | yes | yes | yes | THICK |
| email-marketer | 220 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 8 files | yes | yes | yes | THICK |
| growth-hacker | 174 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 8 files | yes | yes | yes | THICK |
| hr-specialist | 406 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 4 files | yes | yes | yes | THICK |
| ideas-man | 433 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 7 files | yes | yes | yes | THICK |
| lawyer | 251 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| paid-media | 226 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| product-manager | 476 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| project-manager | 315 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 4 files | yes | yes | yes | THICK |
| recruitment | 180 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 3 files | yes | yes | yes | THICK |
| sales | 384 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| seo | 237 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 29 files | yes | yes | yes | THICK |
| skill-builder | 275 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 0 files | NO | NO | NO | THICK |
| social-media | 236 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 10 files | yes | yes | yes | THICK |
| software-engineer | 245 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 6 files | yes | yes | yes | THICK |
| technical-writer | 209 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 5 files | yes | yes | yes | THICK |
| ui-designer | 190 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 7 files | yes | yes | yes | THICK |
| ux-researcher | 273 | name, ver, desc, tools | MISSING | MISSING | 0/5 | 4 files | yes | yes | yes | THICK |

### Legend

- **Lines**: Total line count of SKILL.md
- **Frontmatter Fields**: Which YAML frontmatter keys are present (name/ver/desc/tools = name, version, description, allowed-tools)
- **type / category**: Skillsmith-required fields -- checked separately because they are universally absent
- **XML Sections**: Count of Skillsmith XML tags found (`<activation>`, `<persona>`, `<commands>`, `<routing>`, `<greeting>`)
- **refs/**: Number of files in the `references/` directory
- **methodology**: Whether `methodology.md` exists
- **tmpl**: Whether `SKILL.md.tmpl` exists (GTeam template system)
- **evals**: Whether `evals/` directory exists with content
- **Thickness**: THIN (<100 lines, routing only) or THICK (>100 lines, contains workflow logic)

---

## 2. Cross-Cutting Findings

### 2.1 Format: GTeam vs Skillsmith

GTeam uses a fundamentally different entry-point format from Skillsmith. This is not a deficiency -- it is a design choice. Key differences:

| Aspect | Skillsmith | GTeam |
|---|---|---|
| Entry point format | XML sections (`<activation>`, `<persona>`, `<commands>`, `<routing>`, `<greeting>`) | YAML frontmatter + free-form Markdown with `## Role`, `## Workflow` sections |
| Frontmatter fields | name, type (suite/standalone/task-only), version, category, description | name, version, description, allowed-tools |
| Missing from GTeam | `type`, `category` -- every single specialist is missing both | n/a |
| Missing from GTeam | All 5 XML sections -- **0 out of 125 possible** (25 specialists x 5 sections) | n/a |
| Entry point thickness | Skillsmith recommends THIN entry points (routing only; logic in tasks/) | GTeam is 100% THICK -- every SKILL.md contains full workflow logic inline |
| Task decomposition | Skillsmith splits workflows into `tasks/*.md` files | GTeam uses a single `methodology.md` per specialist |

### 2.2 Frontmatter Consistency (Positive)

All 25 specialists have **identical frontmatter structure**:
- `name`: present, uses `gteam-{kebab-case}` convention consistently
- `version`: present, all at `1.0.0` (no specialist has been versioned beyond initial release)
- `description`: present, one-line, descriptive
- `allowed-tools`: present, varies per specialist (Read/Write minimum; some add Bash, Edit, Glob, Grep, WebSearch, WebFetch, AskUserQuestion)

The template system (`SKILL.md.tmpl` + `bun run gen:skill-docs`) enforces this consistency well.

### 2.3 Directory Structure Consistency (Positive)

24 of 25 specialists follow the exact same structure:
```
specialist-name/
  SKILL.md           # generated entry point
  SKILL.md.tmpl      # template source
  methodology.md     # workflow logic (GTeam equivalent of tasks/)
  references/        # domain knowledge files
  results/           # outcome logging
  evals/             # evaluation scenarios
```

**Exception: `skill-builder`** -- missing `methodology.md`, `SKILL.md.tmpl`, and `evals/`. Its `references/` directory is empty. This specialist was hand-authored and not integrated into the template pipeline.

### 2.4 Entry Point Thickness

Every SKILL.md is THICK (113-476 lines). In Skillsmith terms, the entry point is doing the job of both the router AND the task files. The range:

- **Smallest**: data-analyst (113 lines)
- **Median**: ~245 lines
- **Largest**: product-manager (476 lines), ideas-man (433 lines), hr-specialist (406 lines)

Skillsmith would recommend extracting workflow logic into separate task files and keeping the entry point as a thin router. GTeam's approach works because:
1. Each specialist is a single-concern agent (no sub-routing needed)
2. The `methodology.md` file already acts as an overflow for detailed workflows
3. The template system regenerates SKILL.md from `.tmpl`, so the "source of truth" is already separated

### 2.5 Reference File Quality (Spot-Check)

Sampled 3 reference files from different specialists:

| File | Lines | Teaching? | Examples? | Self-contained? | Confidence markers? |
|---|---|---|---|---|---|
| accountant/financial-review-checklist.md | 170 | Yes -- explains why each check matters | Yes -- formulas, thresholds | Yes | `[HYPOTHESIS]`/`[TESTED]` tags |
| software-engineer/debugging-patterns.md | 135 | Yes -- symptoms/causes/diagnostic/fix pattern | Yes -- concrete code scenarios | Yes | No confidence markers |
| seo/technical-checklist.md | 85 | Partial -- checklist format, less "why" | No code examples (appropriate for SEO) | Yes | `[HYPOTHESIS]`/`[TESTED]` tags |

Reference files are generally well-structured. The `[HYPOTHESIS]`/`[TESTED]` confidence tagging system is a GTeam-specific innovation not present in Skillsmith. Not all reference files use it consistently.

### 2.6 Reference File Volume Variance

The number of reference files varies significantly:
- **seo**: 29 files (highest by far -- likely from bulk skill-seeker scraping)
- **content-creator**: 13 files
- **cro-specialist**: 11 files
- **social-media**: 10 files
- **recruitment**: 3 files (lowest among full specialists)
- **skill-builder**: 0 files

This suggests uneven investment in domain knowledge. The specialists with 3-4 reference files may benefit from additional framework documents.

### 2.7 All Versions Locked at 1.0.0

No specialist has been bumped beyond `1.0.0`. Either version bumping is not part of the workflow, or no specialist has undergone a breaking change. If versioning is intended to track evolution, a `bun run gen:skill-docs` hook could auto-bump patch versions when `methodology.md` or reference files change.

### 2.8 Common Preamble

All 25 SKILL.md files include this identical preamble block (injected by the template system):
```
> GTeam update check: `cd ~/.claude/skills/gteam && git pull && bun run build`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.
```

This is a GTeam-specific affordance with no Skillsmith equivalent. It sets agent autonomy expectations upfront.

---

## 3. Recommendations (if Skillsmith alignment is desired)

These are optional. GTeam's current format works. But if closer Skillsmith alignment is a goal:

1. **Add `type` and `category` to frontmatter** -- even if not using Skillsmith XML, these fields help with routing and discovery. All GTeam specialists would be `type: standalone`.

2. **Consider thin entry points for the largest specialists** -- product-manager (476 lines), ideas-man (433 lines), and hr-specialist (406 lines) could benefit from splitting workflow sections into task files. The remaining 22 specialists are fine as-is.

3. **Standardise confidence markers** -- the `[HYPOTHESIS]`/`[TESTED]`/`[REVISED]` system is excellent. Extend it to all reference files, not just some.

4. **Integrate skill-builder into the template pipeline** -- it is the only specialist without `SKILL.md.tmpl`, `methodology.md`, or `evals/`.

5. **Add activation metadata** -- even without XML, a "When to use / Not for" section at the top of each SKILL.md would improve routing accuracy. Some specialists have this implicitly in their description field, but explicit boundaries help.

6. **Backfill thin reference directories** -- recruitment (3 files), hr-specialist (4 files), project-manager (4 files), and ux-researcher (4 files) have the fewest domain references. Consider running skill-seekers for additional framework content.
