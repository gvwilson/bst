---
---

A carpenter shows up to put an extension on your house, and all he's brought
with him is a hammer and a Swiss army knife. How confident are you that he'll be
able to do the job?

A programmer shows up to fix a couple of memory leaks and add a new splash
screen to your application, and all she's going to use are a plain-text editor
and a compiler. Are you any more confident in her ability to do the job in a
reasonable time?

Tools don't just help us do things more easily; they shape what we consider
possible, and encourage some working practices while discouraging others. They
also advertise how seriously we take our craft: people who want to be good at
something are willing to invest time in learning how to do it better, and in
programming, that means mastering new tools and the practices that go with them.

I actually believe that processes are more important than tools, but that's
because I know how to use whatever tools I have at hand to support the working
practices I think are most productive. However, I tell students that tools are
more important than processes because tools are more tangible: it's easier to
tell if someone is using version control or ticketing than it is to tell if
they're designing or estimating sensibly.

So here, in more-or-less priority order, are the tools you should use in your
project.

## Editor

The most important tool is your editor.  There are literally thousands to choose
from; if you want a plain text editor, your choices range from the very small
(such as Pico, which is included in most Linux installations) to the very large
(like Emacs, whose name doesn't actually stand for "eighty megabytes and
constantly swapping", and which isn't actually a Lisp-based operating system in
disguise). There are also editors that understand the syntax of particular file
formats, and can automatically indent text, complete phrases, and colorize the
stuff you're typing. Finally, there are WYSIWYG tools like Microsoft Word ;
these usually *can't* be used for programming, since they insert non-ASCII
characters and formatting information in files (even files that look
unformatted).

You might already have a favorite editor. If you're like most programmers, you
will change jobs, languages, operating systems, and nationality before you'll
switch to another, because it's taken weeks or months for your hands to master
the current one. However, what you *should* be using is an *integrated
development environment*, or IDE. These were invented in the 1970s, but didn't
really catch on until Borland released Turbo Pascal in the 1980s.  An IDE is a
workbench that includes:

-   a *code browser* that displays an overview of the packages, classes, methods,
    and data in your program;

-   a *GUI designer* that lets you build GUIs by dragging and dropping components;

-   a *console* so that you can type in expressions or call functions and see the
    results without having to start (or restart) your program;

-   a *style checker* that can warn you when your code doesn't meet naming and
    indentation conventions;

-   some *refactoring tools* to help you reorganize your code; and

-   a *test runner* to display the results of tests, and let you jump directly to
    ones that have failed.

The most popular IDE today is probably [Microsoft Visual Studio Code][vs-code],
often referred to simply as "VS Code".  It has hundreds of plugins of varying
quality to support database design, reverse engineering, a dozen different
programming languages, and more.  There are dozens of others, any of which will
make you more productive than their disconnected counterparts. Since most of
these store project data (including build instructions) in a proprietary format,
your team will do much better if you all adopt the same IDE. This will also let
you help one another solve problems and share plugins.

## Programming language

Programmers have fought religious wars over "what's the best programming
language" for as long as there have *been* programming languages. In my
experience, which one you use makes a lot less difference than most people
think…

…as long as you use the right one, that is. Fifteen years ago, there was a
pretty clear tradeoff between how quickly you can get a program running and how
fast was when it ran. Scripting languages like Perl optimized programmers' time;
low-level languages like C optimized the machine's.

Today, the balance has shifted in favor of higher-level languages. One reason is
that modern microprocessors are so complex that only a handful of human beings
can out-code optimizing compilers. Another reason is that just-in-time compilers
and generational garbage collection have made higher-level languages
intrinsically faster. The biggest, though, is that the execution time of modern
applications depends less on squeezing cycles out of processors than it used
to. The bottleneck in a dynamic web site is almost always network latency or the
time required to perform database operations; your code probably accounts for
only a few percent of the total, so doubling or tentupling its speed has less
effect than you'd think.

People still argue the merits of statically-typed and dynamically-typed
languages, though. Java vs. Python, C# vs. Ruby, mustard vs. ketchup...  I
personally prefer the latter, but I don't know of any hard evidence from
empirical studies showing that any is better. In practice, you'll usually make
this choice based on what the instructor tells you to use, what you already
know, and what gives you access to libraries you need.

