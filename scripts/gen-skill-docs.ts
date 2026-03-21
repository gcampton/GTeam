// scripts/gen-skill-docs.ts
import { readFile, writeFile } from 'node:fs/promises'
import { join } from 'node:path'

export const PREAMBLE_TEXT = `> GTeam update check: \`cd ~/.claude/skills/gteam && git pull && bun run build\`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.`

export function resolvePreamble(): string {
  return PREAMBLE_TEXT
}

/** Convert token name back to specialist directory name.
 *  SEO_METHODOLOGY → seo
 *  CONTENT_CREATOR_METHODOLOGY → content-creator
 *  SOCIAL_MEDIA_METHODOLOGY → social-media
 */
function tokenToDir(token: string): string | null {
  if (!token.endsWith('_METHODOLOGY')) return null
  const base = token.slice(0, -'_METHODOLOGY'.length)
  return base.toLowerCase().replace(/_/g, '-')
}

export async function resolveToken(token: string, rootDir: string): Promise<string> {
  if (token === 'PREAMBLE') return resolvePreamble()
  if (token === 'GTEAM_DIR') return '~/.claude/skills/gteam'

  const dir = tokenToDir(token)
  if (!dir) throw new Error(`Unknown token: ${token}`)

  const methodologyPath = join(rootDir, 'specialists', dir, 'methodology.md')
  try {
    return await readFile(methodologyPath, 'utf-8')
  } catch {
    throw new Error(`Cannot resolve {{${token}}}: file not found at ${methodologyPath}`)
  }
}

export async function processTemplate(tmplPath: string, rootDir: string): Promise<string> {
  let content = await readFile(tmplPath, 'utf-8')

  const tokenRegex = /\{\{([A-Z_]+)\}\}/g
  const tokens = [...content.matchAll(tokenRegex)].map(m => m[1])

  const resolved = new Map<string, string>()
  for (const token of new Set(tokens)) {
    resolved.set(token, await resolveToken(token, rootDir))
  }

  content = content.replace(tokenRegex, (_, token) => resolved.get(token)!)
  return content
}

// CLI entry point
if (import.meta.main) {
  const isDryRun = process.argv.includes('--dry-run')
  const rootDir = join(import.meta.dir, '..')

  const patterns = [
    'SKILL.md.tmpl',
    'specialists/*/SKILL.md.tmpl',
    'jobs/*/SKILL.md.tmpl',
  ]

  let hadDiff = false

  for (const pattern of patterns) {
    const glob = new Bun.Glob(pattern)
    for await (const tmplPath of glob.scan({ cwd: rootDir })) {
      const fullTmplPath = join(rootDir, tmplPath)
      const outputPath = fullTmplPath.replace(/\.tmpl$/, '')

      const generated = await processTemplate(fullTmplPath, rootDir)

      if (isDryRun) {
        let existing = ''
        try { existing = await readFile(outputPath, 'utf-8') } catch {}
        if (existing !== generated) {
          console.error(`STALE: ${outputPath} — run bun run gen:skill-docs`)
          hadDiff = true
        }
      } else {
        await writeFile(outputPath, generated)
        console.log(`Generated: ${outputPath}`)
      }
    }
  }

  if (isDryRun && hadDiff) process.exit(1)
}
