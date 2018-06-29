---
layout: post
title: "Planning dialogue with modal logic and Monte Carlo tree search"
description: ""
category: "Chatbots"
tags: []
---

{% include JB/setup %}

I wrote a while ago about how I thought there is a lot of room for
improvement with current chatbot tools. In particular, I want to make
it easy to create chatbots that plan their own dialogue.

Existing tools require you to explicitly tell the chatbot what to say
in each situation. Instead, with our proposed approach, you just need
to say what it is the chatbot can say, and what each of those things
means. The chatbot should then figure out which things are appropriate
to say in each situation.

The goal is to make creating something like Google's Duplex much
simpler. Ultimately, I hope that it will be simple to craft in-depth,
engaging conversations.

In this post I want to flesh out some of the technical background to
what I'm proposing. In particular, I will talk about:

 - How we can use modal logic to represent both a user's and a bot's
   beliefs and desires;
 - How we can express speech acts in terms of these beliefs and
   desires;
 - How we can view dialogue as a planning problem;
 - Solving that problem using Monte Carlo tree search;
 - Steps towards a new semantics for modal logic in terms of
   planning.

That's quite a lot, isn't it? Let's see how we go.

Beliefs and and desires for dialogue
------------------------------------

The central theme I want to discuss is around the idea that beliefs
and desires can be expressed using logic, specifically, modal
logic. This is a very old idea. The idea of applying this to dialogue
is also not new. But so far it doesn't seem to have been applied in a
practical setting in tools that are widely available.

Modal logic is based around the idea that the truth of a statement
depends on its context. In particular, I might believe one thing to be
true, while you might believe the opposite. I might also _desire_ one
thing to be true, while knowing that it is false.

These types of restrictions on how to describe when a statement should
be considered true or false are described using modal _operators_. In
general, these are written using symbols, but for clarity, in this
article, I will write them as `know(i, x)` to means "Agent _i_
knows _x_" and `want(i, x)` to mean "Agent _i_ wants _x_ to be
true."

Imagine a conversational interface for online shopping. If the user
says "I want some tomatoes" we can interpret that as "I want tomatoes
in my online shopping basket". This might be represented as
`want(user, basket(tomatoes))`.

A simple Montague-style grammar
-------------------------------

We are starting to describe a formal language that represents the
meaning of sentences. The design of this language is very important
because it is the interface that people will use to describe meanings
in our framework.

Perhaps the user is not sure what things our shop sells. If they say
"Do you sell tomatoes?" we can interpret this as "I want to know
whether you sell tomatoes." We could write this as `want(user,
know(user, whether(sell(tomatoes))))`. The function `whether` takes a
statement and returns either that statement or its negation, depending
on which one is true.

We give each of the literals `know`, `whether`, `sell` and `tomatoes`
a type as follows:

 - `tomatoes` has type `<e, t>`. This means it is a function from
   entities `e` to truth values `t`. In other words the semantics of
   `tomatoes` is the set of all things that are tomatoes.
 - `sell` has type `<<e, t>, t>`, the type of functions from sets of
   entities to truth values. We could, for example,
   define`sell(tomatoes)` to be true if there is an entity `x` for
   which `tomatoes(x)` is true, and we sell `x`.
 - `whether` has type `<t, t>` since it takes sentences and returns a
   new one.
 - `know` has type `<e, <t, t>>`. It takes an entity (the agent whose
   knowledge is under consideration) and returns back a function that
   takes a sentence, and returns true if and only if that agent knows
   the sentence to be true.

Game-theoretic semantics
------------------------

The normal way to give these expressions meaning is in terms of
"possible worlds". This approach is not ideally suited to our
application, because there are a lot of possible worlds to explore,
and using them to describe the meaning of sentences quickly becomes
unweildy.

Instead, the idea is to interpret a sentence as a commitment on the
behalf of the speaker. Specifically, it is a commitment to behave
consistent with that statement in the future.

So if the user says, "I want tomatoes" we would expect it to be
unlikely that the user would then request tomatoes be removed from the
basket.

This idea matches well with another aspect of our approach. We want to
view dialogue as a planning problem. This allows us to make use of
recent advances in planning such as Monte Carlo tree search. In this
framework, we attach a positive or negative reward to each sequence of
actions. We then try and find sequences that maximise the reward.

Collaboration
-------------

The type of dialogue we're interested in is a collaborative
activity. This means that there is a shared reward between the user
and the AI agent. We encode the idea of consistency sketched above as
follows:

 - There is a negative reward (a cost) associated with committing to
   wanting something.
 - There is a larger positive reward in achieving something that was
   committed to earlier.

The problem with this is that it encourages agents to say they want
things to achieve a reward even if they could achieve it without
saying they want it.

One way around this is to allow agents to commit to wanting something
privately (at a lower cost). They then achieve the same reward if they
get what they wanted.
