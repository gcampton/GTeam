# GTeam development

## Commands

```bash
bun install                  # install dependencies
bun test                     # run Tier 1 static validation
bun run test:evals           # run Tier 3 LLM-as-judge (uses claude -p or Ollama)
bun run test:evals:all       # force all skills regardless of hash
bun run gen:skill-docs       # regenerate all SKILL.md from templates
bun run gen:skill-docs:dry-run  # check if generated files are up to date
bun run skill:check          # health dashboard for all skills
bun run build                # alias for gen:skill-docs
```

## Project structure

- `specialists/` — individual professional skills (standalone + methodology block)
- `jobs/` — orchestrated multi-specialist workflows
- `scripts/gen-skill-docs.ts` — template generator (edit this to change {{PREAMBLE}})
- `scripts/skill-check.ts` — health dashboard

## SKILL.md workflow

SKILL.md files are **generated** from `.tmpl` templates. Never edit `.md` files directly:
1. Edit the `.tmpl` file
2. Run `bun run gen:skill-docs`
3. Commit both `.tmpl` and `.md`

## Adding a new specialist

1. Create `specialists/{name}/SKILL.md.tmpl` (follow existing anatomy)
2. Create `specialists/{name}/methodology.md` (condensed workflow + domain rules)
3. Run `bun run gen:skill-docs`
4. Reference `{{NAME_METHODOLOGY}}` in any job template that needs it

## Token naming rule

Directory `content-creator` → token `{{CONTENT_CREATOR_METHODOLOGY}}`
Rule: `dirName.toUpperCase().replace(/-/g, '_') + '_METHODOLOGY'`

