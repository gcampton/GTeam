// test/skill-validation.test.ts
import { expect, test, describe } from 'bun:test'
import { readFile } from 'node:fs/promises'
import { join } from 'node:path'

// Import browse command sets from gstack submodule
import {
  READ_COMMANDS,
  WRITE_COMMANDS,
} from '../browse/browse/src/commands'

const ROOT = join(import.meta.dir, '..')
const KNOWN_TOKENS = new Set(['PREAMBLE'])
const KNOWN_TOKEN_SUFFIXES = ['_METHODOLOGY']

function isKnownToken(token: string): boolean {
  if (KNOWN_TOKENS.has(token)) return true
  return KNOWN_TOKEN_SUFFIXES.some(suffix => token.endsWith(suffix))
}

const ALL_BROWSE_COMMANDS = new Set([
  ...READ_COMMANDS,
  ...WRITE_COMMANDS,
])

async function discoverSkills(): Promise<string[]> {
  const paths: string[] = []
  const glob = new Bun.Glob('{SKILL.md,specialists/*/SKILL.md,jobs/*/SKILL.md}')
  for await (const p of glob.scan({ cwd: ROOT })) {
    paths.push(join(ROOT, p))
  }
  return paths
}

async function discoverTemplates(): Promise<string[]> {
  const paths: string[] = []
  const glob = new Bun.Glob('{SKILL.md.tmpl,specialists/*/SKILL.md.tmpl,jobs/*/SKILL.md.tmpl}')
  for await (const p of glob.scan({ cwd: ROOT })) {
    paths.push(join(ROOT, p))
  }
  return paths
}

describe('Tier 1: Skill frontmatter', () => {
  test('all SKILL.md files have required frontmatter fields', async () => {
    const skills = await discoverSkills()
    // May be 0 skills early in development — that's OK
    for (const skillPath of skills) {
      const content = await readFile(skillPath, 'utf-8')
      const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/)
      expect(frontmatterMatch, `${skillPath}: missing frontmatter`).toBeTruthy()
      const fm = frontmatterMatch![1]
      expect(fm, `${skillPath}: missing 'name'`).toContain('name:')
      expect(fm, `${skillPath}: missing 'version'`).toContain('version:')
      expect(fm, `${skillPath}: missing 'description'`).toContain('description:')
      expect(fm, `${skillPath}: missing 'allowed-tools'`).toContain('allowed-tools:')
    }
  })
})

describe('Tier 1: Browse command validation', () => {
  test('all $B commands in SKILL.md files exist in browse registry', async () => {
    const skills = await discoverSkills()
    const errors: string[] = []
    for (const skillPath of skills) {
      const content = await readFile(skillPath, 'utf-8')
      const matches = content.matchAll(/\$B\s+(\S+)/g)
      for (const match of matches) {
        const cmd = match[1]
        if (!ALL_BROWSE_COMMANDS.has(cmd)) {
          errors.push(`${skillPath}: unknown $B command '${cmd}'`)
        }
      }
    }
    expect(errors, errors.join('\n')).toHaveLength(0)
  })
})

describe('Tier 1: Template token validation', () => {
  test('all {{TOKEN}} in .tmpl files are known tokens', async () => {
    const templates = await discoverTemplates()
    const errors: string[] = []
    for (const tmplPath of templates) {
      const content = await readFile(tmplPath, 'utf-8')
      const matches = content.matchAll(/\{\{([A-Z_]+)\}\}/g)
      for (const match of matches) {
        const token = match[1]
        if (!isKnownToken(token)) {
          errors.push(`${tmplPath}: unknown token {{${token}}}`)
        }
      }
    }
    expect(errors, errors.join('\n')).toHaveLength(0)
  })
})
