## Enrich Existing Specialist

**Use when:** User says "add X knowledge to the Y specialist" or "enrich X with Y."

**Infer the right specialist if not explicit:**
- Next.js / React / TypeScript / Tailwind → `software-engineer`
- SEO tools / analytics → `seo`
- Stripe / payments → `software-engineer` + `accountant`
- Docker / CI/CD / Kubernetes → `devops`
- Security tools → `security-engineer`

**Process:**
1. Run Source Strategy (SS API → llms.txt → WebFetch → curl)
2. Process into a reference file
3. Install: `cp /tmp/<name>.md ~/dev/1_myprojects/gteam/specialists/<specialist>/references/<name>.md`
4. Confirm installed file size and one-line summary of coverage

The specialist loads the new reference automatically on next invocation.
