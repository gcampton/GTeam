// scripts/skill-check.ts
import { readFile, stat } from 'node:fs/promises'
import { join } from 'node:path'

const ROOT = join(import.meta.dir, '..')

async function fileExists(path: string): Promise<boolean> {
  try { await stat(path); return true } catch { return false }
}

async function checkSkill(skillPath: string) {
  const relPath = skillPath.replace(ROOT + '/', '')
  const tmplPath = skillPath + '.tmpl'

  const [hasMd, hasTmpl] = await Promise.all([
    fileExists(skillPath),
    fileExists(tmplPath),
  ])

  const issues: string[] = []
  if (!hasTmpl) issues.push('missing .tmpl')
  if (!hasMd) issues.push('missing generated .md')

  if (hasMd) {
    const content = await readFile(skillPath, 'utf-8')
    if (!/^---\n[\s\S]*?\n---/.test(content)) issues.push('missing frontmatter')
  }

  const status = issues.length ? '✗' : '✓'
  const issueStr = issues.length ? ` [${issues.join(', ')}]` : ''
  console.log(`  ${status} ${relPath}${issueStr}`)
}

async function main() {
  console.log('\nGTeam Skill Health Dashboard\n')

  const sections = [
    { label: 'Entry Point', pattern: 'SKILL.md' },
    { label: 'Specialists', pattern: 'specialists/*/SKILL.md' },
    { label: 'Jobs', pattern: 'jobs/*/SKILL.md' },
  ]

  for (const { label, pattern } of sections) {
    console.log(`${label}:`)
    let count = 0
    const glob = new Bun.Glob(pattern)
    for await (const p of glob.scan({ cwd: ROOT })) {
      await checkSkill(join(ROOT, p))
      count++
    }
    if (count === 0) console.log('  (none yet)')
    console.log()
  }
}

main()
