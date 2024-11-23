---
date: '2019-09-21'
authors:
- nirant
categories:
- tech
- machine learning
- production ml
title: ML Model Monitoring
---

Mayank asked on [Twitter](https://twitter.com/MayankSatnalika/status/1175446811860824064): 

> Some ideas/papers/tools on  monitoring models in production. A use case would be say a classification task over large inputs. I want to visualise how are the predicted values or even confidence scores vary over time? (paraphrased)

## Quick Hacks

### pandas-profiling

If you are logging confidence scores, you can begin there. The quickest hack is to visualize with pandas-profiling:
https://github.com/pandas-profiling/pandas-profiling/


### Rolling means

Calculate rolling aggregates (e.g. mean, variance) of your confidence scores. pandas inbuilt. Quite quick. Add them to your set of monitoring and alerting product metrics. 

A better version of this would be to do it on cohort level. Actually, doing all the following analysis on cohort level makes sense.

### Confidence Scores and Thresholds

One of the most common mistakes is to use static threshold(s) on a confidence score(s). 

If you hear someone saying that they do not use thresholds for a classification problem. Stop and think. They are using a threshold, usually 0.5 from within the ML library that you are using. 

This is sub-optimal. The better option would be to use a holdout validation set and determine the threshold from that. 

### Tagging Data 

It is obvious that you will tag the predictions for which the model is least confident -- so that the model can learn. 

What you should also do is this: 

- Find out samples which have high confidence and tag them first, this is a form of negative sample mining

- For multi-class classification: Figure out samples which did not clear your threshold, and the prediction is correct. Add these back to your new training+validation set

- Tag samples which are too close to the threshold. This will help you understand your model and dataset's _margin of separation_ better

## Training-Serving

The most common causes of trouble in production ML models is **training-serving skews** or differences.

The differences can be on 3 levels:
Data, Features, Predictions

## Data Differences 
Data differences can be of several types, the most frequest are these:
Schema change - someone dropped a column!, 
Class Distribution Change - When did this 10% training class have 20% predictions, or 
Data Input Drift - users have started typing instead of copy-pasting!

### Schema skew (from Google's ML Guide)
Training and serving input data do not conform to the same schema. 	The format of the serving data changes while your model continues to train on old data. 	

**Solution?** Use the same schema to validate training and serving data. Ensure you separately check for statistics not checked by your schema, such as the fraction of missing values 

### Class Distribution check with Great Expectations
Training and serving input data should conform to the same class frequency distribution. 
Confirm this. If not, update the model by training with updated class frequency distribution. 

For monitoring these first two, check out: https://github.com/great-expectations/great_expectations

For understanding data drift, you need to visualize data itself. This is too data-domain specific (e.g. text, audio, image). And more often than not, it is just as better to visualize features or vectors.

## Feature Viz for Monitoring 

Almost all models for high dimensional data (images or text) *vectorize* data. I am using features and vectorized embedding as loosely synonymous here.

Let's take text as an example:

### Class Level with umap

Use any dimensionality reduction like PCA or umap (https://github.com/lmcinnes/umap) for your feature space. Notice that these are on class level. 

![umap-tweet-plots](https://raw.githubusercontent.com/NirantK/blog/master/content/images/umap-tweets-plot.png "UMAP Tweet Plots")

Plot similar plots for both training and test, and see if they have similar distributions. 

## Prediction Viz for Monitoring

Here you can get lazy, but I'd still recommend that you build data-domain specific _explainers_

### Sample Level with LIME

Consider this for text:

![lime-viz](https://raw.githubusercontent.com/NirantK/blog/master/content/images/lime-viz.png "Lime Visualization for Explaining Model Predictions")

Check out other black box ML explainers: https://lilianweng.github.io/lil-log/2017/08/01/how-to-explain-the-prediction-of-a-machine-learning-model.html by the amazing @lilianweng

### Class Level

You can aggregate your predictions across multiple samples on a class level:

![agg-lime-viz](https://raw.githubusercontent.com/NirantK/blog/master/content/images/agg-lime-viz.png "Aggregated Lime Visualization for Explaining Model Predictions on Class Level")


## Training Data Checks

Expanding on [@aerinykim's tweet](https://twitter.com/aerinykim/status/1259945059085987843)

### Robustness

Adding in-domain noise or perturbations should not change the model training and inference both.


# Citations and Resources

[1] Machine Learning Testing in Production: https://developers.google.com/machine-learning/testing-debugging/pipeline/production

[2] Recommended by DJ Patil as "Spot On, Excellent": http://www.unofficialgoogledatascience.com/2016/10/practical-advice-for-analysis-of-large.html

[3] Practical NLP by Ameisen: https://bit.ly/nlp-insight. The images for umap, LIME, and aggregated LIME are all from nlp-insight

[4] Machine Learning:The High-Interest Credit Card of Technical Debt: https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43146.pdf