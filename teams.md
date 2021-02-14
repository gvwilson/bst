---
title: Teams
---

Study after study has shown that
students learn better in small teams than they do on their own (FIXME Oakley ref).
As long as their teams are run well,
students achieve higher grades,
retain information longer,
are less likely to drop out of school,
and graduate with better communication skills
and a better understanding of what will be expected of them in their subsequent careers.

But that "as long as" is important.
A badly-run team is worse than no team at all,
since people will waste hours or days arguing with one another,
duplicating or undoing each other's work,
and wishing that they had gone into gardening instead.
These conflicts are more wearying than any number of buffer overruns or accidentally erased files,
which is why most computer science courses stick to individual assignments.

It doesn't take much to make a team work smoothly, though.
All you have to do is follow some common-sense advice
and be willing to stand up to people who aren't playing by the rules.

## Picking Teams

I once heard an anthropologist ask a room, "How big is a sports team?"
When people said they are all different sizes,
she explained that in fact they all have about half a dozen members.
Anything larger than that splits into smaller groups:
the forwards and backs in rugby,
the infield and outfield in baseball,
and so on.

She went on to explain that hunting parties in non-agricultural societies
are usually that size as well,
as are basic military units around the world
(a platoon is two squads of six people).
She thought there was a biological reason for this:
since we can only keep seven or so things in our short-term memory at once (FIXME cite Hock)
that's as big as a team can practically be.

The same observation applies to software development.
Three or four people can work tightly on a single piece of code,
but when there are more they define some interfaces and develop in parallel..
Collaborative tools like bug trackers allow groups to coordinate more effectively,
but the groups themselves stay the same size.

Research shows that *teams of three to five are most effective*,
at least for student projects (FIXME citation).
A team of two may not have enough breadth and background to tackle a large piece of work;
more importantly,
one or the other person is likely to take a dominant role.
If you put six people in a team,
on the other hand,
you may not be able to divide up the work in a way that will keep everyone engaged and busy.
Teams that size also increase the odds that at least one member will be
a {% include gloss key="hitchhiker" text="hitchhiker" %}.

Research also shows that *teams formed by instructors work better than
self-selected teams*. Students typically complain about this, sometimes
vehemently: they want to work with their friends, they don't want to be
slowed down by teammates who are slower or less dedicated than they are,
they have a part-time job and can only get together regularly with their
housemates, and so on.

Good instructors will ignore all of these objections except the last
one. If students are allowed to form their own groups, they tend to
clump together by ability. It's easy to see how this hurts teams of weak
students: they are less likely to be able to fill in the gaps in one
another's knowledge. However, it also hurts teams of stronger students.
As any teacher can tell you, the best way to learn something is to
explain it to someone else. Bringing a weaker teammate up to speed will
usually do more for your grade than spending those same hours hacking or
reading.

In addition, teams of strong students are more likely to use a divide
and conquer strategy, effectively reducing the project to a set of
independent sub-projects, each of which is then tackled by only one
person. This may feel more efficient, but in practice, most of the
benefits of working in a team are lost: there's less back-and-forth
discussion of design issues, and little improvement in communication
skills. Those may not be important to you, but if there is a final exam
in your course with questions about the project work, your mark on it
will depend on how much you know about your teammates' work.

There's another strong argument against self-selected teams: the
pre-existing or ongoing relationships between their members make life a
lot easier for hitchhikers, and a lot harder for everyone else. It's
hard enough to tell someone they're not pulling their weight; it's a lot
harder when that person is also on your volleyball team.

The most powerful argument for instructors selecting teams, though, is,
"That's how it works in the real world." If you join a company or an
academic research group, you won't get to pick your colleagues; you'll
be put on a project, and expected to work---and work well---with whoever
else is on it. Your performance will depend as much on your ability to
get along with others as it will on your raw technical ability, so you
might as well start practicing those skills now.

