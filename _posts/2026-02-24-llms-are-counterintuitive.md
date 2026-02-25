---
layout: post
title: "LLMs are Counterintuitive"
tags: []
---
{% include JB/setup %}

I came across [this paper](https://arxiv.org/abs/2602.11988) where the
authors evaluate coding agents ability to complete tasks with and
without AGENTS.md files. The basic conclusion is that these files
reduce success rates slightly, _unless_ you are careful what you put
in them.

Basically make sure you only give instructions to the LLM that you are
sure are going to be useful - as in, you have tried without the
instruction and the LLM got it wrong.

In retrospect, that kind of makes sense, but it doesn't coincide with
my intuition about how to use these tools. I would have naively
thought that you could just tell it how you want it to do a task. And
clearly I am not the only one, as evidenced by the results of the
study.

I was similarly surprised by an experiment I ran at work recently
estimating properties of surveys. I would have thought that the
thinking models (Gemini's "pro" models) would do better at the task,
but it turned out that the models optimised for speed and cost
("flash" models) were far superior at the task.

The lesson I take from all this is, "unless you measure it, you don't
know".

