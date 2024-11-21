---
contributors:
- Nirant Kasliwal
date: '2020-11-15 23:29:18+05:30'
description: Making the best of your Paper Reading Time
draft: false
excerpt: Making the best of your Paper Reading Time
featured_image: images/paper-background.jpg
images: []
lastmod: '2020-11-15 23:29:18+05:30'
tags:
- machine-learning
- tech
title: How to Read a Deep Learning Paper
toc: true
weight: 50
---

## Who is this for? 
Practitioners who are looking to level up their game in Deep Learning

## Why Do We Need Instructions on How to Read a Deep Learning Paper?

Quantity: There are more papers than we can humanly read even within our own niche. For instance, consider EMNLP - which is arguably the most popular Natural Language Processing conference selects more than 2K papers across a variety of topics. And NLP is just one area!

Some people read academic papers like they read novels: Open link. Read the text. Scroll Down. Finish. Close tab. Some people read like a math book with problems, obsessing over every detail. Their Zotero or hypothes.is accounts are filled with annotations which they are probably never going to revisit in their lifetimes. Others skim but without a coherent structure. All of these are valid ways to read a paper. 

Here, I am trying to distill and form a better structure for myself to improve the return on my very limited _energy_.

# Four Types of Reading
- In his cult classic book, "How to Read a Book", Mortimer J Adler explains his Four Types of Reading, mainly keeping a non-fiction book in mind. I am adapting these to the context of Deep Learning paper for us.

## Elementary 
This is the point where you're when you finish a 101 course in Machine Learning. You know the key terms and vocabulary e.g. convergence, loss functions and optimizers. You can understand what the words in the paper mean and read them, maybe follow the narrative, but not much more. Since you're reading this blog, I assume you are already reading at a level above this.

## Inspectional

This is basically skimming. You look at the headings, read the beginning and end of some sections, some of the statements in bold. The intent is to get a _fast & superficial_ sense of what the author is trying to say.

### Intelligently Skimming

- The first type of inspectional reading is systematic skimming, which you can easily put into practice today. This is most useful when you're reading within a topic you've some familiarity with. For instance, within most topics around intent classification in dialogue systems -- this is how I would read. Here’s how you start:

- **Read the title and abstract.** This might seem obvious, but authors do put in the effort to compress their key ideas, findings or contributions in these places. This effect is even more amplified since these are the most important fields on arXiv. If you spend a minute of full attention, you should get a feel for the intent and scope of the work. This will not only prime you for what you might be reading next, but also mentally map this work to ideas which you might be already familiar with.

- **Skim the Section Headings**, which will give you a feel for organization of the paper. Is the paper emphasizing datasets? A new architecture? Or an empirical work which is basically throwing compute and sharing that "See, It works!". I am always a little annoyed when I am discussing a paper when it turns out that the reader has not even got the intent of why the paper sections are organized in a specific way. Obviously, many conferences have specific templates which make it even easier to discover the structure which the authors actually wanted you to pay attention to.  

- **Get a sense of the context** This means skimming the Related Work section. The intent isn't to read every paper or idea mentioned in this section, but only the topics mentioned here. This will help you get a sense of the jargon used, the variety of topics and what the authors consider adjacent problems/areas. 

- **Read the Conclusion.** Authors generally do a good job summarizing their work in the last few pages. This where they sum up what they think is most important about their work. Just jump to this first.

> 💡Pro Tip💡: **Check out their interview, podcast, oral presentation, or Twitter thread or poster.** While this has nothing to do with the actual paper, these can be a great way to get the gist of a paper in 30 minutes or so. Authors do so much promotion now that it's relatively easy to find interviews. Many selected papers have oral presentations. And of course, they use the best examples from the book in these interviews.

### Superficial Reading
This is most useful when you’re reading outside your usual comfort zone. 
Here is the key idea: ^^Read without stopping^^

If you read a lot of papers, you will find that there are some things that you don’t understand. If you stop and try to figure out what it means, it will take a long time to finish the paper. But if you keep on reading, the next thing that happens will help explain what the first thing meant. And so on.

You might get very little of what is being said in the first pass and that's fine. You now know the lay of the land, and when you make a second pass -- you can connect the dots much better and faster.

## Analytical Reading

This is where you really dive into a text. You read slowly and closely, you take notes, you look up words or references you don’t understand, and you try to get into the author’s head in order to be able to really get what’s being said.

**Don't Google Too Early**. If there is a math formula, concept, or word you don’t know, first look at the context to try to discern its meaning. See if the author explains what happens when or why they used it. Warm up and use your brain to get started. If it’s something you simply can’t get past, or the word is clearly too important for you to glance over, then check the citations. If even that isn't enough, then finally Google it. The main point is that you can use the tools around you, but don’t lean on them. Let your brain work a little bit before letting Google work for you.

**Get a sense of the author's background**. Look at what institutions do they mention. Are they from academia? An applied AI lab like Apple or GoogleAI? Or an academic lab, sponsored by industry like DeepMind/FAIR? Two examples of how it can inform your reading:

        1. There are some companies/labs where a person has to write a certain number of papers every year in order to get promoted (or even retain their jobs) -- they typically have narrow ideas which solve a specific problem incredibly well, but are mostly not adaptable to another domain or context.
        2. Teams and labs have distinct flavors and sometimes work on specific themes. This can help you quickly get a sense of whether the paper is part of a longer series and see the papers before and after the one you're reading.  

