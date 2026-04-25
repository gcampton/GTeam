## CI/CD & Infrastructure

**When asked to set up or fix CI/CD pipelines:**

1. Read existing pipeline config first (`.github/workflows/`, `Dockerfile`, `docker-compose.yml`)
2. Understand the current deploy target (Vercel, Railway, Fly.io, AWS, VPS, etc.)
3. Common pipeline stages in order: install deps → lint → test → build → deploy
4. Security practices: never log secrets, use environment variables, pin action versions to SHA
5. Fail fast: put fastest checks (lint) before slowest (integration tests)
6. Cache dependencies between runs to reduce build time

**Common issues to check:**
- Secrets exposed in logs or environment dumps
- Deploy running on every push to every branch (should gate on main/production branch)
- No rollback mechanism defined
- Missing health check after deploy
- Build artefacts committed to git
