---
title: The Important Stuff
---

The things that go wrong most often in software projects have nothing to do with software.
Instead,
the worst mistakes people make are related to the human side of things.

## Crunch Mode

I used to brag about the hours I was working.
Not in so many words, of course---I had *some* social skills.
Instead, I'd show up for work around noon,
unshaven and yawning,
and casually mention how I'd been up 'til 6:00 a.m.
hacking away at some monster bug.

Looking back, I can't remember who I was trying to impress.
Instead,
what I remember is how much of the code I wrote in those all-nighters
I threw away once I'd had some sleep,
and how much damage the bugs I created in those bleary-eyed stupors did to my teammates' productivity.

My mistake was to confuse "working" with "being productive".
You can't produce software (or anything else) without doing some work,
but you can easily do lots of work without producing anything of value.
Scientific study of the issue goes back to at least the 1890s---see [[Robinson2005](../references/#Robinson2005)]
for a short, readable summary.
The most important results for developers are:

1.  Working more than eight hours a day for an extended period of time lowers your total productivity,
    not just your hourly productivity---i.e.,
    you get less done in total (not just per hour)
    when you're in crunch mode than you do when you work regular hours.

1.  Working over 21 hours in a stretch increases the odds of you making a catastrophic error
    just as much as being legally drunk.

These facts have been reproduced and verified through hundreds of experiments
over the course of more than a century.
The data behind them is as solid as the data linking smoking to lung cancer.
However,
while most smokers will admit that their habit is killing them,
people in the software industry still talk and act as if they were somehow exempt from these findings.
To quote Robinson's article:

> When Henry Ford famously adopted a 40-hour workweek in 1926,
> he was bitterly criticized by members of the National Association of Manufacturers.
> But his experiments,
> which he'd been conducting for at least 12 years,
> showed him clearly that cutting the workday from ten hours to eight hours---and
> the workweek from six days to five days---increased total worker output and reduced production cost...
> the core of his argument was that reduced shift length meant more output.
>
> ...many studies, conducted by businesses, universities, industry associations and the military,
> ...support the basic notion that, for most people,
> eight hours a day, five days per week, is the best sustainable long-term balance point
> between output and exhaustion.
> Throughout the 30s, 40s, and 50s, these studies were apparently conducted by the hundreds;
> and by the 1960s,
> the benefits of the 40-hour week were accepted almost beyond question in corporate America.
> In 1962,
> the Chamber of Commerce even published a pamphlet extolling the productivity gains of reduced hours.
>
> But, somehow, Silicon Valley didn't get the memo...

I was part of a data visualization startup in the mid-1990s.
Three months before our first release,
the head of development "asked" us to start coming in on Saturdays.
We were already pulling one late night a week at that point
(without overtime pay---our bosses seemed to think that
ten dollars' worth of pizza was adequate compensation for four hours of work)
and most of us were also working at least a couple of hours at home in the evenings.
It's hardly surprising that we missed our "can't miss" deadline by ten weeks,
and had to follow up our 1.0 release with a 1.1,
and then a 1.2,
in order to patch the crash-and-lose-data bugs we'd created.
We were all zombies,
and zombies can't code.

Those kinds of hours are sadly still normal in many parts of the software industry.
Everyone knows that designing and building software is a creative act that requires a clear head,
but many of those same people then act as if it was like digging a ditch.

The big difference is that it's hard to lose ground when digging (though not impossible).
In software,
on the other hand,
it's very easy to go backward.
It only takes me a couple of minutes to create a bug
that will take hours to track down later---or days,
if someone else is unlucky enough to have to track it down.
This is summarized in Robinson's first rule:

> Productivity varies over the course of the workday,
> with the greatest productivity occurring in the first four to six hours.
> After enough hours,
> productivity approaches zero;
> eventually it becomes negative.

It's hard to quantify the productivity of programmers, testers, and UI designers,
but five eight-hour days per week has been proven to maximize long-term total output
in every industry that has ever been studied.
There's no reason to believe that software development is any different,
or that student programming is different from full-time programming in industry.

Ah, you say, that's "long-term total output".
What about short bursts now and then,
like pulling an all-nighter to meet a deadline?
That's been studied too, and the results aren't pleasant.
Your ability to think drops by 25% for each 24 hours you're awake.
Put it another way,
the average person's IQ is only 75 after one all-nighter,
which puts them in the bottom 5% of the population.
Two all nighters in a row and their effective IQ is 50---the level at which
people are usually judged incapable of independent living.

The catch in all of this is that people usually don't notice their abilities declining.
Just like drunks who think they're still able to drive,
people who are deprived of sleep don't realize that they're not finishing their sentences (or thoughts).
They certainly don't realize that they're passing parameters into function calls the wrong way around,
or that what they're typing in will all have to be deleted and re-done tomorrow,
when it will take longer than it would have if they'd just gone home and gotten a good night's sleep.

The moral of this story?
Think very hard about what's more important to you:
the amount of good work you produce,
or how much of a martyr you appear to be.
Then think about which of those other people are actually going to care about
and pace yourself accordingly.

## Time Management

"But I have so many assignments to do!", you say.
"And they're all due at once!
I *have* to work extra hours to get them all done!"

No.
You can work *smarter* instead.
I'm less intelligent than many of the people I've worked with over the years.
I still manage to get a lot done
because I learned early on that organization and focus
are more important than raw IQ.

In order to be productive you have to do two things:
prioritize and focus.
The first is important because people are naturally very good
at spending hours on things that don't need to be done
and then finding themselves with too little time for the things that actually count.
This approach works better:

1.  Make a list of the things you have to do.
    I still use a hardcover lab notebook for this
    so that I can doodle in it when I'm on the subway,
    but a lot of people keep a personal wiki
    or send themselves email messages that then go into a folder titled "To Do".
    However you do it,
    the important thing is to *write it all down*.
    Your mind can only keep seven or so things in your short-term memory at once
    (FIXME: citation);
    if you try to manage a to-do list longer than that in your head,
    you will forget things.

2.  Weed out everything that you don't need to do right away.
    If you want to mess around with a new blogging tool that's fine,
    but that's play time not work time,
    and we're talking about getting work done.

3.  Prioritize what's left by sorting the list
    so that the most important tasks are at the top.
    I don't worry about getting the stuff below the first three or four lines into order,
    since I'm going to re-check my list before I get to them anyway.

4.  Make sure you have everything you need to see the first task through:
    files from version control,
    the assignment specification,
    whatever libraries and documentation you need,
    a fresh cup of tea,
    a comfortable chair, etc.
    Don't give yourself an excuse to interrupt your own work:
    the world will provide enough of those.

5.  Shut down your mail client and turn off instant messaging and your cell phone.
    Don't panic, it's only for an hour---most people can't stay focused longer than that,
    and you'll need to stretch your muscles and get rid of that tea you drank
    by then anyway.

6.  Set an alarm to go off in fifty minutes and *focus*.
    Don't switch tasks in that time unless you absolutely have to.
    Instead,
    if you remember an email message that needs to be sent
    or discover a couple of tests that really should be written,
    add a note to your to-do list.
    This is another reason I keep mine in a lab notebook:
    the few seconds it takes to pick up a pen and jot something down gives my hands a rest from the keyboard,
    and I'm less likely to be distracted by a notebook than by a text editor.

7.  When your time is up, take a break.
    Check mail (but don't reply to anything that isn't urgent),
    go to the washroom,
    stretch a little,
    and then re-order your to-do list and start the next round.

If any task on your list is more than an hour long,
break it down into into smaller pieces and prioritize those separately.
Keep in mind that the future is approaching at a fixed rate of one day every 24 hours:
if something's going to take sixty hours to do
you had better allow at least ten working days for it,
which means you'd better tackle the first piece two working weeks before the deadline.
And since breaking large tasks down into small ones takes time,
don't be surprised if "plan XYZ" appears as a task in your list.

The point of all this organization and preparation is
to get yourself into the most productive mental state possible.
[[Csikszentmihaly1991](../references/#Csikszentmihaly1991)] popularized the term "flow";
athletes call it "being in the zone",
while musicians talk about losing themselves in what they're playing.
Whatever name you use,
you will produce much more per unit of time in this state than normal.

That's the good news.
The bad news is that it takes roughly ten minutes to get back into a state of flow after an interruption
no matter how short the interruption was.
This means that if you are interrupted half a dozen times per hour
you are *never* at your productive peak.
It's very much like processes being paged in and out by an operating system:
if it happens too often,
the CPU spends all its time moving things around and none doing useful work.

As a concrete example,
a student of mine kept a stopwatch beside his computer for a couple of weeks during term.
Every time he read mail,
put Twitter in the foreground,
or went to Manchester United's web site
he hit the button to stop it.
At the end of two weeks
he discovered that he only spent 28% of his "working" time working.
Put it another way,
he could have finished his assignments in a third of the time they actually took.

Making lists and setting one-hour alarms will probably seem a little earnest at first,
but trust me:
your friends will stop mocking you
once they see that you're able to finish your assignments
and still have time to play some badminton and catch a movie.
They may even start to imitate you.

## Meetings

Pull requests and GitHub issues are good tools for asynchronous work,
but team meetings are often a more efficient way to make decisions,
and help build a sense of community.
Knowing how to run a meeting well
is as important as knowing how to use version control;
the rules doing so are simple but rarely followed:

Decide if there actually needs to be a meeting.
:   If the only purpose is to share information,
    have everyone send a brief email instead.
    Remember, people can read faster than they can speak:
    if someone has facts for the rest of the team to absorb,
    the most polite way to communicate them is to type them in.

Write an agenda.
:   If nobody cares enough about the meeting to prepare a point-form list of what's to be discussed,
    the meeting itself probably doesn't need to happen.
    Note that "the agenda is all the open issues in our GitHub repo" doesn't count.

Include timings in the agenda.
:   Timings help prevent early items stealing time from later ones.
    The first estimates with any new group are inevitably optimistic,
    so we should revise them upward for subsequent meetings.
    However,
    we shouldn't have a second or third meeting just because the first one ran over-time:
    instead, we should try to figure out *why* we're running over and fix the underlying problem.

Prioritize.
:   Tackle issues that will have high impact but take little time first,
    and things that will take more time but have less impact later.
    That way, if the first things run over time,
    the meeting will still have accomplished something.

Make one person responsible for keeping things moving.
:   One person should be made moderator
    and be responsible for keeping items to time,
    chiding people who are having side conversations or checking email,
    and asking people who are talking too much to get to the point.
    The moderator should *not* do all the talking:
    in fact,
    whoever is in charge will talk less in a well-run meeting than most other participants.
    This should be a rotating duty among members.

Require politeness.
:   No one gets to be rude,
    no one gets to ramble,
    and if someone goes off topic,
    it's the moderator's job to say,
    "Let's discuss that elsewhere."

No interruptions.
:   Participants should raise a finger, hand,
    put up a sticky note,
    or make another well understood gesture to indicate
    when they want to speak.
    The moderator should keep track of who wants to speak and give them time in turn.

No distractions.
:   Side conversations make meetings less efficient because
    nobody can actually pay attention to two things at once.
    Similarly,
    if someone is checking their email or texting a friend during a meeting,
    it's a clear signal that they don't think the speaker or their work is important.
    This doesn't mean a complete ban on technology---people may need accessibility aids,
    or may be waiting for a call from a dependent---but by default,
    phones should be face down and laptops should be closed
    during in-person meetings.

Take minutes.
:   Someone other than the moderator should take point-form notes
    about the most important information that was shared,
    and about every decision that was made or every task that was assigned to someone.
    This should be a rotating duty among members.

End early.
:   If the meeting is scheduled for 10:00--11:00,
    aim to end at 10:50 to give people a break before whatever they're doing next.

As soon as the meeting is over,
circulate the minutes by emailing them to everyone
or adding a text file to the project's repository:

People who weren't at the meeting can follow what's going on.
:   We all have to juggle tasks from several projects or courses,
    which means that sometimes we can't make it to meetings.
    Checking a written record
    is a more accurate and efficient way to catch up than asking a colleague,
    "So, what did I miss?"

Everyone can check what was actually said or promised.
:   More than once,
    one of us has looked over the minutes of a meeting and thought,
    "Did I say that?" or,
    "I didn't promise to have it ready then!"
    Accidentally or not,
    people will often remember things differently;
    writing them down gives everyone a chance to correct mistakes,
    misinterpretations,
    or misrepresentations.

People can be held accountable at subsequent meetings.
:   There's no point making lists of questions and action items
    if we don't follow up on them later.
    If we are using an issue-tracking system,
    we should create a ticket for each new question or task right after the meeting
    and update those that are being carried forward.
    This helps a lot when the time comes to draw up the agenda for the next meeting.

## Making Decisions

The purpose of a well-run meeting is to make decisions,
so sooner or later,
the members of a project must decide who has a say in what.
The first step is to acknowledge that every team has a power structure:
the question is whether it's formal or informal---in other words,
whether it's accountable or unaccountable [@Free1972].
The latter can work for groups of up to half a dozen people
in which everyone knows everyone else.
Beyond that,
groups need to spell out
who has the authority to make which decisions
and how to achieve consensus.
In short,
they need explicit [governance](../glossary/#governance).

[Martha's Rules](../glossary/#marthas_rules) are a practical way to do this
in groups of up to a few dozen members [[Minahan1986](../references/#Minahan1986)]:

1.  Before each meeting, anyone who wishes may sponsor a proposal.
    Proposals must be filed at least 24 hours before a meeting
    in order to be considered at that meeting, and must include:
    -   a one-line summary
    -   the full text of the proposal
    -   any required background information
    -   pros and cons
    -   possible alternatives

2.  A quorum is established in a meeting if half or more of voting members are present.

3.  Once a person has sponsored a proposal, they are responsible for it.
    The group may not discuss or vote on the issue unless the sponsor or their delegate is present.
    The sponsor is also responsible for presenting the item to the group.

4.  After the sponsor presents the proposal,
    a [sense vote](../glossary/#sense_vote) is cast for the proposal prior to any discussion:
    -   Who likes the proposal?
    -   Who can live with the proposal?
    -   Who is uncomfortable with the proposal?

5.  If all of the group likes or can live with the proposal,
    it passes with no further discussion.

6.  If most of the group is uncomfortable with the proposal,
    it is sent back to its sponsor for further work.
    (The sponsor may decide to drop it if it's clear that
    the majority isn't going to support it.)

7.  If some members are uncomfortable with the proposal,
    a timer is set for a brief discussion moderated by the meeting moderator.
    After 10 minutes or when no one has anything further to add,
    the moderator calls for a straight yes-or-no vote on the question:
    "Should we implement this decision over the stated objections?"
    If a majority votes "yes" the proposal is implemented.
    Otherwise, it is returned to the sponsor for further work.

Every group that uses Martha's Rules must make two procedural decisions:

How are proposals put forward?
:   In a software development project,
    the easiest way is to file an issue in the project's GitHub repository
    tagged *Proposal*,
    or to create a pull request containing a single file
    with the text of the proposal.
    Team members can then comment on the proposal,
    and the sponsor can revise it
    before bringing it to a vote.

Who gets to vote?
:   The usual answer is "whoever is working on the project,"
    but as it attracts more volunteer contributors,
    a more explicit rule is needed.
    One common method is for existing members to nominate new ones,
    who are then voted on using the process described above.

## Governance

Rules that people don't know about can't help them.
Once your team agrees on a project structure,
a workflow,
how to get items on a meeting agenda,
or how to make decisions,
you should therefore take the time to document this for newcomers.
This information may be included as sections in the existing `README` file
or put into files of their own:

-   `CONTRIBUTING` explains how to contribute,
    i.e.,
    what naming conventions to use for functions,
    what tags to put on issues,
    or how to install and configure the software needed to start work on the project.
    These instructions can also be included as a section in `README`;
    wherever they go,
    remember that the easier it is for people to get set up and contribute,
    the more likely they are to do so [[Steinmacher2014](../references/#Steinmacher2014)].

-   `GOVERNANCE` explains how the project is run.
    It is still uncommon for this to be in a file of its own---it is more often included
    in `README` or `CONTRIBUTING`---but open communities have learned the hard way
    that *not* being explicit about who has a voice in decisions
    and how contributors can tell what decisions have been made
    causes trouble sooner or later.

Having these files helps new contributors orient themselves,
and also signals that the project is well run.

## Conflict

You just missed an important deadline,
and people are unhappy.
The sick feeling in the pit of your stomach has turned to anger:
you did *your* part,
but Sylvie didn't finish her stuff until the very last minute,
which meant that no one else had time to spot the two big mistakes she'd made.
As for Cho,
he didn't deliver at all---again.
If something doesn't change,
contributors are going to start looking for a new project.

Conflicts like this come up all the time.
Broadly speaking, there are four ways we can deal with them:

1.  Cross our fingers and hope that things will get better on their own,
    even though they didn't the last three times.

2.  Do extra work to make up for others' shortcomings.
    This saves us the mental anguish of confronting others in the short run,
    but the time for that "extra" has to come from somewhere.
    Sooner or later,
    our personal lives or other parts of the project will suffer.

3.  Lose our temper.
    People often wind up displacing anger into other parts of their life:
    they may yell at someone for taking an extra thirty seconds to make a change
    when what they really need to do is tell their boss
    that they won't work through another holiday weekend
    to make up for management's decision to short-staff the project.

4.  Take constructive steps to fix the underlying problem.

Most of us find the first three options easiest,
even though they don't actually fix the problem.
The fourth option is harder because we don't like confrontation.
If we manage it properly,
though,
it is a lot less bruising,
which means that we don't have to be as afraid of initiating it.
Also,
if people believe that we will take steps when they bully, lie, procrastinate, or do a half-assed job,
they will usually avoid making it necessary.

Make sure we are not guilty of the same sin.
:   We won't get very far complaining about someone else interrupting in meetings
    if we do it just as frequently.

Check expectations.
:   Are we sure the offender knows what standards they are supposed to be meeting?
    This is where things like job descriptions
    or up-front discussion of who's responsible for what
    come in handy.

Check the situation.
:   Is someone dealing with an ailing parent or immigration woes?
    Have they been put to work on three other projects that we don't know about?
    Use open questions like, "Can you help me understand this?" when checking in.
    This gives them the freedom to explain something you may not have expected,
    and avoids the pressure of being asked directly about something they don't want to explain.

Document the offense.
:   Write down what the offender has actually done and why it's not good enough.
    Doing this helps us clarify what we're upset about
    and is absolutely necessary if we have to escalate.

Check with other team members.
:   Are we alone in feeling that the offender is letting the team down?
    If so, we aren't necessarily wrong,
    but it'll be a lot easier to fix things if we have the support of the rest of the team.
    Finding out who else on the team is unhappy can be the hardest part of the whole process,
    since we can't even ask the question without letting on that we are upset
    and word will almost certainly get back to whoever we are asking about,
    who might then accuse us of stirring up trouble.

Talk with the offender.
:   This should be a team effort:
    put it on the agenda for a team meeting,
    present the complaint,
    and make sure that the offender understands it.
    This is often enough:
    if someone realizes that they're going to be called on their hitchhiking or bad manners,
    they will usually change their ways.

Escalate as soon as there's a second offense.
:   People who don't have good intentions
    count on us giving them one last chance after another
    until the project is finished and they can go suck the life out of their next victim.
    *Don't fall into this trap.*
    If someone stole a laptop, we would report it right away.
    If someone steals time,
    we are being foolish if we give them a chance to do it again and again.

In academic research projects,
"escalation" means "taking the issue to the project's principal investigator".
Of course,
the PI has probably had dozens of students complain to her over the years
about teammates not doing their share,
and it isn't uncommon to have both halves of a pair tell the supervisor that they're doing all the work.
(This is yet another reason to use version control:
it makes it easy to check who's actually written what.)
In order to get her to take us seriously and help us fix our problem,
we should send her an email signed by several people
that describes the problem and the steps we have already taken to resolve it.
Make sure the offender gets a copy as well,
and ask the supervisor to arrange a meeting to resolve the issue.

> **Hitchhikers**
>
> [Hitchhikers](../glossary/#hitchhiker) who show up but never actually do anything
> are particularly difficult to manage,
> in part because they are usually very good at appearing reasonable.
> They will nod as we present our case,
> then say, "Well, yes, but..." and list a bunch of minor exceptions
> or cases where others on the team have also fallen short of expectations.
> Having collaborator guidelines and tracking progress are essential for handling them.
> If we can't back up our complaint,
> our supervisor will likely be left with the impression that the whole team is dysfunctional.

What can we do if conflict becomes more personal and heated,
especially if it relates to violations of our Code of Conduct?
A few simple guidelines will go a long way:

1.  Be short, simple, and firm.

2.  Don't try to be funny.
    It almost always backfires, or will later be used against us.

3.  Play for the audience.
    We probably won't change the person we are calling out,
    but we might change the minds or strengthen the resolve of people who are observing.

4.  Pick our battles.
    We can't challenge everyone, every time,
    without exhausting ourselves and deafening our audience.
    An occasional sharp retort will be much more effective than constant criticism.

5.  Don't shame or insult one group when trying to help another.
    For example,
    don't call someone stupid
    when what we really mean is that they're racist or homophobic.

[Captain Awkward][captain-awkward] has useful advice for discussions like these,
and [Charles' Rules of Argument][charles-rules] are very useful online.

Finally,
it's important to recognize that good principles sometimes conflict.
For example,
consider this scenario:

> A manager consistently uses male pronouns to refer to software and people of unknown gender.
> When you tell them it makes you uncomfortable to treat maleness as the norm,
> they say that male is the default gender in their first language
> and you should be more considerate of people from other cultures.

On the one hand,
we want to respect other people's cultures;
on the other hand,
we want to be inclusive of women.
In this case,
the manager's discomfort about changing pronouns
matters less than the career harm caused by them being exclusionary,
but many cases are not this clear cut.

{% include links.md %}
