---
contributors:
- Nirant Kasliwal
date: '2023-04-29 00:00:00+05:30'
description: Dive into a collection of discussions on diverse AI models and applications,
  such as VectorDB, LlamaIndex, Langchain, aesthetic score models, DSLR photo generation,
  transcription APIs, and more. The conversation also touches on miscellaneous subjects
  like extracting WhatsApp group data, AI avatars, and personalized content.
draft: false
excerpt: Dive into a collection of discussions on diverse AI models and applications,
  such as VectorDB, LlamaIndex, Langchain, aesthetic score models, DSLR photo generation,
  transcription APIs, and more. The conversation also touches on miscellaneous subjects
  like extracting WhatsApp group data, AI avatars, and personalized content.
featured_image: ''
images: []
lastmod: '2023-04-29 00:00:00+05:30'
tags:
- daily_summary
title: Exploring AI Models and Applications
toc: true
weight: 50
---

## VectorDB and LlamaIndex
- Discussion on whether LlamaIndex or Langchain support VectorDB with Sources with GPT4 or GPT3.5-Turbo
- Sharing of GitHub link for LlamaIndex demo
- Suggestion to use response.source_nodes to get sources
- Discussion on using evaluation module or regex to get desired sources
- Mention of OpenAI models not citing references
- Sharing of Langchain link for QA with sources example
- Discussion on limitations of Langchain and need to extend chain functions
- Mention of LlamaIndex not having such limitations

## AI Models and Applications
- Discussion on models for aesthetic score of images
- Mention of ResNet and classification model for user-scored images
- Discussion on generating professional-level DSLR photos using AI
- Mention of LAMINI AI library for fine-tuning LLMs to custom domains
- Announcement of upcoming "Learning Transformers/NLP/ML" discussion
- Discussion on D-ID and SadTalker for generating content
- Mention of Whisper models for Hindi transcription
- Suggestion of Deepgram and Monster API for transcription
- Discussion on building generative model for legible pdf/image documents
- Mention of AI-generated content for social media and advertisements
- Request for transcription API that can handle Hindi and regional languages

## Miscellaneous
- Discussion on automating extraction of WhatsApp group data
- Mention of RunwayML Gen 2 and Text2Video-Zero
- Request for transcription API that can handle Hindi and regional languages
- Announcement of weekly/monthly newsletter
- Request for tech expert in Generative AI for Zoom meet-up
- Request for connections with those working on advertisements
- Discussion on building AI avatars and personalized content
- Mention of guardrails for cloned voices
- Discussion on building QnA over CSVs using Python code or SQL

## Links
The description and link can be mismatched because of extraction errors.

- https://github.com/jerryjliu/llama_index/blob/main/examples/vector_indices/PineconeIndexDemo.ipynb: The response from Vector DB and how to retrieve the sources using response.source_nodes.
- https://python.langchain.com/en/latest/modules/chains/index_examples/qa_with_sources.html - a link related to a discussion about using text-davinci-003 and its trade offs.
- https://github.com/openai/evals/blob/4da6a6115ac03df4f8364903815a6e73e95c2fd1/evals/prompt/base.py#L22 - A user is asking about a code snippet and expressing regret for not thinking of it earlier.
- https://medium.com/airbnb-engineering/when-a-picture-is-worth-more-than-words-17718860dcc2 - An article discussing the use of user-scored images and ResNet in classification models, and how Big Data can be more effective than Big Brains in machine learning.
- The URLs https://replicate.com/cjwbw/damo-text-to-video and https://github.com/Picsart-AI-Research/Text2Video-Zero are related to a text-to-video project.
- https://replicate.com/cjwbw/damo-text-to-video and https://github.com/Picsart-AI-Research/Text2Video-Zero are related to text-to-video conversion. The message in the same link mentions a discussion on "Learning Transformers/NLP/ML" on Sunday from 4-5pm.
- https://twitter.com/bhutanisanyam1/status/1412933178411536384: A message thanking Amir for flagging something, with no further context provided. 
- https://postgresml.org/blog/tuning-vector-recall-while-generating-query-embeddings-in-the-database: A blog post about tuning vector recall while generating query embeddings in the database.
- https://twitter.com/bhutanisanyam1/status/1412933178411536384: A tweet by user @bhutanisanyam1 with the message "Haha - I'm here" and a link to a blog post on tuning vector recall while generating query embeddings in the database on the website postgresml.org.
- The given URL is a Microsoft Teams meeting link and is related to a message requesting a tech expert to drive 15 minutes of a session on Generative AI in a Zoom meet-up.
- https://playbook.samaltman.com: The message in the same link as the URL suggests that generative models are not necessary for converting raw text to PDFs/images and applying simple distortions to get synthetic data for OCR.
- guardrails released something recently, as mentioned in this tweet by ShreyaR: https://twitter.com/ShreyaR/status/1650883072324419587. A phone number was also mentioned but has been removed.