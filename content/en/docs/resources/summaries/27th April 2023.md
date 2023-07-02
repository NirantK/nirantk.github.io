---
contributors:
- Nirant Kasliwal
date: '2023-04-27 00:00:00+05:30'
description: A comprehensive discussion on various AI-related topics, such as Weaviate's
  vector search, learning LLMs and Transformers, Indic-BloomLM training, serverless
  GPU options, OpenAI rate limits, State of AI talk, Pinecone's success, and contributing
  a Spark loader for Hugging Face datasets.
draft: false
excerpt: A comprehensive discussion on various AI-related topics, such as Weaviate's
  vector search, learning LLMs and Transformers, Indic-BloomLM training, serverless
  GPU options, OpenAI rate limits, State of AI talk, Pinecone's success, and contributing
  a Spark loader for Hugging Face datasets.
featured_image: ''
images: []
lastmod: '2023-04-27 00:00:00+05:30'
tags:
- daily_summary
title: Exploring AI Tools, Techniques, and Trends
toc: true
weight: 50
---

## Weaviate
- Weaviate allows pre-filtered vector search based on metadata and builds separate indices for metadata.
- Their managed SaaS charges based on the number and dimensions of vectors, irrespective of the extra metadata stored.

## Learning LLMs/Transformers/ML
- Someone suggested doing a zoom session to discuss learning LLMs/Transformers/ML.
- People discussed how they are dealing with rate limits and 5xx errors with OpenAI.
- Some suggested using a leaky bucket to smoothen the API calling rate.
- Others suggested using proxies like Nginx with Lua JIT or Envoy with WASM/Lua for production setup without adding much latency and performance overhead.

## Indic-BloomLM
- Someone was trying to train Indic-BloomLM but was stuck with a memory leak issue.

## Serverless GPUs
- People discussed using serverless GPUs like bananadev and qblocks.cloud.

## OpenAI Rate Limits
- Someone asked if anyone had gotten higher rate limits from OpenAI.
- Some people mentioned that they had gotten their rate limits upgraded multiple times at Pepper Content.

## State of AI Talk
- Someone shared a link to a talk by two leading US researchers in AI.
- The talk was limited to 20 seats due to venue constraints.
- People asked if there was a chance of a live stream/recording.
- Some recommended resources for learning AI, including fast.ai and a Google Sheets document.

## Pinecone
- Pinecone raised $100 million and is having a moment in the age of langchain.
- People discussed Pinecone's success and the importance of DevRel for Dev products.
- Some people shared their positive experiences with Pinecone and their content game.
- People expressed interest in knowing which startups/companies are using Pinecone.

## Contributing Spark Loader for Hugging Face Datasets
- Someone shared a link to a blog post about contributing a Spark loader for Hugging Face datasets.
- People discussed planning a session on the topic.

## Links
The description and link can be mismatched because of extraction errors.

- The Twitter link leads to a tweet by user @rasbt, which may contain relevant information or a message related to the given context. The phone number has been removed for privacy reasons.
- Replit's latest announcement is interesting: https://twitter.com/swyx/status/1650989632413401089?s=20 (Their managed SaaS right now actually charges only based on the number of vectors and the dimensions of the vectors, irrespective of the extra metadata stored. Anyone started learning LLMs/Transformers/ML in the last 3 months?)
- The context is about Lua JIT and WASM, and the given URLs are related to it. The first URL is for OpenResty, while the second URL is a blog post from Tetrate.io explaining WASM modules and Envoy extensibility.
- https://tetrate.io/blog/wasm-modules-and-envoy-extensibility-explained-part-1/ - This blog post explains how API proxies like Envoy, Istio, and Nginx have a customized layer where multiple filters can be added to extend functionality using Lua, Wasm, etc. It also mentions that Lua interpreters have less overhead and are faster than Python interpreters.
- https://twitter.com/raj_raj88/status/1631018786492157954: A Twitter post discussing the versions 302, 303, etc. in relation to something unspecified.
- https://twitter.com/raj_raj88/status/1631018786492157954 - The tweet mentions "3.5-turbo" which refers to the latest model "3.5-turbo-x". The message in the same link as the tweet is related to the link.
- https://github.com/rasbt/gradient-accumulation-blog/blob/main/src/1_batchsize-1.py - A notebook that helped with training a Bloom model by performing gradient accumulation over multiple batches to emulate a larger batch size without requiring larger GPU memory or tensor sharding across different devices. The message also mentions a memory leak issue.
- https://twitter.com/Replit/status/1651344182425051136?t=246tp7Zj7ABXzT7FXB936g&s=19 - The message suggests trying out qblocks.cloud.
- Link: https://lu.ma/StateofAI 
  Context: Link to register for a talk by two leading US researchers in AI being hosted at 7:30 PM in Indiranagar with limited seating of 20.
- https://course.fast.ai - a recommended resource for training in AI, particularly in NLP and other areas such as Vision and Speech. The message also suggests trying to train with Huggingface to learn more.
- https://docs.google.com/spreadsheets/d/1hHm8_eb4J_8xqMK63LIdn2J560bYH_5FFkxqq46eRcM/edit#gid=962390240 - A spreadsheet that starts from scratch and may or may not be useful to many, but the message in the same link as the URL is related to it. The request is to reshare or link it in the group description, and it's up to the admin's call if they want to add it.
- https://twitter.com/andrewyng/status/1651605660382134274?s=46&t=wdMpftHBI367157ViAY2Gg - Pinecone raised 100m. The message in the same link as the URL is related to the link.
- Pinecone raised 100m: https://twitter.com/pinecone/status/1651602704647553028?t=4BEHwzuba9-bvJ_ocusDQQ&s=19 - The tweet mentions that Pinecone is having a moment similar to Nvidia in the age of Langchain and it's good to raise funds when there's buzz.
- https://www.databricks.com/blog/contributing-spark-loader-for-hugging-face-datasets: The content game of the website is great and they are within 5 in most AI keywords. The message in the same link as the URL is about planning something on the weekend and asking someone to take the lead, with two people CC'd.