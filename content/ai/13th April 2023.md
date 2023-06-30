+++
title =  "Dolly 2.0, Consistency Models, Vector Databases, and Cloud Providers"
date = 2023-04-13T00:00:00+05:30
tags = ["daily_summary"]
featured_image = ""
description = "In this discussion, participants explore the release of Dolly 2.0, a commercially viable LLM by Databricks, OpenAI's consistency models, and various vector databases. They also delve into the APIs of cloud providers like Azure, AWS, and GCP, as well as the future of LLMs, chip supply, code generation, and the use of FAISS, Annoy, ScaNN, and ANNlite."
toc = true
+++

## Dolly 2.0
- Databricks has released Dolly 2.0, a commercially viable LLM.
- The dataset was crowdsourced from Databricks employees.
- The training code, dataset, and model weights have been open-sourced and are suitable for commercial use.
- Link: https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm

## OpenAI's Consistency Models
- OpenAI has proposed consistency models, a new family of generative models that achieve high sample quality without adversarial training.
- Link: https://www.marktechpost.com/2023/03/10/open-ai-proposes-consistency-models-a-new-family-of-generative-models-that-achieve-high-sample-quality-without-adversarial-training/

## Vector Databases
- Participants discussed various vector databases, including Pinecone, Weaviate, Qdrant, Chroma, Redis Vector Cache, Vespa, pgvector on Supabase, and Milvus.
- Participants also discussed the best vector database for production and inferencing costs.
- Links: 
  - https://www.pinecone.io/
  - https://www.weaviate.com/
  - https://qdrant.tech/
  - https://chroma.ai/
  - https://redislabs.com/solutions/use-cases/vector-cache/
  - https://vespa.ai/
  - https://github.com/supabase/pgvector
  - https://milvus.io/

## Cloud Providers
- Participants discussed the APIs of various cloud providers, including Azure, AWS, and GCP.
- Participants also discussed the cost of compute and the expensive APIs of cloud providers.
- Links: 
  - https://aws.amazon.com/comprehend/medical/pricing/

## LLMs and Chip Supply
- Participants discussed the future of LLMs and chip supply.
- Participants also discussed the possibility of smaller models becoming more accurate and the emergence of new chips.
- Links: 
  - https://tenstorrent.com/
  - https://techcrunch.com/2023/01/10/openai-in-talks-to-back-zeloof-and-chip-legend-kellers-startup-at-100-million-valuation/amp/
  - https://zilliz.com/

## Code Generation
- Participants discussed open-source LLMs that are strong with code generation and various programming languages.
- Participants also discussed the use of CodeGen by Replit and AWS CodeWhisperer.
- Links: 
  - https://github.com/huggingface/diffusers/releases/tag/v0.15.0
  - https://github.com/ravenscroftj/turbopilot

## Other Topics
- Participants discussed the use of FAISS, Annoy, ScaNN, and ANNlite.
- Participants also discussed the possibility of open-source ISAs and the moat for a company lying in proprietary datasets.
- Links: 
  - https://github.com/lllyasviel/ControlNet-v1-1-nightly
  - https://github.com/ashe_cs/status/1646543644038397952?s=46&t=0NBX3C3Uma-Su4_rjA3OMA
  - https://www.linkedin.com/posts/harshsinghal_under40-activity-7052341005978615809-EaUX?utm_source=share&utm_medium=member_android

## Links
The description and link can be mismatched because of extraction errors.

- https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm: Love how they crowd sourced the dataset from own employees.
- https://www.marktechpost.com/2023/03/10/open-ai-proposes-consistency-models-a-new-family-of-generative-models-that-achieve-high-sample-quality-without-adversarial-training/ : OpenAI proposes consistency models, a new family of generative models that achieve high sample quality without adversarial training. A summary of the article is provided.
- https://aws.amazon.com/comprehend/medical/pricing/ : This link provides information about the pricing of Amazon Comprehend Medical, a natural language processing service for medical text. The message in the same link mentions that GPT3.5 was cheaper than GPT3.
- https://github.com/lllyasviel/ControlNet-v1-1-nightly: This link leads to a GitHub repository for "ControlNet," and the message following it asks if anyone is using "Milvus."
- https://zilliz.com/ - The message in the same link as the URL says "You didn't have to ruin the joke for everyone by explaining it."
- https://tenstorrent.com: The website is mentioned in the context of discussing the accuracy and emergent abilities of smaller and larger models in certain tasks. The message also includes a greeting to someone who may be present on the website.
- https://techcrunch.com/2023/01/10/openai-in-talks-to-back-zeloof-and-chip-legend-kellers-startup-at-100-million-valuation/amp/ - Jim Keller's new chip company, which OpenAI is in talks to invest in, aims to build a 2 terabyte RAM AI accelerator. The message also notes the company has a Bangalore office.
- https://github.com/ravenscroftj/turbopilot: The user tried running GPT4ALL locally and found it to work well on their 8gb ram laptop. They mention that it's good for text generation and the onboarding is simple, but it's not strong with code yet.
- https://github.com/huggingface/diffusers/releases/tag/v0.15.0 - This link is shared in the context of a humorous comment about the top highlight while selling the contract renewal of the data bricks platform. The message in the same link as the URL is related to the link.
- https://twitter.com/ashe_cs/status/1646543644038397952?s=46&t=0NBX3C3Uma-Su4_rjA3OMA: Message thanking someone for hosting a mixer and expressing delight in meeting people in the Bangalore AI space. Also includes a request to collaborate and a DM sent to the recipient.
- Cerebras is not planning to be consumer focused chips, while Sambanova is building FPGA based chips for AI. (https://www.linkedin.com/posts/harshsinghal_under40-activity-7052341005978615809-EaUX?utm_source=share&utm_medium=member_android)