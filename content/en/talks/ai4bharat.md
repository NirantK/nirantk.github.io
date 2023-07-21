---
title: "AI4Humans: Software x LLMs"
description: "Slides, Citations and References for my talk at AI4Bharat, IIT Madras, July 2023"
excerpt: "Patterns for building AI4Humans"
draft: false
date: 2023-07-21T00:09:00+05:30
lastmod: 2023-07-21T00:09:00+05:30
tags: ["tech", "niranting", "ai4bharat"]
weight: 50
images: []
toc: true
contributors: ["Nirant Kasliwal"]
show_reading_time: true
---

Google Slides are [here](https://docs.google.com/presentation/d/1fzwXZJtLLdXPFHahOlSuaK62VYy2F-F-yPV5SxwA5Xo/edit?usp=sharing)

Here is the outline of topics we discussed: 
# AI4Humans: LLMs x Software Systems

## Introduction

Hello, I'm Nirant, a machine learning engineer and contributor to AI4Bharat. I've had the privilege of working on a range of exciting projects, from publishing an ACL 2020 NLP Paper on Hinglish and writing an NLP book, to contributing to IndicGlue and deploying systems used by Nykaa. I also manage India's largest GenAI community and regularly host meetups. You can find more about my work on [my GitHub profile](https://github.com/NirantK).

In this blog, I'll be discussing the intersection of Large Language Models (LLMs) and software systems, focusing on their potential for creating AI solutions that are cheaper, better, and faster. We'll also delve into the challenges and open problems in this domain.

## Specialised LLMs: Making AI Cheaper, Better, Faster

One of the most frequent patterns in AI development is the use of Retrieval Augmented Generation (RAG). This approach is particularly useful for applications like FAQ bots on WhatsApp, which need to provide factual responses in various languages. Examples of such applications include Kissan.ai and farmer.chat.

Customer support automation is another area where RAG shines. For instance, Bot9.ai from Bengaluru is designed to serve virtually all internet companies worldwide.

## Role of Vector DBs e.g. Qdrant

Orchestration is a crucial aspect of LLMs. Tools like Langchain, Llama Index, and Semantic Kernel play a significant role in orchestrating the process of information retrieval, text splitting, and ranking. However, there are open problems in this area, such as handling documents that don't fit the context window and improving the ranking/selection of top K documents. 

## Embedding Selection and Cross-Encoder Addition

The process of embedding selection involves adding details to the LLM. For instance, we can use OpenAI GPT4 and Ada-002 for embedding, and then add a cross-encoder like Cohere Rerank for further refinement. This process can be further enhanced by a 2-pass search using tools like BM25/ElasticSearch.

## Open Problems in LLMs

There are several open problems in the field of LLMs. One of the most significant is evaluation. How can we automatically evaluate answers? Where do traditional measures like EM, F1, and BERT-score fall short? Another challenge is monitoring. How can we measure model degradation? How can we handle questions that are close to the domain but not exactly within it?

## LLM "Functions"

LLMs can be used for tool augmentation. For example, the Gorilla LLM family offloads tasks to more specialized, reliable models. This approach allows for the conversion from language to programmatic objects or programming code. A demo of this can be seen in the AgentAI library, which I built.

## Conclusion

LLMs hold immense potential for improving AI systems, making them cheaper, better, and faster. However, there are still many open problems to solve, from evaluation and monitoring to security and latency. As we continue to explore and innovate in this field, we can look forward to more robust and efficient AI solutions.

For more details, you can check out executable code of AgentAI [here](https://bit.ly/agentaimed).