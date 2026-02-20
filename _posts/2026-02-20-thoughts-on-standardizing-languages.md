---
layout: post
title: "Thoughts on Standardizing Programming Languages"
tags: []
---
{% include JB/setup %}

I've worked at a few places where there is a "standard" language. From
an organisational perspective, this makes a lot of sense: if everyone
writes the same language, then it's easier to move developers (and
code) around, which should lead to higher productivity.

The downside is that developers tend to have preferences, and they may
not like language X. If the company has had a policy of always using
language X from the start, then employees will probably self-select
themselves out of working there. But imposing a language on developers
who have been used to freedom to choose (even if from a slightly
larger set of languages), risks a developer revolt.

I'm wondering how much this is going to matter in the future. If the
trend continues, and more code is being written by large language
models, then how important is it to know the ins and outs
of a specific language?

Being good at architecture, understanding clean code and best
practices suddenly become much more important.

Of course, there are languages (and frameworks) that LLMs are better
at. But this is also changing fast. A few years ago, LLMs struggled to
write things in Rust, but they seem to have improved a lot.

It will always be true that it is easier to glue things together if
they are written in the same language. But often, a codebase is used
to define an API rather than a library.

Maybe then, language restriction will make more sense for cases like
desktop software, which needs to be compiled into a single package.
For companies that are building APIs, developers should be given more
freedom to choose their own languages.
