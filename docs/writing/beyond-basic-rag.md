---
contributors:
- Nirant Kasliwal
date: '2024-11-22 00:09:00+05:30'
description: Dealing with, and preventing common issues in production RAG systems
excerpt: Dealing with, and preventing common issues in production RAG systems
draft: false
images: []
show_reading_time: true
tags:
- niranting
title: Beyond Basic RAG
---



# Beyond Basic RAG: A Deep Dive into Building Production-Ready AI Systems

!!! example "The Real World of RAG Systems"
    📒 Picture this: You're a developer who just deployed your first RAG system. Everything seems perfect in testing. Then reality hits - users start complaining about irrelevant results, not being able to do "basic stuff" and occasional hallucinations. Welcome to the world of real-world RAG systems.


## The Problem With "Naive RAG"

Let's start with a truth bomb: dumping documents into a vector database and hoping for the best is like trying to build a search engine with just a dictionary - technically possible, but practically useless.

Here's why:

1. **The Embedding Trap**: Think embedding similarity is enough? Here's a fun fact - in many embedding models, "yes" and "no" have a similarity of 0.8-0.9. Imagine asking for "yes" and getting a "no" instead in a legal search 😅

2. **The Context Confusion**: Large Language Models (LLMs) get surprisingly confused when you give them unrelated information. They're like that friend who can't ignore a app notification while telling a story - everything gets mixed up. 

3. **Length Effect**: Just like humans tend to get worse at noticing details the longer a story is, LLMs with large context windows get worse at noticing details the longer the information is.

## The Three Pillars of Production RAG

### 1. Query Understanding 🎯

The first step to better RAG isn't about better embeddings - it's about understanding what your users are actually asking for. Here's the basics:

- **Query Classification**: Before rushing to retrieve documents, classify the query type. Is it a simple lookup? A comparison? An aggregation? Each needs different handling.
    - NIT: Navigational, Informational, Transactional are the 3 very broad types.
- **Metadata Extraction**: Time ranges, entities, filters - extract these before retrieval. Think of it as giving your students sample questions to help them pay attention to what's important in the exam (at query time) much better and faster. 

!!! tip "Metadata Queries"
    The CEO of a company asks for "last year's revenue"

    The CFO asks for "revenue from last year"
    
    The CMO asks for "revenue from the last fiscal year"
    
    Do all these queries mean different things? Not really. The asker role i.e. query metadata changes the query intent.


### 2. Intelligent Retrieval Strategies 🔍

Here's where most systems fall short. Instead of one-size-fits-all retrieval:

- **Hybrid Search**: Combine dense (embedding) and sparse (keyword) retrieval. You can rerank using late interaction, use LLM as a reranker or even use both in a cascade. I can probably write a whole blog post on this, but tl;dr is that you can use a combination of many retrieval strategies to get the best of precision, recall, cost and latency.
- **Query Expansion**: Don't just search for what users ask - search for what they mean. Example: "Q4 results" should also look for "fourth quarter performance."
- **Context-Aware Filtering**: Use metadata to filter before semantic search. If someone asks for "last week's reports," don't rely on embeddings to figure out the time range.

### 3. Result Synthesis and Validation ✅

The final piece is making sure your responses are accurate and useful:

- **Cross-Validation**: For critical information (dates, numbers, facts), validate across multiple sources at ingestion time. It's possible that your ingestion pipeline is flawed and you don't know it.
- **Readability Checks**: Use tools like the [Flesch-Kincaid score](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests) to ensure responses match your user's expertise level.
- **Hallucination Detection**: Implement systematic checks for information that isn't grounded in your retrieved documents. Considering evaluating the pipeline using offline tools like [Ragas](https://docs.ragas.io)

## Real-World Example: The Leave Policy Fiasco

Here's a real story that illustrates why naive RAG fails:

!!! failure "Company X case study"

    Company X implemented a RAG system for HR queries. When employees asked about leave policies, 
    the system kept used the entire company's wiki -- including that of the sales team. 
    And sales "ranked" higher because it contained similar keywords. 

    The result? The entire company was getting sales team vacation policies instead of their own 🤦‍♂️

The solution? They implemented:

1. Role-based filtering

2. Document source validation

3. Query intent classification

## Making Your RAG System Production-Ready

Here's your action plan:

1. **Start with Query Understanding**
   - Implement basic query type classification
   - Extract key metadata (dates, entities, filters)
   - Use this to guide your retrieval strategy

2. **Layer Your Retrieval**
   - Begin with metadata filtering
   - Add keyword-based search
   - Top it off with semantic search
   - Combine results intelligently

3. **Validate Everything**
   - Cross-check extracted dates and numbers
   - Implement hallucination detection
   - Monitor user feedback and adapt

## The Challenge

Stop thinking about RAG as just "retrieve and generate." 

Start thinking about it as a complex system that needs to understand, retrieve, validate, and synthesize information intelligently.

Your homework: Take one query type that's failing in your system. Implement query classification and targeted retrieval for just that type. Measure the improvement. You'll be amazed at the difference this focused approach makes.

---

Remember: The goal isn't to build a perfect RAG system (that doesn't exist). The goal is to ==build a RAG system that improves continuously== and fails gracefully.

!!! question "Your Turn"
    What's your biggest RAG challenge? Let's solve it together. Let me know on [Twitter](https://twitter.com/nirantk) or [email](mailto:nirant@scaledfocus.com).
