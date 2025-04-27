---
title: "Vector Search at Scale: Balancing Cost, Quality, and Sanity"
date: 2025-03-30
authors:
  - nirant
categories:
  - machine-learning
  - RAG
---

At scale, relevance isn't your only enemy. Cost is. Every millisecond of latency, every token passed to an LLM, and every unnecessary reranker call adds up—fast. The iron triangle of retrieval and hence, RAG is relevance, cost, and latency. You can only pick two.

Today, we'll focus on the cost and latency.

Here's a list of things that teams do that can be improved:

- Run full-precision vector search for every query
- Skip lexical signals altogether
- Avoid reranking because "it's too expensive"
- Have no system to analyze why results are bad

This post is a walkthrough of what a real retrieval stack looks like when it's designed not just for correctness, but also for operational efficiency and failure debugging.

![Retrieval Stack Architecture: Query Router, BM25, Vector Search, Aggregation, Reranker](search-scaling.png)
*Figure: Retrieval stack architecture balancing cost, quality, and latency. Each layer maximizes relevance per dollar and enables debugging.*

## The Architecture

Forget monoliths. Retrieval is a pipeline. Here's the architecture I recommend. Each layer exists for a reason: to maximize relevance per dollar and to make debugging sane.

### 1. Query Router
This is your traffic cop. It decides how to fan out the query: to a lexical search engine (BM25), a fast vector index, or both. You can route based on query class, business priority, or budget.

### 2. BM25 Search
Not dead. In fact, BM25 still shines for acronym-heavy domains, product names, and anything with proper nouns. It's cheap, precise, and the ideal complement to lossy vector embeddings. Run it in parallel with your vector retrieval.

### 3. Binary Quantized Vector Search (RAM)
This is your fast recall layer—usually IVFPQ or scalar quantization in FAISS or ScaNN. Gets you top-K quickly, cheaply. Think of it as a rough shortlist generator. Latency under 5ms is normal.

### 4. Full-Precision Vector Search (Disk)
From your shortlist, you can now hit the full-resolution vectors. Higher fidelity, slower access, stored on disk. You should only do this when needed—ambiguous queries, high-value flows, or when the approximate search isn't enough.

### 5. Cross-Encoder Reranker
This is the first component in the stack that actually understands relevance. Embeddings collapse meaning into vectors. Cross-encoders read both the query and the doc, and compute true semantic alignment. Expensive, yes. But reranking the top 20–100 candidates is usually all you need.

### 6. Result Aggregation
Once you've got candidates from both BM25 and vector search, and re-ranked the best ones, you blend them. The fusion logic depends on your goal: pure precision, diversity, confidence thresholds, etc.

## Building Feedback Loops

Most retrieval problems aren't one-off issues. They're patterns. Instead of debugging individual queries, cluster them. Use a mix of token overlap and embedding distance. Add UMAP or HDBSCAN if needed.

The goal isn't just analysis—it's systematic insight:

- Which queries have zero recall?
- Which are poorly reranked?
- Which embeddings collapse semantically distinct queries?

Once you know that, you can prioritize improvements—embedding quality, routing rules, metadata enrichment, or prompt tuning—at the cluster level. Much higher leverage than spot fixes.

## Why This Matters for RAG

If your retrieval is weak, your LLM has to do all the heavy lifting. That means more tokens, more hallucinations, slower responses. And ironically, worse answers.

Your retrieval stack should do two things:
1. Return the most relevant docs
2. Let you understand why it didn't

Without that, you're just doing GPT improv with 3 PDFs in context.

Don't treat retrieval as a "vector db" checkbox. Treat it as a system. The best stacks layer:

- Cheap recall
- Precise reranking
- Old-school lexical sanity checks

1 line summary: RAM-level quantized vectors give you scale, Disk-level full vectors give you fidelity, BM25 gives you robustness, Rerankers give you actual relevance, Query clustering gives you insight.

What's expensive isn't reranking. What's expensive is debugging bad search with no observability.

If you're building RAG at scale and want to audit your retrieval infra, I do this for a living. We go from "it kind of works" to "we know exactly what's wrong and how to fix it."