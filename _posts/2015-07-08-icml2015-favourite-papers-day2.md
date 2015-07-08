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

### [Unsupervised Domain Adaptation by Backpropagation](http://jmlr.org/proceedings/papers/v37/ganin15.pdf)

*Yaroslav Ganin, Victor Lempitsky*

Imagine you have a small amount of labelled training data and a lot of
unlabelled data from a different domain. This technique will allow you
to build a neural network model that fits the unlabelled domain. The
key idea is super cool and really simple to implement. You build a
network that optimises features such that it is difficult to
distinguish which domain the data came from.
  
### [Weight Uncertainty in Neural Networks](http://jmlr.org/proceedings/papers/v37/blundell15.pdf)

*Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, Daan Wierstra*

### [Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks](http://jmlr.org/proceedings/papers/v37/hernandez-lobatoc15.pdf)

*Jose Miguel Hernandez-Lobato, Ryan Adams*

These papers have a very similar goal, namely making neural networks
probabilistic. This is cool because it allows you to not only make a
decision, but know *how sure you are about the decision*. There are a
bunch of other benefits: you don't need to worry about regularisation,
hyperparameter tuning is easier etc.

Anyway, the two papers achieve this in two different ways. The first
uses Gaussian scale mixtures together with a clever trick to
backpropagate expectations. The second one computes the distribution
after rectifying and then approximates this with a Gaussian
distribution. Either way, this is an exciting development for neural
networks.




Want more? Sign up below to get a free ebook
_[Machine Learning in Practice](/machine-learning-practice.html)_, and
updates on new posts:

{% include dc/signup %}