While instructors should try to include as diverse a spread of abilities
in each team as possible, they should avoid isolating at-risk students.
Members of minority groups and women are more likely to drop out of
computer science, particularly in first and second year. I'll talk about
this more in FIXME, but one of the main reasons is feeling
isolated or out of place. Research has shown shown that putting at-risk
students together in the first couple of years can mitigate this problem
<cite>Margolis2002</cite>. It is less necessary in upper
years, though, since by then students have a stronger commitment to
whatever program they're in.

The biggest headache when instructors select teams is scheduling. My
university serves a large metropolitan area; it has three campuses, and
some students commute an hour and a half each way to get to classes.
Instructors can usually take students' schedules into account when
forming teams. If the class is small, the simplest way is to get each
student to fill in a weekly timesheet showing when they're available,
and then group people who have large blocks of overlap. If the class is
larger, a web-based calendaring tool may be easier[^9]. Instructors can
even try to use whatever software the university uses to figure out
course timetables, although that usually doesn't scale down to
intra-class scheduling.

Another factor to take into account is that some people are naturally
early birds, while others are night owls. Putting the two on the same
team pretty much guarantees that someone will miss meetings, or sleep
through them, no matter when they're held. Simply asking people, "Do you
prefer to work in the morning, or the evening?" can be surprisingly
effective.

However you form teams, *each team must have at least one block of two
hours to work together each week*, outside of class. Teams should also
try to find a second block that's half an hour long for a weekly
meeting. Try to keep the two blocks separate, so that it's clear to
everyone when you're supposed to be talking about the project, and when
you're supposed to be doing design, building software, testing, and so
on. If the two are scheduled back-to-back, the meeting will drag on into
working time or vice versa.

Who Does What? {#s:teams-roles}
--------------

All right, you've formed a team: now what? How do you decide who does
what? And just as importantly, how do you make sure that everyone
actually does what they're supposed to?

There are many ways to divide project work between team members. In a
*modular decomposition*, each person is responsible for all aspects of
one part of the program. For example, one person might design and build
the GUI, while another writes the database interface, and a third
implements the business rules. This is generally a bad strategy for
three reasons:

1.  Unless the team is very disciplined, it leads to *big bang
    integration*, in which all the components meet each other for the
    first time right at the end of the project. Big bang almost always
    fails.

2.  Each team member only really understands one aspect of the project
    as a whole. This can hurt a lot if there's a final exam (which is
    just a pointed way of saying "team members will learn less").

3.  If someone drops out or fails to complete their module, the project
    as a whole will fail.

*Functional decomposition*, in which each person is responsible for one
type of task, is usually more successful. With this strategy, one person
does the testing, another handles the documentation, a third does the
bulk of the coding, and the fourth takes care of build and deployment.
This guarantees that everyone understands most of the project by the end
of the term. The obvious drawback is that each person only gets to hone
one set of skills.

Another, less obvious, drawback stems from the fact that some activities
are viewed as being more prestigious than others. If the team decomposes
work functionally, the self-appointed "alpha geeks" will usually wind up
with the plum jobs, like architecture and coding, leaving less appealing
work to people who aren't as pushy or self-confident. This tends to
reinforce existing inequities; it also tends to lower the team's overall
grade, since there's often little relationship between how outspoken
people are and how well they work.

*Uniform decomposition* is a scaled-down version of modular
decomposition that is much more effective. Instead of owning an entire
module for the lifetime of the project, each developer does the design,
coding, testing, and documentation for one small feature after another.
Working this way is central to agile development and is a good way to cope with the
never-ending timeslicing of student life.

Finally, there is *rotating decomposition*: everyone does one task for a
few weeks, then a different task for the new few, and so on[^10]. This
is initially less productive in absolute terms than either of the
preceding strategies, since the team has to pay for ramp-up several
times over. In the long term, though, it outperforms the alternatives:
it is more robust (having a team member drop out is less harmful), and
if everyone on the team is familiar with every aspect of the software,
they can all contribute to design and debugging sessions.

