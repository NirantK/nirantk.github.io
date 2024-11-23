---
authors:
  - nirant
date: 2020-08-30
categories:
  - engineering-management
  - machine-learning
title: Building a Data Science Team at a Startup
---

Hello! 

If we are meeting for the first time, a short version of my story so far: After doing research engineering for almost 4 years across startups and a BigCo, I joined as an early machine learning engineer at [Verloop.io](https://verloop.io) - a B2B startup that makes customer support automation SaaS in 2019. I was there till April 2021. 

We were directly responsible for most Natural Language Processing needs within the business.

While there is plenty of good advice on [making ML work](https://www.shreya-shankar.com/making-ml-work/) and [making a career as a Data Scientist](https://medium.com/@rchang/advice-for-new-and-junior-data-scientists-2ab02396cf5b), I wanted to write my experience as a manager/early engineer who built out a ML team at a startup. 

I hope you find it useful!

# Who is this for? 
People with these questions:

* "What would it be like to be a Data Science Manager?"
* "How can I build a Machine Learning team from scratch?" 
    * This is typically founders e.g. CEO/CTO looking to build out a Machine Learning function 

Bonus: [Beliefs](#beliefs)

# Hiring

Hiring for Machine Learning Engineering is hard. 

Despite what the media might tell you about the glut of data science talent. There are too many people who can model churn well or do the Titanic dataset right with Logistic Regression, not enough people who can come up with a simple TF-IDF model in a language they've not ever worked with e.g. not English. 

In Summer of 2019, I did over 120 introductory calls between February and August. Averaging, 6 calls every week from April to June. This converted to 1 summer intern, and 3 full time people. 

## One Role to Rule Them All

For >1 year, we have hired for exactly ONE role: Machine Learning Engineer. 

As explained in our [MLE Prep Guide](verloop-ml-prep-guide.md), we collapsed several roles into one. This means we don't hire a specialized Data Scientist, Researcher and then separate Product and Data Engineers to productionize the models. 

At Verloop, the same engineer takes the entire system live from research to production, and occassionally several months into maintenance and growth as well.

This allows us to keep the hiring process straightforward, highly repeatable, while still maintaining enough faith in the process.

## T Shaped Skill Maps

Our hiring process evaluates all candidates on primarily 3 skills:

1. Low Level API Design for Web Services
2. Programming Mindset and Quality
3. Natural Language Processing/Machine Learning Skills (see [Prep Guide](verloop-ml-prep-guide.md) if you're curious)

I biased the top of the funnel of the interview process to hire a team of compliments around my weaknesses.Each compliment should bring in a skill which is my weakness, but that individual's strength. 

Of each of the first 3 full time hires, each person was atleast 2x better than me on that skill. This is important as each person has a multiplier effect on the productivity/quality of other developers on the team. 

To give you a sense of these:

1. Person A has clear, proven strengths in High Level System Design and Databases
2. Person B has clear, proven strengths in DevOps and Cloud Deployments
3. Person C has clear, proven strengths in "hacking" with Deep Learning, optimizing for speed

This input biasing seems to work amusingly well because it enables developers to always keep learning from each other. 

For instance, one of the things which I have asked from each team is a load test of their service - this led one developer to simply build an internal wrapper around the popular `locustio` which works with our service design out of the box. 

It frankly makes my job a lot easier if developers do amazing work without me pushing them to do it - specially by observing each other. I can honestly sit back and simply steer their curiosity, instead of investing my attention into solving the "motivation" problem.

## Process

Our hiring process consists of two primary rounds: a programming challenge and ML challenge. You can actually take a deeper look here: [Verloop ML/NLP Interview Prep Guide](verloop-ml-prep-guide.md).

The programming challenge is a take home exercise which is focussed on low level design and straightforward API design. We typically give 2-3 days to the candidate for this. 

For the ML Challenge, we share a dataset for a take home challenge and then discuss the same with the candidate. This round has no right answer. It is deliberately open ended. 

It gives us a lot of signals on a wide variety of things we care about, for instance:

- how the candidate formulates the problem,
- measures the model performance,
- thinks about model selection and important of loss functions,
- prior/acquired experience with real world datasets,
- literature review/comfort with close to research work,
- ability to write clean, readable code,
- whether they include failed experiments, indicates their confidence with sharing honest results

To me, what has suprised most is the number of otherwise skilled people who use "this is what I saw on Medium" as a valid explanation for selecting a particular approach. This lack of agency (autonomy?) is a red flag.

## Onboarding

I am almost devilish when it comes to designing the best possible onboarding experience that I can. In the case of 1 intern, where I let it go off my radar - I think we didn't do our best as a team. The onboarding at Verloop ML consists of two specific pieces:

### 1. Before Joining Verloop
We share 6-8 week learning calendar focussed mostly on Deep Learning and Natural Language Processing. 

Each week is expected to take 8-10 hours of your time (but interns have told me that it takes closer to 30 hours) - and then I get on with them on a 1-1 call and discuss what they did well and what they missed. I share context from research or our own systems when relevant. One core byproduct of this onboarding calendar is that the candidate should get _very_ comfortable writing tons of experimental code of varying quality. 

This onboarding calendar is custom designed to each candidate, depending on their strengths which I should ideally understand during the interview process. 

### 2. After Joining Verloop

The onboarding process for each engineer is customizer to their weaknesses. For instance, an engineer coming from a stronger systems background will be first given a project which is mostly data cleaning and benchmarking ML models. So that they can get a deeper, more intimate understanding of how experiment design and evaluation works. 

Similarly, freshers out of college, who typically come from weaker engineering backgrounds (but stronger DL skills) - will spend the first few months paying off tech debt, learning to read legacy code or building new CRUD services. 

This is obviously in addition to the one heuristic which I've tried to follow: Ensure that every engineer gets one release into production within 4 weeks of joining Verloop.

# Stakeholders

## Managing Up

A common refrain from most senior ML people I spoke to is that: **Leadership does not understand AI/Data Science**

To me, this has always been an opportunity than a handicap. The most inspirational to me in this sense is the work of the likes of DJ Patil. He is the guy who coined the term, "Data Scientist" and was the Chief Data Scientist of the United States of America under Obama administration. 

I somehow think that an analytical & numerical leadership can be worked with, independent of their own training within the domain. For instance, I don't think Barack Obama can tell a random forest from a convolutional neural network.

Communication and convincing non-experts outside your domain is always hard, painstaking and tedious. I should clarify to say that I don't think this is an easy challenge and, hopefully, our peers in Design will hopefully agree. I think that it's worth the effort.

Here is what I would want to do in the future to make this better:

1. Highlight opportunities e.g. this can be our moat/IP or unlock new value with the caveat: "if it works"
2. State assumptions e.g. cost, development time -- this gives you a feedback loop on your assumptions as well 
3. Call out checkpoints in "state of work" and not timeline. E.g. better to say, once we have done 5 experiments instead of 5 weeks, since you might end up realising that cleaning the data itself is going to take 3x as long

It'd be extremely stupid to assume that any of this would have been possible without the high degree of support and autonomy from the CEO, Gaurav himself. 

As much as I'd like to say/think that I earned that unfailing trust, Lord knows that I have made some messes which he had to clean up.

## Managing People 

Of all things, I have received more support here than I deserved here - and I'm truly grateful for that. I think I have made quite a few people/psychology mistakes here. For instance, assuming that people want to be pushed and given maximum autonomy possible, instead of being led and they build mastery on their craft instead. 

I also found myself being extremely angry at quite a lot. Although I'd read Andy Grove's notion of Task Relevant Maturity, I don't think I did anywhere a decent job of implementing it. 

Managing my own mental state has been more work than I'd expected. My blast radius is much larger -- and deeper than I'd expected. I am sure there are plenty of people with far more nuance, patience and empathy who'd have done a better job at this.

Early on, I'd decided that I'd not repeated any of the mistakes that my previous managers had made. I ended up making a different version of the same f**king mistakes anyway. 

After >1 year, the only thing which works for me is to listen to what people want and then do that.

### Reading Reccos

There is so much good written about People Management and Engineering Management in general, that I'd be stupid to add to that clutter. Instead, I should point out books that have shaped how I think about Engineering/ML managment as well: 

- The Manager's Path by Camille Fournier
- Effective Engineer by Edmond Lau

On Managing Myself:

- Managing Oneself by Peter Drucker
- Standout 2.0 by Marcus Buckingham

Books which are highly recommended, but didn't help me enough:

- The Elegant Puzzle by William Larson
- Randical Candor by Kim Scott

Books which will probably have high impact, but in the future:

- HBR's 10 Must Reads: On Communication
- Effective Executive, by Peter Drucker
- Nonviolent Communication, by Rosenberg

### Data Science Management

What we did: 

1. Encouraged every team to manage the project on their won by few key metrics, 
    - Seprated out goal and minimum metrics
2. Measuring the metrics at some cadence, even if this was erratic in the beginning
3. Each team drives their entire process from research to production to deployment
    - This encourages teams to think about engineering challenges pretty early and gives them reasonably high autonomy

What we should have also done: 

1. Encourage every team member to spend time data-ing i.e. exploring datasets, building a mental model around it, tagging it on their own 
2. Introduce Engineering Practices Early: Stronger emphasis on software engineering practices once they joined the team e.g. doing TDD, code hygiene, 
3. Have every 

## Peer Management

While I'd expected this to be easy, this turned out to be quite emotionally hard. Since I transitioned out of backend engineering roles pretty early in my career - there are entire topics and concepts which I am not great at. This is made worse by the fact that I'm familiar with them, but not comfortable. 

So if 2 developers are discussing something, I can very well follow their conversation - but I don't have anything to contribute. 

This is quite frustrating. The sheer, persistent feeling of incompetency. Luckily, I don't have too much of a self respect/ego to care about this. I've always gravitated towards the best what I can do -- and what others cannot do well. At Verloop, that is Machine Learning/Data Science Management right now.

That said, within Verloop - ML has been the first adopter of almost all new dev tooling: 
- alerting and monitoring systems
- inhouse logging library to improve our microservice observability
- porting from previous Proto serving solution to twirpy

This is atleast partially because I didn't want the devs in my team to suffer. 

# Beliefs

## Don't be Clever

Machine Learning is a game where [87% models never go to production](https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/) - almost every model we have picked, has gone to production.

I've worked in B2B SaaS companies, doing Machine Learning research, engineering and deployment for almost 4 years. Hence, I've some opinions on what doesn't work. I don't have strong opinions on what works though.

I encourage my teammates to come up with new ideas and propose everything from the annotation process to the alerting and monitoring configuration. The only place where I really intervene is if the rigour is absent, or they're solving for a problem without complete context.

So far, this mindset of simply trying to avoid mistakes, instead of trying to be clever has worked well. I suspect as long as ML deployment is a failure-prone business, this mindset will serve me well. If something like GPT3/GPT4 lowers the risk considerably well, I will have to adopt a different mindset altogether.

This has not always worked. We've made some stupid (in hindsight) bets which didn't work for a multitude of reasons, including our own overconfidence in our technical skill and market reasons.

For those who are into the risk vs uncertainty nuance, I should add that I think because we deal with narrow Machine Learning problems - we mostly deal with technology risk and not so much uncertainty. It can be quantified, estimated and analyzed - it's just that I don't have the training to do so formally. 

## Premortems

[Pre-mortems](https://hunterwalk.com/2012/04/23/the-premortem-preventing-failure-before-you-fail/) is a habit/tool which is still somewhat better known in Product Management than Data Science. In fact, it's better understood in Military Strategy than Data Science: 

He who knows his enemy ... - Sun Tzu

I typically list down the top 3 causes which will kill a project - and then actively monitor them till the project is so stable that I can pay attention to something else. Despite my best attempts, I have failed to inculcate this mindset in devs working with me. 

It seems to be that discipline and optimism are fairly orthogonal mindsets in software engineering culture at-large.  To them, I remind that Microsoft Teams, TikTok, IRCTC and Instagram have shipped better than some of our B2B "Scaling" Engineering teams. In a world lost to chaos, I think the disciplined optimism ethos is basically a competitive advantage in my line of work.

## Do Less 

I am a low key fan of [Auren Hoffman](https://twitter.com/@auren)'s advice that great things come from focus and not from building optionality. In the design and selection of tasks which our team has picked, this has been my guiding idea. 

Almost every Data Science team can be considered to be built to serve two "purposes": Analytics and Product

Analytics teams contribute in two ways: 
1. Inform decision makers
2. Measure and monitor internal metrics

At Verloop, the Analytics function is purely owned by Product Management. We assist but don't own any outcomes.

We build a reasonable number of ETL and Data Exploration tools for our own use (e.g. a Metabase installation) - which we make available to every Verloop employee, but we don't own the outcomes.

This also has a direct bearing on our team size, scope and skill set: We don't need to hire anyone to handle your common churn, forecasting or similar insights problems. Everyone is a competent, contributing NLP Engineer.

# In Hindsight

In the last 18 months, our team has grown from 1 engineer (me) to 6 engineers. When I joined, ML was a blocker for the wider org with both latency and performance challenges, which quickly compounded because of legacy code and engineering exits. 

We were behind the curve where Machine Learning was seen as a cost center. 

Today, almost 18 months later, we're almost definitely ahead of the curve in terms of shipping. In the best case scenario, we can also become a profit center in as early as 6-12 months. 

Similarly, there is still a lot of room when it comes to our ability to explore quickly and prototyping production-grade software faster. We can shrink this from present 6-8 weeks to 1-3 weeks in the best case scenarios.

A large part of the impact comes from our excellent customer support team, product and engineering. Machine learning is a mere amplifier of what they already do well.

This has been one of the most fulfilling and hard things I have done. 

If you are considering a career in Data Science, I hope this helps you see beauty and effort beyond our love for data and ever increasing technical intricacies.

Till we meet again, 

Nirant