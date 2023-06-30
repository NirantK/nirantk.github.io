+++
title =  "Wide-ranging Tech Discussion: React, AI, Open-Source, and More"
date = 2023-04-15T00:00:00+05:30
tags = ["daily_summary"]
featured_image = ""
description = "Explore a diverse range of topics including React development, controlnet inpainting, Azure Cognitive Search, GPT-5 rumors, LLM output time reduction, bionic reading techniques, open-source project funding, AI in crime detection, and a comparison of AWS CodeWhisperer and GitHub Copilot."
toc = true
+++

React Development:
- Someone is looking for React developers for a paid weekend project
- They ask for leads to be DM'd to them

Controlnet Inpainting:
- Someone asks if anyone has gotten the latest controlnet v1-1 nightly release models working with inpainting
- They mention that they have gotten the models working with multi controlnet, but not for inpainting yet

Azure Cognitive Search:
- Someone brings up MSFT's recommendation to use Azure Cognitive Search with Azure OpenAI for enterprise document search in Azure
- They mention that it may be costly and ask for thoughts from the community on production level deployments
- Another person mentions the option of uploading document embeddings into a Vector DB and doing semantic search
- They share that they are currently using this method with Pinecone and have 10681 vectors in their DB

GPT-5:
- Someone shares a link to an article about rumors of OpenAI's GPT-5
- Another person jokes that they have a friend called GPT-4 who is fairly reasonably priced
- Someone else mentions that they used Copilot for a project and it helped with a good chunk of front end code

LLM Output Time:
- Someone asks if anyone has figured out good ways to reduce time in getting output from an LLM

Bionic Reading Technique:
- Someone asks if anyone knows if there's a mathematical formula to calculate highlighted words in bionic reading technique
- Another person shares a link to a Twitter thread that may be helpful

Open-Source Projects:
- Someone asks why open-source projects like Langchain raise money if their value proposition is the code
- Others suggest that it may be for managed services, enterprise support, or self-hosted and cloud-hosted strategies
- They mention examples like OpenSUSE, RedHat, and dbt cloud

AI for Crime Detection:
- Someone asks if anyone is familiar with AI for crime detection, specifically for loud noises

AWS CodeWhisperer:
- Someone shares that AWS has released their GitHub Copilot knockoff for free and it seems reasonably good
- They share a link to an article about how Accenture is using it to improve developer productivity
- Another person shares a link to a blog post comparing CodeWhisperer and Copilot

## Links
The description and link can be mismatched because of extraction errors.

- https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.ipynb: The message in the same link as the URL is related to the link, but newlines may or may not be related. The message is about getting the latest controlnet v1-1 nightly release models working with inpainting and asking for inputs on how that would fit with multi controlnet.
- https://twitter.com/karpathy/status/1647025230546886658?t=zQ2IYIjiKMNc0mUHUdqlBw&s=19 - Twitter discussion about the size of the DB and choice of Vector DB, with a mention of 10681 vectors and Pinecone.
- https://www.theverge.com/2023/4/14/23683084/openai-gpt-5-rumors-training-sam-altman: Discussion about training a classifier on top of embeddings and explicitly labeling for retrieval, and its similarity to the old world of building classifiers through KNN, SVM, DNN, CNN, etc. Also mentions that this method works well when there aren't too many data refreshes/updates.
- https://twitter.com/pratyush_r8/status/1647104801950552064 - A message expressing gratitude for finding something after searching for 2-3 days, followed by a comment on the concept of bionic reading.
- Redhat has reached $1B, as mentioned in a tweet by Anoushka Vaswani and a LinkedIn post. 
  - https://twitter.com/anoushkavaswani/status/1646976994637406211?t=qixyvkorGoWv78hRdUJPaQ&s=19 
  - https://www.linkedin.com/feed/update/urn:li:activity:7053046289256632320
- https://twitter.com/anoushkavaswani/status/1646976994637406211?t=qixyvkorGoWv78hRdUJPaQ&s=19 - A tweet by Anoushka Vaswani with a message related to the link.
- https://www.linkedin.com/feed/update/urn:li:activity:7053046289256632320 - A LinkedIn post with no context provided.
- https://twitter.com/foyerwork/status/1647282584907579393?s=20 - A tweet by Foyerwork with no context provided.
- https://aws.amazon.com/codewhisperer/ - AWS has released their GitHub Copilot knockoff for free. It seems reasonably good although I don't have a direct comparison with Copilot.
- https://aws.amazon.com/codewhisperer/ - AWS has released their GitHub Copilot knockoff for free. It seems reasonably good although I don't have a direct comparison with Copilot.
- https://aws.amazon.com/codewhisperer/ - AWS has released their GitHub Copilot knockoff for free. It seems reasonably good although I don't have a direct comparison with Copilot.
- The following URLs provide information about Amazon CodeWhisperer, a tool used to improve developer productivity, and its comparison with GitHub Copilot: 
  - https://aws.amazon.com/blogs/machine-learning/how-accenture-is-using-amazon-codewhisperer-to-improve-developer-productivity/ 
  - https://blog.lucas-simon.com/amazon-codewhisperer-vs-github-copilot#heading-final-thoughts