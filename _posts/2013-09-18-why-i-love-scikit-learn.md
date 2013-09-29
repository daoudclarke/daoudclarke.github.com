---
layout: post
title: "Why I Love Scikit-learn"
description: ""
category: "Machine Learning in Practice"
tags: []
---
{% include JB/setup %}

_Scikit-learn is great because it has a clean API, is robust, fast,
easy to use, comprehensive, and well documented and supported,
released under a permissive license and the developers are cool. If
you can implement your project in Python and you don't need massively
scalable algorithms, then it is probably for you._

---------------------------------------------------

Choosing a library is often a crucial task. In the case of machine
learning, it is likely that the library you choose will form the core
of your project, and your choice will impact on many other decisions
you will make when building your software. If you choose the wrong
library, you may spend weeks wrapping a poorly designed API,
inspecting source code to understand undocumented features and working
around bugs and limitations. If you get it right, you will be able to
write clean, bug free code with a minimum of effort.

I have seen this effect first hand. In this article, I want to talk
about my favourite machine learning library, Scikit-learn, and why I
think it is currently one of the best libraries around for doing
machine learning, both for academic work and in production.

<!-- Scikit-learn is a python library -->

## 1. Clean API

The importance of a clean API cannot be overstated. It is much easier
to write clean code if the underlying API is cleanly designed. Your
code will have to conform to the vision of the library writer, and
they can force you to write convoluted code if they want to. Complex
design may sometimes be justified by increased generality, but if it
is hard to implement the common use cases, then the API is poorly
designed.

The objects provided by the library are forced upon you, and they will
litter your code. Well designed objects will lead to terse, readable
code, while poorly designed objects will have you scratching your head
six months down the line trying to remember how the code you wrote
works.

You may be tempted to take a machine learning library that has a poor
API but more algorithms and wrap it in a clean API, but beware!
Creating a good wrapper for a library is no mean feat. Doing machine
learning properly requires a variety of tools that will need to be
wrapped, and you may find that it's not worth the overhead (I learnt
this lesson the hard way). In addition, a library with a poor API is
likely to be lacking in other important qualities such as robustness
and good documentation.

## 2. Robust

If you are planning to use a machine learning library in production
code, then robustness will be a high priority. One of the differences
between Scikit-learn and other machine learning libraries is that the
authors are explicitly targetting not just academic use, but use in
industry as well. They have concentrated on doing a few things really
well, rather than trying to do everything.

Scikit-learn is unit tested, with around 80% unit test coverage,
giving us confidence that old features will not break as new ones are
implemented and bugs are fixed.

UPDATE: [Edward Raff noted on
/r/MachineLearning](http://www.reddit.com/r/MachineLearning/comments/1mq8fb/why_i_love_scikitlearn/)
that his experience with SciKit-learn hasn't been so rosy when the
datasets are large or poorly behaved, so your mileage may vary...

<!-- In my experience, upgrading -->
<!-- Scikit-learn has occasionally broken my code -->

## 3. Fast

If speed is important to you, Scikit-learn is fast. Despite being
implemented in an interpreted language, Python, its foundations are
the compiled libraries NumPy and SciPy, and in addition, the authors
have implemented a lot of tools in Cython, which compiles to C,
giving blazing fast Python-like code.

The authors have also built on top of existing machine learning
libraries, such as LibLinear and LibSVM for support vector machines,
however they didn't stop there, optimising the algorithms to make them
even faster.

## 4. Easy to Use

Being a fan of the Python language, I am undoubtedly a little biased,
however, it is arguably one of the easier languages to learn and
use. The Scikit-learn team have followed Python conventions as much as
possible, which makes using it a joy if you know Python. There are
several methods which Scikit-learn classes can implement:

    fit
	transform
	fit_transform
	predict
	decision_function

Each type of object will implement a subset of these, and duck typing
determines which objects are appropriate in each circumstance. For
example, classifiers are expected to implement the `fit` and `predict`
methods. 

Here's an example from the documentation for the Multinomial Naive
Bayes classifier:

    >>> import numpy as np
    >>> X = np.random.randint(5, size=(6, 100))
    >>> Y = np.array([1, 2, 3, 4, 5, 6])
    >>> from sklearn.naive_bayes import MultinomialNB
    >>> clf = MultinomialNB()
    >>> clf.fit(X, Y)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    >>> print(clf.predict(X[2]))
	[3]

<!-- ## 4. Comprehensive -->

<!-- Machine learning requires a variety of tools for different situations -->
<!-- and purposes, for example, feature extraction, feature selection, -->
<!-- dimensionality reduction, classification and clustering. Scikit-learn -->
<!-- provides most of these tools, while remaining strictly a -->
<!-- general-purpose machine learning library. -->

## 5. Well Documented

I have found the
[Scikit-learn documentation](http://scikit-learn.org/stable/documentation.html)
to be comprehensive, readable, and easy to understand. When doing
something new with Scikit-learn, I have quickly been able to get to
get to grips with how to do it after a quick peruse of the
documentation, either using Python's `help()` function, or the
excellent online documentation, which includes tutorials as well as
documenting the API.

Of course, it also helps that the API is well designed: a lot of the
time you can guess the correct usage of a new class once you get to
know a few of the classes.

Only occasionally have I had to fall back to reading the source to
understand a feature (or, more often, a bug in my own code). Since the
code is mainly fairly clean Python, even this is not much of a chore.

## 6. Permissive License

Scikit-learn is released under the liberal
[BSD License](http://opensource.org/licenses/BSD-3-Clause) so you can
use it freely in commercial applications.

## 7. Well Supported

Scikit-learn must be one of the most actively developed open source
machine learning projects. Check out the
[github stats for the last month](https://github.com/scikit-learn/scikit-learn/pulse/monthly):
at the time of writing, there were 734 commits by 42 authors.

## ...And the Downsides



## Alternatives


Unfortunately, you can't always have the best. There are numerous
factors to bear in mind when choosing a library that may impact your
decision on what to use:

 - __Language__: if you have to integrate your machine learning
   functionality with legacy code, then this may restrict your choice
   of language, although it is often possible to avoid this by using a
   service oriented architecture. Alternatively, you may have to stick
   to a particular language because of company policy, or because
   the developers in your team don't want to abandon their favourite
   language for something new.
 - __Performance__: for many applications, performance is critical, but
   if it is not, then this gives you more freedom in which machine
   learning tools you can use.
 - __Scalability__: if you need something that is massively scalable
   (which in my opinion is fairly rare), then you might want to
   consider something like [Mahout](http://mahout.apache.org/) which
   is not as comprehensive as Scikit-learn, but is scalable to very
   large datasets as it is implemented on top of Hadoop.

Some libraries that you may want to consider:

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
