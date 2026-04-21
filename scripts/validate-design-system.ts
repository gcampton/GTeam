import { readdir, readFile, stat } from 'node:fs/promises'
import { join, relative, resolve } from 'node:path'

type ValidationProblem = {
  path: string
  message: string
}

type ManifestInfo = {
  file: string
  tokenArtifact: string
  componentContracts: string[]
}

const ROOT = process.cwd()
const DESIGN_SYSTEM_DIR = join(ROOT, 'design-system')
const TOKENS_DIR = join(DESIGN_SYSTEM_DIR, 'tokens')
const COMPONENTS_DIR = join(DESIGN_SYSTEM_DIR, 'components')
const RELEASES_DIR = join(DESIGN_SYSTEM_DIR, 'releases')

function prettyPath(target: string): string {
  if (target.startsWith(ROOT)) return relative(ROOT, target)
  return target
}

function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}

async function pathExists(path: string): Promise<boolean> {
  try {
    await stat(path)
    return true
  } catch {
    return false
  }
}

async function collectJsonFiles(dir: string): Promise<string[]> {
  if (!(await pathExists(dir))) return []
  const stack = [dir]
  const files: string[] = []

  while (stack.length > 0) {
    const current = stack.pop()!
    const entries = await readdir(current, { withFileTypes: true })
    for (const entry of entries) {
      const fullPath = join(current, entry.name)
      if (entry.isDirectory()) {
        stack.push(fullPath)
      } else if (entry.isFile() && entry.name.endsWith('.json')) {
        files.push(fullPath)
      }
    }
  }

  return files.sort()
}

async function parseJsonFile(
  file: string,
  problems: ValidationProblem[],
): Promise<unknown | null> {
  try {
    const raw = await readFile(file, 'utf8')
    return JSON.parse(raw)
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error)
    problems.push({
      path: file,
      message: `invalid JSON (${message})`,
    })
    return null
  }
}

function requireStringField(
  payload: Record<string, unknown>,
  field: string,
  file: string,
  problems: ValidationProblem[],
): string | null {
  const value = payload[field]
  if (typeof value !== 'string' || value.trim().length === 0) {
    problems.push({
      path: file,
      message: `missing required string field "${field}"`,
    })
    return null
  }
  return value
}

function requireArrayField(
  payload: Record<string, unknown>,
  field: string,
  file: string,
  problems: ValidationProblem[],
): unknown[] | null {
  const value = payload[field]
  if (!Array.isArray(value)) {
    problems.push({
      path: file,
      message: `missing required array field "${field}"`,
    })
    return null
  }
  if (value.length === 0) {
    problems.push({
      path: file,
      message: `array field "${field}" must not be empty`,
    })
  }
  return value
}

function validateTokensFile(
  file: string,
  payload: unknown,
  problems: ValidationProblem[],
): void {
  if (!Array.isArray(payload)) {
    problems.push({
      path: file,
      message: 'expected token file to be an array of token entries',
    })
    return
  }

  const requiredFields = [
    'id',
    'type',
    'value',
    'description',
    'mode',
    'deprecated',
  ]

  payload.forEach((entry, index) => {
    if (!isObject(entry)) {
      problems.push({
        path: file,
        message: `token[${index}] must be an object`,
      })
      return
    }

    for (const field of requiredFields) {
      if (!(field in entry)) {
        problems.push({
          path: file,
          message: `token[${index}] missing "${field}"`,
        })
      }
    }
  })
}

function validateComponentContractFile(
  file: string,
  payload: unknown,
  problems: ValidationProblem[],
): void {
  if (!isObject(payload)) {
    problems.push({
      path: file,
      message: 'expected component contract JSON object',
    })
    return
  }

  requireStringField(payload, 'componentId', file, problems)
  requireStringField(payload, 'implementationNotes', file, problems)
  requireArrayField(payload, 'variants', file, problems)
  requireArrayField(payload, 'states', file, problems)
  requireArrayField(payload, 'semanticSlots', file, problems)

  if (!isObject(payload.accessibility)) {
    problems.push({
      path: file,
      message: 'missing required object field "accessibility"',
    })
  }
}

