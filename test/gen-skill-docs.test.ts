import { expect, test, describe, beforeEach, afterEach } from 'bun:test'
import { mkdtemp, writeFile, mkdir, rm } from 'node:fs/promises'
import { join } from 'node:path'
import { tmpdir } from 'node:os'
import { resolvePreamble, resolveToken, processTemplate, PREAMBLE_TEXT } from '../scripts/gen-skill-docs'

let tmp: string

beforeEach(async () => {
  tmp = await mkdtemp(join(tmpdir(), 'gteam-test-'))
})

afterEach(async () => {
  await rm(tmp, { recursive: true })
})

describe('resolvePreamble', () => {
  test('returns string containing update check', () => {
    expect(resolvePreamble()).toContain('GTeam update check')
  })

  test('returns string containing autonomy mode', () => {
    expect(resolvePreamble()).toContain('Autonomy mode')
  })

  test('matches PREAMBLE_TEXT constant exactly', () => {
    expect(resolvePreamble()).toBe(PREAMBLE_TEXT)
  })
})

describe('resolveToken', () => {
  test('resolves SEO_METHODOLOGY from specialists/seo/methodology.md', async () => {
    await mkdir(join(tmp, 'specialists', 'seo'), { recursive: true })
    await writeFile(join(tmp, 'specialists', 'seo', 'methodology.md'), '## SEO Workflow\nStep 1: audit')
    const result = await resolveToken('SEO_METHODOLOGY', tmp)
    expect(result).toBe('## SEO Workflow\nStep 1: audit')
  })

  test('resolves CONTENT_CREATOR_METHODOLOGY (kebab name)', async () => {
    await mkdir(join(tmp, 'specialists', 'content-creator'), { recursive: true })
    await writeFile(join(tmp, 'specialists', 'content-creator', 'methodology.md'), '## Content steps')
    const result = await resolveToken('CONTENT_CREATOR_METHODOLOGY', tmp)
    expect(result).toBe('## Content steps')
  })

  test('resolves SOCIAL_MEDIA_METHODOLOGY (multi-word kebab)', async () => {
    await mkdir(join(tmp, 'specialists', 'social-media'), { recursive: true })
    await writeFile(join(tmp, 'specialists', 'social-media', 'methodology.md'), '## Social steps')
    const result = await resolveToken('SOCIAL_MEDIA_METHODOLOGY', tmp)
    expect(result).toBe('## Social steps')
  })

  test('resolves GTEAM_DIR to install path', async () => {
    const result = await resolveToken('GTEAM_DIR', tmp)
    expect(result).toBe('~/.claude/skills/gteam')
  })

  test('throws on unknown token', async () => {
    await expect(resolveToken('UNKNOWN_TOKEN', tmp)).rejects.toThrow('Unknown token: UNKNOWN_TOKEN')
  })

  test('throws if methodology.md does not exist', async () => {
    await expect(resolveToken('SEO_METHODOLOGY', tmp)).rejects.toThrow()
  })
})

describe('processTemplate', () => {
  test('replaces {{PREAMBLE}} with preamble text', async () => {
    const tmplPath = join(tmp, 'SKILL.md.tmpl')
    await writeFile(tmplPath, '# Test\n\n{{PREAMBLE}}\n\nRest of skill.')
    const result = await processTemplate(tmplPath, tmp)
    expect(result).toContain('GTeam update check')
    expect(result).not.toContain('{{PREAMBLE}}')
  })

  test('replaces {{SEO_METHODOLOGY}} with file content', async () => {
    await mkdir(join(tmp, 'specialists', 'seo'), { recursive: true })
    await writeFile(join(tmp, 'specialists', 'seo', 'methodology.md'), '## SEO steps')
    const tmplPath = join(tmp, 'SKILL.md.tmpl')
    await writeFile(tmplPath, '# Test\n\n{{SEO_METHODOLOGY}}\n')
    const result = await processTemplate(tmplPath, tmp)
    expect(result).toContain('## SEO steps')
    expect(result).not.toContain('{{SEO_METHODOLOGY}}')
  })

  test('throws on unrecognised {{TOKEN}}', async () => {
    const tmplPath = join(tmp, 'SKILL.md.tmpl')
    await writeFile(tmplPath, '# Test\n\n{{TOTALLY_UNKNOWN}}\n')
    await expect(processTemplate(tmplPath, tmp)).rejects.toThrow('Unknown token: TOTALLY_UNKNOWN')
  })

  test('handles template with no tokens', async () => {
    const tmplPath = join(tmp, 'SKILL.md.tmpl')
    await writeFile(tmplPath, '# Plain template\n\nNo tokens here.')
    const result = await processTemplate(tmplPath, tmp)
    expect(result).toBe('# Plain template\n\nNo tokens here.')
  })
})