Any of these strategies is better than *chaotic decomposition*. If
people have different ideas about who's supposed to do what, some things
won't be done at all, while others will be done several times over. (You
can tell if your decomposition is chaotic by counting how many times
people says, "I thought *you* were doing that!" or "But I've already
done that!" The more often these phrases are heard, the more trouble
you're in.) All other decompositions tend toward chaos under pressure,
so it's important to establish rules early, and stick to them when the
going is easy, so that the instinct to do the right thing will be there
when you need it.

Your instructor may mandate a particular work decomposition. If she
does, your first team meeting should be devoted to deciding who will do
what. Do *not* allocate work on the basis of who's loudest or most
willing to interrupt: remember, there's only a weak correlation between
how confident someone is, and how competent they are
[@b:kruger-dunning-competence].

No matter what decomposition you use, your team should write, sign, and
hand in a contract outlining what everyone has agreed to do to make the
project a success. In my experience, this is a lot more effective if
students make it up themselves as their first assignment; that way, they
actually have to think about what they're promising their teammates.
Here's an example:

> We, the members of Team 12, agree the following:
>
> 1.  Work on each assignment will be divided according to role. Two
>     people will code, one will test, and one will be responsible for
>     documentation. One of the coders will run the weekly meeting; the
>     other will take minutes, and post them to the project wiki and
>     mailing list on the same day as the meeting. These roles will
>     rotate for each assignment. No one will code two assignments in a
>     row.
>
> 2.  The tester will be responsible for actually submitting the
>     assignment. Someone will only be listed as contributing to that
>     assignment if at least two other members of the team think she
>     completed, or made significant progress on, at least one work
>     item.
>
> 3.  We will aim to get at least 80% on each assignment.
>
> 4.  We will hold a half-hour status meeting every week on Thursdays at
>     4:00 pm. Everyone will attend, and be on time. If someone cannot
>     attend, they will let the rest of the team know by email no later
>     than noon on that day.
>
> 5.  Everyone will email a brief point-form summary of their progress
>     during the week to the team mailing list no later than noon on
>     Thursday. Everyone will read everyone else's summary before the
>     4:00 meeting and make a list of their questions and concerns.
>
> 6.  All email about the project will go to the team mailing list,
>     rather than person-to-person. Everyone will check email at least
>     twice a day during the week, and at least once a day on weekends.
>
> 7.  No one will check code into version control that fails to compile.
>     No one will check in code that fails to pass existing tests
>     without first getting the permission of that round's tester. No
>     one will change the database schema or add dependencies on
>     third-party or open source libraries without first getting
>     permission from the whole team.

It may sound a little silly, like those "contracts" that some parents
and children make up regarding chores and allowances, but it's actually
very effective. First, people really do have different expectations
about what being in a team means. Some people, for example, may be happy
with a bare pass; others may want the team to shoot for an A+ on
everything. Knowing who wants what won't make these tensions go away,
but it certainly helps focus the argument.

Drawing up a contract also prevents later disagreements about who
actually promised or agreed to what. As with meetings, people often remember things
differently; having a signed record is everyone's second-best
defense[^11].

I still don't know if teams should have to give copies of their
contracts to their instructors or not. On the one hand, it's a great way
to let your instructor know how you're planning to operate, and what
you're planning to achieve. Given that she probably has a lot more
experience than you, it gives her a chance to tell you if you've
forgotten anything, or how well those really cool ideas your teammate
talked you into[^12] will actually work. On the other hand, as soon as
something has to be handed in, some students will write what they think
the instructor wants to read, rather than what they actually think.

Two last notes. First, most software development teams in industry and
open source don't bother with contracts like these. There may be
corporate guidelines on good citizenship[^13], or performance metrics
written into your job spec[^14], but in general, people expect that if
you're doing this for a living, you know what others can reasonably
expect of you, and you will live up to those expectations. (This often
turns out not to be the case, which is one of the reasons so many
real-world projects fail.)

Second, if your instructor has you draw up a team contract at the start
of the project, then she can and should base part of your team's grade
on how well you stuck to it. If she handed you a team contract, she
should definitely base part of the grade on compliance. If there was no
contract at all, then I think it's unfair to turn around at the end of
the project and ask people to rate one another, since they won't have
known while they were working what they were going to be rated on.

