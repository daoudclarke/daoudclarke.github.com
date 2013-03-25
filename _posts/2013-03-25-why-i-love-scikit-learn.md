---
layout: post
title: "Why I Love Scikit learn"
description: ""
category: 
tags: []
---
{% include JB/setup %}

TL;DR: _Scikit Learn is great because it has a clean API, is robust,
fast, easy to use, comprehensive, and well documented and supported,
and the developers are cool. If you can implement your project in
Python and you don't need massively scalable algorithms, then it is
probably for you._

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
about my favourite machine learning library, Scikit Learn, and why I
think it is currently the best library around for doing machine
learning, both for academic work and in production.

## 1. Clean API

The importance of a clean API cannot be overstated. It is much easier
to write clean code if the underlying API is cleanly designed. Your
code will have to conform to the vision of the library writer, and
they can force you to write convoluted code if they want to. Complex
design may sometimes be justified by increased generality, but if the
common use cases are difficult, then it is not a good design.

The objects provided by the library are forced upon you, and they will
litter your code. Well designed objects will lead to terse, readable
code.


<!-- I have seen the detrimental effect -->
<!-- of choosing a bad library when we chose to use Weka for an early -->
<!-- project on sentiment analysis. At the time, it was probably the most -->
<!-- comprehensive machine learning library available, however the API it -->
<!-- provided was terrible. We ended up writing our own data format and -->
<!-- converting to -->
