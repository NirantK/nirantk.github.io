+++
title = "MLOps for Startups"
description = ""
date = 2021-07-21T00:09:00+05:30
tags = ["machine learning", "tech"]
toc = true
draft = true
show_reading_time = true
+++

# OVERVIEW

Start your development by writing the overall impact and feature overview in the Press Release doc and README

If your time to ship is more than 2 weeks, write a [functional spec](https://www.joelonsoftware.com/2000/10/03/painless-functional-specifications-part-2-whats-a-spec/)

In case of bug fixes, add bug details or link to Asana/Github Issues

Always. Do [trunk-based development](https://trunkbaseddevelopment.com/). Don’t restrict a deployment trigger to specific people. As soon as you are done, go ahead, deploy and let others deploy.

# SERVICE DETAILS

## DOCS
1. Please provide API documentation for your service (e.g. via API definition)
2. Add auto-generated engineering docs in HTML/Markdown
3. Who is the maintaining team/person at this moment for the service? All maintainers and committers should be listed
Repo README should include instructions to set up this repo for development

## Service Component — DATABASE
1. List down all the database changes, if you added any columns, removed any columns, added or removed any tables.
2. What kind of indexes do you have? If you added a new column does it require an index? If yes, why? If no, why not?
3. Do you make changes to records? Do you do frequent deletes or updates?

## Service Component — MONITORING
1. List all the services you own and list down each server monitoring parameters
2. Alerts for service uptime, service performance degradation e.g. latency, throughput
3. Alerts for service machine disk/CPU/memory — what’s the threshold and how are they triggered

Please include today’s screenshots for each of them e.g. StackDriver. We need to make sure that you have proper monitoring in place.

## Service Component — DEPLOYMENT
#TODO Add a step by step documentation on how to write your first service and deploy it in the dev/stage/production environment for your org

# CODE STYLING

# PYTHON
1. Add a pre-commit with black, sort and flake8 to your code. Follow the happy path convention. Add type hints

2. Start writing code by writing APIs, then tests and then implement code. We use tests as API docs

2. Add proper liveness and/or readiness check for your Kubernetes deployment:

Liveliness check is for Kubernetes to know whether your application is running.

Readiness check is for you to specify when traffic should be sent to the pod. For example, if your pod needs some operations to be done before it can take traffic (such as downloading a dataset), your readiness check should send back 200 only once it's completely ready for taking traffic.

Docs:

1. [Kubernetes Manual](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
2. Blog on [Best Practices](https://medium.com/metrosystemsro/kubernetes-readiness-liveliness-probes-best-practices-86c3cd9f0b4a)

# DATA BEST PRACTICES

## VERSION CONTROL

Use [dvc.org](https://dvc.org) and version all your datasets to Cloud Storage Buckets and include your DVC file in your Github repo

## EXPERIMENTS
1. Aim for reproducible experiments by re-using actively maintained APIs

2. There is no specific tooling to do reproducible experiments, but consider using something simple like [Sacred](https://github.com/IDSIA/sacred) or [Hydra](https://hydra.cc/docs/intro/)