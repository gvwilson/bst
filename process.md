---
title: Process
---

A development process is a set of guidelines that a team follows
when building a piece of software.
Many have been described over the last thirty-five years;
most have passionate advocates and equally passionate detractors.

I am sceptical of most claims made about processes,
partly because many fly in the face of my personal experience,
but also because
teams that adopt diametrically opposed methodologies all see productivity improve.

One possible explanation is that common practice is the worst of all possible worlds,
and any change at all would be an improvement.
(There are days when I believe this.)
A more likely explanation is that what really matters is
deciding that you want to be a better programmer.
If you make a sincere commitment to that,
then exactly how you get there is a detail.
It's kind of like dieting: Atkins, South Beach, macrobiotic, seasonal, or fruitarian
is secondary to being sincere about eating better and exercising more.

## Daily Routine

Before describing the two development processes you're most likely to encounter in courses,
I'd like to talk for a moment about what your day-to-day routine should look like.
As I said above, this "micro process" is pretty much the same
no matter what "macro process" you follow.

First, decide on your tooling.
If some team members are using Make from the command line
while others are building inside an IDE,
or if one person is automating tests with shell scripts, while another is using Python,
you will lose precious time to duplication and contradiction.

Once that's done, establish a routine.
A little every day is great in theory,
but it doesn't work in practice when you're juggling four or five courses.
What's more important is to set aside blocks of time so that your flow isn't interrupted
and to be systematic in those blocks.
Here's an example:

-   3:00 p.m.: you have two hours to spend on your project,
    so you launch VS Code and update your Git repository.
    Your teammates have changed 17 files since the meeting two days ago.

-   3:05 p.m.: you log in to GitHub and look at the event log.
    Five tickets have been closed,
    but eight new ones have been created,
    three of which are assigned to you.
    It looks like the file parser you wrote last week
    doesn't handle the "clarification" the prof posted on Monday.
    You start writing unit tests to check the things that are breaking.

-   3:25 p.m.: you have added twelve new tests to the project.
    Eleven currently fail the way you expect;
    the twelfth triggers an assertion in a data structure one of your teammates built.
    You file a ticket with a reference to the test case,
    check the tests in,
    and start fixing your code.

-   4:00 p.m.: the eleven tests whose failure was your fault now pass,
    so you check in your fixes and close the tickets.
    You're careful to refer to the commit that contains the fix
    in your comments when you close the issues,
    and to the issues in the comment on your commit---it only takes a second
    to type in this information,
    and it makes it much easier for your teammates to keep track of what you've done.
    You then take a five-minute break to check email
    and then close your mail client again
    (since you've learned the hard way
    that you can't resist looking at new messages if you know they're there).

-   Now you can start work on the new feature you want to add
    (which translates part of the program's internal data structure
    into a blob of JSON to send to a web server).
    You have an hour less to do this than you originally planned,
    but that's OK:
    by fixing bugs first,
    you've avoided the all-too-common situation
    of only half the code working when the project is "done".
    As with bug fixes,
    you start by writing some test cases
    to help you think through the details of the classes you're going to add.

-   4:20 p.m.: after rewriting your test cases a couple of times
    you're happy with the API for the new feature.
    Time to start coding?
    Not quite:
    with only 40 minutes to go, you know you won't finish it today.
    Instead, you decide to write stubs of the classes to capture your thinking.
    These stubs have the methods you think you're going to need,
    but all of them return 0 or `null`.

-   4:45 p.m.: after checking everything in,
    you write a short message on the project's chat
    to tell your teammates what you've done.
    You then reward yourself by checking email
    and watching a few YouTube videos of cats doing stupid things.

Three sessions like that a week from each person on the project
plus a single team meeting
and you'll be in great shape.

## Agile vs. Sturdy

Broadly speaking,
modern software development processes can be divided into two camps.
In order to understand the differences between them
it helps to look at the Boehm Curve,
which shows the effort required to fix a bug based on when it is caught.

Boehm's original work in the 1970s showed that
fixing bugs becomes exponentially more expensive
as you move later and later in the development cycle.
Better tools and vastly more powerful computers
have flattened this curve over the past thirty years,
but it is still more expensive to fix things later than earlier.

Development teams deal with this in three ways.
The first is to ignore it.
If you're being paid a steady salary
by a company that can survive delays and cost overruns in your project,
or if you're willing to give up your evenings and weekends,
then this approach still doesn't make much sense,
but a lot of people adopt it anyway.

The second strategy is to do a lot of planning and design
to catch as many errors as possible
during the early phases of the project.
This is the classical engineering mindset:
when you're building a dam,
fixing mistakes means moving several million tons of earth around,
so it's the only one that makes sense.
Until recently,
most academic software engineering research focused on this strategy as well,
which meant it was what most courses and textbooks taught.
I call this approach *sturdy development*:
it may feel a little slow at times,
but it can carry a lot of weight.

