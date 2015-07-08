---
layout: post
title: "My favourite ICML 2015 papers - part two"
description: ""
category: "Machine Learning in Practice"
tags: []
---
{% include JB/setup %}

Yesterday I [posted]({% post_url 2015-07-07-icml2015-favourite-papers-day1 %})
on my favourite papers from the beginning of ICML (some of those
papers were actually presented today, although the posters were
displayed yesterday). Here's today's update, which includes some
papers to be presented tomorrow, because the posters were on display
today...

Neural Nets
-----------

[Unsupervised Domain Adaptation by Backpropagation](http://jmlr.org/proceedings/papers/v37/ganin15.pdf)

*Yaroslav Ganin, Victor Lempitsky*

**Why this paper is cool:** Imagine you have a small amount of
  labelled training data and a lot of unlabelled data from a different
  domain. This technique will allow you to build a neural network
  model that fits the unlabelled domain. The key idea is super cool
  and really simple to implement. You build a network that optimises
  features such that it is difficult to distinguish which domain the
  data came from.
  


Want more? Sign up below to get a free ebook
_[Machine Learning in Practice](/machine-learning-practice.html)_, and
updates on new posts:

{% include dc/signup %}
