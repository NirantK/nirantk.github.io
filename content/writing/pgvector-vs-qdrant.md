+++
title =  "1M OpenAI Benchmark: PGVector vs VectorDB (Qdrant)"
date = 2023-06-30T00:00:18+05:30
tags = ["tech", "machine learning", "production ml"]
featured_image = "images/ink.png"
description = "When You Should Think Twice Before Using pgvector for Production"
toc = true
show_reading_time = true
+++

## 1M OpenAI Benchmark: pgvector vs VectorDB (Qdrant)

If you're considering pgvector, for your production environment, you may want to reconsider. 

![](../images/1M_QPS.jpeg)

Our benchmark informs that pgvector lags behind a robust vector database like Qdrant by a factor of 20 when it comes to throughput e.g Queries per second. 

Indeed, that's a 2000% speed deficit! But speed isn't the only metric to consider when evaluating a database; accuracy is just as crucial. Regrettably, pgvector falls short here too, delivering a disappointing 18% fewer relevant documents than Qdrant.

Interestingly, these disparities start to surface with as few as 100,000 chunked documents. 

![](../images/QPSvsVectorpgvector.png)

As an ardent supporter of Postgres, it is disheartening to witness that pgvector doesn't just commence at under half the queries per second (QPS) at 100,000 vectors when compared to Qdrant - it plunges precipitously beyond that. 

![](../images/QPSvsVectorQdrant.png)

One might try to rationalize this by assuming that, albeit slow, Postgres is more accurate? Unfortunately, this is a misconception. Our data reveals that pgvector is not just slower, but also ~18% less accurate!

![](../images/1M_kNN.jpeg)

Latency provides another important lens through which to evaluate these platforms. In this category too, Qdrant holds its own. The worst p95 latency for Qdrant is 2.85s, a stark contrast to pgvector, whose best p95 latency is a full 4.02s. Even more astonishing, pgvector's worst p95 latency skyrockets to an unbelievable 45.46s.

For the data enthusiasts among us, we have provided a comprehensive Google Sheet that details all the numbers for a more in-depth analysis: [Google Sheet](https://docs.google.com/spreadsheets/d/1t2-tXID2LJCXdLv1JTPQaYhmMs6woOnK7W7nkEuDsUc/edit?usp=sharing)

These surprising revelations are courtesy of Erik Bernhardsson's [ann-benchmarks](https://ann-benchmarks.com) code, with special thanks to Kumar Shivendu for their forked version. 

As we continue to test and compare platforms, our commitment to finding the best possible solutions for our production environments remains unwavering. As it stands, the numbers suggest Qdrant could be the preferable choice over pgvector.

Machine: t3.2xlarge