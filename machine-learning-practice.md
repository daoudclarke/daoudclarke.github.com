---
layout: default
hidetitle: true
# category: "Machine Learning in Practice"
title: Machine Learning in Practice
---
<!-- {% include JB/setup %} -->

{% include dc/title %}

{% include dc/signup %}

# Seven Steps to Success

## Machine Learning in Practice

Project failures in IT are all too common. The risks are higher if you
are adopting a new technology that is unfamiliar to your
organisation. Machine learning has been around for a long time in
academia, but awareness and development of the technology has only
recently reached a point at which its benefits are becoming attractive
to business. There is huge potential to reduce costs and find new
revenue by applying this technology correctly, but there are also
pitfalls.

This guide will help you apply machine learning effectively to solve
practical problems within your organisation. I'll talk about issues
that I've encountered applying machine learning in industry. My
experience is in applying machine learning to analysis of text,
however I believe the lessons I have learnt are generally
applicable. I have been able to deliver significant and measurable
benefits through applying machine learning, and I hope that I can
enable you to do the same.

I will assume that you know the basics of machine learning, and that
you have a real-world problem that you want to apply it to. This is
not an introduction to machine learning (there are already plenty of
those), however I don't assume that you're a machine learning
expert. A lot of the advice is non-technical and would be just as
useful to a product manager wanting to understand the technology as a
software developer creating a solution.

### Clearly understand the business need

Understanding the business need is important for any project, but it
is easy to get blinded by technological possibilities. Is machine
learning really going to benefit the company, or is it possible to
achieve the same goals (or most of them) with some simple rules? The
goal is to build a solution, not to do machine learning for the sake
of it.

Try and identify all the metrics that are important to the business.
The metrics we are optimising for have a profound effect on the
solution we choose, so it is important to identify these early on. It
also affects what alternatives there are to machine learning.

In the case of **classification** problems, potential metrics to
consider are

 - **accuracy**: the proportion of all instances classified
  correctly. Note that this can be very misleading if the data is
  biased (if 90% of the data is from class 1, we can get 90%
  accuracy by simply classifying everying as being from that
  class). Real data is normally biased in some way. For this reason,
  you may want to consider an average of the accuracy on each class,
  or some other measure.

 - **precision** is needed when the results
  need to look good, for example if they are being presented to
  customers without any manual filtering after the machine learning
  phase.

 - high **recall** is important when combining machine
  learning with manual analysis to produce a combined system with high
  overall accuracy.

 - **F<sub>1</sub> score**, or more generally F<sub>&beta;</sub> score is useful
  when a trade-off between precision and recall is needed, and &beta;
  can be adjusted to prefer one over the other.

#### Customer Service at Direct Electric

Direct Electric are a large electricity company based in the south of
England. Dave, the head of customer service, is concerned about
response times for upset customers who contact the company online. He
wants to ensure that if a customer sends an angry email, a
representative will get back to them quickly.

&ldquo;At the moment, it takes about two days to respond, and I'd like to
get that down to half a day,&rdquo; he explains to Samantha, the resident
machine learning expert on the software development team. Dave has
heard about automated sentiment analysis, and wonders if that could be
used to quickly identify the emails of interest, so that they can be
prioritised by the customer service team.

&ldquo;What we could do,&rdquo; suggests Samantha, &ldquo;is try and identify the
emails that are likely to carry negative sentiment automatically, and
send those to your team to look at first.&rdquo;

&ldquo;That sounds good!&rdquo;

&ldquo;The thing is,&rdquo; says Samantha, &ldquo;A machine-learning based system
isn't going to get everything right. Would it matter if we missed some
of the negative sentiment emails?&rdquo; Samantha thinks a high precision
system may be what they are looking for. In this case, we will most
likely have to sacrifice recall, and miss some of the emails of
interest.

&ldquo;Well, not really,&rdquo; says Dave, &ldquo;it's only really useful to us if it
finds them all.&rdquo;

&ldquo;Well, if you want to guarantee you find all of them,&rdquo; says
Samantha, &ldquo;the only way to do that is to examine them manually.&rdquo;
Dave looks crestfallen. &ldquo;But,&rdquo; she continues, &ldquo;we could probably
get nearly all of them. Would it matter if we accidentally prioritised
some articles that aren't really negative?&rdquo; She is thinking of trying
to build a system with high recall, which will probably mean lower
precision.

&ldquo;That would be fine,&rdquo; says Dave. &ldquo;After all, at the moment, we're
reading them all.&rdquo;

----------------------------------------------------------------------

<i>Sign up below to read all seven chapters:</i>
#### 1. Clearly understand the business need
#### 2. Know what's possible
#### 3. Know the data
#### 4. Plan for change
#### 5. Avoid premature optimisation
#### 6. Mitigate risks
#### 7. Use common sense

Or download <a href="guide.pdf">here</a> if you don't want to sign up.

{% include dc/signup %}

## About the Author

Hi, I'm Daoud Clarke. I wrote this guide as a summary of my
experiences applying machine learning in industry. I'm currently a
Data Scientist at <a href="http://lumi.do">Lumi</a>, and I also work
part time as a researcher at the
<a href="http://www.sussex.ac.uk">University of Sussex</a>. My name is
<a href="http://www.google.co.uk/search?q=daoud+clarke">quite
googleable</a>.
