// scripts/gen-skill-docs.ts
export const PREAMBLE_TEXT = `> GTeam update check: \`cd ~/.claude/skills/gteam && git pull && bun run build\`
> Autonomy mode: execute fully automatically. Only pause for decisions with meaningful consequences to the user.`

export function resolvePreamble(): string {
  throw new Error('not implemented')
}

export async function resolveToken(token: string, rootDir: string): Promise<string> {
  throw new Error('not implemented')
}

export async function processTemplate(tmplPath: string, rootDir: string): Promise<string> {
  throw new Error('not implemented')
}
