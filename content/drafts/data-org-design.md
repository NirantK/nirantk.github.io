+++
title = "Data Science Org Designs"
description = ""
date = 2020-09-15T00:09:00+05:30
tags = ["career", "verloop", "machine learning", "tech"]
toc = true
draft = true
show_reading_time = true
+++

# Data Science Org Design
 
While there is plenty of good advice on [making ML work](https://www.shreya-shankar.com/making-ml-work/) and [making a career as a Data Scientist](https://medium.com/@rchang/advice-for-new-and-junior-data-scientists-2ab02396cf5b) -  I think very little discussion happens on the organization design for Data Science itself.

> Organization Design is determined by these 3 broad categories:
>
> 1. Software Engineer vs Research: To what extent is the Machine Learning team responsible for building or integrating with software? How important are Software Engineering skills on the team?
>
> 2. Data Ownership: How much control does the Machine Learning team have over data collection, warehousing, labeling, and pipelining?
>
> 3. Model Ownership: Is the Machine Learning team responsible for deploying models into production? Who maintains the deployed models?
>
> --- Josh Tobin at [Full Stack Deep Learning](https://course.fullstackdeeplearning.com/course-content/ml-teams/team-structure)

It's harder for ML/DS teams to succeed than your typical product and platform engineering functions. This is because:

* High Skill Transfer from one role to another, which makes talent _both_: liquid and expensive
* Management is unclear on what does "success" look like for ML as a function?

These were the two key pitfalls which I wanted to solve for when designing the ML team and how it sits in the larger org. The most well known ways in which companies organise Machine Learning Teams are these:

## 1. Research & Development Labs

Of these, a R&D Lab is ideal for most well capitalized businesses because it enables them to attract talent, which can in turn work on long term business/tech challenges. 

Uber AI Labs, Google AI Research, DeepMind, and FAIR are some examples from the top of my head. Microsoft Research - with contributions almost all of Computer Science, should probably be the gold standard for this. I have personally spent some time working in such an org design [ATL] 

The limitation with this org design is that R&D teams don't own inputs (data) and outputs (model performance in production).  This makes this org design all but useless for a pre/near Product Market Fit startup.

## 2. Embedded within Business & Product Teams

By far the most popular org design in Indian startups, is a Data Scientist is embedded into an engineering team along with an analyst which is then assigned to a business or product team. From the top of my head, this is how some of the best Data Science teams like AirBnb, Flipkart, and Facebook organize their ML teams.

I strongly considered this org design, but ultimately opted against this because it would not play to my strengths at all. Specifically, I expected these challenges:

1. Hard to maintain uniform data standards and practices across the org
2. Management Complexity, in terms of the ever increasing breadth of problems across different features

## 3. Data Science Consultant

Small business which themselves had a services arm or revenue love this.

Business or product teams bring specific problems to a data science lead, who then scopes out a plan, defines a succsess criteria and hands it off to a Data Scientist within the team. 

There are so many understated but commonly known limitations of this, which ultimately hurt the gross margins of a SaaS business. This was dropped fairly early as a candidate for that specific reason.

## 4. [Near Future] Productized Data Science Team

When I studied more modern teams, especially in B2B SaaS or eCommerce from outside, I _felt_ they made a small but important change in this model: Instead of a matrix where the Data Scientist was ultimately responsible to their own unit and nothing else, they had a central Data Science function to which all Data Scientists reported. 

Some teams created a new, "Chief Data Scientist" or "VP, Machine Learning" designations to reflect this increased autonomy and status within the org. Notice, that this is quite similar to how some Design teams are organized.

While I had not worked under this org design, I had interned at a place which was small (10-50 employees) and I could understand the limitations of this org design when I was told the same. 

The most common warning was the amount of context which any lead/manager Data Science had to keep beyond a certain project count within the company. I expect that **Verloop ML Team will evolve into this** over the next 12-24 months. I'm estimating this on the basis of the problem complexity and the head count needed  engineering and data science teams both  

## 5. [Verloop Today] Full Stack Data Science

This is the **org design at Verloop ML today**. The defining characteristic of this org design is that the every ML person does things end to end - there is no division of labour. 

There is a brilliant explanation on this from StitchFix: https://multithreaded.stitchfix.com/blog/2019/03/11/FullStackDS-Generalists/ 

> The goal of data science is not to execute. Rather, the goal is to learn and develop new business capabilities. … There are no blueprints; these are new capabilities with inherent uncertainty. … All the elements you’ll need must be learned through experimentation, trial and error, and iteration. – Eric Colson

As Eric calls out, Data Science, unlike say Platform Engineering functions - is not a pure "execution" function. It's an iteration and discovery function of the organisation. In business terms, you might call this Market Research, but where techonology is applied to develop new capabilities.

This full cycle development [seems to be endorsed](https://eugeneyan.com/writing/end-to-end-data-science/) by Netflix Tech officially and Data Science folks at Lazada as well. 

The other quirk in org design is that the ML function reports directly to the CEO. The CEO directly brings the business context and drives quick wins. The ML Lead needs to negotiate continuously on organisational goals, constantly query for added context, and makes long term bets.

Part of the ML Product Manager role also got absorbed into what I've been doing as a Machine Learning Manager because we did not have a full time Product Manager in the company for more than 6 months:
- Does: Work with ML team, data owners to prioritize, execute and spec out projects
- Tools: Jupyter for PoC, JIRA, Slack, Google Docs for Comms

Another advantage of this org design is that it makes attracting talent easier by giving them quite high autonomy. The team also owns model performance and deployment. 

The deployment ownership is made possible by a ML System Design decision as well. The strong adherence to multi-tenant models instead of client specific models.

There are so many reasons that this org design is a bad design that it'd take us an entire night to spell it out. Since the team can influence everything (to varying degrees) from engineering to front end changes - the blast radius of what this team can screw up or drastically improve is quite large. 
