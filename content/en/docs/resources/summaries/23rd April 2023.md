---
contributors:
- Nirant Kasliwal
date: '2023-04-23 00:00:00+05:30'
description: An assortment of AI-focused conversations covering topics such as Anthropics
  pitch deck, RLHF in instruct models, political deepfakes, AI courses and resources,
  ControlNet Inpaint guidelines, asymmetric vector embeddings, GenAI hiring, tokenization
  and word embeddings, ControlNet image generation, and open domain Q&A and retrieval
  algorithms.
draft: false
excerpt: An assortment of AI-focused conversations covering topics such as Anthropics
  pitch deck, RLHF in instruct models, political deepfakes, AI courses and resources,
  ControlNet Inpaint guidelines, asymmetric vector embeddings, GenAI hiring, tokenization
  and word embeddings, ControlNet image generation, and open domain Q&A and retrieval
  algorithms.
featured_image: ''
images: []
lastmod: '2023-04-23 00:00:00+05:30'
tags:
- daily_summary
title: 'Diverse AI Topics: Pitch Decks, Education, Employment, and Applications'
toc: true
weight: 50
---

## Anthropics pitch deck
- Does anyone have access to Anthropics pitch deck?

## RLHF for instruct models
- OpenAI's John Schulman gave an interesting talk at Berkeley last week on why RLHF was needed to get the instruct models to behave nicely.

## Deepfakes and audio synthesis
- First instance of an Indian politician referring to deepfakes / audio synthesis?

## AI courses and resources
- course.fast.ai for being able to make sense of all of this — even as it changes in 2-3 months and we add VQA (Vision) to mainstream OpenAI APIs
- Lot of new work should come from STT and TTS side, including performance improvements like Whisper-JAX in the coming 4-6 month and more important, voice cloning, avatars and the like. They should have their own "Lensa moment" as such if someone markets it well.
- if i had to recommend a course to cover the NLP hands-on with theory - https://www.udemy.com/course/nlp-with-transformers/
- You can still pretty affordable (about $2/mo) instances on Fly.io
- If there's anyone interested, Mckay Wrigley is starting a course on Replit on AI dev. The advanced stuff is coming soon but here's the day 0 course. https://twitter.com/mckaywrigley/status/1649492404943323136

## ControlNet Inpaint guidelines
- controlnet Inpaint guidelines for A1111. https://github.com/Mikubill/sd-webui-controlnet/issues/968 [PHONE REMOVED] you can try out with this and let me know how it is working for you.

## Asymmetric vector embeddings for directional similarity search
- From the author of controlnet repo: Hi everyone! Shreyas here, I’m a product designer at Clari working on revGPT, a chat interface to get on top of everything happening with sales in an organisation ( and a few personal projects:) ). I saw this tweet by the guy who made BabyAGI, with a new approach to vector search & embeddings: https://twitter.com/yoheinakajima/status/1650049673770725378?s=46&t=WT1iAtjftW-5_e62F8FZTg
- https://yoheinakajima.com/asymmetrix-asymmetric-vector-embeddings-for-directional-similarity-search/

## Hiring for GenAI
- what are some places to hire tech folks interested in GenAI? understanding of how GenAI works and the nuances of embeddings, text processing
- This WhatsApp group 🙈
- I hear OpenAI has some decent folks
- should have a job board :)
- How about a board that takes natural language input from job seekers and start-ups and matches them? Does something like this exist? Shouldn't be hard to build one.
- Looking to hire folks as well - full time or part time! Job board would be ideal

## Tokenization and word embeddings
- I knew tokens used for non English languages is different but looking at the OpenAI bills, it gave me a shock. Some Asian languages take a lot more - is there a comparsion somewhere?
- I haven’t come across a lang2lang comparison. But openAi has a tokenizer you can use to estimate tokens and build a comparison set.
- For tokenization and word embeddings to reduce cost, you may like to use Sentence Transformers / [ something like that ] and pass the Embeddings to OpenAI for completion
- They’re also building foundation models
- [PHONE REMOVED] has built a wrapper around openai tiktoken to count tokens in a file or text -

## Image generation with ControlNet
- I was trying to generate an image of "a key ring with the OpenAI logo on it"
- u can use ControlNet canny model https://huggingface.co/spaces/hysts/ControlNet, just start with the openai logo, select the canny model and give the promptt
- This was controlnet only btw, both canny and hed boundary worked well (you can change that in settings)

## Open domain Q&A and retrieval algorithms
- Anyone working on open domain Q&A type problems or ones which make use of retreievers/dense embeddings?
- Yes I am. My product helps businesses set this up for internal function (esp. customer service and customer success).
- Oh cool, can you share what kind of models and retrieval algorithms you are using?

## Links
The description and link can be mismatched because of extraction errors.

- https://www.udemy.com/course/nlp-with-transformers/ - recommended course for NLP hands-on with theory, mentioned in a message about a good learning path that skips LLM theory and the usefulness of deploying applications on Heroku.
- https://twitter.com/mckaywrigley/status/1649492404943323136 - McKay Wrigley is starting a course on Replit on AI dev and the day 0 course is available. The message also mentions that affordable instances on Fly.io are available for about $2/mo.
- GitHub link for controlnet Inpaint guidelines for A1111: https://github.com/Mikubill/sd-webui-controlnet/issues/968. The author of the repo also provides a phone number for testing purposes.
- https://twitter.com/yoheinakajima/status/1650049673770725378?s=46&t=WT1iAtjftW-5_e62F8FZTg - A tweet by the creator of BabyAGI discussing a new approach to vector search and embeddings, created with ChatGPT.
- https://yoheinakajima.com/asymmetrix-asymmetric-vector-embeddings-for-directional-similarity-search/ - Nakajima has been tinkering with AGI for long, indicating that the given URL is not fluff and has actual basis.
- https://huggingface.co/spaces/hysts/ControlNet (used for generating an image of a key ring with the OpenAI logo on it)