---
contributors:
- Nirant Kasliwal
date: '2020-08-29 00:09:00+05:30'
description: What we share in our ML/NLP round
draft: false
excerpt: What we share in our ML/NLP round
images: []
lastmod: '2020-08-29 00:09:00+05:30'
show_reading_time: true
tags:
- career
- machine learning
- verloop
- tech
title: Verloop NLP Interview Prep Guide
toc: true
weight: 50
---

Update, September 2021: This guide is a little outdated, but not obsolete. I no longer work at Verloop.io. 

# Preparation Guide

I've been an early Machine Learning Engineer at [Verloop.io](https://verloop.io) for almost 1.5 years, primarily working on NLP problems and now more in an Engineering Manager-ish role. 

This is the guide which I sometimes send to our candidates after they submit the Programming Challenge. If a candidate has relevant open source code sample, specially to other repositories we may choose to waive off the Programming Challenge completely. 

I originally wrote this to give a chance to folks coming from non-NLP background to get a sense of the problem space a little better. I'd hoped that it'd absolve smart people of the assumption that Churn, Text Generation and Image Segmentation can be all solve with the same idea-kit, but no luck. 

I hope this is most useful to candidate interviewing for ML roles in companies similar to us in terms of size, scale and challenges. This is also useful to:

* Early career folks - typically less than 2 years of NLP experience
* Folks coming from Computer Vision/Tabular Data/Classical ML background

# The Role 

Machine Learning Engineers at Verloop develop technologies that influence how users interact, engage and feel about chat and customer service. As a/an MLE, you will specialize in supervised/unsupervised learning and apply techniques to various problems, mostly dealing with high volume natural language processing applications.

At Verloop, the same team of engineers owns the entire stack from research to production. This means that the following roles HAVE NOT EXISTED at Verloop:

1. Data Scientist: 
    - Does: Data Analytics, Exploration, Model A/B Testing and Data Modeling
    - Tools: Everything from Data Viz to Excel, Pandas, spaCy and Scikit-Learn

2. Data Engineer: 
    - Does: Builds ata pipelines, storage, data version control, monitoring
    - Tools: Kafka, Airflow etc.

3. ML Researcher: 
    - Does: Trains forward looking, NOT production ready models. Focussed on experimentation
    - Tools: huggingface/transformers, spaCy, flair (by Zolando Research)

All of the above is done by MLE at Verloop. Every engineer is expected to build a strong suite in one or more of the above roles, while maintaining a high minimum at the others. 

Verloop MLE often contribute to adjacent/overlapping challenges such as DevOps for Machine Learning aka ML Ops. These are often problems in model serving, automated deployment, data versioning, model monitoring, alerting and other parts of developer tooling.

# Programming Tips

Write your code (unless otherwise stated) as if you are deploying this code to production. So anything which you'd want to pay attention to for your production code should ideally be there. 

That said, here are some things which we pay attention to in your code sample: 

## API & Object Oriented Design
- Almost always useful to separate views from models
- If you are implementing REST, do REST properly
- Keeping common sense names for endpoints make everyones life easier

See [12 Factor App](https://12factor.net) for the gold standard on App Dev practices, here we select only a few and explain what we pay attention to

## Code Readability, Style & Design
- Use tools like `isort` in Python to neatly organize your imports. Avoid using `fastai` style imports of `from X import *`
- Docstrings for functions, inline comments where applicable to explain the "why" or "how" - but not what
- We like the style to be consistent. E.g. in case of Python, following PEP8 or Google Styleguide will improve your code readability by a lot 
- In Python, type hints will make your and our life easier when we have to debug something

## Developer Hygiene
- Use a `requirements.txt`, conda `environment.yml` or Dockerfile to declare your dependencies
- Write tests!
- Use logging. Generously with levels. But not so much that it slows your production performance. 
- README with comments, notes, assumptions and what the code is doing

# Machine Learning Tips

In contrast to interview processes which go wide, covering everything from Probability, Statistics, Linear Algebra to Deep Learning and everything in between - we go deep on primarily one aspect: Applied Natural Language Processing. We operate close to Research, occassionally doing research even. 

These are supposed to be indicative/descriptive of the technical skill we desire. These are not prescriptive i.e. you do not have to do the course to clear our interviews. 

We just have seen everyone with equivalent skill as these courses do well in our interview process.

## Deep Learning
* Basics for Beginners: [FastAI Part 1 & 2](https://course.fast.ai)
    * Trivia: 2 out of our team of 6 have been fast.ai International Fellows. 

### Natural Language Processing Deep Dive

* [NLP: Code First Introduction](https://www.fast.ai/2019/07/08/fastai-nlp/) by FastAI’s Dr. Rachel Thomas

* NLP with Deep Learning: [cs224n by Stanford](https://web.stanford.edu/class/cs224n/)
    * For a SDE 2 role, having Deep Learning skills equivalent to this course is necessary but not sufficient

* (Hard Mode) Yandex Data School’s [NLP Course](https://github.com/yandexdataschool/nlp_course)

# General Interview Tips

**Think Out Loud** -- We want to understand how you think, so explain your thought process and decision making throughout the interview. 

Remember we’re not evaluating your technical ability alone, but also how you solve problems.

**Clarify** -- Many questions will be deliberately open-ended to provide insight into what parts and information you value within the technological puzzle.

We’re looking to see how you engage with the problem and your primary method for solving it. 

Be sure to talk through your thought process and feel free to ask specific questions if you need clarification.

**Do your Homework** -- The primary reason that this is a Take Home Challenge plus a discussion is that we don't want to evaluate your ability to think on your feet. 

That said, if you come to the interview without enough homework on your own submission and question -- you'll be put in a place where a lot of thinking will in fact be on your feet.

# Machine Learning Interview Technical Prep

* At least one interview will be focused on your expertise within Machine Learning. General knowledge of the field and its main concepts should be demonstrated throughout the interview, such as supervised learning, unsupervised learning, overfitting, boosting, and regularization.

* Experience with common learning paradigms such as decision trees, k-means, LSTMs and understanding of how to apply those techniques to various problems is important.

# How to Prepare?

* Get extremely comfortable with writing code to do Machine Learning (and by extension, Deep Learning). This means knowing what to google, what libraries to use and so on is very valuable.

* Be mentally prepared to talk about your approaches and results. This is effectively a defence of your work. Help us understand why you made certain decisions, choices, and what went in your head.

* Get comfortable working with real world text datasets, for instance multi-lingual datasets, code-mixed. Look for sample efficient learning methods and learn where these models fail or mislead.

# Things to Think About

* This round is case-study driven. We value initiative and experimentation speed+quality over success. This means that even if you try an approach, which does not work for some reason - show us the work that you did: We’d love to learn what you tried.

* Ask yourself why would they have selected this problem for the challenge? What are some basics in this domain I should know about?

* What is the highest level of accuracy that others have achieved with this dataset or similar problems/datasets?

* What types of visualizations will help me grasp the nature of the problem/data?

* Which modelling techniques are good at capturing the types of relationships I see in this data?

* What are some of the weaknesses of the model and how can the model be improved with additional work?

* How do I measure performance? Does it help to have confidence values against the prediction?

* What is latency and compute needs for this model?

---

This document is inspired by similar documents by Google Inc. I borrowed from the best when relevant.