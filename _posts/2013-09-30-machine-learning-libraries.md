---
layout: post
title: "Machine Learning Libraries"
description: ""
category: "Machine Learning in Practice"
tags: []
---
{% include JB/setup %}

_After wonderful feedback on my
[previous post on Scikit-learn]({% post_url 2013-09-18-why-i-love-scikit-learn %})
from the guys at
[/r/MachineLearning](http://www.reddit.com/r/MachineLearning/comments/1mq8fb/why_i_love_scikitlearn/),
I decided to collect the list of machine learning libraries into this
seperate note. Let me know if there's a library that should be
included here._

---------------------------------------------------


### Python

 - __[Scikit-learn](http://scikit-learn.org)__: comprehensive and easy
   to use, I wrote [a whole article]({% post_url 2013-09-18-why-i-love-scikit-learn %})
   on why I like this library.
 - __[PyBrain](http://pybrain.org/)__: Neural networks are one thing
   that are missing from SciKit-learn, but this module makes up for
   it.
 - __[nltk](http://nltk.org/)__: really useful if you're doing
   anything NLP or text mining related.


### Java

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
 - __[JSAT](https://code.google.com/p/java-statistical-analysis-tool/)__:
   stands for "Java Statistical Analysis Tool" - created by Edward
   Raff and was born out of his frustation with Weka (I know the
   feeling). Looks pretty cool.

### .NET

 - __[Accord.NET](http://accord-framework.net/intro.html)__: this
   seems to be pretty comprehensive, and comes recommended by
   [primaryobjects](http://www.reddit.com/user/primaryobjects) on
   Reddit. There is perhaps a slight slant towards image processing
   and computer vision, as it builds on the popular library
   [AForge.NET](http://www.aforgenet.com/) for this purpose.
 - Another option is to use one of the Java libraries compiled to .NET
   using [IKVM](http://www.ikvm.net/) - I have used this approach
   with success in production.

### C++

 - __[Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit)__:
   designed for very fast learning and released under a BSD license,
   this comes recommended by
   [terath](http://www.reddit.com/user/terath) on Reddit.

### General

 - [__LibSVM__](http://www.csie.ntu.edu.tw/~cjlin/libsvm/) and
   [__LibLinear__](http://www.csie.ntu.edu.tw/~cjlin/liblinear/):
   these are C libraries for support vector machines; there are also
   bindings or implementations for many other languages. These are the
   libraries used for support vector machine learning in Scikit-learn.

### Conclusion

This article is a work in progress, so please send me your comments or
criticisms!

Want more? Sign up below to get a free ebook
_[Machine Learning in Practice](/machine-learning-practice.html)_, and
updates on new posts:

{% include dc/signup %}

<!-- I have seen the detrimental effect -->
<!-- of choosing a bad library when we chose to use Weka for an early -->
<!-- project on sentiment analysis. At the time, it was probably the most -->
<!-- comprehensive machine learning library available, however the API it -->
<!-- provided was terrible. We ended up writing our own data format and -->
<!-- converting to -->
