---
layout: post
title: "So you want to be a data scientist? (Part 1)"
description: ""
category: "Machine Learning in Practice"
tags: []
---
{% include JB/setup %}

&ldquo;Data Scientist&rdquo; is definitely the hot new job
description. It is such a new title that the roles and
responsibilities associated with it are still not clearly
defined. What skills do you need to be a data scientist? Well, not
everyone agrees. In this article we will try to be objective by
looking at statistics on what skills employers recruiting data
scientists are looking for. We will use data from
[IT Jobswatch](http://www.itjobswatch.co.uk/jobs/uk/data%20scientist.do),
which is a fantastic resource for those looking to upskill themselves:
it provides comprehensive statistics on the keywords that recruiters
mention in job advertisements. I will also give my own opinions based
on my experience recruiting data scientists and working as one at
[Lumi](http://lumi.do).

Some caveats:

- The data is from jobs advertised in the UK, so your mileage may
vary.
- Recruiters might not necessarily know what the employer really
*needs*
- *Employers* might not know what they really need

The last point is important because it is easy to fall prey to the
bandwagon phenomenon: &ldquo;Everyone is doing *big data* so we need
to do it too&rdquo;. The company may not actually have enough data to
benefit from big data technology, and may benefit more from a careful
statistical analysis of the data that they do have.

So, what do you need to know to be a data scientist? Here's what
recruiters are asking for, broken down into the following sections:

 - Qualifications
 - Applied skills
 - Knowledge-based skills
 - Programming languages
 - Technologies

Qualifications
--------------

If you know you want to be a data scientist, and you're trying to
decide whether to go to university, or what course you might do, then
the answer is quite clear. 37% of data science jobs advertised mention
the word &ldquo;degree&rdquo;, and 34% mention &ldquo;PhD&rdquo;. A PhD
involving experimentation, numerical analysis or computer programming
may well be beneficial to getting a data scientist position, but
anyone who can demonstrate analytical ability and knowledge of how to
run experiments is in a good position.

Keywords mentioned relating to degrees are (predictably) Mathematics
(50%), Computer Science (37%) and Physics (25%), and any of these
would provide a good foundation for a career in data science. However,
it is not enough to know just Mathematics or Computer Science - as a
data scientist you will need to combine many skills. As someone who
studied physics myself, I am biased, but a typical physics course will
cover many of the things you need to know: how to run experiments, how
to analyse results and how to program - a very good starting point.

Some universities are now offering courses in data science - these
could be a good choice, but are certainly not necessary if this is
what you want to do.

Skills
------

Just as for any other type of scientist, data scientists need to be
inquisitive and enjoy solving hard problems. You need to be able to
truly understand and characterise a problem, perhaps describe it
mathematically, break it down, and come up with a plan for a
solution. 48% of job adverts cite &ldquo;Analytical Skills&rdquo; - a
catch-all phrase for this type of ability.

Other skills mentioned in data science job adverts are:

 - Data Mining (38%) - a very general area relating to the use of
   statistics and machine learning techniques to extract information
   from typically unstructured sources of content such as web pages or
   log files.
 - Statistics (37%) - undoubtedly, every data scientist needs to have
   a basic grasp of statistics and know best practices for statistical
   analysis of data.
 - Machine Learning (28%) - the science of analysing data to find
   patterns and make predictions. This is a very broad area that is
   long established in the academic research community; its usage is
   only just starting to become widespread in industry.
 - Visualisation (23%) - in general, communication skills are very
   important for a data scientist, and being able to visualise data
   in ways that draw out the patterns of interest is a very useful
   skill to help communicate ideas.
 - Finance (19%) - many jobs in data science are in finance - if you
   are interested in working in this area, then any knowledge you have
   will be beneficial.
 - Information Retrieval (10%) - the science of search, typically text
   documents (think Google search), but also images and sound.
 - Natural Language Processing (5%) - technologies related to natural
   language such as part of speech tagging, parsing, named entity
   recognition, machine translation and question answering.
   
I would add to this that it is generally important for all data
scientists to have some general business acumen, so that they can
focus their efforts on tasks that are strategically beneficial to the
company.

Other skills mentioned are: Analytics, Predictive Modelling, Data
Modelling and Data Analysis (66%, 24%, 23% and 19%
respectively). These are either synonyms for, or applications of the
above skills to specific areas, each with a different emphasis.

Technologies
------------

56% of jobs mention &ldquo;Big Data&rdquo; a term which basically
means the ability to analyse and work efficiently with very large
datasets. Practically this means experience with Hadoop (49%) and
MapReduce (26%) and perhaps Mahout for machine learning (17%). Other
big data technologies include NoSQL databases (9%) such as MongoDB
(7%), Cassandra (3%) and search technologies such as Elasticsearch
(0.25%) and Solr (0.25%).

Not all data is big however. It is also important to know how to work
with relational databases (16%) such as Oracle (5%), Postgres (3%) and
MySQL (3%), and you will need to have at least a basic knowledge of
SQL (43%).

Other technologies mentioned are more business oriented, such as the
statistics packages SAS (25%) and SPSS (20%), however the overall
demand trend for both these technologies seems to be downward.

Programming Languages
---------------------

If you want to be a data scientist, you will have to be able to
program, which means you will need to know at least one language. Here
are your options:

- By far the most popular is R (55%) because of its very comprehensive
set of libraries for scientific computing;
 - This is followed by Java (45%), because it's so darned popular
(personally I'm not a fan);
 - Python (43%) is my favourite because of its resources for machine
learning
([I wrote a whole article about it](http://daoudclarke.github.io/machine%20learning%20in%20practice/2013/09/18/why-i-love-scikit-learn/)),
it's really fast to write code, the code is generally very readable
and runs quickly because it uses C libraries internally, and can be
used for production code as well as quick scripts for analysis;
 - MATLAB (33%) is an old favourite for scientific computing; whilst
   it is powerful, unlike other options it is not freely available.
 - Other popular languages for data scientists are C++
(21%), Scala (17%), C# (7%), Visual Basic (7%), Clojure (7%) and Ruby
(6%).

