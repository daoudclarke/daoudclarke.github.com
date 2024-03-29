---
layout: post
title: "Manifesto for an Intelligent Chatbot Platform"
description: ""
category: "Chatbots"
tags: []
---
{% include JB/setup %}


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

The above diagram is a very rough idea of what the new platform might
consist of. My goal is just to show how I think the proposed goals can
be achieved using existing technology. I'll try and flesh out in
future posts what each component might look like, but for now, here's
a high level summary, following the diagram anti-clockwise from the
user:

 - A natural language query or response from the user is
   received. This is parsed by a *semantic parser*. I've not found a
   good concise description of semantic parsing on the interwebs,
   which is strange, but it's not the same as parsing (although
   similar) and it's not the same as (traditional) semantics. A
   semantic parser takes a natural language expression and translates
   it to some "logical form" where the logical form is anything that a
   computer would naturally understand, such as a SQL query, an
   expression in first order logic, a JSON string or an "intent". The
   typical application is to use natural language to perform database
   queries. Anyway, this is a well studied sub-field of natural
   language processing (despite its lack of a Wikipedia page). An
   example of an almost-state-of-the-art system is the
   [SEMPRE system](https://nlp.stanford.edu/software/sempre/) from
   Stanford.
 - A *planning system* then chooses the next best action to take given
   its knowledge of the current state of the world and the latest user
   input. This problem is also a well studied one. A very general way
   of describing planning problems is something called a
   [Partially Observable Markov Decision Process](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process),
   or POMDP (pronounced "pom dee pee") for short. In fact, POMDPs have
   been used to plan dialogue, as described in
   [this overview by Steve Young at Cambridge](http://mi.eng.cam.ac.uk/~sjy/papers/ygtw13.pdf).
   My idea is to use
   [Monte-Carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
   to solve our planning problem, an aproach described in
   [this paper from NIPS 2010](https://papers.nips.cc/paper/4031-monte-carlo-planning-in-large-pomdps).
   I'm really excited about the potential for Monte-Carlo tree search
   to do something other than playing games really well (in case you
   didn't know it's a large component of
   [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo)). The planning
   system makes use of the Knowledge Modules provided by the bot
   designer to inform the decisions it makes.
 - Once an action has been decided upon, an *action interpreter* makes
   use the the ability modules provided by the bot designer to perform
   actions on external APIs, or passes on a logical form to the next
   system to send a response to the user.
 - A [*natural language generator*](https://en.wikipedia.org/wiki/Natural_language_generation)
   interprets the logical forms and sends the response back to the
   user. The generator can make use of the style modules to determine
   the best expression for each logical form.

Hopefully this is enough to convince you that the plan is not entirely
crazy. Each component is well studied (at least in a research
setting), so it is not too far-fetched to assume that they can be put
together into something useful. The biggest uncertainty in my mind is
around the planning system, and exactly how this will work
effectively. I plan to flesh that out in a future blog post.

Some readers may be disappointed that I'm not proposing some
new-fangled deep learning technique to solve this humongous
problem. In fact, I'm pretty much proposing the same good old
fashioned AI techniques that were popular in the 70s and 80s. Actually
I think systems built in that time period got a lot of things right,
but the individual components were not developed enough to make the
system as a whole a success, at least when applied to a general
setting. In fact, in some cases, the improvements in the individual
components are because of algorithmic developments like deep learning,
along with the abundance of data and computing power. There is
definitely potential for making use of deep learning to improve the
three major components of the system:

 - [Here's a paper](https://arxiv.org/abs/1706.04326) on using deep
   learning for semantic parsing
 - Deep learning was a large part of AlphaGo's success so it can
   definitely be used to improve
   planning. [Here's a paper](https://arxiv.org/pdf/1507.06527.pdf) on
   using deep learning to solve POMDPs which happen to be Atari games
   (what is it with the games?).
 - And [here's a paper from NIPS 2014](http://www.cs.umd.edu/~miyyer/pubs/2014_nips_generation.pdf)
   on natural language generation using deep learning. Also
   [language modeling](https://en.wikipedia.org/wiki/Language_model)
   is often an important component in natural language generation, and
   neural networks have been very successful at this task.

It's almost inevitable that deep learning will take over most
components of my proposed system at some point. But they are not
essential, at least initially.

But still, I should probably try and answer the question of why not
build a single big deep net to rule them all? One answer is that we
don't know how to do this yet. But even if it were possible, I do not
think I would want to try and do this. The answer is engineering. When
I know how each component is supposed to work, I can fix it. When a
deep net doesn't work, all I can do is add more data and tweak the
algorithm, which may or may not solve the problem (and may introduce
new ones).

The argument I'm trying to make here is that natural language
interfaces should be a solved problem, given that we have such
sophisticated components around now, and all it requires is putting
them together in the right way and engineering the thing correctly. Of
course, that's still a huge challenge, but one I'm quite excited about
undertaking. I like big challenges.

Practical considerations
========================

Now I can hear you thinking "It's all very well taking on such a grand
challenge, but who's going to pay for it?" One option would be to try
and build this thing in academia, after all, I've done the academic
thing, so it should be possible to follow that route. The problem is,
speaking with my metaphorical mortarboard on, in my experience, and
speaking for myself, us academics tend not to build useful things
things. You see, our motivation is naturally skewed towards publishing
papers, which is what academics do, rather than building something
that people actually want. And if we can squeeze a few percentage
points of improvement out of a problem, we can publish a paper.

So if not academia, then what? I happen to find myself in the lucky
situation of having some spare time at the moment. My current contract
requires me to work only 15 hours a week, so that leaves plenty of
spare time. I could try and build this just for fun, as a side
project. However, at some point, my spare time will run out and I
suspect this is going to take a lot longer than the three months I
have left on my contract. The next obvious option is to try and build
a company from it. This would either be a traditional startup, with
funding and all the craziness that goes along with it, or a
bootstrapped company. Actually a startup would not be a bad vehicle
for something as ambitious as this. However, there are at least two
reasons I don't want to go down the traditional startup route:

 - I'm not convinced that this can be a billion dollar business
   (yet). The thing is, people want chatbots, but they don't know they
   want what I'm building (although they may well _need_ it). At some
   point in the future that may change.
 - I don't personally enjoy the pressure to grow quickly that comes
   with a startup. I would rather build a successful and sustainable
   business slowly. That's particularly true because I think it's
   going to take a long time to build this properly. Also, I don't
   hold with "stealth mode" - I'd rather do this out in the open.

So the current plan is for a simple bootstrapped company selling
chatbots as a service. Yes, I know, there are a lot already, but I
think there is space for another. The market is predicted to grow
quickly in the next few years - we'll see whether this turns out to be
true or not. Of course I won't be building my full crazy idea above
straight away, I will only build each component properly as it is
needed, and instead focus on building something that people want,
preferable in focused niche.

One niche that I think is likely to be profitable is
chatbots for marketing, specifically,
[Facebook Messenger bots as a landing point for Facebook ads](https://blog.whatshelp.io/3-strategies-to-use-messenger-bot-and-facebook-ads-for-lead-generation-8a40f033510c).
So, if you're interested in this idea, please get in touch! I think it
has a lot of potential for increasing the return on investment of
Facebook ads.