Asking people on a team to rate their peers is a common practice in
industry. Instructors sometimes shy away from it because they're afraid
students will gives everyone in the team a high rating in order to boost
grades. However, the evidence shows that this actually occurs fairly
infrequently [@b:kaufman-felder-accounting].

What's more, as long as evaluation is based on observables, rather than
personality traits, peer assessment can actually be as accurate as
assessment by TAs and other outsiders. "Observables" means that instead
of asking, "Is the person outgoing," or "Does the person have a positive
attitude," assessments should ask, "Does the person listen attentively
during meetings," or, "Does the person attempt to solve problems before
asking for help."
Table FIXME shows a sample evaluation form, taken from
[@b:seat-mcanear-team] to get you started. To use it, rank yourself and
each of your teammates, then calculate and compare scores.

-   **Communication**

    -   Listens attentively to others without interrupting

    -   Clarifies with others have said to ensure understanding

    -   Articulates ideas clearly and concisely

    -   Gives good reasons for ideas

    -   Wins support from others

-   **Decision Making**

    -   Analyzes problems from different points of view

    -   Applies logic in solving problems

    -   Offers solutions based on facts rather than "gut feel" or
        intuition

    -   Solicits new ideas from others

    -   Generates new ideas

    -   Accepts change

-   **Collaboration**

    -   Acknowledges issues that the team needs to confront and resolve

    -   Encourages ideas and opinions even when they differ from his/her
        own

    -   Works toward solutions and compromises that are acceptable to
        all involved

    -   Shares credit for success with others

    -   Encourages participation among all participants

    -   Accepts criticism openly and non-defensively

    -   Cooperates with others

-   **Self-Management**

    -   Monitors progress to ensure that goals are met

    -   Puts top priority on getting results

    -   Defines task priorities for work sessions

    -   Encourages others to express their views even when they are
        contrary

    -   Stays focused on the task during meetings

    -   Uses meeting time efficiently

    -   Suggests ways to proceed during work sessions

Scale: Never (1), Rarely (2), Sometimes (3), Frequently (4), Always (5)

This may all seem rather fuzzy for a course that's supposed to be about
building software. But as the performance review guidelines in
FIXME shows, how well you code is only a one part of
how useful you are to a software development company.