function validateManifestFile(
  file: string,
  payload: unknown,
  problems: ValidationProblem[],
): ManifestInfo | null {
  if (!isObject(payload)) {
    problems.push({
      path: file,
      message: 'expected release manifest JSON object',
    })
    return null
  }

  requireStringField(payload, 'version', file, problems)
  const tokenArtifact = requireStringField(
    payload,
    'tokenArtifact',
    file,
    problems,
  )

  const componentContractsValue = requireArrayField(
    payload,
    'componentContracts',
    file,
    problems,
  )

  const componentContracts = (componentContractsValue ?? [])
    .filter(entry => typeof entry === 'string' && entry.trim().length > 0)
    .map(entry => entry as string)

  if (componentContractsValue && componentContracts.length !== componentContractsValue.length) {
    problems.push({
      path: file,
      message: 'field "componentContracts" must contain only non-empty strings',
    })
  }

  if (!tokenArtifact) return null

  return {
    file,
    tokenArtifact,
    componentContracts,
  }
}

function resolveReferencedPath(baseFile: string, reference: string): string {
  if (reference.startsWith('design-system/')) return join(ROOT, reference)
  return resolve(join(baseFile, '..'), reference)
}

async function main(): Promise<void> {
  const problems: ValidationProblem[] = []

  if (!(await pathExists(DESIGN_SYSTEM_DIR))) {
    problems.push({
      path: DESIGN_SYSTEM_DIR,
      message: 'missing required directory',
    })
    printAndExit(problems)
    return
  }

  const tokenFiles = await collectJsonFiles(TOKENS_DIR)
  const componentFiles = (await collectJsonFiles(COMPONENTS_DIR)).filter(file =>
    file.endsWith('.contract.json'),
  )
  const manifestFiles = (await collectJsonFiles(RELEASES_DIR)).filter(
    file => file.endsWith('/manifest.json') || file.endsWith('\\manifest.json'),
  )

  if (tokenFiles.length === 0) {
    problems.push({
      path: TOKENS_DIR,
      message: 'expected at least one JSON token artifact',
    })
  }

  if (componentFiles.length === 0) {
    problems.push({
      path: COMPONENTS_DIR,
      message: 'expected at least one *.contract.json component contract',
    })
  }

  if (manifestFiles.length === 0) {
    problems.push({
      path: RELEASES_DIR,
      message: 'expected at least one releases/*/manifest.json file',
    })
  }

  for (const tokenFile of tokenFiles) {
    const payload = await parseJsonFile(tokenFile, problems)
    if (payload !== null) validateTokensFile(tokenFile, payload, problems)
  }

  for (const componentFile of componentFiles) {
    const payload = await parseJsonFile(componentFile, problems)
    if (payload !== null) {
      validateComponentContractFile(componentFile, payload, problems)
    }
  }

  const manifests: ManifestInfo[] = []
  for (const manifestFile of manifestFiles) {
    const payload = await parseJsonFile(manifestFile, problems)
    if (payload === null) continue
    const manifest = validateManifestFile(manifestFile, payload, problems)
    if (manifest) manifests.push(manifest)
  }

  const referencedTokenArtifacts = new Set<string>()
  const referencedComponentContracts = new Set<string>()

  for (const manifest of manifests) {
    const tokenPath = resolveReferencedPath(manifest.file, manifest.tokenArtifact)
    referencedTokenArtifacts.add(tokenPath)
    if (!(await pathExists(tokenPath))) {
      problems.push({
        path: manifest.file,
        message: `tokenArtifact path does not exist: ${manifest.tokenArtifact}`,
      })
    }

    for (const contractRef of manifest.componentContracts) {
      const contractPath = resolveReferencedPath(manifest.file, contractRef)
      referencedComponentContracts.add(contractPath)
      if (!(await pathExists(contractPath))) {
        problems.push({
          path: manifest.file,
          message: `componentContracts entry does not exist: ${contractRef}`,
        })
      }
    }
  }

  for (const tokenFile of tokenFiles) {
    if (!referencedTokenArtifacts.has(tokenFile)) {
      problems.push({
        path: tokenFile,
        message: 'not referenced by any release manifest tokenArtifact',
      })
    }
  }

  for (const componentFile of componentFiles) {
    if (!referencedComponentContracts.has(componentFile)) {
      problems.push({
        path: componentFile,
        message: 'not referenced by any release manifest componentContracts entry',
      })
    }
  }

  printAndExit(problems)
}

function printAndExit(problems: ValidationProblem[]): void {
  if (problems.length === 0) {
    console.log('Design-system contract validation passed.')
    process.exit(0)
  }

  console.error('Design-system contract validation failed:')
  for (const problem of problems) {
    console.error(`- ${prettyPath(problem.path)}: ${problem.message}`)
  }
  process.exit(1)
}

await main()