The third strategy emerged in the late 1990s under the name *agile development*.
It starts from three related premises:

1.  You *can't* plan a software project very far in advance
    because requirements and technology are constantly changing.

2.  You *shouldn't* plan very far in advance
    because your customers won't know what they want
    until they see something working.

3.  You can *afford* not to lock yourself into a long-term plan
    because software is much more malleable than concrete or steel.

According to agile advocates,
the correct response to these three factors
is to move in many small steps rather than a few large ones.
FIXME shows the difference:
the traditional approach tries to flatten Boehm's Curve
by taking better aim at the outset,
while agile development re-aims more frequently so that the curve never climbs too high.

That's the theory.
In practice,
the differences between the two camps are a lot smaller
than their rhetoric would lead you to believe.
Regardless of what process they're officially using,
most developers do some long-range planning at the start of the project
(if only because customers are usually not willing to sign a blank check)
and then revise their plans and aims as they go along.

Which process makes the most sense for an undergraduate course project?
The odds are that the question won't even come up:
your instructor will probably tell you to follow
the analyze-design-code-test-deploy cycle of the classical (sturdy) model
or to work in two- or three-week agile iterations.
I usually use the former in courses,
since (a) you're very likely to encounter it after you graduate,
(b) it gives you more chance to hone your planning and scheduling skills,
and (c) close interaction with customers is a central tenet of most agile processes,
but isn't really possible in a classroom setting.