Dealing With Conflict {#s:teams-conflict}
---------------------

Grades just came back for the second assignment. Your team got 51%,
which is far lower than you're used to. The sick feeling in the pit of
your stomach has turned to anger: you did *your* part, and so did most
of the rest of the team, but Marta didn't turn in her stuff until the
very last minute, which meant that no one else had time to spot the two
big mistakes she'd made. As for Chul, well, he didn't turn his stuff in
at all---again. If something doesn't change, this course is going to
pull your GPA down so far that you might lose your scholarship.

Situations like this come up all the time in the real world, and in all
parts of life. Broadly speaking, there are four ways you can deal with
them:

1.  Cross your fingers and hope that things will get better on their
    own, even though the last eight times you hoped they would, they
    didn't.

2.  Do extra to make up for others' shortcomings. This sometimes seems
    to work in the short term, and saves you the mental anguish of
    confronting others, but the time for that "extra" has to come from
    somewhere; what usually ends up happening is that other courses, or
    your personal life, suffer.

3.  Lose your temper and start shouting. Unfortunately, people often
    wind up displacing their anger into other parts of their life: I've
    seen developers yell at waitresses for bringing incorrect change
    when what they really needed to do was tell their boss, "No, I
    *won't* work through another holiday weekend to make up for your
    decision to short-staff the project."

4.  Take constructive steps to fix the underlying problem.

Most of us find number four hard because we don't like confrontation. If
you manage confrontation properly, though, it is a lot less bruising,
which means that you don't have to be as afraid of initiating it. Also,
if people believe that you will actually take steps when they bully,
lie, procrastinate, or do a half-assed job, they will almost always pull
up their socks.

Here are the steps you should take when you feel that a teammate isn't
pulling his or her weight:

1.  *Make sure you're not guilty of the same sin.* You won't get very
    far complaining about someone else interrupting in meetings if you
    do it just as frequently.

2.  *Check expectations.* Are you sure the offender knows what standards
    he is supposed to be meeting? This is where a team contract comes in
    useful.

3.  *Document the offense.* Write down what the offender has actually
    done, and why it's not good enough. Doing this will help you clarify
    matters in your own mind. It's also absolutely necessary if you have
    to escalate.

4.  *Check with other team members.* Are you alone in feeling that the
    offender is letting the team down? If so, that doesn't necessarily
    mean you're wrong, but it'll be a lot easier to fix things if you
    have the support of the rest of the team[^15].

5.  *Talk with the offender.* This should be a team effort: put it on
    the agenda at a team meeting, present your complaint, and make sure
    that the offender understands it. In most cases, this is enough:
    human beings are herd animals, and if someone realizes that they're
    going to be called on their hitchhiking or bad manners, they will
    usually change their ways.

6.  *Escalate as soon as there's a second offense.* Hitchhikers and
    others who really don't have good intentions are counting on you
    giving them one "last chance" after another until the term is
    finished and they can go suck the life force out of their next
    victim. *Don't fall into this trap.* If someone stole your laptop,
    you'd report it right away. If someone steals your time or your
    grades, you're being pretty generous giving them even one chance to
    mend their ways.

In the context of a student project, "escalation" means "taking the
issue to the instructor". (If you're reluctant to do this because you
don't want to be a snitch, go back and read what I just wrote about
people stealing your laptop.) Of course, your instructor has probably
had dozens of students complain to her over the years about partners and
teammates not doing their share[^16]. In order to get her to take you
seriously and help you fix your problem, you should send her an email,
signed by the whole team (or as many as you can get on side) describing
the problem and the steps you have already taken to resolve it. Make
sure the offender gets a copy as well, and ask your instructor to
arrange a meeting to resolve the issue.

This is where documentation (step three in the list above) is crucial.
Hitchhikers are usually very good at appearing reasonable; they're very
likely to nod as you present your case, then say, "Well, yes, but..."
and rhyme off a bunch of minor exceptions, or cases where others on the
team have also fallen short of expectations. If you can't back up your
complaint, your instructor will likely be left with the impression that
the whole team is dysfunctional, and nothing will improve.

One technique your instructor may ask you to use in a meeting of this
kind is *active listening*. As soon as one person makes a point, the
person on the opposite side of the issue explains it back to him, as in,
"So what I think Igor is saying is..." This guarantees that the second
person has actually paid attention to what the first person said. It can
also defuse a lot of tension, since explaining your position back to you
clearly forces the other person to see the world through your eyes, if
only for a few moments.

