# Advanced Enterprise RAG System (Aligned with Full RAG Architecture)

## Overview

This repository implements an **enterprise-grade Retrieval-Augmented Generation (RAG)** system that **directly follows the advanced RAG architecture shown in the reference diagram**.

The design is **modular, extensible, and production-ready**, allowing gradual adoption of advanced techniques such as query translation, routing, re-ranking, and active retrieval—without compromising security or accuracy.

> **Core principle:** Retrieval, ranking, and validation control generation.

---

## Architecture Alignment

This implementation aligns with the following major RAG layers:

1. Query Translation
2. Routing
3. Query Construction (SQL / Graph / Vector)
4. Indexing
5. Retrieval, Ranking & Refinement
6. Generation & Self-Feedback

Each layer can be enabled incrementally based on business needs.

---

## High-Level Workflow

```
User Question
      ↓
Query Translation
      ↓
Routing Decision
      ↓
Query Construction
      ↓
Retrieval (Vector / SQL / Graph)
      ↓
Ranking & Refinement
      ↓
Context Assembly
      ↓
Controlled Generation
      ↓
Answer + Sources
```

---

## Project Structure

```
advanced-rag/
│
├── ingest/                     # Indexing layer
│   ├── loader.py               # Load documents
│   ├── chunker.py              # Semantic chunking
│   └── vector_store.py         # Embeddings + Vector DB
│
├── translation/                # Query translation layer
│   └── query_translation.py    # Multi-query, HyDE, decomposition
│
├── routing/                    # Routing layer
│   └── router.py               # Logical & semantic routing
│
├── retrieval/                  # Retrieval & ranking
│   ├── retriever_vector.py     # Vector DB retrieval
│   ├── retriever_sql.py        # SQL retrieval
│   ├── retriever_graph.py      # Graph DB retrieval
│   └── reranker.py             # Cross-encoder re-ranking
│
├── prompts/                    # Prompt control
│   └── qa_prompt.py            # Strict QA prompt
│
├── chains/                     # Orchestration
│   └── rag_chain.py            # End-to-end RAG pipeline
│
├── app.py                      # Application entry
└── requirements.txt
```

---

## Step-by-Step System Explanation

### 1. Query Translation

The user question is first translated into forms better suited for retrieval.

Supported strategies:

- Rephrasing & abstraction
- Multi-query expansion
- Step-back questioning
- HyDE (Hypothetical Document Embeddings)

**Purpose:** Improve recall and avoid missing relevant documents.

> The model does not retrieve yet—it prepares the question.

---

### 2. Routing

The translated query is routed to the appropriate backend:

- **Vector DB** → policies, manuals, unstructured text
- **SQL DB** → counts, metrics, structured reports
- **Graph DB** → relationships, dependencies, lineage

Routing methods:

- Rule-based routing
- Semantic routing via embeddings
- LLM-based routing (optional)

> Not all questions belong in a vector database.

---

### 3. Query Construction

The system constructs backend-specific queries:

- Text → SQL for relational databases
- Text → Cypher for graph databases
- Self-query retriever for metadata filtering

**Security rule:**

- Raw databases are never exposed to the LLM
- Only query results are returned

---

### 4. Indexing

Documents are prepared during ingestion using:

- Semantic chunking (not fixed-size splits)
- Overlapping chunks for context preservation
- Parent–child or summary-based indexing (optional)
- Domain-specific embeddings (optional)

**Why this matters:**
Indexing quality determines retrieval quality.

---

### 5. Retrieval

At query time:

- Top-K relevant chunks are retrieved
- Metadata filters and access control are applied
- Full datasets are never loaded

This step ensures relevance and security.

---

### 6. Ranking & Refinement

Retrieved documents are refined using:

- Cross-encoder re-ranking
- Document compression
- Corrective RAG (CRAG) if relevance is low
- Active re-retrieval when needed

> Retrieval is optimized before generation occurs.

---

### 7. Context Assembly

Only the highest-quality, re-ranked chunks are:

- Combined into a compact context
- Tracked with source metadata

This keeps prompts small, relevant, and auditable.

---

### 8. Controlled Generation

The LLM is invoked with strict rules:

- Answer only using provided context
- Explicitly state when information is unavailable
- Low or zero temperature

Optional enhancements:

- Self-RAG feedback loops
- Rewrite–Retrieve–Read (RRR)

---

## Why This Architecture Is Enterprise-Grade

- **Accuracy:** Grounded in verified data
- **Security:** No raw data leakage
- **Explainability:** Source-level transparency
- **Scalability:** Modular, backend-agnostic
- **Compliance:** Auditable retrieval and answers

---

## RAG vs Fine-Tuning

| Dimension      | RAG       | Fine-Tuning |
| -------------- | --------- | ----------- |
| Data freshness | Real-time | Static      |
| Governance     | High      | Low         |
| Cost           | Low       | High        |
| Explainability | Yes       | No          |

> Fine-tuning changes behavior. RAG controls knowledge.

---

## When to Use This Architecture

Best suited for:

- Enterprise knowledge assistants
- Regulated industries (healthcare, finance, legal)
- Compliance & policy systems
- Customer support automation
- Internal analytics assistants

---

## Key Takeaway

> **This RAG system follows the full advanced RAG architecture, while allowing phased, safe adoption in production.**

Accuracy comes from **retrieval discipline**, not larger models.

---

## Final One-Liner

> _"We don’t let the AI guess — we make it retrieve, rank, and verify before it answers."_

## Feel Free to reach out

Github: https://github.com/surinderlohat
Linkdin: https://www.linkedin.com/in/surinder-singh-lohat/
