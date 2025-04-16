---
title: "RAG Metrics for Technical Leaders: Beyond Recall"
date: 2025-04-12
authors:
  - nirant
categories:
  - machine-learning
  - RAG
---

**Title: MRR, nDCG, Hit Rate, and Recall: Know Your Retrieval Metrics**

If you're working on RAG, search, or anything that touches vector databases, you've probably run into a mess of evaluation metrics: MRR, nDCG, hit rate, recall. Everyone throws these terms around. Few explain them well. 

This post is for practitioners who want to go from vague intuition to confident decisions.

If you're just starting out and debugging a hallucinating LLM, use **Hit Rate**.
If you're ready to get serious, use **MRR + Recall** during retriever tuning.
If you're ready to get serious, use **nDCG + Hit Rate** when tuning reranker or doing system evals.

## TL;DR: When to Use What

| Use Case / Need                                 | Metric to Use            | Why                                                      |
|--------------------------------------------------|---------------------------|-----------------------------------------------------------|
| You just want to check if **any correct result was retrieved** | **Hit Rate**              | Binary success metric, useful for RAG "was it in the top-k?" |
| You want to know **how many of the correct results were found** | **Recall**                | Focused on completeness — how much signal did you recover |
| You want to know **how early the 1st correct result appears** | **MRR**                   | Good for single-answer QA and fast-hit UIs               |
| You care about **ranking quality across all relevant results** | **nDCG**                  | Ideal for multi-relevance tasks like document or product search |

## Understanding Each Metric in Detail

### ✅ Hit Rate

- Binary metric: did **any** relevant doc show up in top-k?
- Doesn’t care if it’s Rank 1 or Rank 5, just needs a hit.

**Use Hit Rate when:** You're debugging RAG. Great for checking if the chunk with the answer even made it through.

> Think: "Did we even get *one* hit in the top-k?"

### ↑ Recall

- Measures what **fraction of all relevant documents** were retrieved in top-k.
- Penalizes for missing multiple relevant items.

**Use Recall when:** You want completeness. Think medical retrieval, financial documents, safety-critical systems.

> Think: "Did we find *enough* of what we needed?"

### 🔮 MRR (Mean Reciprocal Rank)

- Tells you how early the **first relevant document** appears.
- If the first correct answer is at Rank 1 → score = 1.0
- Rank 2 → score = 0.5; Rank 5 → score = 0.2

**Use MRR when:** Only one answer matters (QA, intent classification, slot filling). You care if your system gets it fast.

> Think: "Do we hit gold in the first result?"

### 🔠 nDCG (Normalized Discounted Cumulative Gain)

- Looks at **all** relevant docs, not just the first.
- Discounts docs by rank: higher = better.
- Supports graded relevance ("highly relevant" vs "somewhat relevant").

**Use nDCG when:** Ranking quality matters. Ideal for search, recsys, anything with many possible good results.

> Think: "Did we rank the good stuff higher overall?"


## How They Differ

| Metric     | Binary or Graded | 1st Hit Only? | Sensitive to Rank? | Use For...                   |
|------------|------------------|----------------|---------------------|------------------------------|
| Hit Rate   | Binary           | ❌ No          | ❌ No (thresholded) | RAG debugging, presence check |
| Recall     | Binary or Graded | ❌ No          | ❌ No               | Completeness, coverage       |
| MRR        | Binary           | ✅ Yes         | ✅ Yes              | Fast hits, QA                |
| nDCG       | Graded           | ❌ No          | ✅ Yes              | Ranking quality, search      |

## Retrieval Is Not One Metric

People default to one number because it's convenient. But retrieval is multi-objective:

- You want **early** relevant hits (MRR)
- You want **most** relevant hits (Recall)
- You want them **ranked well** (nDCG)
- You want to know if you're even in the game (Hit Rate)

Choose the metric that matches your product surface.

## Pro Tips

- Use **Hit Rate** when you're just starting out and debugging a hallucinating LLM

And then use the right metric for the right job:
- Use **MRR + Recall** during retriever tuning
- Use **nDCG + Hit Rate** when tuning reranker or doing system evals

## Final Word

MRR isn’t better than nDCG. Recall isn’t cooler than Hit Rate. They just answer different questions.

So the next time someone asks, "What's your retrieval performance?"
You can say: "Depends. What do you care about?"

