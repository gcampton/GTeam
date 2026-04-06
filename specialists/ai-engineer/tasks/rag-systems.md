### RAG Architecture Overview

**Pipeline stages:**
```
Documents → Ingestion → Chunking → Embedding → Vector Store → [Index]
                                                                  ↓
User Query → Query Embedding → Retrieval → Re-ranking → Context Assembly → Generation → Response
```

**Design decisions to make upfront:**
1. What documents? (PDFs, HTML, structured data, code, mixed)
2. How often do they change? (static corpus vs live-updating)
3. What queries will users ask? (factual lookup, synthesis, comparison, how-to)
4. What quality bar? (must be correct vs best-effort)
5. What latency budget? (< 2s for chat, < 10s for deep research)

---

### Document Ingestion

**Preprocessing pipeline:**
- Extract text from source format (PDF, HTML, Markdown, DOCX)
- Clean: remove headers/footers, navigation, boilerplate
- Preserve structure: headings, lists, tables, code blocks — these carry semantic meaning
- Extract metadata: title, author, date, source URL, section hierarchy
- Deduplication: hash-based detection for exact dupes; embedding similarity for near-dupes

**Update strategy:**
- Full re-index: simple, use for < 100K documents or infrequent updates
- Incremental: track document hashes, only re-embed changed documents
- Streaming: webhook or queue-triggered ingestion for real-time sources

---

### Chunking Strategies

| Strategy | How It Works | Best For | Drawback |
|---|---|---|---|
| Fixed-size | Split every N tokens with M overlap | Simple baseline, unstructured text | Breaks mid-sentence, loses context |
| Recursive | Split by paragraph → sentence → token, respecting boundaries | General-purpose, mixed content | Uneven chunk sizes |
| Semantic | Group sentences by embedding similarity | Narrative content, articles | Slower, requires embedding at chunk time |
| Document-structure | Split by heading/section hierarchy | Technical docs, legal, manuals | Requires structured input |
| Parent-child | Small chunks for retrieval, return parent chunk for context | When precision and context both matter | More complex indexing |

**Chunk size guidelines:**
- Too small (< 100 tokens): loses context, retrieves fragments
- Too big (> 1000 tokens): dilutes relevance signal, wastes context window
- Sweet spot: 200-500 tokens with 50-100 token overlap for most use cases
- Always test with real queries — the right size depends on your content and questions

**Overlap is mandatory.** Without overlap, information at chunk boundaries is lost. 10-20% overlap is standard.

---

### Vector Databases

| Database | Best For | Hosted | Self-hosted | Notes |
|---|---|---|---|---|
| Pinecone | Production SaaS, managed scaling | Yes | No | Serverless option, good filtering |
| Weaviate | Hybrid search (dense + sparse) | Yes | Yes | Built-in BM25 + vector, GraphQL API |
| ChromaDB | Prototyping, small datasets | No | Yes | Simple API, in-process, SQLite backend |
| pgvector | Already using PostgreSQL | Via cloud PG | Yes | No separate infra, good enough for < 1M vectors |
| Qdrant | High performance, filtering | Yes | Yes | Rust-based, strong filtering, good for production |
| Milvus | Large scale (billions of vectors) | Yes (Zilliz) | Yes | Complex setup, overkill for < 10M vectors |

**Selection rule:** Start with pgvector if you already have Postgres. Move to a dedicated vector DB only when you hit performance limits (typically > 1M vectors or need sub-50ms P99 latency).

---

### Retrieval Optimisation

**Hybrid search (recommended for production):**
- Dense retrieval (embeddings): catches semantic similarity, handles paraphrasing
- Sparse retrieval (BM25/TF-IDF): catches exact keyword matches, handles proper nouns and codes
- Combine with Reciprocal Rank Fusion (RRF) or learned weighting
- Hybrid consistently outperforms either alone

**Re-ranking:**
- Retrieve top-K candidates (K=20-50) with fast vector search
- Re-rank with a cross-encoder model (Cohere Rerank, BGE-reranker) to top-N (N=3-5)
- Re-ranking adds 100-300ms latency but significantly improves relevance

**Metadata filtering:**
- Filter by document type, date range, category, access level BEFORE vector search
- Pre-filtering reduces search space and improves relevance
- Store filterable metadata alongside vectors, not just in the document

**Query transformation:**
- HyDE (Hypothetical Document Embeddings): generate a hypothetical answer, embed that instead of the query
- Query expansion: rephrase the query 2-3 ways, retrieve for each, merge results
- Step-back prompting: for specific questions, also retrieve broader context

---

### Context Window Management

| Strategy | How It Works | Best For |
|---|---|---|
| Stuff | Put all retrieved chunks into one prompt | Short documents, few chunks (< 5) |
| Map-reduce | Summarise each chunk, then summarise summaries | Long documents, many chunks |
| Refine | Process chunks sequentially, refining the answer | When order matters, detailed analysis |
| Map-rerank | Score each chunk's answer, return the best | Factual lookup, single-answer questions |

**Context assembly rules:**
- Put the most relevant chunks first — models attend more to early context
- Include source metadata (document title, section) with each chunk for attribution
- Set a context budget (e.g., 4K tokens for retrieval context) and enforce it
- Always leave room for the system prompt, few-shot examples, and generation

---

### RAG Evaluation

| Metric | What It Measures | How to Compute |
|---|---|---|
| Retrieval recall | Did we find the right documents? | % of gold passages in top-K results |
| Retrieval precision | Are retrieved documents relevant? | % of top-K results that are actually relevant |
| Faithfulness | Is the answer grounded in the context? | LLM-as-judge: "Is every claim in the answer supported by the context?" |
| Answer relevance | Does the answer address the question? | LLM-as-judge: "Does this answer the user's question?" |
| Answer correctness | Is the answer factually correct? | Compare against gold-standard answers (exact match, F1, human eval) |

**Evaluation dataset:** Build a set of 50-100 question-answer pairs with source documents identified. This is your regression test suite. Run it on every pipeline change.

---

### Common RAG Failures

| Failure | Symptom | Fix |
|---|---|---|
| Retrieval miss | Correct answer exists in corpus but isn't retrieved | Improve chunking, add hybrid search, try query expansion |
| Chunk boundary | Answer spans two chunks, neither has full context | Increase overlap, use parent-child chunking |
| Hallucination despite context | Model ignores retrieved context and makes things up | Stronger grounding instructions, add "if not in context, say so" |
| Wrong document | Retrieves semantically similar but incorrect document | Add metadata filtering, improve embedding model |
| Stale data | Answer is correct for old version of document | Implement incremental re-indexing, add date awareness |
| Context overflow | Too many chunks dilute the relevant signal | Reduce K, improve re-ranking, use map-reduce for synthesis |
