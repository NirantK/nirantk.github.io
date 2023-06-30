+++
title =  "1M OpenAI Benchmark: PGVector vs VectorDB (Qdrant)"
date = 2023-06-30T00:00:18+05:30
tags = ["tech", "machine learning", "production ml"]
featured_image = "/images/ink.png"
description = "Consider This Before Using pgvector in Production"
toc = true
show_reading_time = true
+++

# 1M OpenAI Benchmark: pgvector vs VectorDB (Qdrant)

You may have considered using PostgreSQL's `pgvector` extension for vector similarity search. There are good reasons why this option is **strictly inferior** to dedicated vector search engines, such as [Qdrant](https://qdrant.tech/).

We ran both benchmarks using the [vectordb framework](https://github.com/qdrant/vector-db-benchmark) solely dedicated to processing vector data. The difference in performance is quite staggering. 

## Query Speed

![](../images/1M_QPS.jpeg)

Final results show that `pgvector` lags behind Qdrant by a factor of 20 when it comes to throughput.  

That is a 2000% deficit in speed. However, we shouldn't only consider speed as the main metric when evaluating a database. In terms of accuracy, `pgvector` delivers way fewer relevant results than Qdrant.

## Workload

Interestingly, these disparities start to surface with as few as 100,000 chunked documents. 

![](../images/QPSvsVectorpgvector.png)

As an ardent supporter of PostgreSQL, it is disheartening to witness that `pgvector` doesn't just commence at under half the QPS at 100,000 vectors, when compared to Qdrant - it plunges precipitously beyond that. 

![](../images/QPSvsVectorQdrant.png)

## Accuracy 

One might try to rationalize this by assuming that Postgres is slower, but more accurate? Data reveals that `pgvector` is not just slower, but also ~18% less accurate!

![](../images/1M_kNN.jpeg)

We measure this using the same methodology as the [ann-benchmarks](https://ann-benchmarks.com) codebase: k-NN bruteforce as ground truth.

## Latency

Here, Qdrant holds its own. The worst p95 latency for Qdrant is 2.85s, a stark contrast to pgvector, whose best p95 latency is a full 4.02s. Even more astonishing, pgvector's worst p95 latency skyrockets to an unbelievable 45.46s.

### Benchmark Specs

Machine used: t3.2xlarge, 8 vCPU, 32GB RAM

For the data enthusiasts among us, we have provided a comprehensive Google Sheet that details all the numbers for a more in-depth analysis: [Google Sheet](https://docs.google.com/spreadsheets/d/1t2-tXID2LJCXdLv1JTPQaYhmMs6woOnK7W7nkEuDsUc/edit?usp=sharing)

### Configuration 

We use the default for both Qdrant and pgvector:

```
Qdrant(quantization=False, m=16, ef_construct=128, grpc=True, hnsw_ef=None, rescore=True)
```

```
PGVector(lists=200, probes=2)
```

There is much more to be tested. We will continue to explore the configuration space for both platforms and update this. 

## Conversations with the Community

{{ < tweet 1674395120395747331 >}}

## Acknowledgements
These surprising revelations are courtesy of Erik Bernhardsson's [ann-benchmarks](https://ann-benchmarks.com) code, with special thanks to [Kumar Shivendu](https://www.linkedin.com/in/kshivendu) for their forked version.