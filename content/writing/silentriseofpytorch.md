+++
title =  "The Silent Rise of PyTorch Ecosystem"
date = 2019-08-27T23:29:18+05:30
tags = ["python", "machine learning", "tech", "deeplearning"]
featured_image = "https://miro.medium.com/max/8250/1*ZLLZPo4kiH-cBzUYEukEVg.png"
description = "What is blazing across the PyTorch Ecosystem?"
toc = true
show_reading_time = true
+++

# The Silent Rise of PyTorch Ecosystem

While Tensorflow has made peace with Keras as it’s high level API and mxNet now support Gluon — PyTorch is the bare matrix love.

PyTorch has seen rapid adoption in academia and all the industrial labs that I have spoken to as well. One of the reasons people (specially engineers doing experiments) like PyTorch is the ease of debugging.

What I don’t like about PyTorch is it’s incessant requirement of debugging because of inconsistent dimensions problems. In fact, one of the most recommended speed hacks for faster development: assert tensor shapes!

This is something which Keras abstracts out really well. Additionally, PyTorch has no high level abstractions which picks good defaults for most common problems.

This leads us to the observation that there are three niche problems unsolved in the PyTorch ecosystem:

## Unsolved Problems

-   **General Purpose Abstraction**: Over PyTorch similar to Keras or tf.learn
-   **Adoption**: Something to help traditional ML practitioners adopt PyTorch more easily
-   **Production Use Cases**: Something which allows engineers to take Pytorch code as-is in production or port to Caffe2 with minimal effort. I like Gluon for this, it has no community support but is backed by MSFT and AWS both.

Few specialized efforts like [AllenAI’s NLP](https://github.com/allenai/allennlp) though built for NLP, or PyTorch [torchvision](https://github.com/pytorch/vision) & [torchtext](https://github.com/pytorch/text) are domain specific instead of a generic abstraction similar to Keras. They deserve their own discussion space, separate from here.

## The Better Alternatives

## fast.ai 
- [github](https://github.com/fastai/fastai), [docs](https://docs.fast.ai/)

fastai has outrageously good defaults for both vision and NLP. They have several amazing implementations for Cyclic Learning Rate, learning rate schedulers, data augmentation, decent API design, interesting dataloaders, and most important: extremely extensible!

It as seen some rather great adoption among Kagglers and beginners alike for faster experimentation. It is also helped by their amazing MOOC course.

## Ignite 
- [github](https://github.com/pytorch/ignite), [docs](https://pytorch.org/ignite/)

Ignite helps you write compact but full-featured training loops in a few lines of code. It is fairly extensible, and results in a lot of compact code. There is no peeking under the hood. This is the best contender for Keras for PyTorch power users.

I do not know of any power users of Ignite, despite their elegant design. Nor have I seen it’s adoption in the wild.

## PTL: PyTorch-Lightning
- [github](https://github.com/williamFalcon/pytorch-lightning) 

Built by folks over at NYU and FAIR, Lightning is gives you the skeleton to flesh our your experiments. The best contender to **Keras for Researchers**. The built in mixed precision support (via apex) and distributed training is definitely helpful.

The biggest value add I guess will be explicit decision, all in one class— instead of the scattered pieces we see with PyTorch. Yay Reproducibility!

The lib is still very new, and that shows up in it’s lack of adoption but is getting a lot of star counts in first week of launch!

Check out detailed [comparison between Lightning and Ignite](https://towardsdatascience.com/pytorch-lightning-vs-pytorch-ignite-vs-fast-ai-61dc7480ad8a) from the creator of Lightning

## Skorch
- [github](https://github.com/dnouri/skorch) 

skorch is attacking the bringing ML people to Deep Learning problem above

skorch is a scikit-learn style wrapper (with metrics and pipelines support!) for Pytorch by a commercial entity invested in it’s adoption. It is being developed fairly actively (most recent master commit is less than 15 days old) and marching to v1.

## Summary
fast.ai: researchers, rapid iterators like Kagglers
skorch: welcome people coming from more traditional Machine learning backgrounds
PyTorch Lightning: custom built for DL experts looking for experimentation tooling

**Ending Note**: What are using for deep learning experiments? Have you seen the light with PyTorch or still going with Tensorflow? Tell me @nirantk