If you *do* have a choice, keep in mind that dynamically-typed interpreted
languages (like Python, Ruby, Visual Basic, and Perl) are better suited to
building little tools and programming aides than statically-typed compiled
languages (like C++, Java, and C#). Since multilingual projects are harder to
manage than unilingual ones, this ought to bias you in favor of the former. On
the other hand, there are a lot more commercial-grade tools for the second group
of languages, and even today, a lot more documentation.

## Build manager

No matter what language you use, you're going to need a build manager---a tool
that will transform what you've typed into what you want to deliver. The
best-known builder in the Unix world is Make, which was invented in 1975 by a
summer intern at Bell Labs. In order to use Make, you create a configuration
file that specifies the dependencies between the files in your project, and the
commands needed to update them. For example:

```make
game.exe : game.bc graphics.bc utils.bc
        tx -E -o game.exe game.bc graphics.bc utils.bc

%.bc : %.grace
        tx -C $<
```

{: .noindent}
tells Make that `game.exe` can't be built until `game.bc`, `graphics.bc`, and
`utils.bc` exist, and that once they do, the way to create `game.exe` is to run
the `tx` compiler with several options.  Below that is a <span
g="pattern-rule">pattern rule</span> telling Make how to create any `.bc` file
from a `.grace` file with the same root name; the cryptic expression `$<` is
Make's way of saying "the first thing the target depends on".

Make was invented to recompile programs, but it can be used for a lot more.
Here, for example, is a configuration file that updates a web site:

```make
SRC_DIR = ${HOME}/webstuff
DST_DST = /www/personal/gvwilson

SRC_FILES = $(wildcard ${SRC}/*.html) $(wildcard ${SRC}/*.png)
DST_FILES = $(subst ${SRC},${DST},${SRC_FILES})

all : ${DST_FILES}

${DST}/%.html : ${SRC}/%.html
        replace AUTHOR="Greg Wilson" DATE="${DATE}" $< $@

${DST}/%.png : ${SRC}/%.png
        cp $< $@
```

This says that the source files are all the `.html` pages and `.png` images in
my `webstuff` directory. Whenever I change an HTML page, I want the `AUTHOR` and
`DATE` fields replaced with appropriate values as the file is copied to my web
site. If a PNG image changes, it should be copied over unchanged (since treating
the bytes in a PNG as ASCII characters will almost certainly result in an
unreadable image).

Make has been used by hundreds of thousands of programmers for more than thirty
years, but has some fundamental flaws. The first, as you can see, is its
syntax. The second is that it runs commands by handing them over to whatever
operating system it is running on, which make portability a constant
headache. (Quick, should you use `rm` or `del` to delete a file?) Third, Make
doesn't have a debugger: the only way to track down problems in your build
configuration is to stare at the configuration file until little drops of blood
form on your forehead.

Newer builders like Ant tried to fix the first two problems by using XML for
their configuration file syntax, and by providing a library of commands for
programmers to call (which Ant then translates into operating system calls as
necessary). Ant is now widely used in the Java world, and clones like NAnt are
popular as well, but its XML syntax is still pretty ugly, and it still doesn't
have a real debugger.

Now, I could live with ugly syntax---if Ie kan lurn Inglish speling, Ie kan lurn
eneething. But the lack of a debugger is a never-ending headache, because real
build systems aren't just configured: they're programmed. Take the HTML notes
for the course I'm currently teaching, for example: at 341 lines, the Makefile
that checks the consistency of cross-references, makes sure all the bibliography
citations are in place, updates the license, and copies files to my web site is
more complex than many programs I've written. Thinking of it as a
"configuration" file is a mistake: you *have* to approach system builds as a
programming problem. This means that every build system eventually turns into a
small programming language, which is why James Duncan Davidson, the inventor of
Ant, wrote in 2004:

> If I knew then what I know now, I would have tried using a real scripting
> language, such as JavaScript via the Rhino component or Python via JPython,
> with bindings to Java objects which implemented the functionality expressed in
> todays tasks. Then, there would be a first class way to express logic and we
> wouldn't be stuck with XML as a format that is too bulky for the way that
> people really want to use the tool.

The current generation of builders dispense with custom configuration file
syntaxes and use the data strcuctures of dynamic languages like Python and
Ruby. SCons and Rake are examples of such a system: its users write their
"configurations" as small Python or Ruby programs, making use of an extensive
support library that handles dependencies, invokes appropriate compilers, and so
on.  Debugging is still problematic, but at least it's possible.

Whatever you choose (or are told to use), stick to the following rules:

Pick something that plays nicely with your other tools.
:   Most Java editors and IDEs integrate with Ant, so that you can (for example)
    jump directly to compilation errors when they occur.

Always use the builder---never compile or copy things by hand.
:   This isn't just for efficiency's sake: if any of the twelve things you need
    to do to get your application up on your web site have to be done by hand,
    the odds are that you'll forget a crucial step right before your end-of-term
    demo, and wind up looking silly.

Always use the builder---never compile or copy things by hand.
:   Yes, I know I'm repeating myself, but this time the reason is different. If
    you do something by hand, one of your teammates might do it differently.
    "But it works on my machine!" isn't something you want to hear an hour
    before a deadline...

A good way to start using a builder is to create a "version zero" of the
project. Set up the build and make sure it works even when there isn't anything
to compile, run, test, or copy. Now add something---anything.  Does the build
still work? If it does, you're on your way.

Once you've got that, *never check anything into version control that breaks the
build*. This is one of the golden rules of working in a team: if your code won't
compile, or doesn't pass whatever automated tests you have, then putting it into
the repository means putting every other person on your team into exactly the
same broken state you're in. When you're working on your own, it's OK to use
version control as a way to transfer files from one machine to another, or as a
way to back things up at the end of the day. Do *not* carry this habit over to
teamwork.

## Debugger

A <span g="symbolic-debugger">symbolic debugger</span> is a program that allows
you to control and inspect the execution of another program. You can step
through the target program a line at a time, display the values of variables or
expressions, look at the call stack, or (my personal favorite) set *breakpoints*
to say "pause the program when it reaches this line" . Depending on the language
you're using, you may have to compile your program with certain options turned
on to make it debuggable, but that's a small price to pay for the hours or days
a debugger can save you when you're trying to track down a problem.

Some debuggers, like GDB, are standalone programs; others are build into
IDEs. Both are better than adding `print` statements to your program,
recompiling it, and re-running it, because:

-   adding `print` statements takes longer than clicking on a line and setting a
    breakpoint;

-   adding `print` statements distorts the code you're debugging by moving things
    around in memory, altering the flow of control, and/or changing the timing
    of thread execution; and

-   it's all too easy to make a mistake in the `print` statement---few things are
    as frustrating as wasting an afternoon debugging a problem, only to realize
    that the `print` statement you copied and pasted isn't displaying the values
    you thought it was.

A company I used to work for never hired people immediately. Instead,
prospective employees were put on a three-month contract. This gave us a chance
to see how well they worked, and them a chance to see if they actually wanted to
work with us.

Two things meant automatic disqualification in the assessment at the end of
those three months: checking broken code into version control, and using `print`
statements instead of a symbolic debugger. The first was justified because we
didn't want to hire people who put themselves ahead of their teammates. The
second was justified because we didn't want to hire people who were too stupid
or stubborn to program efficiently.

Over the years, I've been surprised by how strongly some programmers resist
using a debugger. The reason can't be the five or ten minutes it takes to learn
how to use one---that pays for itself almost immediately.  The only explanation
I've been able to come up with is that some people *enjoy* being
inefficient. Typing in `print` statements and paging through screens of output
lets them feel like they're being productive, when in fact they're just being
busy (which isn't the same thing at all). If your brain needs a break (which it
sometimes will), then take a break: stretch your legs, stare out a window,
practice your juggling, or do whatever else you can to take your mind away from
your problem for a few minutes. Don't drag out the process of finding and fixing
your bug by using sloppy technique just to let your brain idle for a while.

And by the way: if you're allowed to choose your teammates at the start of the
course, treat it like a job interview. Ask the people you think you might want
to work with whether they use a debugger. If they say "no", ask yourself what
impact that's going to have on your grade in the course...

## Other ways to communicate

Tickets are the best way to keep track of where you are, but there are lots of
other ways the team can and should communicate. The most popular is easily
email, which has been used to run projects since the 1970s.  It brings content
directly to people while allowing everyone to deal with issues when it's
convenient for them, and supports long-running conversations. Email really comes
into its own, though, when messages are routed through a central mailing list,
so that people don't have to remember to CC the other five people on their team,
and a shared archive can be created for later searching. The second point is as
important as the first: if you can't go back and find out what was said a month
ago---or, just as importantly, if someone *else* can't do that---you might as
well not have said it.

Wikis* seem like a good way to keep notes, create documentation, and so
on. Their strengths are a syntax that's (a little) simpler than HTML, and the
fact that content is automatically and immediately visible on the web. In
practice, you'll probably get as much mileage out of a bunch of HTML pages under
version control---you have to set up a repository anyway, and version control
systems are much better at reconciling conflicts between concurrent authors than
wikis.

Blogs, on the other hand, have proven more useful. One kind of project blog
consists of articles written by the team's members as a journal of their
progress. This is most useful for people who are watching the project from the
outside, like instructors.

The second kind of blog is one created automatically by tools. In many project
management systems, every project has a blog.  Every time someone checks code
into version control, creates or closes a ticket, or sends email, an entry is
added to that blog. This allows the project's members to see changes scroll by
in their usual blog reader, which is a handy way to keep track of what their
teammates are doing.

Finally, there's instant messaging, such as Slack. I realize it's the
communication medium of choice for all you hip young things, but I'm not a fan:

1.  IM is the most effective method ever invented for disrupting the state of
    flow that is so essential to productivity.

2.  IM conversations tend to be permanently out of phase: if you ask, "Can we
    move on to the next item?", and someone doesn't say either "yes" or "no",
    what usually happens is that you wait a minute, then move on, and then they
    pop up with a lengthy comment on the preceding item.

I think these faults can all be fixed, but until they are---oh, who am I
kidding? You're going to use IM no matter what I say. If there's more than two
people in the conversation, follow the same rules you would for a meeting. In
particular, post a summary of the conversation to your project's web site, just
as you would post meeting minutes. And if you want to figure out how to make IM
a productivity enhancer, please send me email: I'm always looking for good
graduate students.

## Portals

All of which brings us to project management portals, which do for groupware
what IDEs do for desktop tools. The best-known by far is GitHub, which hosts
millions of projects, but there are many others to choose from. A portal
typically provides a read-only view of the project's version control repository
with a issue tracker, a wiki, mailing lists, blogs, and other odds and ends.

Portals are attractive because setting up one system that does all of these
things is a lot less work than setting up one system for each. In addition, each
tool becomes more powerful when it can easily be used with others: if tickets
can easily link to change sets in version control, which can link to wiki pages,
which can link to email messages, each piece of information becomes more
valuable.

## The next level

You and your teammates could use many other tools to make yourselves more
productive. Some aren't part of the standard undergraduate curriculum yet, even
though good developers have been relying on them for a decade or more. Others
may be touched on, but only briefly, so a quick recap won't hurt.

The first is a <span g="doc-generator">documentation generator</span> like
[JSDoc][jsdoc]. This is a compiler of a sort, but instead of translating source
code into something executable, it extracts information from specially-formatted
comments and strings, and turns it into human-readable documentation.  The
justification for this is that when code and documentation are stored
separately, programmers won't keep the latter up to date. Since "rusty"
documentation can be worse than no documentation at all, it makes a lot of sense
to keep the source of the documentation right beside the code. Many introductory
courses require students to document their packages, classes, and methods this
way; it's a good habit, and one you should cultivate.

Along with testing frameworks, *style checkers* have become a lot more popular
since the turn of the century. Early style checkers looked at code to make sure
that it obeyed formatting rules, such as "no method can be longer than 100
lines" or "class names must be written in CamelCase". Today's, like PMD and
CheckStyle, can do a lot more: they can find code that is never called,
parameters that are never used, duplicated code that could be factored out, and
a lot more.

Style checkers are more properly called *static analysis* tools, since they work
by parsing the source code for your programs and looking for patterns that might
indicate problems. Compilers also do a lot of static analysis; the non-fatal
warnings they produce are a lot more useful than many students realize, and a
"zero warnings" policy can prevent a lot of subtle bugs.

Another class of tools uses *dynamic analysis*: they watch your program run, and
look for things like memory leaks, or inconsistent locking that might lead to
deadlocks or race conditions. FindBugs is the best-known in the Java world; the
Valgrind toolset is a lifesaver if you're using C or C++.

All of these tools will do a lot more for you if you adopt some kind of
*continuous integration* system, such as Travis CI.  These can be set up to run
either at regular intervals (say, every hour, or a three a.m.), or every time
someone checks into version control (which I find more useful). Each time they
run, they check a fresh copy of the project out of version control, build it,
re-run all the tests, and post the results to the project's blog, web site, and
mailing list.  This acts as a "heartbeat" for the project: as soon as anything
goes wrong, everyone knows. It also encourages good development practices: if
someone checks something in that doesn't compile, run, or pass the project's
tests, everyone will know very quickly. Funnily enough, after the system has
shamed you a couple of times, you'll stop checking in broken code...

Real development projects rely on a lot of other tools as well: schedule
builders like Microsoft Project, requirements tracing tools, visual editors for
GUIs and class diagrams, and so on. Most are bigger hammers than undergraduate
projects really require (except possibly the GUI editors), so I'd like to close
this section by asking you to invest some time in something else:
scripting. Good programmers don't just use tools, they build them. I have dozens
of small programs in my `tools` directory that do things like update my working
copies of all the projects I'm involved in or check whether the links to
Amazon.com in my course notes are still valid. Anything worth doing repeatedly
is worth automating; if you and your teammates find yourselves typing in the
same commands over and over again, *write a program to do it for you*. And
please, use a language like Python or Ruby rather than Java or C#: the "try it
and see" nature of the former is a lot better suited to one-of-a-kind scripts
than the latter's type checking and compilation.

## You may also be interested in…

A complete working environment needs more than just software.
Unfortunately, most university labs seemed designed to make everything
below difficult or impossible to achieve.

Peace and quiet.
:   Study after study has proved that this has more impact on productivity than
    a fast network, a fat disk, or caffeine, but most workplaces are still too
    crowded, too noisy, and filled with too many interrupts. As mentioned
    earlier, it takes most people ten minutes to get back into a state of flow
    after being distracted, which means that half a dozen interruptions per hour
    effectively renders someone zero percent effective. I know people say, "If I
    can't overhear what other people are talking about, I might miss something
    important," but that only applies if the only people you're overhearing are
    members of your own team (and even then, it's a dubious claim).

Comfortable seating.
:   A good chair with a firm back costs half what a mid-range laptop does. A
    full-sized keyboard (I have large hands---most laptop keyboards force me to
    bend my wrists uncomfortably) costs fifty dollars, and a lamp with a
    soft-light bulb is another forty. The combination doesn't just let me
    program longer each day; it also helps ensure that I'll still be able to
    program five or ten years from now without chronic back and wrist
    pain. Compare this with what's in most computer labs: their lighting gives
    glare without illumination, the dark desktops make the optical mice jerky,
    and the low-budget chairs are guaranteed to make your lower back ache after
    an hour.

A pad of gridded paper and several ballpoint pens.
:   I often make notes for myself when programming, or draw box-and-arrow
    diagrams of my data structures when debugging. I used to keep an editor open
    in a background window to do the former, but when my wrists started acting
    up, I discovered that taking my hands away from the keyboard for a few
    moments to scribble something down provided welcome relief. I also quickly
    discovered that the odds of me being able to read my own notes the next day
    rose dramatically if I used gridded paper to line them up.

A heavy mug for coffee or tea.
:   I don't know why, but a styrofoam cup, or a normal teacup, just isn't as
    satisfying as a little hand-sized ceramic boulder. Maybe it satisfies my
    subconscious Neanderthal urge to club my computer to death when it
    misbehaves…

A rubber duck.
:   One of the creators of Unix kept a rubber duck next to his
    computer. Whenever a bug took more than a few minutes to track down, he put
    the duck on his desk and explained the problem to it. Why? Because speaking
    out loud forces you to marshal your thoughts, which in turn highlights any
    contradictions or missed steps that you hadn't noticed while everything was
    just swirling around inside your head.

A squirt bottle of glass cleaner and a box of kleenex.
:   I can't stand smears on my screen. They drive me nuts. Whenever I'm showing
    something to someone, and they actually *touch my screen* instead of just
    pointing, I find myself reaching for that heavy mug… Then I take a breath
    and clean my screen.

A chess set, or a deck of cards, or some knitting.
:   I'm a very bad chess player. Luckily, so are most people, so it's usually
    possible to find someone at my level for a ten-minute game at lunch.  Other
    programmers I know play euchre, or knit---a programmers' "stitch and bitch"
    session can be jaw-dropping to listen to. Few people can focus for more than
    a few hours before their productivity drops; it's better to acknowledge
    this, and take a break in the middle of the day, than to say, "Must… keep…
    coding…" and produce garbage that just has to be rewritten later.

A yoga mat.
:   Back when I was a part-time grad student, I had a settled routine: I brought
    three sets of gym gear to the office at the start of the week, worked out at
    lunchtime on Monday, Wednesday, and Friday, and took my stuff home at the
    end of the week. After two months of this, I came in to find that my
    co-workers had hung a little chandelier made of air fresheners over my
    desk. Since then, I've rented a locker at the gym, but I still try to get
    some exercise several times a week---it helps my concentration and stamina a
    lot more than any amount of coffee..

Pictures.
:   Everyone wants to feel at home; everyone wants to make wherever they are
    uniquely theirs. I hang a few postcards on the wall wherever I work, along
    with a photograph of my wife and daughter taken a few months after she was
    born (my daughter, that is), just to remind me what's really important.

{% include links.md %}
