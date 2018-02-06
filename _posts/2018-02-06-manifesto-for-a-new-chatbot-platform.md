---
layout: post
title: "Benefit People: Thinking Through Culture and Values"
description: ""
category: "Startups"
tags: []
---
{% include JB/setup %}

Planning for the Perfect Dialogue with Monte Carlo Tree Search
==============================================================

I've always found it frustrating that chatbot developers seem to be
satisfied with frameworks that don't even attempt to mimic anything
close to real intelligence. There seem to be two basic approaches:

 - Intent-based approaches, in which a query is mapped to a template,
   perhaps with some slots to be filled, for example, a query like "I
   need a train to Norwich" would prompt the chatbot to question the
   user with the goal of filling in slots relating to the departure
   location and the desired arrival time.
 - Tree-based approaches, where there is a tree of possibilities the
   user can explore, kind of like the "make your own adventure" books
   I used to read as a kid. This is useful in informational settings
   like customer support, where giving a useful responses depends on
   exploring a tree of possibilities to determine the user's problem.

Sometimes these are augmented with features like the ability to
remember past values for slots, that improve the perception that the
chatbot knows what's going on. But as soon as the user steps off the
beaten track, the chatbot will be confused and the user experience
will suffer. And what about if you want to combine the tree-based
approach with an intent-based approach? So far there's no clean way of
doing this.

I believe there is a better way, and that's why I've started working
on my own chatbot framework. These are the design goals of the
framework:

 1. The chatbot should automatically choose the next best action out
    of all possible actions
 2. The chatbot should learn which responses are most likely, and
    optimise its behaviour accordingly
 3. The chatbot behaviour should be specified by independent modules
    that can be combined freely

As an example, I'll describe how these goals could work out in
practice for a bot to allow users to make purchases on an e-commerce
website. Imagine a user is buying their weekly supermarket shop from
BigMart. The conversation might go something like this:

"I'd like some apples."

"How about 6 Russet apples for £1.20 or 12 Golden Delicious for
£1.70?"

"I've just remembered I need milk"

"1 litre of whole milk like last time?"

"Yes"

"Do you still want apples?"

"Yes, the Golden Delicious."

"Ok."

In this conversation, the bot has remembered that the user wanted
apples, even after the distraction of buying milk. The point is that
this behaviour shouldn't need to be explicitly planned by the bot
designer: the bot should automatically know that the user has a goal
of buying apples that needs to be fulfilled. Also, note that the bot
has learnt the type of milk that the user likes to buy, which saves
the user time. Again, this behaviour should be built into the platform
rather than needing to be programmed by the bot designer.

If the bot designer does not need to program these behaviours, what
would bot development look like? We envisage three types of bot
"modules" that can be developed:

 - Modules that specify the *style of conversation* between the bot
   and the user. This allows the bot designer to specify the preferred
   expressions to be used by the bot when interacting with the
   user. For example, you could write a module for bots to talk like
   pirates, perhaps restricted to a specific domain.
 - Modules that describe *world knowledge*. For example, you might try
   and write a bot that helps people choose the correct visa for a
   journey to the UK (this is actually something I've done before, and
   it's a non-trivial problem). Such a bot would need to know about
   the different types of visa available, the conditions for each one,
   their cost and so on.
 - Modules that endow the bot with *new abilities*. For example, a
   module may allow a bot to interact with a specific API. Different
   e-commerce bots could then choose the correct API module for their
   e-commerce platform, while re-using the same style and world
   knowledge modules as other bots.

The three goals combined should make it very easy for a bot designer
to create a bot: in the most common case, their job would be to simply
choose the best modules for their application, customizing each one
according to their needs.

Is it possible?
---------------

I can hear you thinking, "It's all very well having such lofty goals,
but is it achievable?" I believe it is, and in this section I will
outline my proposed solution.

![Chatbot platform architecture]({{"/img/chatbot-platform.png"}})
