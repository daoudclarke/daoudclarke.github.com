---
layout: post
title: "Why I Love Scikit-learn"
description: ""
category: "Machine Learning in Practice"
tags: []
---
{% include JB/setup %}

_After my [previous post]({% post_url 2013-09-18-why-i-love-scikit-learn %})
---------------------------------------------------


Java based:
 - __[Weka](http://www.cs.waikato.ac.nz/ml/weka/)__: this is a Java
   based library with a graphical user interface that allows you to
   run experiments on small datasets. This is great if you restrict
   yourself to playing around to get a feel for what is possible with
   machine learning. However, I would avoid using this in production
   code at all costs: the API is very poorly designed, the algorithms
   are not optimised for production use and the documentation is often
   lacking.
 - __[Mallet](http://mallet.cs.umass.edu/)__: another Java based library
   with an emphasis on document classification. I'm not so familiar
   with this one, but if you have to use Java this is bound to be
   better than Weka.
 -  __[JSAT]__(https://code.google.com/p/java-statistical-analysis-tool/):
   stands for "Java Statistical Analysis Tool" - created by Edward
   Raff and was born out of his frustation with Weka (I know the
   feeling). Looks pretty cool.

Python based:
 - __[PyBrain]__(http://pybrain.org/): Neural networks are one thing
   that are missing from SciKit-learn, but this module makes up for
   it.
 - __[NLTK]__(http://nltk.org/): really useful if you're doing
   anything NLP or text mining related.

General:
 - [__LibSVM__](http://www.csie.ntu.edu.tw/~cjlin/libsvm/) and
   [__LibLinear__](http://www.csie.ntu.edu.tw/~cjlin/liblinear/):
   these are C libraries for support vector machines; there are also
   bindings or implementations for many other languages. These are the
   libraries used for support vector machine learning in Scikit-learn.


Of course there are many more; let me know if there is something that
should be included on this list and why, and I'll add it.

## Conclusion

 - Choose your library carefully
 - Scikit-learn is robust, with a clean API, and fast implementation
 - It may not suit every application

Want more? Signup below to get a free ebook
_[Machine Learning in Practice](/machine-learning-practice.html)_, and
updates on new posts:

{% include dc/signup %}

<!-- I have seen the detrimental effect -->
<!-- of choosing a bad library when we chose to use Weka for an early -->
<!-- project on sentiment analysis. At the time, it was probably the most -->
<!-- comprehensive machine learning library available, however the API it -->
<!-- provided was terrible. We ended up writing our own data format and -->
<!-- converting to -->
