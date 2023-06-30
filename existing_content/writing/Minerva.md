+++
title = "Airbnb's Metric Store: Minerva"
description = "Data Transformation, Serving and a lot more"
date = 2022-07-31T00:09:00+05:30
tags = ["data", "tech"]
toc = true
show_reading_time = true
+++

Data lineage is a problem because most companies have several tables and queries before humans consume it!

This has well known challenges: changes do not propagate downstream from the source, and reliable (fresh, updated or complete) data is not always available.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FpbpeqpoIIi.png?alt=media&token=15868e09-ed90-48da-b96d-84d02108d960)

## What does Minerva do?

I was expecting Minerva to a database (collection of tables), but it turns out that Minerva is what I'll call: **Data Transformation Manager**.

It overlaps quite a bit with `dbt` but it's not a pure execution layer. It also stores metadata, orchestrates the DAG itself, and provides a way to query the data (Hive/Druid here)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FZjlrPzp3wp.png?alt=media&token=8ede65ca-57bf-4a0a-a358-652728aceac4)

Minerva solves for one major problem in the analytics space: **Time to insights** — as [[Julie Zhuo]] has mentioned several times at Sundial

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FZe2HgOAiZl.png?alt=media&token=1393b3bc-034e-4681-9ea8-c00b8c04c215)

## Minerva 1.0

This is a bit preview about the past and what problems did they first solve, what was left undone and some tooling/technology choices.

### Pre-computation engine
Quite similar to how we were building Sundial till very recently.

1. De-normed measures and dimensions
2. Segments and behaviours were both separated out

De-norming measures can be quite expensive but useful. We converged to this design across multiple clients while working with Event-level data. We also see some of our clients maintaining a similar table: "User Segments Table".

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FBJGBLW0Ny-.png?alt=media&token=f6fb2f32-5146-4cb4-9c6f-ba0ed732ad96)


### Tradeoffs in the Precomputing Approach

1. Cubing — SQL
Minerva already knows what SQL query to run, across what segments and what durations upfront. This means it can leverage CUBE operations. 

Some people believe that [OLAP CUBE has fallen out of use](https://www.holistics.io/blog/the-rise-and-fall-of-the-olap-cube/), but that's clearly not true here. As companies get larger, "old" pressures on compute and storage should re-appear and so should already known solutions like cubing. 

2. Fast Query Time: Since the results are precomputed - fast at query time

3. Exponential in query cost. Backfill — damn expensive and wastes time and money


![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FinnYTZ9VFz.png?alt=media&token=8513b551-1582-4a34-8d6f-11aa7b46ae5a)

Everything has to be asked ahead of time, so you end up calculating too many things

# Minerva 2.0

This is what a truly "modern" data transformation manager should look like in my opinion.

Here are some of the design choices:

1. On the fly joins
2. On the fly aggregations
3. Optional denorm and cubing
4. Enable precompute to be turned on 

The way I see it, this is striking a balance between flexibility (the ability to do on-the-fly joins and aggregations) and cost (the ability to precompute with denorm and cubing).

## Engineering Choices

### Moved from Druid to StarRocks

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2F1eQ3GfuPTo.png?alt=media&token=bdd3b32a-67ac-417e-9538-55c15a9eeed6)

### Why StarRocks?

Minerva is SQL generation tool, not a Druid ingestion tool

Minerva has a SQL Interface now, early was JSON

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2F7e9FOXGP8E.png?alt=media&token=cbc9732e-791e-442e-a4d1-1cd797770c71)

SQLGlot — Python SQL Parser and Transpiler -- this is very similar to `dbt` for how it generates SQL using a parser and transpiler. SQLGlot is open source btw: https://github.com/tobymao/sqlglot

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FShwgLouRXk.png?alt=media&token=8e284885-0e47-4b3a-9014-5d6d8afad0f9)

## Near Real Time Metrics

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FrSO3V1xTlK.png?alt=media&token=42966ecd-1820-49d6-8fc4-80f7e92e81aa)

Summary of changes made for 2.0 release

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fpeople-notes%2FOd85otZtyc.png?alt=media&token=ba65cd85-0207-48dd-9877-a8fe97f39874)

## Major changes is that SQL is now a first class citizen

This is quite important. We should resist the temptation of inventing a Python transformation layer/logic. While some Python is inevitable for doing more interesting things like forecasting, using Python for calculating ratios is a bit overkill. We should instead try and consider pushing the limits of SQL for the same. 

SQL is not only more widely spoken, it'd be a lot more efficient and more scalable. The downside? It's less general purpose language, and we'd have to write some tooling to make SQL work like Python.


---

These are some notes and screen grabs from a talk which I'd found on [Youtube](https://www.youtube.com/watch?app=desktop&v=ksWwdYwXhh0&ab_channel=Databricks). Thanks to [Kunal Kundu](https://twitter.com/kunal__kundu) for finding the talk link which I'd lost!
