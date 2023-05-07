+++
title =  "Exploring Cloud GPUs, Model Training, and Privacy in Enterprises"
date = 2023-04-22T00:00:00+05:30
tags = ["daily_summary"]
featured_image = ""
description = "A comprehensive discussion on leveraging cloud GPUs for model training, comparing popular platforms like Google Colab and Kaggle Notebooks, and addressing privacy concerns when implementing chatGPT in enterprise settings. The conversation also includes valuable tips, resources, and tools such as Qblocks.cloud and event decks."
toc = true
+++

Cloud GPUs:
- Discussion on using GPUs for training models
- Google Colab and Kaggle Notebooks suggested as options
- Comparison table for cloud GPUs shared
- Cheapest option for model fine tuning mentioned as rtx5000 on runpod.io
- Pricing of cloud GPUs discussed, including economies of scale and interest rates on capital investment
- Vast.ai mentioned as a cloud GPU rental option

Model training:
- Tips shared for reducing container image size when using Sentence Transformers for word embeddings
- Question asked about enabling multiple checkpoints in automatic1111 while fine tuning a model using dreambooth

Privacy concerns:
- Discussion on privacy concerns when using chatGPT in enterprises
- Use cases where privacy is important and chatGPT may be necessary discussed
- GPT-4 mentioned as a potential solution for privacy concerns, with McKinsey as a client
- Best way to figure out which model will work for a particular use case asked

Resources:
- Link shared for using Google Colab with VS Code
- Qblocks.cloud suggested as a cloud GPU option
- Decks from the event mentioned as available for attendees

## Links
The description and link can be mismatched because of extraction errors.

- https://colab.research.google.com/drive/1YORPWx4okIHXnjW7MSAidXN29mPVNT7F?usp=sharing: Link to a Google Colab notebook where one can train/run models using a free Tesla T4 from Google.
- https://fullstackdeeplearning.com/cloud-gpus/ - A comparison table for cloud GPUs is suggested as useful for downloading lots of data and doing it on a recurring basis. The message also mentions trying Google Colab despite it not being suitable for the task.
- https://www.freecodecamp.org/news/how-to-use-google-colab-with-vs-code/ : The article discusses how to use ngrok and vscode with hosted notebooks to code with scripts and use GPU resources for free. It also mentions that this method used to work with Colab but seems to have been banned.
- https://vast.ai/ - The message asks for reviews on this cloud GPU rental platform.
- URL: N/A (not provided in the given context)
- Context: The message in the given link provides information on how to reduce the size of a container image when using Sentence Transformers for word embeddings by using the Torch CPU image instead of the Torch GPU image. The Docker file command for installing Torch CPU is also provided.
- https://www.qblocks.cloud/ is run by a friend and is recommended for use. The message also offers to put the reader in touch with the founder if needed.