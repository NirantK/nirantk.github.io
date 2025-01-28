---
date: 2025-01-28
authors:
- nirant
categories:
- niranting
- machine-learning
title: Deepseek R1 Ideas for GPU Poor and Middle Class
---

The internet is abuzz right now with DeepSeek. I want to here suggest some ideas and opportunities which engineers have - most of them are exciting to do for engineering curiosity. 

## Agents with Better Planning

R1 is exceptional at planning and significantly cheaper than O1/O3, and we expect the prices for reasoning models to go continuously cheaper. So, with that in mind, I want to suggest some ideas which benefit from better planning agents. 

### Multi-file Code Editing

Early evidence: [R1 Sonnet set SOTA on Aider's Polyglot Benchmark](https://aider.chat/2025/01/24/r1-sonnet.html#r1sonnet-set-sota-on-aiders-polyglot-benchmark)

> R1 as architect with Sonnet as editor has set a new SOTA of 64.0% on the aider polyglot benchmark. They achieve this at 14X less cost compared to the previous o1 SOTA result.
> o1 paired with Sonnet didn’t produce better results than just using o1 alone.

This is a very good result and as part of the broader trend, there's enough evidence to pursue this direction. 

There is an opportunity to improve upon Cursor's interfaces for multi-file cold code editing as it stands today in Q1 2025. For instance, what would it look like if you could directly interact between a user feature request in their own words with the code base to generate a pull request and run an A/B test over for that specific feature?

### Browser Agents

Early evidence: [John Rush](https://x.com/johnrushx/status/1883872256121774401) benchmarked multiple LLMs for browser usage. 

tl;dr: One could build a better benchmark for evaluating your LLM's ability to do reasoning with function calling in addition to [WebVoyager](https://arxiv.org/abs/2401.13919). This is a great start for anyone wanting to build a LLM for a specialized use case (not workflow or task oriented) at a lower cost. 

### Open Source Document Inlining

The core idea here is that you can convert any text based LLM into a Vision LLM. Most folks like try to do this right now by doing some sort of thin OCR. But I think a more promising approach would be to lightly fine tune and update the weights to work with the Vision component. And I guess that is what Fireworks has been doing. And this is very promising when combined with Reasoning LLMs.

Early evidence: [Fireworks Document Inlining](https://fireworks.ai/blog/document-inlining-launch)

![Document Inlining](https://fireworks.ai/_next/image?url=https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fc285f3eb-d4f2-4ce1-8c53-25d0d3a0337b%2Fc04477f2-0600-4879-a1a2-fd816ce93068%2FScreenshot_2024-12-23_at_9.21.43_AM.png%3FX-Amz-Algorithm%3DAWS4-HMAC-SHA256%26X-Amz-Content-Sha256%3DUNSIGNED-PAYLOAD%26X-Amz-Credential%3DAKIAT73L2G45FSPPWI6X%252F20250128%252Fus-west-2%252Fs3%252Faws4_request%26X-Amz-Date%3D20250128T062520Z%26X-Amz-Expires%3D3600%26X-Amz-Signature%3De95840cc5026398d3f114bcffe5d4d25c279a8398dab73bc87d3db947ad460d4%26X-Amz-SignedHeaders%3Dhost%26x-id%3DGetObject&w=1080&q=75)

> Today, we are excited to launch a public preview of our first use case, Document Inlining, a compound system that automatically turns any LLM into a vision model to ingest images or PDFs for document-based vision tasks. Document Inlining parses images and pipes them directly into an LLM of your choice to deliver:

> Higher quality - Achieve better reasoning and generation capabilities by utilizing any LLM of choice or specialized/fine-tuned models
> Input flexibility - Automatically transform multiple file types like PDFs and screenshots. We can also handle rich document structures like tables/charts
> Ultra-simple usage - Our API is OpenAI compatible. Enable this capability by editing 1-line to specify “#transform=inline” alongside your file

## Reasoning Distilation

Early evidence: [Bespoke Labs](https://www.bespokelabs.ai/blog/bespoke-stratos-the-unreasonable-effectiveness-of-reasoning-distillation) and [Sky T1](https://novasky-ai.github.io/posts/sky-t1/)

tl;dr: This is part of a broader evidence that distillation of all kinds really works!

How? They took the reasoning traces from R1, collected over a large set of math and code problems and distilled it into Qwen. They use it to beat the previous SOTA on math and code problems. 

We already knew this for deep learning based models, but given the higher utility and cost savings — it's great to know that it holds for LLMs too! 

Sky T1 was fine-tuned on a $450 run, so it's quite cheap. 

### Reasoning models with Structured Outputs (JSON/XML)

Opportunity: Open source reasoning models currently don't prioritize function calling and structured outputs. Even less so when used with images, scans and pdf-images. 

We have abundant training data available:
  - [GorillaBench](https://gorilla.cs.berkeley.edu/leaderboard.html) datasets
  - [ComplexFuncBench](https://github.com/THUDM/ComplexFuncBench) is another resource for evaluating your LLM's ability to do reasoning with function calling.

While closed source models have so far excelled at function calling, this advantage may be diminishing:
  - We now have access to direct traces from R1
  - These traces can be used for training

#### How to do this?

Approach 1: You need the traces:

  1. Prompt R1 to generate XML traces of outputs
  2. Verify these traces against existing datasets
  3. Fine-tune reasoning models to produce structured JSON/XML

Approach 2: You don't need the traces:

  1. Use reasoning models to generate structured JSON/XML
  2. Fine-tune reasoning models to produce structured JSON/XML