---
layout: post
title: "Why the world needs a non-profit search engine"
description: ""
category: "Search Engines"
tags: []
---
{% include JB/setup %}

Sometimes I forget why I've taken on this crazy, huge task. Why am I [building](https://github.com/mwmbl/) a [search engine](https://mwmbl.org)? Will
it really be better than Google one day? Will people support it? Will people even use it?

And then I read something like [The Bullshit Web](https://pxlnv.com/blog/bullshit-web/) and I remember, that, yes, there
is a point. Even if I make the web better for one person, it's worth it. Because the way things are is just wrong.

Search engines are in a unique position to fix the situation. Not only do we create a view on the world's knowledge, we
influence it too. If we promote bullshit-free sites, then people will create more bullshit-free sites.

More importantly, search engines are a filter on the world's
knowledge. Do you really want your filter to be "whatever makes
$SEARCH_ENGINE more money", particularly when that means, "show ads
instead of search results, and prioritise search results that also
make us more money"?  We can and should do better.


### What will it mean in practice?


What would the ideal non-profit search engine look like in practice,
and what would make it better than what we have now?

 1. **Ad-free.** While this can be achieved now with ad-blockers,
    this is clearly not a sustainable solution if everyone were to
    apply it.
 2. **Open source.** The technology for organising the world's
    knowledge should be owned by everyone.
 3. **Profit agnostic ranking.** Google has an incentive to rank
    pages that contain Google ads because it makes them more
    revenue. More generally, Google has an incentive to rank
    profit-making sites higher so that they make more money. This both
    gives them more money to spend on advertising, and makes them
    dependent on their Google ranking, making them more likely to
    spend on advertising should their ranking get worse.
 4. **Community powered ranking.** Google tries to work out which
    sites are interesting by how long you spend on the site. This has
    an unfortunate side effect for e.g. recipe sites, where there is
    an absurd incentive to hide the actual recipe after a ton of
    background and repetitive descriptions of the recipe, to make it
    more likely for you to get distracted on the way to get to the
    actual recipe. Instead of looking at how long people spend on a
    site, we would encourage users to give explicit feedback on
    rankings and use this to improve our ranking system.
 5. **Fast.** Google search is surprisingly slow, taking up to half a
    second for a page load to complete in my measurements. It doesn't
    need to be this way. In 2010, Google announced [Instant
    Search](https://searchengineland.com/google-instant-complete-users-guide-50136)
    that would search as you typed. This was meant to [save users two
    to five seconds per
    search](https://www.theatlantic.com/technology/archive/2010/09/the-pros-and-cons-of-google-instant/62666/). Yet
    Google quietly [dropped this
    feature](https://searchengineland.com/google-dropped-google-instant-search-279674)
    in 2017, ostensibly to bring search more in line with mobile. I do
    wonder though, if the change was more motivated by some
    requirement around adverts. It must be hard to manage auctioning
    adverts in real-time as users type, particularly if you want the
    adverts to blend into the search results.
 6. **Frictionless.** Google has an incentive to show you a results
    page, so that you see some adverts and are thus more likely to
    click on them. But often you don't need to see a results page, for
    example if there is a single page you need. For example if you are
    typing "facebook" or "hmrc login" you *could* go straight there
    from the address bar. But Google wants you to see a results page
    first.

Our current implementation of [Mwmbl](https://mwmbl.org) is a long way
from doing all these things well, but this is what we're aiming
towards.

### The funding question

Search funded by advertising is a recipe for disaster because there will always be a conflict of interest. Get the user
to the site as quickly as possible, or show them some ads on the way? Guess which one you will choose if you care about
revenue.

There are two ways forward that I can see:

 - The paid subscription model, like [kagi.com](https://kagi.com)
 - Donation funded, non-profit model, like Mwmbl - [donate here!](https://github.com/sponsors/mwmbl)

There is no guarantee that either approach will work - but it's got to be worth a try.


### The donation model


While I wish Kagi the best, we have chosen the donation model because
we want to make the best search engine possible available to
everyone. Not everyone can afford to pay for search.

When I read the numbers it makes me feel a little sick. Google's revenue for search was around [$40 billion in Q1 2022](https://searchengineland.com/alphabet-q1-microsoft-q3-earnings-search-advertising-383869).
A number so large, I can't even conceive how big it is. Just 1% of 1% of this would be more money than I'd know what to
do with ($4m).

But it also makes me hopeful. If I can create something that just a
tiny fraction of people find useful, then I can create a huge amount
of value. If there is value, then people will pay for it, if we find
the right way to ask.  Our current plan is to offer different
sponsorship tiers with intangible rewards, for example virtual badges
displayed on the user's profile page.

Of course, there are plenty of non-profits in adjacent spaces that have been successful. I think Wikimedia is the best
example to look up to. Also, I believe our values are very closely aligned. If they were open to collaborating or taking
on this project then I would seriously consider it, because I think it would give it a much greater chance of success.



### What next?


Our current goals are:
 - Index 1 billion pages a month. Help us by [installing our Firefox
   extension](https://addons.mozilla.org/en-GB/firefox/addon/mwmbl-web-crawler/)
   to crawl the web. Our ranking evaluations have shown that the
   biggest improvements come from indexing more pages. So that is our
   first priority.
 - Raise enough money to form an official non-profit
   organisation. This will be the first step in making Mwmbl
   sustainable, beyond being a side-project for a few people.
 - Get to £50 monthly recurring revenue to enable us to upgrade our
   server (currently costing under €5 a month) - [donate
   here](https://github.com/sponsors/mwmbl)! This will allow us to
   increase the size of our index, improving our search results.

If you're interested in helping out, we're [recruiting
volunteers](https://github.com/mwmbl/mwmbl/wiki/Open-positions), or if
you're a developer, check out the [open issues](https://github.com/mwmbl/mwmbl/issues).


### Thanks


Thank you so much to all those that have helped out so far, whether by [donating
your CPU and bandwidth](https://addons.mozilla.org/en-GB/firefox/addon/mwmbl-web-crawler/) to crawl the web, [giving money](https://github.com/sponsors/mwmbl) to cover our
costs, giving your time and skills to [fix issues](https://github.com/mwmbl/mwmbl/issues) or giving feedback on our
[Matrix server](https://matrix.to/#/#mwmbl:matrix.org).

In particular, [Colin Espinas](https://matrix.to/#/#mwmbl:matrix.org)
has been instrumental in designing and building the new front end, and
supporting the development of the extension - thanks Colin!


<!-- ### The motivation question -->

<!-- At the moment, I'm loving working on Mwmbl. I relish the technical challenges, and I enjoy seeing something I've created -->
<!-- come to life. But I know I have limits. I tend to get bored of my side projects after a few months. This is by far the -->
<!-- longest I've worked on something - and it hasn't by any means been continuous. I've realised that I sometimes need to -->
<!-- step away for a while, and that's ok. -->

<!-- At this point, I'm not going to force myself to work on something I don't enjoy. If I don't feel like it, I'll take a -->
<!-- break. No one's paying me to do this (see above!) - perhaps if they were, then I could consider this a job, which -->
<!-- would be amazing. -->