Since your project has to fit in one or two terms,
you'll probably be asked to go around the loop once or twice,
which in turn determines how much you'll be expected to deliver in each iteration.
This is called [time boxing](../glossary/#time_boxing):
you specify how long a cycle will last,
then see how much work you can fit into that interval.
The alternative is [feature boxing](../glossary/#feature_boxing):
you decide what you want to do
and then build a schedule that gives you enough time to do it.
Most people believe that time boxing works better,
since it encourages developers to take smaller steps
and allows them to give customers more frequent demos
(which serve as course corrections).

FIXME: explain that waterfall doesn't exist.

## Planning and Scheduling

If you're going to spend three days driving across the country,
it makes sense to spend half an hour figuring out a good route.
Equally,
if you're going to spend several months building a complex piece of software,
*and you know what the final result is supposed to look like*,
it makes sense to spend some time figuring out what you're going to do
and how long it ought to take.
This is called [scheduling](../glossary/#scheduling);
since most students have never had to do it,
many find it the most valuable part of their first project course.
In order to explain how to go about it,
I need to describe two important roles in real software projects:
the [product manager](../glossary/#product_manager)
and the [project manager](../glossary/#project_manager).

The product manager is the person who owns the spec.
While developers are building Version N,
she is talking to customers to find out what should go into Version N+1.
She doesn't ask them what features they want;
if she does,
she'll get a mish-mash of conversations overheard in frequent flyer lounges
and buzzwords plucked from recent Twitter threads.
Instead, she asks:

1.  What can't you do right now that you want to?

1.  What do you find irritating in the current product?

1.  Why are you using our competitor's software instead of ours?

She then translates the answers into a list of features to be considered for Version N+1.
The product manager usually also talks to developers
to find out what they don't like about the current software
and adds their wishes to the pile.
Typically,
these are things like "refactor the persistence layer",
"clean up the build",
and "upgrade to the latest version of Node.js".

So, it's Monday morning.
Version N shipped last Thursday;
the team has had a weekend to catch its collective breath
and is ready to start work once again.
(If people are so burned out from the previous round that they need a whole week to recover,
go back and re-read [the first chapter](../important-stuff/).)
At this point the product manager divides up the list of desired features
and assigns them to the developers.
Each developer then has some time---typically a few days to a couple of weeks---to
do a little research,
write some throwaway prototype code,
and most importantly *think*.
How could this feature be implemented?
Is there an alternative that would take a tenth the time
but only deliver half of what was asked for?
What impact will each alternative have on the build?
On deployment?
How will the feature be tested?
And so on.

This process is called [analysis and estimation](../glossary/#a_and_e) (A&E).
The result is a short document,
typically 1--5 pages long.
There's no set form for this,
but they usually include whatever background information
a well-informed developer is unlikely to already know,
a discussion of the alternatives,
lessons learned from any prototyping that was done,
and an estimate of how much time would be needed to build each alternative.
This time includes estimates from QA (for testing),
the technical writer (for documenting),
the dev ops team responsible for managing deployment,
and so on.

So now it's Monday morning again.
Three weeks have gone by and all the A&E's are done.
When the time estimates are totaled,
they come to 700 developer-days.
Unfortunately, there are only 240 available:
the size of the team is fixed and the next release has to be available in May.
*This is normal.*
There is *never* enough time to add everything
that everyone wants to a piece of software,
and even if there was,
it probably shouldn't be done anyway.

What you do now is find a large whiteboard and draw a 3×3 grid.
The X axis is labeled "effort",
the Y axis "importance",
and each is divided into "low", "medium", and "high".

Next,
write each feature's name on a yellow sticky note
and put it on the grid.
You should wind up with something like this:

FIXME: figure

You then throw away the high-effort, low-importance items in the bottom-right three cells---you
aren't going to get to those.
Next,
you start assembling the other items into a schedule,
starting with the upper-left corner.
These are the things that will give the highest return on invested time;
more importantly,
starting with these means that if something goes wrong
the team will still have delivered something useful.

The items on the diagonal are the ones youave have to argue over.
Should the team tackle Feature 14 (high effort, high importance)
or Features 18, 19, and 22
(individually lower importance, but the same total effort)?
It can take several sessions to sort this out;
the most important thing is that people don't start shaving estimates to make things fit.
If they do,
estimators will start padding their numbers in self-defense.
Since managers aren't stupid,
they'll shave the estimates even more,
so developers will add even more padding,
at which point you might as well abandon the whole exercise.

The hardest step in this process for beginners
is coming up with time estimates for particular tasks.
How can you possibly guess how long it will take
to write a database persistence layer for some JavaScript classes
if you have never used a persistence layer before?

1.  You're not expected to pull an number out of thin air
    (at least, not by managers who know what they're doing).
    Instead,
    you should budget enough time to write some throwaway code
    or download and mess around with an open source tool
    in order to get a feel for it.

2.  You've had to learn other new technologies before
    and then apply them in courses.
    A guess based on that experience might be off by a factor of two or three,
    but it probably won't be off by a factor of ten.
    Even if it is,
    it's better than no guess at all.

Remember:
the more estimating you do the better you'll get.

## Cutting Corners

A schedule's primary purpose is not to tell you
what you're supposed to be doing on any given day,
but to tell you when you should start cutting corners.
Suppose that you have ten weeks in order to accomplish some task.
Five weeks after you start,
you've only done the first four weeks' worth of work.
You have several options:

Denial.
:   This is very popular but doesn't actually solve the problem.

Start working evenings and weekends.
:   This is also very popular, but ultimately self-defeating.
    As [the first chapter](../important-stuff/) explained,
    the quality of your work goes down when you're tired,
    so any ground you gain by working 'til three a.m.
    you lose to extra debugging and rewriting.

Ask for more time.
:   Groups working in industry often do this
    (often in combination with the previous solution),
    but it usually isn't an option in an academic setting.
    Instructors have to submit marks at the end of the term;
    as far as the university is concerned,
    whatever hasn't been done by then might as well not be done at all.

Cut corners.
:   You can either do less testing (which is quickly self-defeating)
    or update the schedule to reflect the rate at which you're actually working
    and drop features if it now shows that
    you won't be able to finish in time.

Let's return to our example.
At the start of the project
you believed it would take ten weeks.
You're now at week five through, but you've
done only the first four weeks' worth of work.
Looking at it another way,
your estimates for how long tasks would take
were too optimistic by about 25%.
You should therefore go back to your schedule
and add 25% to each task's estimate.
That means some of the things you originally planned to do
will now spill off the end of your ten-week window.
That's OK:
it's a shame you won't get to them,
but at least you know it now
and can start taking action
(like lowering your customer's expectations)
well in advance of delivery.

In the real world these calculations are
the responsibility of the project manager.
Her job is to make sure everyone is doing what they're supposed to,
to handle interruptions (there are *always* interruptions),
and to track the team's progress.
After a few weeks,
the project manager should compare how much has actually been done
with how much was supposed to be done
and adjust plans accordingly.

Real customers will thank you for doing this
provided you do it early.
"I'm sorry, we're not going to have the frobnosticator for May 1"
is OK on October 1,
or even January 1,
since it gives whoever was counting on the frobnosticator
time to make other plans.
It is *not* OK on April 30;
neither is saying (or worse, not saying) that it's "done" but full of bugs.

It's more problematic in student projects,
particularly if the instructor has specified the full feature set needed for an A.
In that case the best you can do is ask which features are worth the fewest marks
and cut those.

Taking scheduling seriously
is one of the things that distinguishes good software development teams from bad ones.
It's unfortunate that you'll only get to do it once or twice during your project course,
since you only really see the benefits with practice,
but I hope that even once will be enough to convince you that it's worth doing.

Which brings me to a pet peeve.
Engineering project management textbooks often say that
there's a tradeoff between schedule, resources, and features:
if you fix the number of people working on something
and what features they're to produce,
that determines the schedule, and so on.
Some people claim that it's actually a four-way tradeoff,
with "quality" as the fourth attribute.
That's nonsense:
if a feature only works half the time,
it isn't done.

## Agile

FIXME discussion

## Test-Driven Development

FIXME discussion
