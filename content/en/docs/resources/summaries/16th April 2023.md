---
contributors:
- Nirant Kasliwal
date: '2023-04-16 00:00:00+05:30'
description: An engaging conversation delving into the world of sci-fi literature,
  AI breakthroughs, LLMs, multimodal systems, community guidelines, GPT-related topics,
  fine-tuning strategies, deployment, and cost efficiency.
draft: false
excerpt: An engaging conversation delving into the world of sci-fi literature, AI
  breakthroughs, LLMs, multimodal systems, community guidelines, GPT-related topics,
  fine-tuning strategies, deployment, and cost efficiency.
featured_image: ''
images: []
lastmod: '2023-04-16 00:00:00+05:30'
tags:
- daily_summary
title: Exploring Sci-Fi, AI, and GPT Technologies
toc: true
weight: 50
---

## Sci-Fi and AI
- Discussion on sci-fi authors such as Asimov, Clarke, and Heinlein
- Comparison of Multivac from Asimov's stories to today's LLMs/Auto-GPT
- Sharing of a sci-fi story by Greg Egan
- Multimodality and its potential to improve LLMs' understanding of reality
- Sharing of a paper on color clustering
- Appreciation for Asimov's work and genius
- Recommendation of Cixin Liu as a favorite author

## Community Guidelines
- Drafting of community guidelines for the group
- Sharing of a website for sci-fi enthusiasts (Orion's Arm)

## GPT-Related Topics
- Request for a service that allows using chatGPT interface with API key
- Sharing of a website for chatbot UI
- Discussion on context window handling of such services
- Recommendation to use GPT-4 with large context windows for cost efficiency
- Request for guidance on fine-tuning with custom data and sharing of a GitHub example
- Sharing of articles by Databricks on tuning Dolly LLM
- Discussion on deploying a Docker image with Sentence Transformers and OpenAI combined
- Recommendation to deploy the model separately behind a service endpoint to avoid distributing the model in application containers
- Discussion on the use of embeddings and OpenAI for cost reduction
- Sharing of a Twitter thread on fine-tuning and prompting
- Recommendation to use external vector databases like Pinecone or Weaviate instead of fine-tuning for cost efficiency
- Discussion on chunk size for converting text dump and documents into embeddings
- Sharing of Langchain's conversation memory types for optimization
- Question on the possibility of specialized hardware speeding up embedding search
- Request for a summary of the GPT-related topics due to the increasing number of messages in the group
- Sharing of a post by Vespa founder on introducing embeddings and vector search
- Sharing of an IPython ChatGPT extension
- Discussion on Auto GPT's intermediate summary phase for webpage parsing
- Experience with LLMs and plans to add new tasks in classifier and separate their workflow standalone
- Sharing of Langchain's memory chains and conversation memory for summarization and retrieval

## Links
The description and link can be mismatched because of extraction errors.

- https://www.gregegan.net/MISC/CRYSTAL/Crystal.html: A message discussing the similarity between Multivac and today's LLMs/Auto-GPT, with a reference to AI.
- https://www.chatbotui.com/ : "I figured that's cheaper than buying chatGPT plus. And also, how is the context window handling of such services? Surely they'll lose the memory ability once the past chats get out of the max token limit?"
- https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb: Request for guidance on the number of documents required for fine-tuning and resources for fine-tuning, specifically with custom data.
- The following URLs provide information about fine-tuning large language models using Hugging Face and DeepSpeed, and the first open commercially viable instruction-tuned LLM called Dolly: 
https://www.databricks.com/blog/2023/03/20/fine-tuning-large-language-models-hugging-face-and-deepspeed.html 
https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm
- https://www.databricks.com/blog/2023/03/20/fine-tuning-large-language-models-hugging-face-and-deepspeed.html: An article by Databrick on how they've fine-tuned the open source Dolly LLM using Hugging Face and DeepSpeed.
- https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm: Another article by Databrick on the first open commercially viable instruction-tuned LLM, Dolly, for reference.
- https://stackoverflow.com/questions/63521958/is-this-a-right-way-to-descrease-size-of-my-docker-images: A question about finetuning and generating embeddings, with a message about Harrison's strategy and plans.
- The article at https://medium.com/@TheHaseebHassan/pytorch-onnx-sentence-transformer-optimization-e24bdbed9696 is a nice resource for converting ST into ONNX format, and Harrison is praised for being open about their strategy and sharing their plans.
- The tweet from Tree Industries (@tree_industries) discusses the potential improvements in similarity search with the use of GPT3.5 and GPT4 embeddings. The URL provided leads to the tweet.
- https://huggingface.co/spaces/microsoft/HuggingGPT is shared in the message as a resource to learn about ways to make the model smarter without burning huge computation powers.
- https://platform.openai.com/docs/guides/fine-tuning: Request for a comprehensive guide on how to update weights with example data.
- https://python.langchain.com/en/latest/modules/memory/how_to_guides.html and https://trib.al/HIuiF1K are related to optimizing memory types for chunks in langchain's conversation.
- The given URL (https://python.langchain.com/en/latest/modules/memory/how_to_guides.html) is related to a question about whether specialized hardware can speed up embedding search, with a link to an article (https://trib.al/HIuiF1K) for further information.
- https://github.com/jdagdelen/hyperDB: A person is raising funds through their GitHub repository and someone mentioned that Langchain will integrate it by the end of the day.
- https://bergum.medium.com/four-mistakes-when-introducing-embeddings-and-vector-search-d39478a568c5: A post by Vespa founder discussing mistakes when introducing embeddings and vector search, which has inspired the speaker to launch their own database next week.
- The URL https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html is being discussed in relation to an umbrella term used by langchain for memory chains or conversation memory.