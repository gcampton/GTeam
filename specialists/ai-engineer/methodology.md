The AI engineer workflow is split into focused task files. Load the relevant task for the user's request:

| Task | File | Use When |
|---|---|---|
| Model Integration | `tasks/model-integration.md` | User needs to select a model, integrate an API, handle errors, or optimise costs |
| RAG Systems | `tasks/rag-systems.md` | User is building retrieval-augmented generation — chunking, embeddings, vector stores, retrieval |
| Prompt Engineering | `tasks/prompt-engineering.md` | User needs to design, optimise, or debug prompts for production use |
| MLOps | `tasks/mlops.md` | User needs model deployment, monitoring, A/B testing, or observability for AI systems |

**How to load:** Use Grep to search the relevant task file for specific keywords. Do NOT read all task files upfront — load only what the current request needs.
