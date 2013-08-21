---
layout: post
title: "Why I Love Scikit-learn"
description: ""
category: "Machine Learning in Practice"
tags: []
---
{% include JB/setup %}

TL;DR: _Scikit-learn is great because it has a clean API, is robust,
fast, easy to use, comprehensive, and well documented and supported,
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
design may sometimes be justified by increased generality, but if the
common use cases are difficult, then it is not a good design.

The objects provided by the library are forced upon you, and they will
litter your code. Well designed objects will lead to terse, readable
code, while poorly designed objects will have you scratching your head
six months down the line trying to remember how the code you wrote
works.

You may be tempted to take a machine learning library that has a poor
API but more algorithms and wrap it in a clean API but beware!
Creating a good wrapper for a library is no mean feat. Doing machine
learning properly requires a variety of tools that will need to be
wrapped, and you may find that it's not worth the overhead. In
addition, a library with a poor API is likely to be lacking in other
important qualities such as robustness and good documentation.

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

<!-- ## 4. Comprehensive -->

<!-- Machine learning requires a variety of tools for different situations -->
<!-- and purposes, for example, feature extraction, feature selection, -->
<!-- dimensionality reduction, classification and clustering. Scikit-learn -->
<!-- provides most of these tools, while remaining strictly a -->
<!-- general-purpose machine learning library. -->

## 5. Well Documented

## 6. Permissive License

## 7. Well Supported


<!-- I have seen the detrimental effect -->
<!-- of choosing a bad library when we chose to use Weka for an early -->
<!-- project on sentiment analysis. At the time, it was probably the most -->
<!-- comprehensive machine learning library available, however the API it -->
<!-- provided was terrible. We ended up writing our own data format and -->
<!-- converting to -->
