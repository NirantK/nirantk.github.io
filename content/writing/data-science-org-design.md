+++
title = "Data Science Org Design for Startups"
description = "" 
date = 2021-08-02T00:09:00+05:30
tags = ["career", "machine learning", "tech"] 
toc = true draft = true 
show_reading_time = true
image = "/images/data-science-org-design.jpeg"
+++


# Data Science Org Design for Startups

While there is plenty of good advice on [making ML work](https://www.shreya-shankar.com/making-ml-work/) and [making a career as a Data Scientist](https://medium.com/@rchang/advice-for-new-and-junior-data-scientists-2ab02396cf5b) - I think very little discussion happens on the organization design for Data Science itself.

This blog will hopefully help folks not just build their team, but also understand the ecosystem from which they are hiring.

Organization Design is determined by these 3 broad categories:

> 1. Software Engineer vs Research: To what extent is the Machine Learning team responsible for building or integrating with software? How important are Software Engineering skills on the team?
> 2. Data Ownership: How much control does the Machine Learning team have over data collection, warehousing, labeling, and pipelining?
> 3. Model Ownership: Is the Machine Learning team responsible for deploying models into production? Who maintains the deployed models?

> --- Josh Tobin at [Full Stack Deep Learning](https://course.fullstackdeeplearning.com/course-content/ml-teams/team-structure)

It's harder for ML/DS teams to succeed than your typical product and platform engineering functions in startups. This is because:

> * Good folks are hard to retain as their skills are highly transferable across multiple role (i.e., possibly high team attrition)
> * Management is unclear on what does "success" look like for ML as a function

These were the two key pitfalls which I wanted to solve for when designing the ML team and how it sits in the larger org. The most well known ways in which companies organise Machine Learning Teams are these:


## 1. Research & Development Labs

Of these, a R&D Lab is ideal for most well capitalized businesses because it enables them to attract talent, which can in turn work on long term business/tech challenges.

Uber AI Labs, Google AI Research, DeepMind, and FAIR are some examples from the top of my head. Microsoft Research - with contributions across almost all of Computer Science, should probably be the gold standard for this. I have personally spent some time working in such an org design[^1]

The limitation with this org design is that R&D teams don't own the pipeline to their work i.e. inputs (data) and outputs (model performance in production). To clarify, R&D teams in some cases do own data inputs in some places which does make the process more end to end - but often, the deployment in production is still not under them. This makes this org design _all but useless for a pre/near Product Market Fit startups_.


## 2. Embedded within Business & Product Teams

By far the most popular org design in Indian startups, is a Data Scientist is embedded into an engineering team along with an analyst which is then assigned to a business or product team. From the top of my head, this is how some of the best Data Science teams like AirBnb, Flipkart, and Facebook organize their ML teams. 

I strongly considered this org design, but ultimately opted against this because it would not play to my strengths at all. 

I expected these challenges:


1. Hard to maintain uniform data and engineering standards across the org

In this org structure, the primary, and sometimes only stakeholder for each Data person is their Product manager. There is a lot of work which is repeated e.g. data pipelines, cleaning, pre-processing. The larger organisations enforce some degree of uniformity via their Data Platforms or equivalent. In the early stages, this effort is not worth the decoupling speed.

2. Management Complexity, in terms of the ever increasing breadth of problems across different features

In the embedded space, each team could itself be working on a wide variety of “small” ML problems e.g. demand forecasting, text embedding, and sentiment analysis could be all worked on by a single Data Scientist. 

Since the Product Manager doesn’t have the technical skill to evaluate whether the solution approach was apt or not, it falls on the Data Science Manager to have a lot of breadth and assist several IC Data Scientists across multiple problems at the same time.


## 3. Data Science Consultant 

Small businesses which themselves had a services arm or revenue love this.

Business or product teams bring specific problems to a data science lead, who then scopes out a plan, defines a success criteria and hands it off to a Data Scientist or Machine Learning Engineer within the team.

There are so many understated but commonly known limitations of this: 

1. **Less Engaged Team**: Since the problem solving and implementation are separated - the engineer feels less creative and empowered to make changes and is less invested in getting the small details right. There is no single owner of the data or models, and thereby no single person responsible for the technical outcomes of the project.

2. **Communication overhead** in terms of energy and time both, which happens 2x: first, when the consultant understands the problem from the person on the team and second when the consultant transfers/shares the proposed solution. This is not just slow, it’s error-prone and expensive.

This makes completing feedback loops even harder, since no one person has all the necessary context which can be carried forward to the next project.  This was dropped fairly early as a candidate for that specific reason.


## 4. [Near Future] Productized Data Science Team

When I studied more modern teams, especially in B2B SaaS or eCommerce from outside, I _felt_ they made a small but important change in this model: Instead of a matrix where the Data Scientist was ultimately responsible to their own product/pod and nothing else, they had a central Data Science function to which all Data Scientists reported.

Some teams created a new, "Chief Data Scientist" or "VP, Machine Learning" designations to reflect this increased autonomy and status within the org. Notice that this is quite similar to how some Design teams are organized.

While I had not worked under this org design, I had interned at a place which was small (10-50 employees) and I could understand the limitations of this org design when I was told the same.

The most common warning was the amount of context which any lead/manager Data Science had to keep beyond a certain project count within the company. I expect that the Verloop.io ML Team will evolve into this over the next 12-24 months. I'm estimating this on the basis of the problem complexity and the headcount needed for engineering and data science teams both. If we can have ICs reporting to both the Product Manager and a Data Science org, the added management complexity would be worth it in the faster shipping speed via shared tooling and context. 


## 5. [Verloop Today] Full Stack Data Science

This is the org design at Verloop.io ML today. The defining characteristic of this org design is that  every ML person does things end to end - there is no division of labour.

There is a brilliant explanation on this from StitchFix: [https://multithreaded.stitchfix.com/blog/2019/03/11/FullStackDS-Generalists/](https://multithreaded.stitchfix.com/blog/2019/03/11/FullStackDS-Generalists/)

The goal of data science is not to execute. Rather, the goal is to learn and develop new business capabilities. … There are no blueprints; these are new capabilities with inherent uncertainty. … All the elements you’ll need must be learned through experimentation, trial and error, and iteration. – Eric Colson

As Eric calls out, Data Science, unlike say Platform Engineering functions - is not a pure "execution" function. It's an iteration and discovery function of the organisation. In business terms, you might call this Market Research, but where technology is applied to develop new capabilities.

This full cycle development [seems to be endorsed](https://eugeneyan.com/writing/end-to-end-data-science/) by Netflix Tech officially and Data Science folks at Lazada as well.


# Case Study: ML Org at Verloop.io

I hope the above gives you a sense of common data science team organisations. If you’ve seen them in the past, now we both have a shared vocabulary to talk about it. 

As a case study, let me share some of the operational things we had at Verloop.io. This was mostly as part of our 0 to 1 journey as a B2B SaaS product. 

These are not recommendations, but just how things shaped up in the early days. I hope this gives you a case study to concretely think about what we just discussed. 


1. ML function reported directly to the CEO for the longest time. The CEO directly brings the business context and drives quick wins. The ML Lead needs to negotiate continuously on organisational goals, constantly query for added context, and make long term bets.

Part of the ML Product Manager role also got absorbed into what I'd been doing as a Machine Learning Lead/Manager because we did not have a full time Product Manager in the company for more than 6 months.

2. Attracting young talent was easier by giving them quite high autonomy. The team also owns model performance and deployment.

The deployment ownership is made possible by a ML System Design decision as well. The strong adherence to multi-tenant models instead of client specific models.

3. Talent pool is smaller + retention is hard

We had a smaller talent pool for at least 2 reasons: A few data science candidates refused to join the team because they were not interested in engineering, and wanted to focus on modeling tasks exclusively. 

In some other cases, the conversation broke down because we couldn’t match their pay expectations. 

We managed to make our retention hard because of good intentions, but with bad outcomes: 

The engineering org in our early stages did a lot of ad hoc development in smaller, demo-driven sprint cycles. We assumed that separating ML from the rest of the engineering org would allow us to ship faster. It would also allow us to focus longer on one project, without being distracted by ad hoc tasks. This did work to a certain extent.

In hindsight, _this was a mistake_. It definitely empowered us to ship faster, but teammates felt isolated, and it was hard to complete the feedback loop with our end users via the Product Manager alone. Additionally, if we needed engineering’s help to ship something, they’d pick “their” work over integrating our shipped work. This slowed down our shipping pace itself over a longer duration. This in turn, hurt the morale of the team, and made retention much harder. 

I’d do this differently the next time around.

There are 3 things I’d do differently:

1. **Remove the middleman** (i.e me): PM and the Data Scientist should work directly with each other. Instead of the information flowing/gathered with me as the nodal person.
2. **Better Retrospectives**: We did a few reviews i.e. what went well or wrong, but not enough of “How does this inform our future?”
3. **Add Front End, DevOps Skills**: Lot of our releases would reach the end user because the interface was designed, but not implemented. Engineering teams would quite obviously pick their own OKRs above ours. The short term fix is to add Front End and DevOps skills.

Even something as simple as being able to build+deploy Gradio or Streamlit demos would go a long way in convincing the org to prioritise the shipped work.


## Ending Note

The terms are borrowed from the amazing blog by Pardis Noorzad: [Models for integrating data science teams within companies | by Pardis Noorzad | Medium](https://djpardis.medium.com/models-for-integrating-data-science-teams-within-organizations-7c5afa032ebd)

Thanks to [Eugene Yan](https://twitter.com/eugeneyan) and [Maneesh Mishra](https://twitter.com/maneesh_mishra) for taking the time to review this piece. A lot of the improvements are thanks to their comments. 

Photo by <a href="https://unsplash.com/@hckmstrrahul?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Rahul Chakraborty</a> on <a href="https://unsplash.com/s/photos/alignment?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
## Notes

[^1]:
     Advanced Technologies Lab at Samsung Research Institute, Bengaluru