### Answer the 4 Key Questions
- This, Adler says, is actually the key to analytical reading. To be able to answer these questions shows that you have at least some understanding of the paper and what you've read. If you can’t answer them, you probably haven’t quite paid attention well enough. I also find it personally helpful that you should actually write (or type) these answers out. Consider it to be like a book journal. It’ll stay with you and become much more ingrained than if you just answer them in your head. 
    
**What is the paper about, as a whole?** This is essentially the abstract or conclusion. You could cheat, but that's not going to be very helpful. Instead use your own words and write a the highlights of what you can recall about the paper. See if you can connect it to the wider knowledge base which you've read in the past.

**What is being said in detail, and how?** This is where you start to dig a little deeper. Briefly go back and skim through the paper, jogging your memory of the key points, formulae, section headings, graphs and tables with results. With most papers, outlining is pretty straightforward since the section headings do bulk of the job for you. For short papers, this could be as short as 5-10 lines. Pay special attention to what datasets, experiment configurations and ablation results if they're mentioned.

**Is the paper true - in whole or in part?** If you're reading within your own comfort zone, you'll begin to see by now the scenarios/tasks/areas where the paper falls short. For instance, if you're reading up on Long Range Transformers -- based on your knowledge of pre-trained Transformer models like BERT, RoBERTa or T5, you should expect them do better at summarization and Q&A tasks than these. If the paper falls short, you can quickly jot that down as a question to ask, ponder upon or experiment yourself. This is true for both peer-reviewed and pre-print papers - they can often have glaring errors and mistakes which you might notice.  

**So what? What’s the significance?** Most papers are _incremental_ in their contribution to the world. This is not necessarily a bad thing. As long as the paper made you see the field or area in a new light, or even a new nugget of knowledge - it was helpful. We should aim for reading papers which at-least give us something valuable in either perspective, knowledge (e.g. empirical facts) or methods. This is by far the most useful question to ask since it helps contextualize the contributions of the author against your own _personal context, understanding and knowledge_.
        
The core idea here is that reading is not a passive process. You have to actively engage with the text and think about what you read. It's natural to just scan over the text without actually retaining anything. To counteract this, you need to make a conscious effort to stop and think about what the author is saying. A good way of doing this is to write down a list of questions about what the author says. This will force you to stop and think about the content. When answering these questions, you need to write them in your own words. This means that you can't just parrot the authors words back at them. Instead, you need to rephrase the question in your own words. This will help you engage with the ideas in a more meaningful way.

> 💡Pro Tip💡: [Generate questions](https://www.wikiwand.com/en/Inquiry-based_learning) about the content of the reading. For example, convert headings and sub-headings into questions, and then look for answers in the content of the text. Other more general questions may also be formulated:
>    - _What is this paper about?_
>    - _What question is this section trying to answer?_
>    - _How does this information help me?_

    
**Optional, critique and share your thoughts with others.** This step is dead last. Only after having read the entire paper, or sets of papers, and thoughtfully answering the 4 Key Questions can you critique or have meaningful discussions about the paper.
    - For starters, a reasonable critique asks more questions ("Did they assume X?", "What would happen if I replaced method M1 with M3?") than it makes verdicts ("The paper is amazing", "This is stupid").
    - The second point is to fight the temptation to write a paper summary instead of a critique. That's the fad these days but isn't quite meaningful enough. You writing a measly, annoying Medium blog might feel like an achievement to yourself (thanks to cheap applause) but doesn't improve your understanding as much as writing a critique will.
            - Also, you don't have to take everything that the authors claim as God's Gospel. Having a disagreement is completely fine and valid. But give them the benefit of doubt and ask questions instead of making assumptions. It goes without saying, that you don't have to disagree or agree with every part of the paper. You can freely completely love one part and ignore the rest. There is no need (or advantage) to have an opinion about everything.

> 💡Pro Tip💡: You can use the Question Generation idea even during "Intelligently Skimming", especially for topics where you're comfortable. This will save you a lot of time and energy during Analytical Reading.

**Syntopical** — This is mostly used by researchers and professors. It’s where you read multiple papers on a single subject and form a thesis or original thought by comparing and contrasting various other authors’ thoughts. This is time and research intensive, and it’s not likely that you’ll do this type of reading very much, unless your day job is paying you to read and write papers. I do not have the relevant expertise to help you with this. 

## To quickly recap:

- Use Inspectional Reading when you're first reading a paper
- Use Analytics Reading and Answer the 4 questions when you're looking to get a deeper, better gist of the paper
    
### Four Questions You Should Be Able to Answer ###
- What is this book about?
- What is being said in detail, and how?
- Is this paper true in whole or in part?
- So what?

## Resources
- [Art of Manliness](https://www.artofmanliness.com/articles/how-to-read-a-book/)
- [Farnam Street](https://fs.blog/how-to-read-a-book/)


Thanks for Gokula Krishnan and Pratik Bhavasar for reviewing early versions of this. 