People to Watch Out For {#s:teams-uhoh}
-----------------------

Tolstoy wrote that all happy families resemble one another, but each
unhappy family is unhappy in its own way. Similarly, all good team
members share certain characteristics, but bad ones can be bad in many
different ways. Here are a few:

-   *Anna* knows more about every subject than everyone else on the team
    put together---at least, she thinks she does. No matter what you
    say, she'll correct you; no matter what you know, she knows better.
    Annas are pretty easy to spot: if you keep track in team meetings of
    how often people interrupt one another, her score is usually higher
    than everyone else's put together.

-   *Bao* is a contrarian: no matter what anyone says, he'll take the
    opposite side. This is healthy in small doses, but when Bao does it,
    there's always another objection lurking behind the first half
    dozen.

-   *Caitlin* has so little confidence in her own ability (despite her
    good grades) that she won't make any decision, no matter how small,
    until she has checked with someone else. Everything has to be
    spelled out in detail for her so that there's no possibility of her
    getting anything wrong.

-   *Frank* believes that knowledge is power. He enjoys knowing things
    that other people don't---or to be more accurate, he enjoys it when
    people know he knows things they don't. Frank can actually make
    things work, but when asked how he did it, he'll grin and say, "Oh,
    I'm sure you can figure it out."

-   *Hediyeh* is quiet. Very quiet. She never speaks up in meetings,
    even when she knows that what other people are saying is wrong. She
    might contribute to the mailing list, but she's very sensitive to
    criticism, and will always back down rather than defending her point
    of view. Hediyeh isn't a troublemaker, but rather a lost
    opportunity.

-   *Kenny* is a hitchhiker. He has discovered that most people would
    rather shoulder some extra work than snitch, and he takes advantage
    of it at every turn. The frustrating thing is that he's so damn
    *plausible* when someone finally does confront him. "There have been
    mistakes on all sides," he says, or, "Well, I think you're
    nit-picking." The only way to deal with Kenny is to stand up to him:
    remember, if he's not doing his share, *he's the bad guy*, not you.

-   *Melissa* would easily have made the varsity procrastination team if
    she'd bothered to show up to tryouts. She means well---she really
    does feel bad about letting people down---but somehow something
    always comes up, and her tasks are never finished until the last
    possible moment. Of course, that means that everyone who is
    depending on her can't do their work until *after* the last possible
    moment...

-   *Petra*'s favorite phrase is "why don't we". Why don't we write a
    GUI to help people edit the program's configuration files? Hey, why
    don't we invent our own little language for designing GUIs? Her
    energy and enthusiasm are hard to argue with, but argue you must.
    Otherwise, for every step you move forward, the project's goalposts
    will recede by two. This is called *feature creep*, and has ruined
    many projects that might otherwise have delivered something small,
    but useful.

-   *Raj* is rude. "It's just the way I talk," he says, "If you can't
    hack it, maybe you should find another team." His favorite phrase
    is, "That's stupid," and he uses obscenity as casually as minor
    characters in Tarantino films. His only redeeming grace is that he
    can't dissemble in front of the instructor as well as Kenny, so he's
    easier to get rid of.

-   *Sergei* is simply incompetent. He doesn't understand the problem,
    he hasn't bothered to master the tools and libraries he's supposed
    to be using, the code he checks in doesn't compile, and his
    thirty-second bug fixes introduce more problems than they solve. If
    he means well, try to re-partition the work so that he'll do less
    damage. If he doesn't, he should be treated like any other
    hitchhiker.

Irreconcilable Differences {#s:teams-failure}
--------------------------

Sometimes, it isn't just one person on the team who's a problem.
Sometimes, the whole team is dysfunctional. In the mid-1990s, for
example, I worked in a data visualization startup. Individually, we were
all smart, decent people. Put us together, though, and somehow our
personalities and IQs canceled out, leaving us all dumb and nasty.

According to [@b:oakley-teams], instructors can allow for this by
announcing at the start of the course that teams will be dissolved and
re-formed halfway through the project, *unless* every member on the team
submits a separate signed request to stay together. There's a bit of
psychology here: if people are required to ask for their team to be
dissolved, they will often think, "It's more trouble than it's worth,
I'll just put up with it." If dissolution is the default, though, then
students won't be inhibited by any stigma attached to being the one who
caused trouble.

Students also usually understand that dissolving their team and forming
a new one takes time that could be invested in earning a higher grade.
In practice, therefore, teams will almost always choose to stick
together if they see that hitchhikers and rudies are actually being
dealt with.

Respect {#s:teams-respect}
-------

And now for a topic most undergraduates would rather not think about.
There's an element of truth in the popular stereotype of programmers
having poor social skills. It might be self-selection: if you don't like
people much, or find it hard to navigate the vicious unwritten rules of
high school dances, computers will be your friends. Alternatively, it
may be something that young programmers learn from their grumpy,
poorly-dressed mentors. Whatever it is, it's bad, and you should fight
it. In particular, *if you and your teammates don't respect one another,
your project will fail*. You won't be able to run a meeting, or divide
up work fairly; you especially won't be able to cope with the pressure
when things go wrong.

People can be disrespectful on many levels. The most obvious is simple
rudeness, which in student teams usually takes the form of interrupting
people. I've been in meetings in which no one could get more than a
sentence and a half out before someone would cut them off. The signal
people send when they do that is that they think their teammates are
less intelligent than they are. In fact, the reverse is usually true: if
someone isn't smart enough to realize that letting his teammates finish
their thoughts is productive as well as polite, he's probably just not
smart, period.

Disrespect can take more serious forms. For example,
Figure [4.1](#f:women-science){reference-type="ref"
reference="f:women-science"} shows that the number of women earning
bachelor's degrees in science and engineering in the US has been
climbing steadily since the 1960s.
Figure [4.2](#f:women-cs){reference-type="ref" reference="f:women-cs"},
on the other hand, shows that the number of women earning bachelor's
degrees in Computer Science has been dropping, even as male numbers have
risen.

![Science and Engineering Degrees 1966-2004 (from
[@b:women-science-stats]).](sci-eng-degrees.png){#f:women-science}

![Computer Science Degrees 1985-2004 (from
[@b:women-science-stats]).](cs-degrees.png){#f:women-cs}

Why is that? Why are women choosing not to do computer science degrees,
even while they're entering other sciences (and professions like law and
medicine) in ever-increasing numbers?

Well, here's another fact: not only do fewer women go into computer
science than men, the dropout rate among female students is higher than
it is among males. Studies like [@b:margolis-fisher-unlocking-clubhouse]
have shown that this has nothing to do with intelligence, grades, or
ability to do the work. Instead, women are more likely to be made to
feel that they don't belong, or that computing "isn't for them". Even a
small amount of unequal pressure can have a large result: if there's
just a 10% chance per year of a female student dropping out because the
guys around her are listening to "Slap My Bitch Around" in the lab, or
because her male partners have decided to "take care of" the coding in
the graphics course project, and left the testing and documentation for
her, then *one third* of women will be gone after four years.

"Hey, survival of the fittest, dude---if women can't handle the
pressure, they should study something else." I've heard that argument
many times, and my answer is always the same: if a 200-pound Phys Ed
student came up to you, whacked you on the head, and took your wallet
and iPod, you wouldn't shrug and say, "Survival of the fittest." The
fact that what you're doing doesn't involve physical assault doesn't
make it any less unfair.

Here's a story to illustrate what I mean. The first time I taught a
programming course at the University of Toronto, I had my students write
a couple of five-line biographies for themselves as a way to get used to
checking things into CVS. In the first, they were to describe who they
were; in the second, they were to describe who they hoped to be in ten
years' time. A quarter of the male students made a point of mentioning
their "beautiful" wife in the second bio; a few even specified that she
was an actress or a model.

When I pointed this out to the class, many of them laughed. I don't
think they'd have laughed as hard if I'd said, "A quarter of the white
students think they're going to have Chinese houseboys doing their
laundry ten years from now." And if they thought that most programmers
saw them that way, I bet that fewer of them would choose to become
programmers themselves. Pervasive disrespect is like water dripping on a
stone: no single drop seems to matter much, but its erosive effects are
tremendously powerful.

It's important to realize that *the forces that make computing
uncongenial for women also make it uncongenial for a lot of men*. If
you're a guy with a well-balanced life who thinks social skills matter,
you're going to be subject to many of the same differential pressures as
your female colleagues. I think this is one of the reasons there's so
much bad software in the world: too many of the people who could make
*good* user interfaces, and elicit real requirements from customers, and
design programs that would actually meet those needs, are choosing to do
other things with their lives.

This isn't going to be easy to fix, but team programming projects give
you a chance to start. Don't monopolize the discussion, no matter how
many bright ideas you think you have; hear your teammates out, keep
*their* schedules in mind when you're thinking about leaving your share
of the work 'til the last moment, don't say anything in email that you
wouldn't say to someone's face[^17], and remember that "please" and
"thank you" are always stylish.
