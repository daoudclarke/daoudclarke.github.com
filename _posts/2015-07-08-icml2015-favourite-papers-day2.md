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

### [Training Deep Convolutional Neural Networks to Play Go](http://jmlr.org/proceedings/papers/v37/clark15.pdf)

*Christopher Clark, Amos Storkey*

Although I've never actually played the game, I have an interest in AI
Go players, because it's such a hard game for computers, which still
can't reach the level of human players. The current state of the art
uses [Monte Carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
which is a really cool technique. The authors of this paper use neural
networks to play the game but don't quite achieve the same level of
performance. I asked the author whether the two approaches could be
combined, and they think they can! Watch this space for a new state of
the art Go player.

Natural Language Processing
---------------------------

### [Phrase-based Image Captioning](http://jmlr.org/proceedings/papers/v37/lebret15.pdf)

*Remi Lebret, Pedro Pinheiro, Ronan Collobert*

This is a new state of the art in this very interesting task of
labelling images with phrases. The clever bit is in the syntactic
analysis of the phrases in the training set, which often follow a
similar pattern. The authors use this to their advantage: the model is
trained on the individual sub-phrases that are extracted, which allows
it to behave compositionally. This means that it can describe, for
example, both the fact that a plate is on a table, and that there is
pizza on the plate. Unlike previous approaches, the sentences that are
generated are not often found in the training set, which shows
that it is doing real generation and not retrieval. Exciting stuff!

### [Bimodal Modelling of Source Code and Natural Language](http://jmlr.org/proceedings/papers/v37/allamanis15.pdf)

*Miltos Allamanis, Daniel Tarlow, Andrew Gordon, Yi Wei*

Another fun paper; this one tries to generate source code given a
natural language query, quite an ambitious task! It is trained on
snippets of code extracted from StackOverflow.

Optimisation
------------

### [Gradient-based Hyperparameter Optimization through Reversible Learning](http://jmlr.org/proceedings/papers/v37/maclaurin15.pdf)

*Dougal Maclaurin, David Duvenaud, Ryan Adams*

Hyperparameter optimisation is important when training neural networks
because there are so many of the things floating around. How do you
know what to set them to? Normally you have to perform some kind of
search on the space of possible parameters, and Bayesian techniques
have been very helpful at doing this. This paper suggests something
entirely different and completely audacious. The authors are able to
compute gradients for hyperparameters using automatic differentiation
*after going through a whole round of stochastic gradient descent
learning*. That's quite a feat. What this means is that we can answer
questions about what the optimal hyperparameter settings look like in
different settings - and makes a whole set of things that was
previously a &ldquo;black art&rdquo; a lot more scientific and
understandable.

And more...
-----------

There were many more interesting papers - too many to write up
here. Take a look at the [schedule](http://icml.cc/2015/?page_id=825)
and find your favourite! Let me know on [Twitter](https://twitter.com/daarkecloud).

