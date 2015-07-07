---
layout: post
title: "My favourite papers from day one of ICML 2015"
description: ""
category: "Machine Learning in Practice"
tags: []
---
{% include JB/setup %}

Aargh! How can I possibly keep all the amazing things I learnt at ICML
today in my head?! Clearly I can't. This is a list of pointers to my
favourite papers from today, and why I think they are cool. This is
mainly for my benefit, but you might like them too!

Neural Nets / Deep Learning
---------------------------

### [BilBOWA: Fast Bilingual Distributed Representations without Word Alignments](http://jmlr.org/proceedings/papers/v37/gouws15.pdf)

*Stephan Gouws, Yoshua Bengio, Greg Corrado*

**Why this paper is cool:** It simultaneously learns word vectors for
  words in two languages without having to learn a mapping between
  them.
  
### [Compressing Neural Networks with the Hashing Trick](http://jmlr.org/proceedings/papers/v37/chenc15.pdf)

*Wenlin Chen, James Wilson, Stephen Tyree, Kilian Weinberger, Yixin Chen*
 
**Why this paper is cool:** Gives a huge reduction (32x) in the amount
  of memory needed to store a neural network. This means you can
  potentially use it on low memory devices like mobile phones!
  

### [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](http://jmlr.org/proceedings/papers/v37/ioffe15.pdf)

*Sergey Ioffe, Christian Szegedy*

**Why this paper is cool:** Makes deep neural network training super
  fast, giving a new state of the art for some datasets.
  
### [Deep Learning with Limited Numerical Precision](http://jmlr.org/proceedings/papers/v37/gupta15.pdf)

*Suyog Gupta, Ankur Agrawal, Kailash Gopalakrishnan, Pritish Narayanan*

**Why this paper is cool:** Train neural networks with very limited
  fixed precision arithmetic instead of floating points. The key
  insight is to use randomness to do the rounding. The goal is to
  eventually build custom hardware to make learning much faster.


Conclusion
----------

That's it - what a day!

Want more? Sign up below to get a free ebook
_[Machine Learning in Practice](/machine-learning-practice.html)_, and
updates on new posts:

{% include dc/signup %}
