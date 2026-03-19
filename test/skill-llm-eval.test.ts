// test/skill-llm-eval.test.ts
import { expect, test, describe } from 'bun:test'
import { readFile, writeFile, mkdir } from 'node:fs/promises'
import { join } from 'node:path'
import { createHash } from 'node:crypto'
import { homedir } from 'node:os'

const ROOT = join(import.meta.dir, '..')
const EVALS_DIR = join(homedir(), '.gteam-dev', 'evals')
const HASH_FILE = join(EVALS_DIR, '.skill-hashes.json')

// Judge backend detection
async function detectJudgeBackend(): Promise<'claude' | 'ollama'> {
  if (process.env.GTEAM_JUDGE === 'ollama') return 'ollama'
  try {
    const proc = Bun.spawn(['which', 'claude'], { stdout: 'pipe', stderr: 'pipe' })
    const code = await proc.exited
    return code === 0 ? 'claude' : 'ollama'
  } catch {
    return 'ollama'
  }
}

async function runJudge(backend: 'claude' | 'ollama', prompt: string): Promise<string> {
  if (backend === 'claude') {
    const proc = Bun.spawn(['claude', '-p', prompt], { stdout: 'pipe', stderr: 'pipe' })
    await proc.exited
    return await new Response(proc.stdout).text()
  } else {
    const model = process.env.GTEAM_OLLAMA_MODEL ?? 'llama3'
    const res = await fetch('http://localhost:11434/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model, prompt, stream: false }),
    })
    const data = await res.json() as { response: string }
    return data.response
  }
}

function computeHash(content: string): string {
  return createHash('sha256').update(content).digest('hex')
}

async function loadHashes(): Promise<Record<string, string>> {
  try { return JSON.parse(await readFile(HASH_FILE, 'utf-8')) } catch { return {} }
}

async function saveHashes(hashes: Record<string, string>) {
  await mkdir(EVALS_DIR, { recursive: true })
  await writeFile(HASH_FILE, JSON.stringify(hashes, null, 2))
}

const DOMAIN_PROMPTS: Record<string, string> = {
  lawyer: 'Does this skill check for: liability clauses, indemnification, IP ownership, termination rights, governing law?',
  accountant: 'Does this skill flag: cash flow issues, tax exposure, missing categorisation, reconciliation gaps?',
  seo: 'Does this skill check: title tags, meta descriptions, Core Web Vitals, backlink profile, keyword cannibalisation?',
  'social-media': 'Does this skill cover: platform-specific formats, posting cadence, engagement hooks, hashtag strategy?',
  'email-marketer': 'Does this skill cover: subject line testing, segmentation, deliverability, sequence timing, CTA clarity?',
  'content-creator': 'Does this skill check: keyword integration, readability, CTA presence, internal linking?',
}

function buildJudgePrompt(skillName: string, skillContent: string): string {
  const domainCheck = DOMAIN_PROMPTS[skillName] ?? 'Does this skill provide clear, actionable professional guidance?'
  return `You are evaluating an AI skill document. Score it 0-100 on each dimension. Return ONLY a JSON object.

Skill name: ${skillName}
Skill content:
---
${skillContent.slice(0, 3000)}
---

Score these dimensions:
1. clarity: Can a non-expert understand the output and deliverables?
2. completeness: Does the workflow cover key professional obligations?
3. actionability: Does it produce concrete deliverables, not vague advice?
4. domain_accuracy: ${domainCheck}

Return only this JSON: {"clarity": N, "completeness": N, "actionability": N, "domain_accuracy": N, "pass": true/false}
pass = true if all scores >= 70.`
}

describe('Tier 3: LLM skill evaluation', () => {
  test('all specialists score ≥70 on all dimensions', async () => {
    const forceAll = process.env.EVALS_ALL === '1'
    const hashes = await loadHashes()
    const backend = await detectJudgeBackend()
    console.log(`\nJudge backend: ${backend}`)

    const skills: string[] = []
    const glob = new Bun.Glob('specialists/*/SKILL.md')
    for await (const p of glob.scan({ cwd: ROOT })) {
      skills.push(join(ROOT, p))
    }

    const newHashes = { ...hashes }
    const failures: string[] = []

    for (const skillPath of skills) {
      const content = await readFile(skillPath, 'utf-8')
      const hash = computeHash(content)
      const key = skillPath.replace(ROOT + '/', '')

      if (!forceAll && hashes[key] === hash) {
        console.log(`  SKIP ${key} (unchanged)`)
        continue
      }

      const skillName = skillPath.split('/').at(-2)!
      const prompt = buildJudgePrompt(skillName, content)
      console.log(`  EVAL ${key}`)

      const response = await runJudge(backend, prompt)
      let scores: Record<string, number> & { pass: boolean }

      try {
        const jsonMatch = response.match(/\{[\s\S]*\}/)
        scores = JSON.parse(jsonMatch?.[0] ?? '{}')
      } catch {
        failures.push(`${key}: could not parse judge response: ${response.slice(0, 100)}`)
        continue
      }

      if (!scores.pass) {
        const low = Object.entries(scores)
          .filter(([k, v]) => k !== 'pass' && typeof v === 'number' && v < 70)
          .map(([k, v]) => `${k}=${v}`)
        failures.push(`${key}: failed on [${low.join(', ')}]`)
      } else {
        newHashes[key] = hash
      }
    }

    await saveHashes(newHashes)
    expect(failures, failures.join('\n')).toHaveLength(0)
  }, 120_000)
})
