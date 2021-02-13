Tooling {#s:tooling}
=======

A carpenter shows up to put an extension on your house, and all he's
brought with him is a hammer and a Swiss army knife. How confident are
you that he'll be able to do the job?

A programmer shows up to fix a couple of memory leaks and add a new
splash screen to your application, and all she's going to use are a
plain-text editor and a compiler. Are you any more confident in her
ability to do the job in a reasonable time?

Tools don't just help us do things more easily; they shape what we
consider possible, and encourage some working practices while
discouraging others. They also advertise how seriously we take our
craft: people who want to be good at something are willing to invest
time in learning how to do it better, and in programming, that means
mastering new tools and the practices that go with them.

I actually believe that processes are more important than tools, but
that's because I know how to use whatever tools I have at hand to
support the working practices I think are most productive. However, I
tell students that tools are more important than processes because tools
are more tangible: it's easier to tell if someone is using version
control or ticketing than it is to tell if they're designing or
estimating sensibly.

So here, in more-or-less priority order, are the tools you should use in
your project.

Version Control {#s:tooling-versioning}
---------------

Version control is the collective memory of the project. It's what lets
you move files from one machine to another without clobbering stuff you
just spent three hours writing, and without worrying about whether you
forgot an all-important file. It's also what lets you undo your
mistakes: if you spend an hour or two going down the wrong path, and
want to get back to where you were, version control lets you do it
reliably with a single command. And if all that wasn't enough, version
control lets you keep track of who did what, so that you can allocate
credit and blame where they're due.

Dozens of version control systems exist. For many years, CVS was the
workhorse of the open source world, and very popular in commercial
projects as well. It has now largely been replaced by Subversion, which
fixes many of CVS's flaws (while introducing a few minor ones of its
own). Alternatively, if you have money to spend, there's Perforce, which
is my personal favorite.

These three, and most others, all have the same general architecture.
The master copy of the project resides in a *repository*, which is
located on a server
(Figure [\[f:version-control-architecture\]](#f:version-control-architecture){reference-type="ref"
reference="f:version-control-architecture"}). No one ever edits the
repository files directly; instead, each member of the team keeps a
*working copy* on her machine. When she wants to share her work with her
teammates, she *commits* her files, which copies any changes she has
made to the repository. She can also *update* her working copy, which
copies changes other people have committed to the repository into her
working copy.

What happens when two or more people change the same file at the same
time? One or the other will commit first; her changes will go into the
repository. When the second person tries to commit, though, the version
control system notices the *conflict*, and gives him three options:

1.  Throw away his work.

2.  Throw away what his teammate has done.

3.  *Merge* the changes, i.e., go through the conflicts and decide what
    to keep or rewrite.

Version control means never having to say you're sorry: since the
repository keeps a record of all the changes ever checked in, any
developer who wants to can *revert* to earlier versions of files.

Using a version control system is one of the things that distinguishes
professional programmers from amateurs. Yes, you can share files by
mailing them back and forth, or copying them from one laptop to another
over wireless or with a USB stick. But why would you? A version control
system will do all the hard work for you, and get it right every time.

The only drawback of version control systems is that they work best with
plain text files---most of them don't really know what to do with binary
files, such as sound clips, images, or Microsoft Word documents. When
changes have been made to a Java source file, for example, Subversion
can find and display the lines that have been edited. When you and your
teammates all edit the Word version of your final report during the same
boring lecture, on the other hand, all Subversion can do is tell you
that the files have been changed---it can't find and highlight the
changes for you. This isn't really its fault: there are hundreds of
different binary file formats, and most don't come with tools for
diffing (i.e., finding differences) or merging. Still, programmers'
heavy use of version control is one of the things that keeps them in the
ASCII dark ages.

Editor {#s:tooling-editor}
------

The next most important tool after a version control system is your
editor. There are literally thousands to choose from; if you want a
plain text editor, your choices range from the very small (such as Pico,
which is included in most Linux installations) to the very large (like
Emacs, whose name doesn't actually stand for "eighty megabytes and
constantly swapping", and which isn't actually a Lisp-based operating
system in disguise). There are also editors that understand the syntax
of particular file formats, and can automatically indent text, complete
phrases, and colorize the stuff you're typing: JEdit for Java, Amaya for
HTML, and many others. Finally, there are WYSIWYG tools like Microsoft
Word and OpenOffice; these usually *can't* be used for programming,
since they insert non-ASCII characters and formatting information in
files (even files that look unformatted).

You probably already have a favorite editor. If you're like most
programmers, you will change jobs, languages, operating systems, and
nationality before you'll switch to another, because it's taken weeks or
months for your hands to master the current one. However, if your editor
doesn't pass the following tests, switching now will save you enough
time and grief in the future to make the temporary loss of productivity
worthwhile:

Programming Language {#s:tooling-lang}
--------------------

Programmers have fought religious wars[^24] over "what's the best
programming language" for as long as there have *been* programming
languages. In my experience, which one you use makes a lot less
difference than most people think...

...as long as you use the right one, that is. Fifteen years ago, there
was a pretty clear tradeoff between how quickly you can get a program
running[^25], and how fast was when it ran. Scripting languages like
Perl optimized programmers' time; low-level languages like C optimized
the machine's.

Today, the balance has shifted in favor of higher-level languages. One
reason is that modern microprocessors are so complex that only a handful
of human beings can out-code optimizing compilers. Another reason is
that just-in-time compilers and generational garbage collection have
made higher-level languages intrinsically faster. The biggest, though,
is that the execution time of modern applications depends less on
squeezing cycles out of processors than it used to. The bottleneck in a
dynamic web site is almost always network latency or the time required
to perform database operations; your code probably accounts for only a
few percent of the total, so doubling or tentupling its speed has less
effect than you'd think.

People still argue the merits of statically-typed and dynamically-typed
languages, though. Java vs. Python, C\# vs. Ruby, mustard vs. ketchup...
I personally prefer the latter, but I don't know of any hard evidence
from empirical studies showing that any is better. In practice, you'll
usually make this choice based on what the instructor tells you to use,
what you already know, and what gives you access to libraries you need.

If you *do* have a choice, keep in mind that dynamically-typed
interpreted languages (like Python, Ruby, Visual Basic, and Perl) are
better suited to building little tools and programming aides than
statically-typed compiled languages (like C++, Java, and C\#). Since
multilingual projects are harder to manage than unilingual ones, this
ought to bias you in favor of the former. On the other hand, there are a
lot more commercial-grade tools for the second group of languages, and
even today, a lot more documentation.

Builder {#s:tooling-builder}
-------

No matter what language you use, you're going to need a builder---a tool
that will transform what you've typed into what you want to deliver. The
best-known builder in the Unix world is Make, which was invented in 1975
by a summer intern at Bell Labs[^26]. In order to use Make, you create a
configuration file that specifies the dependencies between the files in
your project, and the commands needed to update them. For example:

`game.exe``\ `{=latex}`:``\ `{=latex}`game.bc``\ `{=latex}`graphics.bc``\ `{=latex}`utils.bc`\
`tx``\ `{=latex}`-E``\ `{=latex}`-o``\ `{=latex}`game.exe``\ `{=latex}`game.bc``\ `{=latex}`graphics.bc``\ `{=latex}`utils.bc`

`%.bc``\ `{=latex}`:``\ `{=latex}`%.grace`\
`tx``\ `{=latex}`-C``\ `{=latex}$<
\end{alltt}

\noindent tells Make that {\tt game.exe} can't be built until
{\tt game.bc}, {\tt graphics.bc}, and {\tt utils.bc} exist, and
that once they do, the way to create {\tt game.exe} is to run the
{\tt tx} compiler with several options.  Below that is a
\emph{pattern rule} telling Make how to create any {\tt .bc}
file from a {\tt .grace} file with the same root name; the cryptic
expression {\tt \$<} is Make's way of saying ``the first thing
the target depends on''.

Make was invented to recompile programs, but it can be used for
a lot more.  Here, for example, is a configuration file that updates a
web site:

\begin{alltt}
SRC_DIR =$`HOME``/webstuff`\
`DST_DST``\ `{=latex}`=``\ `{=latex}`/www/personal/gvwilson`

`SRC_FILES``\ `{=latex}`=``\ `{=latex}$(wildcard$`SRC``/*.html)``\ `{=latex}$(wildcard$`SRC``/*.png)`\
`DST_FILES``\ `{=latex}`=``\ `{=latex}$(subst$`SRC``,`${DST},$`SRC_FILES``)`

`all``\ `{=latex}`:``\ `{=latex}${DST\_FILES}$`DST``/%.html``\ `{=latex}`:``\ `{=latex}${SRC}/\%.html
        replace AUTHOR=''Greg Wilson'' DATE=''$`DATE``”``\ `{=latex}$<$`@`

${DST}/\%.png :$`SRC``/%.png`\
`cp``\ `{=latex}$<$`@`

This says that the source files are all the `.html` pages and `.png`
images in my `webstuff` directory. Whenever I change an HTML page, I
want the `AUTHOR` and `DATE` fields replaced with appropriate values as
the file is copied to my web site. If a PNG image changes, it should be
copied over unchanged (since treating the bytes in a PNG as ASCII
characters will almost certainly result in an unreadable image).

Make has been used by hundreds of thousands of programmers for more than
thirty years, but has some fundamental flaws. The first, as you can see,
is its syntax. The second is that it runs commands by handing them over
to whatever operating system it is running on, which make portability a
constant headache. (Quick, should you use `rm` or `del` to delete a
file?) Third, Make doesn't have a debugger: the only way to track down
problems in your build configuration is to stare at the configuration
file until little drops of blood form on your forehead.

Newer builders like Ant try to fix the first two problems by using XML
for their configuration file syntax, and by providing a library of
commands for programmers to call (which Ant then translates into
operating system calls as necessary). Ant is now widely used in the Java
world, and clones like NAnt are popular as well, but its XML syntax is
still pretty ugly, and it still doesn't have a real debugger.

Now, I could live with ugly syntax---if Ie kan lurn Inglish speling, Ie
kan lurn eneething. But the lack of a debugger is a never-ending
headache, because real build systems aren't just configured: they're
programmed. Take the HTML notes for the course I'm currently teaching,
for example: at 341 lines, the Makefile that checks the consistency of
cross-references, makes sure all the bibliography citations are in
place, updates the license, and copies files to my web site is more
complex than many programs I've written. Thinking of it as a
"configuration" file is a mistake: you *have* to approach system builds
as a programming problem. This means that every build system eventually
turns into a small programming language, which is why James Duncan
Davidson, the inventor of Ant, wrote in 2004:

> If I knew then what I know now, I would have tried using a real
> scripting language, such as JavaScript via the Rhino component or
> Python via JPython, with bindings to Java objects which implemented
> the functionality expressed in todays tasks. Then, there would be a
> first class way to express logic and we wouldn't be stuck with XML as
> a format that is too bulky for the way that people really want to use
> the tool.

The next generation of builders are therefore almost certainly going to
dispense with custom configuration file syntaxes, and be layered on top
of dynamic languages like Python and Ruby. SCons and Rake are examples
of such a system: its users write their "configurations" as small Python
or Ruby programs, making use of an extensive support library that
handles dependencies, invokes appropriate compilers, and so on.
Debugging is still problematic, but at least it's possible.

Whatever you choose (or are told to use), stick to the following rules:

-   *Pick something that plays nicely with your other tools.* Most Java
    editors and IDEs (Section [6.6](#s:tooling-ide){reference-type="ref"
    reference="s:tooling-ide"}) integrate with Ant, so that you can (for
    example) jump directly to compilation errors when they occur.

-   *Always use the builder---never compile or copy things by hand.*
    This isn't just for efficiency's sake: if any of the twelve things
    you need to do to get your application up on your web site have to
    be done by hand, the odds are that you'll forget a crucial step
    right before your end-of-term demo, and wind up looking silly.

-   *Always use the builder---never compile or copy things by hand.*
    Yes, I know I'm repeating myself, but this time the reason is
    different. If you do something by hand, one of your teammates might
    do it differently. "But it works on my machine!" isn't something you
    want to hear an hour before a deadline...

A good way to start using a builder is to create a "version zero" of the
project. Set up the build and make sure it works even when there isn't
anything to compile, run, test, or copy. Now add something---anything.
Does the build still work? If it does, you're on your way.

Once you've got that, *never check anything into version control that
breaks the build*. This is one of the golden rules of working in a team:
if your code won't compile, or doesn't pass whatever automated tests you
have, then putting it into the repository means putting every other
person on your team into exactly the same broken state you're in. When
you're working on your own, it's OK to use version control as a way to
transfer files from one machine to another, or as a way to back things
up at the end of the day. Do *not* carry this habit over to teamwork.

Debugger {#s:tooling-debugger}
--------

A *symbolic debugger* is a program that allows you to control and
inspect the execution of another program. You can step through the
target program a line at a time, display the values of variables or
expressions, look at the call stack, or (my personal favorite) set
*breakpoints* to say "pause the program when it reaches this line"
(Figure [\[f:debugger\]](#f:debugger){reference-type="ref"
reference="f:debugger"}). Depending on the language you're using, you
may have to compile your program with certain options turned on to make
it debuggable, but that's a small price to pay for the hours or days a
debugger can save you when you're trying to track down a problem.

Some debuggers, like GDB, are standalone programs; others are build into
IDEs (Section [6.6](#s:tooling-ide){reference-type="ref"
reference="s:tooling-ide"}). Both are better than adding `print`
statements to your program, recompiling it, and re-running it, because:

-   adding `print` statements takes longer than clicking on a line and
    setting a breakpoint;

-   adding `print` statements distorts the code you're debugging by
    moving things around in memory, altering the flow of control, and/or
    changing the timing of thread execution; and

-   it's all too easy to make a mistake in the `print` statement---few
    things are as frustrating as wasting an afternoon debugging a
    problem, only to realize that the `print` statement you copied and
    pasted isn't displaying the values you thought it was.

A company I used to work for never hired people immediately. Instead,
prospective employees were put on a three-month contract. This gave us a
chance to see how well they worked, and them a chance to see if they
actually wanted to work with us.

Two things meant automatic disqualification in the assessment at the end
of those three months: checking broken code into version control, and
using `print` statements instead of a symbolic debugger. The first was
justified because we didn't want to hire people who put themselves ahead
of their teammates. The second was justified because we didn't want to
hire people who were too stupid or stubborn to program efficiently.

Over the years, I've been surprised by how strongly some programmers
resist using a debugger. The reason can't be the five or ten minutes it
takes to learn how to use one---that pays for itself almost immediately.
The only explanation I've been able to come up with is that some people
*enjoy* being inefficient. Typing in `print` statements and paging
through screens of output lets them feel like they're being productive,
when in fact they're just being busy (which isn't the same thing at
all). If your brain needs a break (which it sometimes will), then take a
break: stretch your legs, stare out a window, practice your juggling, or
do whatever else you can to take your mind away from your problem for a
few minutes. Don't drag out the process of finding and fixing your bug
by using sloppy technique just to let your brain idle for a while.

And by the way: if you're allowed to choose your teammates at the start
of the course, treat it like a job interview. Ask the people you think
you might want to work with whether they use a debugger. If they say
"no", ask yourself what impact that's going to have on your grade in the
course...

IDE {#s:tooling-ide}
---

A smart editor, a build system, and a debugger, all talking to one
another: that's a pretty good description of an *integrated development
environment*, or IDE. These were invented in the 1970s, but didn't
really catch on until Borland released Turbo Pascal in the 1980s[^27].
Along with the tools described above, modern IDEs usually include:

-   a *code browser* that displays an overview of the packages, classes,
    methods, and data in your program;

-   a *GUI designer* that lets you build GUIs by dragging and dropping
    components;

-   an *interactive prompt* so that you can type in expressions or call
    functions and see the results without having to start (or restart)
    your program;

-   a *style checker* that can warn you when your code doesn't meet
    naming and indentation conventions;

-   some *refactoring tools* to help you reorganize your code; and

-   a *test runner* to display the results of tests, and let you jump
    directly to ones that have failed.

In short, an IDE is to programming what a well-equipped workbench is to
a carpenter. The most popular one among open source developers is
undoubtedly Eclipse , which has hundreds of plugins of varying quality
to support database design, reverse engineering, a dozen different
programming languages, and more. Microsoft Visual Studio is still my
personal favorite, largely because of how well its debugger handles
multithreaded programs; as of May 2007, the Express Edition is still
free.

There are dozens of others, any of which will make you more productive
than their disconnected counterparts. Since most of these store project
data (including build instructions) in a proprietary format, your team
will do much better if you all adopt the same IDE. This will also let
you help one another solve problems and share plugins[^28].

Ticketing {#s:tooling-ticketing}
---------

You probably have a to-do list somewhere. It might be scribbled in a
calendar or lab notebook, kept in a text file on your laptop, or in your
head; wherever and however you maintain it, it lists the things you're
supposed to do, when they're due, and (possibly) how urgent they are.

At its simplest, a *ticketing system* is a shared to-do list. Ticketing
systems are also called *bug trackers*, because most software projects
use one to keep track of the bugs that developers and users find. These
days, ticketing systems are almost invariably web-based. To create a new
ticket, you enter a title and a short description; the system then
assigns it a unique serial number
(Figure [\[f:ticketing\]](#f:ticketing){reference-type="ref"
reference="f:ticketing"}). You can usually also specify:

-   who is responsible for the ticket (e.g., who's supposed to fix the
    bug, or test the fix, or update the documentation);

-   what kind of ticket it is (a bug report, a request for a new
    feature, a question to be answered, or some other task);

-   how important it is; and

-   when it's due.

If version control keeps track of where your project has been, your
ticketing system keeps track of where you're going. After version
control, ticketing is therefore the most essential part of a team
project. Without it, you and your teammates will have to constantly ask
each other "What are you working on?", "What am I supposed to be working
on?", and "Who was supposed to do that?" Once you start using one, on
the other hand, it's easy to find out what the project's status is: just
look at the open tickets, and at those that have been closed recently.
You can use this to create agendas for your status meetings
(Section [2.1](#s:important-meetings){reference-type="ref"
reference="s:important-meetings"}), and to remind yourself what you were
doing three months ago when the time comes to write your final report
(Section [8.3](#s:wrapup-report){reference-type="ref"
reference="s:wrapup-report"}).

Of course, a ticketing system is only as useful as what you put into it.
If you're describing a bug in a large application, you should include
enough information to allow someone[^29] to reproduce the problem, and
someone else to figure out how urgent the bug is, who should work on it,
and what other parts of the application might be affected by a fix. This
is why industrial-strength ticketing systems like Bugzilla have upwards
of two dozen fields per ticket to record:

-   what version of the software you were using
    (Section [7.4](#s:design-numbering){reference-type="ref"
    reference="s:design-numbering"});

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on;

-   whatever stack traces, error reports, or log messages the program
    produced (Section [7.5](#s:design-logging){reference-type="ref"
    reference="s:design-logging"});

-   its severity (i.e., how much damage the bug might do);

-   its priority (how urgently the bug needs to be fixed); and

-   other tickets that might be related.

This is a lot more information than student projects require. In
addition, students are almost always working on several courses at once,
and it's common for students to have to put their team project aside for
a few days to work on assignments for other courses. For these reasons,
I've found that most student teams won't actually use anything more
sophisticated than a web-base to-do list unless they're forced to by the
course's grading scheme. In that case, most come away with the
impression that tickets are something you only use when you have to,
rather than a vital team coordination tool.

Other Ways to Communicate {#s:tooling-communicate}
-------------------------

Tickets are the best way to keep track of where you are, but there are
lots of other ways the team can and should communicate. The most popular
is easily *email*, which has been used to run projects since the 1970s.
It brings content directly to people while allowing everyone to deal
with issues when it's convenient for them, and supports long-running
conversations. Email really comes into its own, though, when messages
are routed through a central mailing list, so that people don't have to
remember to CC the other five people on their team, and a shared archive
can be created for later searching. The second point is as important as
the first: if you can't go back and find out what was said a month
ago---or, just as importantly, if someone *else* can't do that---you
might as well not have said it.

*Wikis* seem like a good way to keep notes, create documentation, and so
on. Their strengths are a syntax that's (a little) simpler than HTML,
and the fact that content is automatically and immediately visible on
the web. In practice, you'll probably get as much mileage out of a bunch
of HTML pages under version control---you have to set up a repository
anyway, and version control systems are much better at reconciling
conflicts between concurrent authors than wikis.

*Blogs*, on the other hand, have proven more useful. One kind of project
blog consists of articles written by the team's members as a journal of
their progress. This is most useful for people who are watching the
project from the outside, like instructors.

The second kind of blog is one created automatically by tools. In
DrProject, for example, every project has a blog called its *event log*.
Every time someone checks code into version control, creates or closes a
ticket, or sends email, an entry is added to the event log. This allows
the project's members to see changes scroll by in their usual blog
reader, which is a handy way to keep track of what their teammates are
doing.

The problem with blogs, at least right now, is that the RSS
standard[^30] that blogging relies on does not provide for
authentication: there's no uniform way for blog readers to pass
credentials like passwords to blog sites. In practice, this means that
blogs have to be open for everyone to read. This is OK for open source
projects, but it's problematic for students, since instructors usually
don't want Team A to be able to see what Team B is doing, and vice
versa. Emerging standards like OpenID may eventually solve this problem,
but for now, per-project blogs are something that instructors have to
think about very carefully.

Finally, there's *instant messaging*. I realize it's the communication
medium of choice for all you hip young things, but I'm not a fan:

1.  IM is the most effective method ever invented for disrupting the
    state of flow that is so essential to productivity
    (Section [2.3](#s:important-time){reference-type="ref"
    reference="s:important-time"}).

2.  Most chat systems don't provide "always-on" chat rooms (IRC being a
    notable exception), so every time you want to talk to all your
    teammates, you have to round them up.

3.  Most IM systems don't archive conversations in the way that mailing
    lists do, so participants have to save the chat on their personal
    machines, then upload it to the project's site. In my experience,
    that's just enough trouble for most people to never get around to
    doing it...

4.  IM conversations tend to be permanently out of phase: if you ask,
    "Can we move on to the next item?", and someone doesn't say either
    "yes" or "no", what usually happens is that you wait a minute, then
    move on, and then they pop up with a lengthy comment on the
    preceding item.

I think these faults can all be fixed, but until they are---oh, who am I
kidding? You're going to use IM no matter what I say. If there's more
than two people in the conversation, follow the same rules you would for
a meeting. In particular, post a summary of the conversation to your
project's web site, just as you would post meeting minutes. And if you
want to figure out how to make IM a productivity enhancer, please send
me email: I'm always looking for good graduate students.

Portals {#s:tooling-portal}
-------

All of which brings us to project management portals, which do for
groupware what IDEs do for desktop tools. The best-known by far is
SourceForge, which hosts over a hundred thousand open source
projects[^31], but there are many others to choose from, such as Google
Code. A portal typically provides a read-only view[^32] of the project's
version control repository with a ticketing system, a wiki, mailing
lists, blogs, and other odds and ends.

Portals are attractive because setting up one system that does all of
these things is a lot less work than setting up one system for each. In
addition, each tool becomes more powerful when it can easily be used
with others: if tickets can easily link to change sets in version
control, which can link to wiki pages, which can link to email messages,
each piece of information becomes more valuable.

Most portals are either too heavyweight for undergraduate projects, or
lack features that undergraduate courses need[^33]. Trac is a flawed
exception: it does most of the things student teams want, but can only
handle one project per installation, and doesn't offer mailing lists. We
forked[^34] Trac in 2005 to create DrProject, a portal that specifically
addresses these needs; if your instructor hasn't already picked
something out for your course, take a look at
`http://www.drproject.org`.

The Next Level {#s:tooling-next}
--------------

You and your teammates could use many other tools to make yourselves
more productive. Some aren't part of the standard undergraduate
curriculum yet, even though good developers have been relying on them
for a decade or more. Others may be touched on, but only briefly, so a
quick recap won't hurt.

The first is a *documentation generator* like Javadoc. This is a
compiler of a sort, but instead of translating source code into
something executable, it extracts information from specially-formatted
comments and strings, and turns it into human-readable documentation.
The justification for this is that when code and documentation are
stored separately, programmers won't keep the latter up to date. Since
"rusty" documentation can be worse than no documentation at all, it
makes a lot of sense to keep the source of the documentation right
beside the code[^35]. Many introductory courses require students to
document their packages, classes, and methods this way; it's a good
habit, and one you should cultivate.

Another tool you should be fanatical about is some kind of *test
harness* that can re-run your tests for you at the push of a button. I
won't repeat the arguments in favor of test-driven development
(Section [5.5](#s:process-tdd){reference-type="ref"
reference="s:process-tdd"}) here; suffice to say that while *you* won't
ever make silly mistakes, your teammates undoubtedly will, and testing
is your best way to prevent them from sinking your project.

The most widely used test harness today is JUnit[^36]. Programmers write
tests as methods, and group them together into classes. JUnit uses
*reflection* to find and execute the tests, keeping track of how many
pass, fail, or encounter unexpected errors (which usually indicate that
the test itself is broken, rather than the code under test). Every
modern Java IDE can run JUnit tests and display the results, typically
with a red bar if some tests are failing, or a green one if all have
passed.

Clones of JUnit exist for most major programming languages, as do
extensions of various kinds for testing web applications (HttpUnit),
databases (SqlUnit), and how systems behave under heavy load
(JUnitScenario). Whatever your project is building, there's probably a
JUnit extension to help you.

Along with testing frameworks, *style checkers* have become a lot more
popular since the turn of the century. Early style checkers looked at
code to make sure that it obeyed formatting rules, such as "no method
can be longer than 100 lines" or "class names must be written in
CamelCase". Today's, like PMD and CheckStyle, can do a lot more: they
can find code that is never called, parameters that are never used,
duplicated code that could be factored out, and a lot more.

Style checkers are more properly called *static analysis* tools, since
they work by parsing the source code for your programs and looking for
patterns that might indicate problems. Compilers also do a lot of static
analysis[^37]; the non-fatal warnings they produce are a lot more useful
than many students realize, and a "zero warnings" policy can prevent a
lot of subtle bugs.

Another class of tools uses *dynamic analysis*: they watch your program
run, and look for things like memory leaks, or inconsistent locking that
might lead to deadlocks or race conditions. FindBugs is the best-known
in the Java world; the Valgrind toolset is a lifesaver if you're using C
or C++.

All of these tools will do a lot more for you if you adopt some kind of
*continuous integration* system, such as CruiseControl or BuildBot.
These can be set up to run either at regular intervals (say, every hour,
or a three a.m.), or every time someone checks into version control
(which I find more useful). Each time they run, they check a fresh copy
of the project out of version control, build it, re-run all the tests,
and post the results to the project's blog, web site, and mailing list.
This acts as a "heartbeat" for the project: as soon as anything goes
wrong, everyone knows. It also encourages good development practices: if
someone checks something in that doesn't compile, run, or pass the
project's tests, everyone will know very quickly. Funnily enough, after
the system has shamed you a couple of times, you'll stop checking in
broken code...

Real development projects rely on a lot of other tools as well: schedule
builders like Microsoft Project, requirements tracing tools, visual
editors for GUIs and class diagrams, and so on. Most are bigger hammers
than undergraduate projects really require (except possibly the GUI
editors), so I'd like to close this section by asking you to invest some
time in something else: scripting. Good programmers don't just use
tools, they build them. I have dozens of small programs in my `tools`
directory that do things like update my working copies of all the
projects I'm involved in[^38] or check whether the links to Amazon.com
in my course notes are still valid. Anything worth doing repeatedly is
worth automating; if you and your teammates find yourselves typing in
the same commands over and over again, *write a program to do it for
you*. And please, use a language like Python or Ruby rather than Java or
C\#: the "try it and see" nature of the former is a lot better suited to
one-of-a-kind scripts than the latter's type checking and compilation.

You May Also Be Interested In... {#s:tooling-other}
--------------------------------

A complete working environment needs more than just software.
Unfortunately, most university labs seemed designed to make everything
below difficult or impossible to achieve.

-   *Peace and quiet.* Study after study has proved that this has more
    impact on productivity than a fast network, a fat disk, or caffeine,
    but most workplaces are still too crowded, too noisy, and filled
    with too many interrupts. As mentioned in
    Section [2.3](#s:important-time){reference-type="ref"
    reference="s:important-time"}, it takes most people ten minutes to
    get back into a state of flow after being distracted, which means
    that half a dozen interruptions per hour effectively renders someone
    zero percent effective. I know people say, "If I can't overhear what
    other people are talking about, I might miss something important,"
    but that only applies if the only people you're overhearing are
    members of your own team (and even then, it's a dubious claim).

-   *Comfortable seating.* A good chair with a firm back costs one fifth
    of what a mid-range PC does. A full-sized keyboard (I have large
    hands---most laptop keyboards force me to bend my wrists
    uncomfortably) costs fifty dollars, and a lamp with a soft-light
    bulb is another forty. The combination doesn't just let me program
    longer each day; it also helps ensure that I'll still be able to
    program five or ten years from now without chronic back and wrist
    pain. Compare this with what's in most computer labs: their lighting
    gives glare without illumination, the dark desktops make the optical
    mice jerky, and the low-budget chairs are guaranteed to make your
    lower back ache after an hour. In short, they look like the kind of
    places that get full-page spreads in architectural magazines; as
    [@b:brand-how-buildings-learn] points out, those are rarely
    comfortable places to work.

-   *A pad of gridded paper and several ballpoint pens.* I often make
    notes for myself when programming, or draw box-and-arrow diagrams of
    my data structures when debugging. I used to keep an editor open in
    a background window to do the former, but when my wrists started
    acting up, I discovered that taking my hands away from the keyboard
    for a few moments to scribble something down provided welcome
    relief. I also quickly discovered that the odds of me being able to
    read my own notes the next day rose dramatically if I used gridded
    paper to line them up.

-   *A heavy mug for coffee or tea.* I don't know why, but a styrofoam
    cup, or a normal teacup, just isn't as satisfying as a little
    hand-sized ceramic boulder. Maybe it satisfies my subconscious
    Neanderthal urge to club my computer to death when it misbehaves...

-   *A rubber duck.* One of computing's many apocryphal stories holds
    that someone---Brian Kernighan, maybe, or Dennis Ritchie---keeps a
    rubber duck next to his computer. Whenever a bug takes more than a
    few minutes to track down, he puts the duck on his desk and explains
    the problem to it. Why? Because speaking out loud forces you to
    marshal your thoughts, which in turn highlights any contradictions
    or missed steps that you hadn't noticed while everything was just
    swirling around inside your head.

-   *A squirt bottle of glass cleaner and a box of kleenex.* I can't
    stand smears on my screen. They drive me nuts. Whenever I'm showing
    something to someone, and they actually *touch my screen* instead of
    just pointing, I have another Neanderthal fantasy, except this time
    it's not subconscious...

-   *A chess set*, or a deck of cards, or some juggling balls. I'm a
    very bad chess player. Luckily, so are most people, so it's usually
    possible to find someone at my level for a ten-minute game at lunch.
    Other programmers I know play euchre, or knit---a programmers'
    "stitch and bitch" session can be jaw-dropping to listen to. Few
    people can focus for more than a few hours before their productivity
    drops; it's better to acknowledge this, and take a break in the
    middle of the day, than to say, "Must... keep... coding..." and
    produce garbage that just has to be rewritten later.

-   *Books.* You can find a lot on-line, but it's hard to google with
    your feet up on your desk, and even harder to fold down the corners
    on web pages. When I want API documentation, I use the web; when I
    want a tutorial, I still prefer the printed page. Right now, for
    example, I have [@b:berkun-art-proj-mgmt],
    [@b:doar-practical-dev-env], [@b:fogel-producing-open-source], and
    [@b:ely-marmot-understanding-offices] within reach.

-   *Running shoes.* Back when I was a part-time grad student, I had a
    settled routine: I brought three sets of gym gear to the office at
    the start of the week, worked out at lunchtime on Monday, Wednesday,
    and Friday, and took my stuff home at the end of the week. After two
    months of this, I came in to find that my co-workers had hung a
    little chandelier made of air fresheners over my desk. Since then,
    I've rented a locker at the gym, but I still try to get some
    exercise several times a week---it helps my concentration and
    stamina a lot more than any amount of coffee..

-   *Pictures.* Ah, the nesting instinct. Everyone wants to feel at
    home; everyone wants to make wherever they are uniquely theirs. I
    hang a few postcards on the wall wherever I work, along with a
    photograph of my wife and daughter taken ten hours after she was
    born (my daughter, that is), just to remind me what's really
    important.

Design {#s:design}
======

Building large programs with other people is different from building
small programs on your own. This section describes a few of the things
that you'll want to do in the former case that might not crop up in your
regular classes.

I should confess up front that I can't tell you how to design software.
I don't know anyone who can, either. I can *show* you by working through
examples on a whiteboard, asking rhetorical questions, and setting
problems for you to think about, but that doesn't translate well to
print. If you can talk a handful of good software designers into letting
themselves be videotaped as they work through problems on a whiteboard,
please let me know---I'm sure I'd learn a lot by watching them.

Describing Designs {#s:design-describe}
------------------

I can, however, tell you a little about how to describe designs. If you
watch experienced developers drawing on the whiteboard as they're
talking to one another, you'll generally see them sketching the
following:

-   *Data structures*. These are blob-and-arrow pictures of the objects
    and containers that make up the program, and the references that
    stitch them together. The more experience someone has, the fewer of
    these they need to draw, but everyone falls back on them eventually
    (particularly during difficult debugging sessions).

-   *Schemas* or *data models*. These can be fairly literal pictures of
    the tables in a database, possibly augmented with arrows to show
    what's a foreign key for what, or entity-relationship diagrams that
    show the things the system stores, and the relationships between
    them.

-   The *conceptual architecture* of the system. This is the most
    important diagram of all, since it's the "big picture" view of how
    everything in the system fits together. It's also the least
    constrained, since it can include everything from specific sections
    of configuration files to class hierarchies to replicated web
    servers. I'll talk more about conceptual architectures below.

-   The system's *physical architecture*, which is the files, processes,
    sockets, database tables, etc., that make it up. In most cases, this
    consists of a bunch of boxes representing the machines the
    application's components run on, trees showing files and
    directories, and circles showing running processes. A lot of this
    stuff can show up in the conceptual architecture as well.

-   The *workflow architecture*, which shows how users accomplish the
    things they want to do. This is almost always drawn as a finite
    state machine. In the web world, it is often called a *navigation
    diagram* or *roadmap*; each blob represents a page, and the arrows
    connecting them show how users can navigate from one page to
    another.

With the exception of schemas and data models, all these diagrams
consist of *components* and *connectors*, i.e., things and the
relationships between them. In a physical architecture diagram, for
example, the components represent machines, processes, and files, and
the connectors represent sockets and the "reads/writes" relationship for
files.

The most important diagram is the conceptual architecture, which is the
"big picture" view of how the most important pieces of the system relate
to one another. What qualifies as "important" depends on what aspect(s)
of the system you're currently concerned with. If I'm trying to explain
a bug that only arises when the application is configured incorrectly, I
might draw its configuration files, and the database tables that store
user preferences, but leave out the password database and log files
entirely. If we're trying to figure out a better load balancing
strategy, on the other hand, I would draw most of what would go into a
physical architecture diagram, plus just enough of the class inheritance
hierarchy to show how the servers will load user request handlers
dynamically.

The goal of these diagrams is always to help your readers, listeners, or
viewers (including yourself) understand enough of the system to be able
to decide what to do next. This is why I'm not a fan of the *Unified
Modeling Language* (UML). UML defines over a dozen different types of
diagrams for showing the relationships between classes, the order in
which things happen when methods are invoked, the states a system goes
through when performing an action, and so on.

Hundreds of books and thousands of articles have been written about UML,
and no other notation is as well described. That's the good news; the
bad news is that in all the years I've been programming, I've only ever
met one person who drew UML diagrams of his own free will on a regular
basis. I've known a handful of other people who occasionally sketched
class diagrams as part of a larger description of a design, and that's
pretty much it. When I contrast that with blueprints in architecture, or
flow diagrams in chemical engineering, the only conclusion I can reach
is that software developers don't actually find UML very helpful.

I think there are several reasons for this, including its lack of a
well-defined semantics and the fact that UML diagrams can't be diffed
and merged by version control systems
(Section [6.1](#s:tooling-versioning){reference-type="ref"
reference="s:tooling-versioning"}). However, since it's all that we
have, in most books, likely to be on the final exam, and might come up
in an interview, it's still worth mastering the basics.

Getting Started {#s:design-start}
---------------

What if you're starting with a blank sheet of paper (or an empty
whiteboard)? How do you describe something that doesn't exist yet? The
best way to start is to write your elevator pitch
(Section [3.2](#s:basics-pitch){reference-type="ref"
reference="s:basics-pitch"}). Next, write one or two paragraph-long
stories describing how the application, feature, or library would be
used. Be as concrete as possible: instead of saying, "Allows the user to
find overlaps between their calendar and their friends' calendars," say,
"The user selects one or more of her friends' calendars (and optionally
her own), and the system displays a page showing events that two or more
people are going to, color coded to show how popular they are."

Once you have those narratives, go through and highlight the key
"things" and "relationships" you've just described. In the example
above, you would highlight "user", "friend", "calendar", "event",
"page", and so on. As soon as you try to draw a blob-and-arrow diagram
showing how these are related to one another, you'll have to start
making design decisions: for example, is "friend" an entity, or a
relationship between two entities (i.e., is it a blob or an arrow)?

If, during this process, you hear yourself say, "We'll use a linked list
to..." then step back and catch your breath. Details like that do need
to be worked out at some point, but:

-   you're probably worrying about that as a way to *not* think about
    the bigger design questions (which are scarier for beginners);

-   you probably don't know enough yet about your design to make the
    right decision; and

-   you're probably a good enough coder by now that you can worry about
    that when the time comes to actually write the code. Remember, not
    everything actually needs to be designed...

Once you have a diagram---any kind of diagram---you should start
iterating around it. Pick one open problem (such as "how will users
control who can see their calendars?"), think of a way to solve it
("they can mark them as 'public', or invite specific people to view
them"), figure out how to implement your solution, then revisit any
previous decisions that your most recent decisions affect. Design is a
very cyclic process: every time you add or change one thing, no matter
how small, you may need to go back and re-design other things.

There are two traps here for the inexperienced. The first is *analysis
paralysis*, in which you find yourself revisiting issues over and over
again without ever making any decisions that stick. The second is the
*already invented here* syndrome, in which someone (possibly you) says,
"Look, we've already made a decision about that, let's not reopen the
debate." Either can sink a project; together, they show why it's so hard
to teach design, since what I'm basically saying is, "Argue enough, but
not too much." Helpful, isn't it?

Design for Testability {#s:design-testability}
----------------------

When most developers hear the word "design", they think about either the
application's structure or its user interface. If you don't think about
how you're going to test your application while you're designing it,
though, the odds are very good that you'll build something that can't
(or cannot easily) be tested. Conversely, if you *design for test*,
it'll be a lot easier to check whether your finished application
actually does what it's supposed to.

For example, let's consider a typical three-tier web site that uses the
Model-View-Controller (MVC) design pattern
(Figure [\[f:design-mvc\]](#f:design-mvc){reference-type="ref"
reference="f:design-mvc"}). The model, which is stored in a relational
database, is the data that the application manipulates, such as purchase
orders and game states. The controller layer encapsulates the
application's business rules: who's allowed to cancel games while
they're in progress, how much interest to add on out-of-province orders,
and so on. Finally, the view layer translates the application's state
into HTML for display to the user.

This architecture presents (at least) three challenges from the point of
view of testing:

1.  Unit testing libraries like JUnit (and its clones in other
    languages) aren't built to handle this: as the word "library"
    implies, they're made up of code that's meant to be called *within*
    a process. Despite the ubiquity of multi-process applications, most
    debuggers and testing libraries cannot track "calls" *between*
    processes.

2.  Configuring a test environment is a pain: you have to set up a
    database server, clear the browser's cache, make sure the right
    clauses are in your Apache configuration file, and so on.

3.  Running tests is slow. In order to ensure that tests are
    independent, you have to create an entirely new fixture for each
    test. This means reinitializing the database, restarting the web
    server, and so on, which can take several seconds *per test*. That
    translates into an hour or more for a thousand tests, which is
    pretty much a guarantee that developers won't run them routinely
    while they're coding, and might not even run them before checking
    changes in.

The first step in fixing this is to get rid of the browser and web
server. One way to do this is to replace the browser with a script that
generates HTTP requests as multi-line strings and passes them to a "fake
CGI" library via a normal function call
(Figure [\[f:design-back-end\]](#f:design-back-end){reference-type="ref"
reference="f:design-back-end"}). After invoking our actual program, the
fake CGI library passes the text of an HTTP response back to our script,
which then checks that the right values are present (about which more in
a moment). The "fake CGI" library's job is to emulate the environment
the web app under test would see if it was being invoked as a CGI by
Apache: environment variables are set, standard input and output are
replaced by string I/O objects, and so on, so that the web app has no
(easy) way of knowing that it's being invoked via function call, rather
than being forked.

Why go through this rigmarole? Why not just have a top-level function in
the web app that takes a URL, a dictionary full of header keys and
values, and a string containing the POST data, and check the HTML page
it generates? The answer is that structuring our tests in this way
allows us to run them both in this test harness, and against a real
system. By replacing the fake CGI adapter with code that sends the HTTP
request through a socket connected to an actual web server, and reads
that server's response, we can check that our application still does
what it's supposed to when it's actually deployed. The tests will run
much more slowly, but that's OK: if we've done our job properly, we'll
have caught most of the problems in our faked environment, where
debugging is much easier to do.

Now, how to check the result of the test? We're expecting HTML, which is
just text, so why not store the HTML page we want in the test and do a
string comparison? The problem with that literal approach is that every
time we make any change at all to the format of the HTML, we have to
rewrite every test that produces that page. Even something as simple as
introducing white space, or changing the order of attributes within a
tag, will break string comparison.

A better strategy is to add unique IDs to significant elements in the
HTML page, and only check the contents of those elements. For example,
if we're testing login, then somewhere on the page there ought to be an
element like this:

`<div``\ `{=latex}`id="currentuser">Logged``\ `{=latex}`in``\ `{=latex}`as``\ `{=latex}`<strong>gvwilson</strong>`\
`(<a``\ `{=latex}`href="http://www.drproject.org/logout">logout</a>`\
`|`\
`<a``\ `{=latex}`href="http://www.drproject.org/preferences">preferences</a>)`\
`</div>`

We can find that pretty easily with an *XPath* query, or by crawling the
DOM tree produced by parsing the HTML ourselves[^39]. We can then move
the `div` around without breaking any of our tests; if we were a little
more polite about formatting its internals (i.e., if we used something
symbolic to highlight the user name, and trusted CSS to do the
formatting), we'd be in even better shape.

We've still only addressed half of our overall problem, though: our web
application is still talking to a database, and reinitializing it each
time a test runs is sloooooooow.

We can solve this by moving the database into memory
(Figure [\[f:design-replacing-db\]](#f:design-replacing-db){reference-type="ref"
reference="f:design-replacing-db"}). Most applications rely on an
external database server, which is just a long-lived process that
manages data on disk. An increasingly-popular alternative is the
*embedded* database, in which the database manipulation code runs inside
the user's application as a normal library. Berkeley DB (now owned by
Oracle) and SQLite (still open source) are probably the best known of
these; their advocates claim they are simpler to build and faster to
run, although there are lots of advantages to using servers as well.

The advantage of embedded databases from a testing point of view is that
they can be told to store data in memory, rather than on disk. This
would be a silly thing to do in a production environment (after all, the
whole point of a database is that it persists), but in a testing
environment, it can speed things up by a factor of a thousand or more,
since the hard drive never has to come into play. The cost of doing this
is that you have to either commit to using one database in both
environments, or avoid using the "improvements" that different databases
have added to SQL.

Once these changes have been made, the application zips through its
tests quickly enough that developers actually will run the test suite
before checking in changes to the code. The downside is the loss of
*fidelity*: the system we're testing is a close cousin to what we're
deploying, but not exactly the same. However, this is a good economic
tradeoff: we may miss a few bugs because our fake CGI layer doesn't
translate HTTP requests exactly the same way Apache and Python's
libraries do, but we catch (and prevent) a lot more by making testing
cheap.

This example just scratches the surface of designing for testability. If
you want to go further, [@b:meszaros-xunit] includes some good
discussion of how to make things more testable, and in 2007, Michael
Bolton posted a fairly complete list of things developers can do to the
Agile Testing list:

1.  scriptable interfaces to the product, so that we can drive it more
    easily with automation

2.  logging of activities within the program

3.  monitoring of the internals of the application via another window or
    output over the network

4.  simpler setup of the application

5.  the ability to change settings or configuration of the application
    on the fly

6.  clearer error/exception messages, including unique identifiers for
    specific points in the code, or *which* damn file was not found

7.  availability of modules separately for earlier integration-level
    testing

8.  information about how the system is intended to work (ideally in the
    form of conversation or "live oracles" when that's the most
    efficient mode of knowledge transfer)

9.  information about what has already been tested (so we don't repeat
    someone else's efforts)

10. access to source code for those of us who can read and interpret it

11. improved readability of the code (thanks to pairing and refactoring)

12. overall simplicity and modularity of the application

13. access to existing ad hoc (in the sense of "purpose-built") test
    tools, and help in creating them where needed

14. proximity of testers to developers and other members of the project
    community

Adam Goucher added two more:

15. a "stub mode" where you can test a module without needing another
    module reading/working

16. information about what has changed since the last code delivery in
    order to better target testing

Of these, numbers 2, 6, 7, 9, and 15 are the most important for
students' projects; most of the others only really come into play when
you're building something very large, or have a team that's so big that
it has to be broken down into functional groups. That said, they're all
still good ideas at every level of development.

Keeping Track {#s:design-numbering}
-------------

If your project is run like most, you're going to submit your work
several times over the course of the term. That means it's important for
you to keep track of exactly what version you're working on at any time,
where it came from, and where it's going.

The usual way to do this is with *version numbers*. If you see a number
like "6.2.3.1407" attached to a piece of software, it generally means:

-   major version 6

-   minor version 2

-   patch 3

-   build 1407

The major version number is only incremented when significant changes
are made. In practice, "significant" means "changes that make it
impossible for older versions to read the new version's data or
configuration files". In practice, major version numbers are often under
the control of the marketing department---if a competitor releases a new
major version, we'd pretty much have to as well.

Minor version numbers are what most people think of as releases. If
you've added a few new features, changed part of the GUI, etc., you
increment the minor version number so that your customers can talk
intelligently about which version they have.

Patches are things that don't have their own installers. If, for
example, you need to change one HTML form, or one DLL, you will often
just mail that out to customers, along with instructions about where to
put it, rather than creating a new installer. You should still give it a
number, though, and make an entry in your release log[^40].

The build number is incremented every time you create a new version of
the product for QA to test. Build numbers are never reset, i.e. you
don't go from 5.2.2.1001 to 6.0.0.0, but from 5.2.2.1001 to 6.0.0.1002,
and so on. Build numbers are what developers care about: they're often
only matched up with version numbers after the fact (i.e. you create
build \#1017, QA says, "It looks good," so you say, "All right, this'll
be 6.1.0," and voila, you have 6.1.0.1017.)

Finally, groups will sometimes identify pre-releases as "beta 1", "beta
2", and so on, as in "6.2 beta 2". Again, this label is usually attached
to a particular build after the fact---you wait until QA (or whoever)
says that build \#1017 is good enough to send out to customers, then tag
it in version control.

A four-part numbering scheme is more than you need for an undergraduate
course. You can probably get away with just two numbers: one to identify
the assignment the software was submitted for, and another to identify
the files that went into that "release".

Why include this in a discussion of design? Well, it turns out that
Subversion and other version control systems will include version
numbers automatically in every file
(Section [7.4](#s:design-numbering){reference-type="ref"
reference="s:design-numbering"}). If you put the string `$Revision:$` in
a file, and set the `svn:keywords` property on that file, then every
time you commit changes, Subversion will replace everything between the
colon and the trailing dollar sign with the revision number of the file.
Subversion will do the same thing for `Author`, `Date`, and several
other keywords.

For example, if the file contains:

`#``\ `{=latex}`cleanup.py``\ `{=latex}`:``\ `{=latex}`Clean``\ `{=latex}`up``\ `{=latex}`files``\ `{=latex}`left``\ `{=latex}`behind``\ `{=latex}`by``\ `{=latex}`the``\ `{=latex}`CAD``\ `{=latex}`software.`\
`#``\ `{=latex}$Revision: 81$\
`#``\ `{=latex}$Author: aturing$

`import``\ `{=latex}`sys,``\ `{=latex}`os`\
`…`

and Grace Hopper commits changes that update the repository to version
99, the file will be changed to:

`#``\ `{=latex}`cleanup.py``\ `{=latex}`:``\ `{=latex}`Clean``\ `{=latex}`up``\ `{=latex}`files``\ `{=latex}`left``\ `{=latex}`behind``\ `{=latex}`by``\ `{=latex}`the``\ `{=latex}`CAD``\ `{=latex}`software.`\
`#``\ `{=latex}$Revision: \textbf{99}$\
`#``\ `{=latex}$Author: \textbf{ghopper}$

`import``\ `{=latex}`sys,``\ `{=latex}`os`\
`…`

Now, take a look at this snippet of Java:

`public``\ `{=latex}`class``\ `{=latex}`Student``\ `{=latex}`extends``\ `{=latex}`Person``\ `{=latex}\
`public``\ `{=latex}`static``\ `{=latex}`final``\ `{=latex}`String``\ `{=latex}`Revision``\ `{=latex}`=``\ `{=latex}`"$Revision:``\ `{=latex}`82";`\
`…`\
`public``\ `{=latex}`String``\ `{=latex}`getRevision()``\ `{=latex}\
`return``\ `{=latex}`Revision;`\
\

Whenever a change to this file is committed to version control, the
class's version number is automatically updated. Inside a running
program, you can then ask any `Student` object, "What version of this
class are you?" (As an exercise, write a method that strips the front
and back off the revision string, and returns the revision number as an
integer.) If you are working with systems that load classes dynamically,
like the Tomcat servlet container or the Eclipse IDE, knowing exactly
which version of your code has actually been loaded can save you many,
many hours.

Logging {#s:design-logging}
-------

Something else you can design into your system to make your life easier
later on is *logging*. This is the grown-up way to debug with print
statements. Instead of writing:

`def``\ `{=latex}`extrapolate(basis,``\ `{=latex}`case):`\
`print``\ `{=latex}`"entering``\ `{=latex}`extrapolate..."`\
`trials``\ `{=latex}`=``\ `{=latex}`count_basis_width(basis)`\
`if``\ `{=latex}`not``\ `{=latex}`trials:`\
`print``\ `{=latex}`"...no``\ `{=latex}`trials!"`\
`raise``\ `{=latex}`InvalidDataException("no``\ `{=latex}`trials")`\
`print``\ `{=latex}`"...running",``\ `{=latex}`len(trials),``\ `{=latex}`"trials"`\
`result``\ `{=latex}`=``\ `{=latex}`run_trial(trials[0])`\
`for``\ `{=latex}`t``\ `{=latex}`in``\ `{=latex}`range(1,``\ `{=latex}`len(trials)):`\
`result``\ `{=latex}`=``\ `{=latex}`max(result,``\ `{=latex}`run_trial(trials[i]))`\
`print``\ `{=latex}`"...exiting``\ `{=latex}`extrapolate``\ `{=latex}`with",``\ `{=latex}`result`

you use your language's logging library[^41], like this:

**`from``\ `{=latex}`logging``\ `{=latex}`import``\ `{=latex}`error,``\ `{=latex}`debug`**\
`def``\ `{=latex}`extrapolate(basis,``\ `{=latex}`case):`\
**`debug("entering``\ `{=latex}`extrapolate...")`**\
`trials``\ `{=latex}`=``\ `{=latex}`count_basis_width(basis)`\
`if``\ `{=latex}`not``\ `{=latex}`trials:`\
**`warning("...no``\ `{=latex}`trials!")`**\
`raise``\ `{=latex}`InvalidDataException("no``\ `{=latex}`trials")`\
**`debug("...running``\ `{=latex}`%d``\ `{=latex}`trials"``\ `{=latex}`%``\ `{=latex}`len(trials))`**\
`result``\ `{=latex}`=``\ `{=latex}`run_trial(trials[0])`\
`for``\ `{=latex}`t``\ `{=latex}`in``\ `{=latex}`range(1,``\ `{=latex}`len(trials)):`\
`result``\ `{=latex}`=``\ `{=latex}`max(result,``\ `{=latex}`run_trial(trials[i]))`\
**`debug("...exiting``\ `{=latex}`extrapolate``\ `{=latex}`with``\ `{=latex}`%d"``\ `{=latex}`%``\ `{=latex}`result)`**

At first glance, this is just more verbose. The benefit, though, is that
your messages are now divided into two classes. If you want to get all
the messages, you put:

`logging.basicConfig(level=logging.DEBUG)`

somewhere near the start of your program. `DEBUG` identifies the least
important messages in your program---the ones you probably only want to
see when you're trying to figure out what's gone wrong. In order, the
more important levels (in Python's logging framework---other libraries
define these slightly differently) are `INFO`, `WARNING`, `ERROR`, and
`CRITICAL`. If you only want messages at the `WARNING` level and above,
you change the configuration to:

`logging.basicConfig(level=logging.WARNING)`

so that `DEBUG` and `INFO` messages aren't printed.

A logging library allows you to control how much your program tells you
about its execution by making one change, in one place. It also means
that you can leave these messages in your code, even when you release
it. No more commenting out `print` statements, only to add them back in
later. (And no more inappropriately-worded messages that *weren't*
commented out popping up in the middle of demos.)

But wait, there's more. Logging libraries also let you control where
your messages are sent. By default, they go to the screen, but you can
send them to a file instead simply by changing the configuration:

`logging.basicConfig(level=logging.ERROR,`\
`filename="/tmp/mylog.txt",`\
`filemode="append")`

This is handy if it takes your program a while to get to the point where
the error occurs. It's also handy if you don't know whether your program
contains an error or not: if you leave logging turned on every time you
run it, then whenever it does something unexpected (like crashing), you
will have at least some idea of what it was doing beforehand.

Most logging libraries also support *rotating files*, i.e., they will
write to `log.1` on the first day, `log.2` on the second day, and so on
until they reach (for example) `log.7`, then wrap around and overwrite
`log.1`. Web servers and other long-lived programs are usually set up to
do this so that they don't fill up the disk with log information.

Finally, logging libraries can send output to mail servers, cell phones,
web servers, and Lava Lamps to notify system administrators when
something `CRITICAL` happens. You can also define message categories,
like "database operations" or "login and logout", and then tell the
logging library to only save specific kinds of messages. It's all
straightforward to set up, and once it's in place, it gives you a lot
more insight into what your program is actually doing.

Wrapping Up {#s:wrapup}
===========

In most courses, once you've handed in an assignment you're done with
it. Course projects are different: they often roll forward from one term
to the next, so the end of one team's involvement isn't necessarily the
end of the project, and they are meant to simulate real life, where
delivery of a particular version is just another step in the product
lifecycle. Here, then, are some of the things you might be asked to do
at the end of your project.

The Project {#s:wrapup-project}
-----------

As I've already said several times, software development teams in
industry care almost as much about handing their projects off cleanly as
they do about what's actually in any particular release (in part because
they themselves are the people most likely to be affected). This usually
isn't part of undergraduate project courses, but it should be; if your
instructor is enlightened enough to include this in her grading scheme,
here are some things she might look for:

1.  An attractive home page, with a short vision statement
    (Section [3.2](#s:basics-pitch){reference-type="ref"
    reference="s:basics-pitch"}) and a few paragraphs or bullet lists to
    help newcomers orient themselves.

2.  An FAQ.

3.  An architectural overview, including block diagrams of the major
    components and a walkthrough of the processing cycle.

4.  An installation guide.

5.  An up-to-date set of tickets. If the work has been done, the ticket
    should be closed; if it hasn't, the ticket should describe the state
    of the bug (or enhancement, or question) fully and accurately.

Bugs {#s:wrapup-bugs}
----

It's OK to have bugs in your code when you finish your project. After
all, almost all products have bugs in them when they ship. This isn't
because developers are lazy or careless; instead, it's a matter of
economics. More than half of first attempts to fix a problem contain
bugs[^42]. That means that if you're near the end of the development
cycle, "fixing" a minor bug can actually *increase* the chances of the
program crashing or destroying users' data. It's safer to document it
(and a workaround, if any exists).

This is another way in which student projects differ from their
industrial counterparts. I have yet to see an instructor give students
marks for cataloging the bugs still in their code at the end of term,
probably because it would be so much work to mark. Instead, grades are
often allocated based on a set of automated pass/fail acceptance tests,
and a subjective evaluation of the code's quality (which usually means
its conformance to basic rules of indentation, commenting, and variable
naming).

The Final Report {#s:wrapup-report}
----------------

The other thing student projects usually have to deliver is some kind of
final report. Most students short-change this part of the course, in
part because it comes at the end, but also because they think, "I want
to write code, not a novel." But here's Karl Fogel, one of the
architects of Subversion and author of *Producing Open Source Software*,
on writing [@b:fogel-producing-open-source]:

> The ability to write clearly is perhaps the most important skill one
> can have in an open source environment. In the long run it matters
> more than programming talent. A great programmer with lousy
> communication skills can only get one thing done at a time, and even
> then may have trouble convincing others to pay attention. But a lousy
> programmer with good communication skills can coordinate and persuade
> many people to do many different things, and thereby have a
> significant effect on a project's direction and momentum.

End-of-project reports can range from half a dozen to fifty pages,
depending on the course's structure and the instructor's whims.
Regardless of their size, they will usually include the following:

-   A *title page*, *abstract*[^43], and *table of contents*. The first
    identifies the document; the second summarizes it in three or four
    sentences, so that busy people can decide whether they ought to read
    the whole thing; and the third helps people navigate.

-   An *introduction* which sets the stage for the rest of the document.
    This explains what problem the team set out to solve, and summarizes
    any background knowledge needed to understand the team's solution.
    It shouldn't state the obvious: there's no need to tell readers what
    the Internet is, or how a parser works. Instead, it should cover
    whatever general knowledge the *next* team will need in order to
    continue the project.

-   A *description of what was done*. This should *not* simply rehash
    the A&E (Section [5.3](#s:process-plansched){reference-type="ref"
    reference="s:process-plansched"}), although that's a good place to
    start. Instead, it should describe the system's architecture, any
    features of its data formats, class structure, or UI that won't
    immediately make sense to a knowledgeable observer, and so on. As
    with the introduction, the target audience is the next team to work
    on the project.

-   A *summary of the current state of the project*, including
    high-level criticism ("The persistence layer works fine, but in
    retrospect, our concurrency control mechanism was a bad choice") and
    pointers to specifics ("Ticket 213 should be addressed before any
    further work is done on user preferences").

-   An *evaluation* of the project. What did the team learn about
    teamwork? What went well? What should they never do again?
    Motherhood-and-apple-pie statements about the importance of version
    control don't belong here (or anywhere else). Instead, the team
    should conduct a proper post mortem
    (Section [8.4](#s:wrapup-postmortem){reference-type="ref"
    reference="s:wrapup-postmortem"}) and present as honest a summary of
    its findings as possible.

-   *References*, including books, papers, and links that the team found
    helpful.

As you can see, this report is neither a user's guide nor maintenance
documentation. Instead, it is like the end-of-contract reports I had to
prepare when I was a consultant. What had I done to earn my customers'
money? What should the next person (who might not be me) do? What could
I tell them that would save them time? Internal documentation (like
Javadoc) doesn't help with these questions, and anyway, the team should
be producing that as they go along, not all in a rush at the end of
term.

So much for what the final report should include; how should you
actually go about writing it? It will probably include:

-   paragraphs of text;

-   equations;

-   source code;

-   vector graphics (such as graphs and line drawings); and

-   raster graphics (such as screen shots).

Lots of tools exist that will handle these, but they all have their
flaws. You can create your report as a set of wiki pages, but most wikis
don't handle conflicts between concurrent authors, and wikis don't do
equations or graphics any better than plain old HTML.

On the other end of the spectrum are WYSIWYG editors like Microsoft Word
and OpenOffice. Unfortunately, these get in the way at least as much as
they help:

1.  They store documents in non-text formats that version control
    systems can't diff or merge
    (Section [6.1](#s:tooling-versioning){reference-type="ref"
    reference="s:tooling-versioning"}).

2.  It's hard to write scripts to process documents, so inclusions (such
    as code fragments) have to be done manually.

3.  Neither one handles equations very well (although both are getting
    better).

4.  It's very easy to format things using low-level primitives ("make
    this italic") rather than logical styles ("making this a book
    title"), which makes it difficult to keep the document consistent
    over time.

For these reasons, most teams format their reports as a set of HTML
pages under version control. That solves the problem of multiple authors
(HTML is a text format, so diff and merge will work), and if you know a
little CSS, you can make it look as pretty as you want. Diagrams and
screenshots work well, but equations are problematic: MathML (the
mathematical markup language) is complicated to write and poorly
supported, so many people still resort to embedding pictures of
equations in web pages.

If you're really keen, you can use an XML markup format like DocBook,
which provides a set of semantically-meaningful tags like `<author>` and
`<citation>`. Various tools can then compile the XML into HTML, PDF, or
other formats. I've tried this, but have never been satisfied: it takes
a lot of typing (or mousing) to add all those tags, which makes DocBook
feel like overkill for a simple end-of-term report.

Then there's LaTeX, a markup language that's much more sophisticated
than HTML, and has literally thousands of add-on packages for equations,
code formatting, and just about everything else you could want. Like
HTML, LaTeX is a text format, so it plays nicely with version control.
However, its power comes at a steep price: LaTeX is as hard to master as
a programming language. It also has a frustratingly slow formatting
cycle, since documents have to be compiled into PDF or another viewable
format before you can see the effects of your changes (although WYGIWYG
tools like LyX are making great strides).

The Post Mortem {#s:wrapup-postmortem}
---------------

The most valuable part of your project isn't the software you write, or
the grade you're given. It's the project's *post mortem*. Literally,
this is an examination of a deceased person; in a software project, it's
a look back at what went right, and what went wrong.

The aim of a post mortem is to help the team and its members do better
next time by giving everyone a chance to reflect on what they've just
accomplished. It is *not* to point the finger of shame at individuals,
although if that has to happen, the post mortem is the best place for
it.

Post mortems are pretty easy to run---just add the following to the
rules for running a meeting
(Section [2.1](#s:important-meetings){reference-type="ref"
reference="s:important-meetings"}):

1.  *Get a moderator who wasn't part of the project* and doesn't have a
    stake in it. Otherwise, the meeting will either go in circles, or
    focus on only a subset of important topics. In the case of student
    projects, this moderator might be the course instructor, or (if the
    course is too large, or the instructor is lazy) a TA.

2.  *Set aside an hour, and only an hour.* In my experience, nothing
    useful is said in the first ten minutes of anyone's first post
    mortem, since people are naturally a bit shy about praising or
    damning their own work. Equally, nothing useful is said after the
    first hour: if you're still talking, it's probably because one or
    two people have a *lot* they want to get off their chests.

3.  *Require attendance.* Everyone who was part of the project ought to
    be in the room for the post mortem. This is more important than you
    might think: the people who have the most to learn from the post
    mortem are often least likely to show up if the meeting is optional.

4.  *Make two lists.* When I'm moderating, I put the headings "Good" and
    "Bad" on the board, then do a lap around the room and ask every
    person to give me one item (that hasn't already been mentioned) for
    each list.

5.  *Comment on actions, rather than individuals.* By the time the
    project is done, some people simply won't be able to stand one
    another. Don't let this sidetrack the meeting: if someone has a
    specific complaint about another member of the team, require him to
    criticize a particular event or decision. "He had a bad attitude"
    does *not* help anyone improve their game.

Once everyone's thoughts are out in the open, organize them somehow so
that you can make specific recommendations about what to do next time.
This list is one of the two major goals of the post mortem (the other
being to give people a chance to be heard). For example, here are the
recommendations that came out of a post mortem I did with students in
2006:

1.  Do a better job of tracking actual progress, rather than reported
    progress. Maybe require a one-minute demo every time a feature is
    supposedly completed?

2.  Teams should find one block of 2-3 hours per week when they can work
    side by side: IM meetings and email resulted in a lot of dropped
    balls.

3.  Having someone who worked on the project in the previous term come
    in to get the new team up to speed made a huge difference.

4.  Team members should read each other's code, at least during the
    early stages of the project, to make sure everyone is actually
    following the coding guidelines.

5.  A large number of small commits is better than a small number of
    massive commits.

6.  Ticketing system was too complicated for students' needs: really
    just want a shared online to-do list.

7.  Teams should have to report test coverage at every progress meeting
    to make sure that a lot of untested code doesn't pile up during the
    term.

Final Words {#s:final}
===========

So, let's see how you're doing. Give yourself one mark for each "yes", 0
for a "no", and -1 for "I don't know" or "I don't understand the
question".

1.  Does your project have a vision statement, and does everyone know
    what it is?

2.  Do you have a up-to-date spec[^44], and does everyone know what and
    where it is?

3.  Is every project resource saved in version control?

4.  Can you rebuild your project with a single command?

5.  Do you write tests before writing code?

6.  Do you always run your tests before checking changes into version
    control?

7.  Do you have a bug database?

8.  Do you use assertions and other defensive programming techniques?

9.  Do you use a symbolic debugger to track problems down?

10. Do you embed your documentation in your code?

11. Is there a searchable archive of discussions about the project?

12. Do you use a style checker to maintain code quality?

13. Do you have an up-to-date schedule?

14. Do you do development in a distraction-free environment (yes, that
    means "with instant messaging and email turned off")?

15. Do you work steadily, without all-nighters or last-minute panic
    sessions?

How did you do?

-   Negative: please re-read this document, make some changes, and then
    come back and take this quiz again.

-   0-5: your project will probably fail to deliver anything useful.

-   6-10: most mature development teams are in this range, and can
    bootstrap other improvements they need on their own.

-   11-15: if you're looking for a job, please let me know.

Why I Teach {#s:final-why-teach}
-----------

When I was your age, I thought universities existed to teach people how
to learn. Later, when I was in grad school, I thought universities were
about doing research and creating new knowledge. Now that I'm in my
forties, though, I've realized that what we're really doing here is
teaching you how to take over the world---because whether you like it or
not, you're going to have to one day.

My parents are in their seventies, and retired. Their generation doesn't
run the world any more; instead, it's people my age, or a bit older, who
pass laws, decide whether interest rates will go up or down, and make
life-and-death decisions in hospitals. As scary as it seems, *we* are
now the grownups.

Twenty years from now, though, we'll be heading for retirement, and
*you* will be in charge, because there won't be anyone else to do it.
That may sound like a long time when you're nineteen, but let me tell
you, you take three breaths, and it's gone. That's why we give you
problems whose answers can't be cribbed from last year's notes. That's
why we put you in situations where you have to figure out what needs to
be done right now, what can be left for later, and what you can simply
ignore. It's because if you don't start learning how to do these things
now, you won't be ready to do them on your own when you have to.

Stirring stuff, isn't it? But it's not the whole answer. I don't just
want my students to make the world a better place so that I can retire
in comfort. I want them to make it a better place for everyone, because
I think that's the great adventure of our times. Forget about landing on
the moon and unraveling the genetic code: when future historians write
about our era, what they'll focus on is that for the first time in
history, our species started taking the Golden Rule seriously.

Just think: a hundred and fifty years ago, most societies still
practiced slavery. A hundred years ago, when my grandmother was a young
girl, she wasn't legally a person in Canada. Fifty years ago, most of
the world's people suffered under totalitarian rule; in the year I was
born, African-Americans couldn't vote in Southern states, and judges
could---and did---order electroshock therapy to "cure" homosexuals. Yes,
there's still a lot wrong with the world, but look at how many more
choices you have than your grandparents did. Look at how many more
things you can know, and be, and enjoy. And most importantly, look at
how many other people can too.

This didn't happen by chance. It happened because millions of us made
millions of little decisions, the sum of which was a better world. For
the most part, we don't think of these day-to-day decisions as being
political, but they are. Every time we buy one brand of running shoe
instead of another, every time we choose to take this class instead of
that one, every time we *don't* give the homeless guy on the corner
fifty cents, every time we decide to shout an anatomical insult instead
of a racial one at a cabbie who shouldn't be allowed to drive a shopping
cart, we're putting our weight behind one vision of what the world
should be rather than another. We don't think about this bigger picture
most of the time---we'd be paralyzed if we did. But the last century and
a half shows that once enough people make "doing the right thing" a
habit, the big picture more or less takes care of itself.

In his 1947 essay "Why I Write" [@b:orwell-why-i-write], George Orwell
said:

> In a peaceful age I might have written ornate or merely descriptive
> books, and might have remained almost unaware of my political
> loyalties. As it is I have been forced into becoming a sort of
> pamphleteer... Every line of serious work that I have written since
> 1936 has been written, directly or indirectly, against
> totalitarianism... It seems to me nonsense, in a period like our own,
> to think that one can avoid writing of such subjects. Everyone writes
> of them in one guise or another. It is simply a question of which side
> one takes and what approach one follows.

Replace "writing" with "teaching", and you'll have the real reason I'm
taking on twenty students next term. Every line of code you write
changes the world in some small way. Every deadline you meet, every
security hole you don't plug, every user need you satisfy, every
disability you don't accommodate---each one makes tomorrow different
from today.

I teach because I want you to be aware of that. I want you to be
conscious of the fact that you're shaping the future we're all going to
spend the rest of our lives in. I want you to do things right, and to
believe that doing things right is important, because the world doesn't
get better by chance, or on its own. The world gets better because
people like you make it better: penny by penny, brick by brick, vote by
vote, and one line of code at a time.

Performance Evaluation {#s:evaluation}
======================

*The material reproduced below is taken from the guidelines for annual
performance reviews used at a well-known (and rather cool) software
development company. It's an accurate depiction of what companies really
care about, and look for, in software developers.*

The purpose of this document is to define best practices for all
software developers in order to facilitate their professional
development.

1.  **Software engineering** (technical design; architecture; coding;
    debugging; testing; performance optimization; release; maintenance)

    1.  Records technical requirements, architectural decisions, and
        other relevant information (does "just enough" design to answer
        all stakeholders' questions; analyzes and reviews peers'
        designs; takes resource usage into account during design; no
        "hidden features"; takes security needs into account)

    2.  Plans for evolution and maintenance (avoids excessive
        dependencies; allows for future maintenance; accounts for
        deployment issues, particularly upgrades)

    3.  Uses configuration management system effectively (all
        project-related material is versioned; never breaks the build;
        all changes are connected to tickets in an auditable way)

    4.  Uses ticketing system effectively (all questions, tasks, and
        issues are ticketed; all work is associated with ticketed items;
        tickets are kept up to date to serve as a basis for auditable
        status reports; avoids creating redundant/duplicate tickets)

    5.  Manages schedule (provides time estimates on work items, and
        updates completion estimates as work progresses; proactively
        reports delays and other scheduling-related issues to affected
        stakeholders; proactively searches for ways to reduce the
        project's critical path)

    6.  Conforms to company coding guidelines (code always passes format
        checks; documentation of all inter-module and externally-visible
        APIs is always up to date on main branch; developer-oriented
        documentation phrased in terms of recognized design patterns
        where relevant)

2.  **Communication** (verbal communication; written reports;
    presentations; email; wikis; blogs; active listening skills;
    feedback and critiques)

    1.  Effectively communicates with peers and stakeholders in a
        regular and timely fashion (collaborates regularly with
        colleagues from other divisions; updates manager and team
        regularly and accurately on status)

    2.  Asks for assistance when needed (seeks answers before asking for
        assistance, but escalates problems when blocked; when asking for
        help, clearly and accurately explains what has been tried, and
        why it didn't work)

    3.  Provides helpful feedback to peers (takes active role in design
        meetings, code reviews, etc.; provides specific examples and
        suggestions for improvement when critiquing colleagues' work)

    4.  Improves efficiency (automates repetitive tasks through scripts,
        macros, etc.; proactively does in-phase work that will reduce
        time and overhead in subsequent work phases)

    5.  Proactively expands network of personal contacts (participates
        in relevant internal discussion groups; takes initiative to
        establish contacts with colleagues in upstream and downstream
        groups)

3.  **Domain Expertise** (sharing knowledge; innovating; continued
    development of personal skills)

    1.  Proactively shares knowledge with peers (mentoring; blogging
        tips and tricks; updating project wiki; provides training)

    2.  Looks for opportunities to innovate (willing to import relevant
        knowledge from other groups/projects/companies; stays current
        with relevant literature; proposes and pursues patents)

    3.  Actively improves expertise (attends training courses; seeks to
        understand goals and techniques of upstream and downstream
        groups; proactively adopts good practices used by peers)

4.  **Leadership** (communicating vision to peers and subordinates;
    fostering a supportive environment; taking a "big picture" view of
    product development)

    1.  Takes part in team-building activities (interviews potential
        hires; helps orient new hires; communicates consistently with
        subordinates regarding their status and performance; takes part
        in out-of-hours social events)

    2.  Solves problems proactively and methodically (identifies risks;
        prioritizes outstanding issues; looks for low-cost/low-risk ways
        to solve or avoid problems; prefers "win-win" solutions to
        "zero-sum" solutions)

    3.  Uses metrics for process improvement (measures and records
        development times, memory/CPU loads, etc.; translates this data
        into recommendations for process and/or product improvement)

    4.  Contributes to project planning (participates in post mortems;
        evaluates feasibility of design and feature proposals; explains
        technical issues/opportunities to upstream and downstream
        colleagues)

Links {#s:links}
=====

-   Amaya: http://www.w3.org/Amaya

-   Ant: http://ant.apache.org

-   Apache: http://httpd.apache.org

-   Bugzilla: http://www.bugzilla.org

-   BuildBot: http://buildbot.sourceforge.net

-   CVS: http://www.nongnu.org/cvs

-   CheckStyle: http://checkstyle.sourceforge.net

-   CruiseControl: http://cruisecontrol.sourceforge.net

-   Debian Linux: http://www.debian.org

-   DocBook: http://www.docbook.org

-   Doctor Dobb's Journal: http:/www.ddj.com

-   DrProject: http://www.drproject.org

-   Eclipse: http://www.eclipse.org

-   Emacs: http://www.gnu.org/software/emacs

-   FindBugs: http://findbugs.sourceforge.net

-   GDB: http://sourceware.org/gdb

-   Google Code: http://code.google.com

-   HttpUnit: http://httpunit.sourceforge.net

-   IRC: http://www.irc.org

-   JEdit: http://www.jedit.org

-   JUnitScenario: http://junitscenario.sourceforge.net

-   JUnit: http://www.junit.org

-   Javadoc: http://java.sun.com/j2se/javadoc/

-   LaTeX: http://www.latex-project.org

-   log4j: http://logging.apache.org/log4j/docs/index.html

-   LyX: http://www.lyx.org

-   Make: http://www.gnu.org/software/make/

-   MathML: http://www.w3.org/Math/

-   Microsoft Visual Studio: http://msdn.microsoft.com/vstudio

-   Microsoft Word: http://office.microsoft.com/word

-   NAnt: http://nant.sourceforge.net

-   OpenID: http://www.openid.net

-   OpenOffice: http://www.openoffice.org

-   Oracle: http://www.oracle.com/

-   PMD: http://pmd.sourceforge.net

-   Perforce: http://www.perforce.com

-   PostgreSQL: http://www.postgresql.org

-   Python: http://www.python.org

-   Rake: http://rake.rubyforge.org

-   Ruby: http://www.ruby-lang.org

-   SCons: http://www.scons.org

-   SQLite: http://www.sqlite.org

-   Selenium: http://www.openqa.org/selenium

-   SourceForge: http://www.sourceforge.net

-   SqlUnit: http://sqlunit.sourceforge.net

-   Subversion: http://subversion.tigris.org

-   Tomcat: http://tomcat.apache.org

-   Trac: http://trac.edgewall.org

-   University of Toronto: http://www.cs.toronto.edu

-   Valgrind: http://valgrind.org

License {#s:license}
=======

This work is licensed under the Creative Commons Attribution-ShareAlike
License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/1.0/ or send a letter to
Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305,
USA. A summary of the license is given below, followed by the full legal
text. If you wish to distribute some or all of this work under different
terms, please contact the author, Greg Wilson, at
`gvwilson@cs.toronto.edu`.

You are free:

-   to copy, distribute, display, and perform the work

-   to make derivative works

-   to make commercial use of the work

under the following conditions:

-   **Attribution**: You must give the original author credit.

-   **Share Alike**: If you alter, transform, or build upon this work,
    you may distribute the resulting work only under a license identical
    to this one.

For any reuse or distribution, you must make clear to others the license
terms of this work.

Any of these conditions can be waived if you get permission from the
author.

Your fair use and other rights are in no way affected by the above.

The above is a summary of the full license below.

`Creative``\ `{=latex}`Commons``\ `{=latex}`Legal``\ `{=latex}`Code`

`Attribution-ShareAlike``\ `{=latex}`1.0`

`CREATIVE``\ `{=latex}`COMMONS``\ `{=latex}`CORPORATION``\ `{=latex}`IS``\ `{=latex}`NOT``\ `{=latex}`A``\ `{=latex}`LAW``\ `{=latex}`FIRM``\ `{=latex}`AND``\ `{=latex}`DOES``\ `{=latex}`NOT``\ `{=latex}`PROVIDE`\
`LEGAL``\ `{=latex}`SERVICES.``\ `{=latex}`DISTRIBUTION``\ `{=latex}`OF``\ `{=latex}`THIS``\ `{=latex}`DRAFT``\ `{=latex}`LICENSE``\ `{=latex}`DOES``\ `{=latex}`NOT``\ `{=latex}`CREATE``\ `{=latex}`AN`\
`ATTORNEY-CLIENT``\ `{=latex}`RELATIONSHIP.``\ `{=latex}`CREATIVE``\ `{=latex}`COMMONS``\ `{=latex}`PROVIDES``\ `{=latex}`THIS`\
`INFORMATION``\ `{=latex}`ON``\ `{=latex}`AN``\ `{=latex}`"AS-IS"``\ `{=latex}`BASIS.``\ `{=latex}`CREATIVE``\ `{=latex}`COMMONS``\ `{=latex}`MAKES``\ `{=latex}`NO``\ `{=latex}`WARRANTIES`\
`REGARDING``\ `{=latex}`THE``\ `{=latex}`INFORMATION``\ `{=latex}`PROVIDED,``\ `{=latex}`AND``\ `{=latex}`DISCLAIMS``\ `{=latex}`LIABILITY``\ `{=latex}`FOR`\
`DAMAGES``\ `{=latex}`RESULTING``\ `{=latex}`FROM``\ `{=latex}`ITS``\ `{=latex}`USE.`

`License`

`THE``\ `{=latex}`WORK``\ `{=latex}`(AS``\ `{=latex}`DEFINED``\ `{=latex}`BELOW)``\ `{=latex}`IS``\ `{=latex}`PROVIDED``\ `{=latex}`UNDER``\ `{=latex}`THE``\ `{=latex}`TERMS``\ `{=latex}`OF``\ `{=latex}`THIS`\
`CREATIVE``\ `{=latex}`COMMONS``\ `{=latex}`PUBLIC``\ `{=latex}`LICENSE``\ `{=latex}`("CCPL"``\ `{=latex}`OR``\ `{=latex}`"LICENSE").``\ `{=latex}`THE``\ `{=latex}`WORK``\ `{=latex}`IS`\
`PROTECTED``\ `{=latex}`BY``\ `{=latex}`COPYRIGHT``\ `{=latex}`AND/OR``\ `{=latex}`OTHER``\ `{=latex}`APPLICABLE``\ `{=latex}`LAW.``\ `{=latex}`ANY``\ `{=latex}`USE``\ `{=latex}`OF``\ `{=latex}`THE`\
`WORK``\ `{=latex}`OTHER``\ `{=latex}`THAN``\ `{=latex}`AS``\ `{=latex}`AUTHORIZED``\ `{=latex}`UNDER``\ `{=latex}`THIS``\ `{=latex}`LICENSE``\ `{=latex}`IS``\ `{=latex}`PROHIBITED.`

`BY``\ `{=latex}`EXERCISING``\ `{=latex}`ANY``\ `{=latex}`RIGHTS``\ `{=latex}`TO``\ `{=latex}`THE``\ `{=latex}`WORK``\ `{=latex}`PROVIDED``\ `{=latex}`HERE,``\ `{=latex}`YOU``\ `{=latex}`ACCEPT``\ `{=latex}`AND`\
`AGREE``\ `{=latex}`TO``\ `{=latex}`BE``\ `{=latex}`BOUND``\ `{=latex}`BY``\ `{=latex}`THE``\ `{=latex}`TERMS``\ `{=latex}`OF``\ `{=latex}`THIS``\ `{=latex}`LICENSE.``\ `{=latex}`THE``\ `{=latex}`LICENSOR``\ `{=latex}`GRANTS`\
`YOU``\ `{=latex}`THE``\ `{=latex}`RIGHTS``\ `{=latex}`CONTAINED``\ `{=latex}`HERE``\ `{=latex}`IN``\ `{=latex}`CONSIDERATION``\ `{=latex}`OF``\ `{=latex}`YOUR``\ `{=latex}`ACCEPTANCE``\ `{=latex}`OF`\
`SUCH``\ `{=latex}`TERMS``\ `{=latex}`AND``\ `{=latex}`CONDITIONS.`

`1.``\ `{=latex}`Definitions`

`a.``\ `{=latex}`"Collective``\ `{=latex}`Work"``\ `{=latex}`means``\ `{=latex}`a``\ `{=latex}`work,``\ `{=latex}`such``\ `{=latex}`as``\ `{=latex}`a``\ `{=latex}`periodical``\ `{=latex}`issue,`\
`anthology``\ `{=latex}`or``\ `{=latex}`encyclopedia,``\ `{=latex}`in``\ `{=latex}`which``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`in``\ `{=latex}`its``\ `{=latex}`entirety``\ `{=latex}`in`\
`unmodified``\ `{=latex}`form,``\ `{=latex}`along``\ `{=latex}`with``\ `{=latex}`a``\ `{=latex}`number``\ `{=latex}`of``\ `{=latex}`other``\ `{=latex}`contributions,`\
`constituting``\ `{=latex}`separate``\ `{=latex}`and``\ `{=latex}`independent``\ `{=latex}`works``\ `{=latex}`in``\ `{=latex}`themselves,``\ `{=latex}`are`\
`assembled``\ `{=latex}`into``\ `{=latex}`a``\ `{=latex}`collective``\ `{=latex}`whole.``\ `{=latex}`A``\ `{=latex}`work``\ `{=latex}`that``\ `{=latex}`constitutes``\ `{=latex}`a`\
`Collective``\ `{=latex}`Work``\ `{=latex}`will``\ `{=latex}`not``\ `{=latex}`be``\ `{=latex}`considered``\ `{=latex}`a``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`(as`\
`defined``\ `{=latex}`below)``\ `{=latex}`for``\ `{=latex}`the``\ `{=latex}`purposes``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License.`

`b.``\ `{=latex}`"Derivative``\ `{=latex}`Work"``\ `{=latex}`means``\ `{=latex}`a``\ `{=latex}`work``\ `{=latex}`based``\ `{=latex}`upon``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`or``\ `{=latex}`upon``\ `{=latex}`the``\ `{=latex}`Work`\
`and``\ `{=latex}`other``\ `{=latex}`pre-existing``\ `{=latex}`works,``\ `{=latex}`such``\ `{=latex}`as``\ `{=latex}`a``\ `{=latex}`translation,``\ `{=latex}`musical`\
`arrangement,``\ `{=latex}`dramatization,``\ `{=latex}`fictionalization,``\ `{=latex}`motion``\ `{=latex}`picture`\
`version,``\ `{=latex}`sound``\ `{=latex}`recording,``\ `{=latex}`art``\ `{=latex}`reproduction,``\ `{=latex}`abridgment,`\
`condensation,``\ `{=latex}`or``\ `{=latex}`any``\ `{=latex}`other``\ `{=latex}`form``\ `{=latex}`in``\ `{=latex}`which``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`may``\ `{=latex}`be``\ `{=latex}`recast,`\
`transformed,``\ `{=latex}`or``\ `{=latex}`adapted,``\ `{=latex}`except``\ `{=latex}`that``\ `{=latex}`a``\ `{=latex}`work``\ `{=latex}`that``\ `{=latex}`constitutes``\ `{=latex}`a`\
`Collective``\ `{=latex}`Work``\ `{=latex}`will``\ `{=latex}`not``\ `{=latex}`be``\ `{=latex}`considered``\ `{=latex}`a``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`for``\ `{=latex}`the`\
`purpose``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License.`

`c.``\ `{=latex}`"Licensor"``\ `{=latex}`means``\ `{=latex}`the``\ `{=latex}`individual``\ `{=latex}`or``\ `{=latex}`entity``\ `{=latex}`that``\ `{=latex}`offers``\ `{=latex}`the``\ `{=latex}`Work`\
`under``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License.`

`d.``\ `{=latex}`"Original``\ `{=latex}`Author"``\ `{=latex}`means``\ `{=latex}`the``\ `{=latex}`individual``\ `{=latex}`or``\ `{=latex}`entity``\ `{=latex}`who``\ `{=latex}`created``\ `{=latex}`the`\
`Work.`

`e.``\ `{=latex}`"Work"``\ `{=latex}`means``\ `{=latex}`the``\ `{=latex}`copyrightable``\ `{=latex}`work``\ `{=latex}`of``\ `{=latex}`authorship``\ `{=latex}`offered``\ `{=latex}`under``\ `{=latex}`the`\
`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License.`

`f.``\ `{=latex}`"You"``\ `{=latex}`means``\ `{=latex}`an``\ `{=latex}`individual``\ `{=latex}`or``\ `{=latex}`entity``\ `{=latex}`exercising``\ `{=latex}`rights``\ `{=latex}`under``\ `{=latex}`this`\
`License``\ `{=latex}`who``\ `{=latex}`has``\ `{=latex}`not``\ `{=latex}`previously``\ `{=latex}`violated``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License`\
`with``\ `{=latex}`respect``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`Work,``\ `{=latex}`or``\ `{=latex}`who``\ `{=latex}`has``\ `{=latex}`received``\ `{=latex}`express``\ `{=latex}`permission`\
`from``\ `{=latex}`the``\ `{=latex}`Licensor``\ `{=latex}`to``\ `{=latex}`exercise``\ `{=latex}`rights``\ `{=latex}`under``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`despite``\ `{=latex}`a`\
`previous``\ `{=latex}`violation.`

`2.``\ `{=latex}`Fair``\ `{=latex}`Use``\ `{=latex}`Rights.``\ `{=latex}`Nothing``\ `{=latex}`in``\ `{=latex}`this``\ `{=latex}`license``\ `{=latex}`is``\ `{=latex}`intended``\ `{=latex}`to``\ `{=latex}`reduce,`\
`limit,``\ `{=latex}`or``\ `{=latex}`restrict``\ `{=latex}`any``\ `{=latex}`rights``\ `{=latex}`arising``\ `{=latex}`from``\ `{=latex}`fair``\ `{=latex}`use,``\ `{=latex}`first``\ `{=latex}`sale``\ `{=latex}`or`\
`other``\ `{=latex}`limitations``\ `{=latex}`on``\ `{=latex}`the``\ `{=latex}`exclusive``\ `{=latex}`rights``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`copyright``\ `{=latex}`owner``\ `{=latex}`under`\
`copyright``\ `{=latex}`law``\ `{=latex}`or``\ `{=latex}`other``\ `{=latex}`applicable``\ `{=latex}`laws.`

`3.``\ `{=latex}`License``\ `{=latex}`Grant.``\ `{=latex}`Subject``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`and``\ `{=latex}`conditions``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License,`\
`Licensor``\ `{=latex}`hereby``\ `{=latex}`grants``\ `{=latex}`You``\ `{=latex}`a``\ `{=latex}`worldwide,``\ `{=latex}`royalty-free,``\ `{=latex}`non-exclusive,`\
`perpetual``\ `{=latex}`(for``\ `{=latex}`the``\ `{=latex}`duration``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`applicable``\ `{=latex}`copyright)``\ `{=latex}`license``\ `{=latex}`to`\
`exercise``\ `{=latex}`the``\ `{=latex}`rights``\ `{=latex}`in``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`as``\ `{=latex}`stated``\ `{=latex}`below:`

`a.``\ `{=latex}`to``\ `{=latex}`reproduce``\ `{=latex}`the``\ `{=latex}`Work,``\ `{=latex}`to``\ `{=latex}`incorporate``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`into``\ `{=latex}`one``\ `{=latex}`or``\ `{=latex}`more`\
`Collective``\ `{=latex}`Works,``\ `{=latex}`and``\ `{=latex}`to``\ `{=latex}`reproduce``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`as``\ `{=latex}`incorporated``\ `{=latex}`in``\ `{=latex}`the`\
`Collective``\ `{=latex}`Works;`

`b.``\ `{=latex}`to``\ `{=latex}`create``\ `{=latex}`and``\ `{=latex}`reproduce``\ `{=latex}`Derivative``\ `{=latex}`Works;`

`c.``\ `{=latex}`to``\ `{=latex}`distribute``\ `{=latex}`copies``\ `{=latex}`or``\ `{=latex}`phonorecords``\ `{=latex}`of,``\ `{=latex}`display``\ `{=latex}`publicly,``\ `{=latex}`perform`\
`publicly,``\ `{=latex}`and``\ `{=latex}`perform``\ `{=latex}`publicly``\ `{=latex}`by``\ `{=latex}`means``\ `{=latex}`of``\ `{=latex}`a``\ `{=latex}`digital``\ `{=latex}`audio`\
`transmission``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`including``\ `{=latex}`as``\ `{=latex}`incorporated``\ `{=latex}`in``\ `{=latex}`Collective`\
`Works;`

`d.``\ `{=latex}`to``\ `{=latex}`distribute``\ `{=latex}`copies``\ `{=latex}`or``\ `{=latex}`phonorecords``\ `{=latex}`of,``\ `{=latex}`display``\ `{=latex}`publicly,``\ `{=latex}`perform`\
`publicly,``\ `{=latex}`and``\ `{=latex}`perform``\ `{=latex}`publicly``\ `{=latex}`by``\ `{=latex}`means``\ `{=latex}`of``\ `{=latex}`a``\ `{=latex}`digital``\ `{=latex}`audio`\
`transmission``\ `{=latex}`Derivative``\ `{=latex}`Works;`

`The``\ `{=latex}`above``\ `{=latex}`rights``\ `{=latex}`may``\ `{=latex}`be``\ `{=latex}`exercised``\ `{=latex}`in``\ `{=latex}`all``\ `{=latex}`media``\ `{=latex}`and``\ `{=latex}`formats``\ `{=latex}`whether``\ `{=latex}`now`\
`known``\ `{=latex}`or``\ `{=latex}`hereafter``\ `{=latex}`devised.``\ `{=latex}`The``\ `{=latex}`above``\ `{=latex}`rights``\ `{=latex}`include``\ `{=latex}`the``\ `{=latex}`right``\ `{=latex}`to``\ `{=latex}`make`\
`such``\ `{=latex}`modifications``\ `{=latex}`as``\ `{=latex}`are``\ `{=latex}`technically``\ `{=latex}`necessary``\ `{=latex}`to``\ `{=latex}`exercise``\ `{=latex}`the``\ `{=latex}`rights`\
`in``\ `{=latex}`other``\ `{=latex}`media``\ `{=latex}`and``\ `{=latex}`formats.``\ `{=latex}`All``\ `{=latex}`rights``\ `{=latex}`not``\ `{=latex}`expressly``\ `{=latex}`granted``\ `{=latex}`by`\
`Licensor``\ `{=latex}`are``\ `{=latex}`hereby``\ `{=latex}`reserved.`

`4.``\ `{=latex}`Restrictions.``\ `{=latex}`The``\ `{=latex}`license``\ `{=latex}`granted``\ `{=latex}`in``\ `{=latex}`Section``\ `{=latex}`3``\ `{=latex}`above``\ `{=latex}`is``\ `{=latex}`expressly`\
`made``\ `{=latex}`subject``\ `{=latex}`to``\ `{=latex}`and``\ `{=latex}`limited``\ `{=latex}`by``\ `{=latex}`the``\ `{=latex}`following``\ `{=latex}`restrictions:`

`a.``\ `{=latex}`You``\ `{=latex}`may``\ `{=latex}`distribute,``\ `{=latex}`publicly``\ `{=latex}`display,``\ `{=latex}`publicly``\ `{=latex}`perform,``\ `{=latex}`or``\ `{=latex}`publicly`\
`digitally``\ `{=latex}`perform``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`only``\ `{=latex}`under``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License,`\
`and``\ `{=latex}`You``\ `{=latex}`must``\ `{=latex}`include``\ `{=latex}`a``\ `{=latex}`copy``\ `{=latex}`of,``\ `{=latex}`or``\ `{=latex}`the``\ `{=latex}`Uniform``\ `{=latex}`Resource``\ `{=latex}`Identifier`\
`for,``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`with``\ `{=latex}`every``\ `{=latex}`copy``\ `{=latex}`or``\ `{=latex}`phonorecord``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`You`\
`distribute,``\ `{=latex}`publicly``\ `{=latex}`display,``\ `{=latex}`publicly``\ `{=latex}`perform,``\ `{=latex}`or``\ `{=latex}`publicly`\
`digitally``\ `{=latex}`perform.``\ `{=latex}`You``\ `{=latex}`may``\ `{=latex}`not``\ `{=latex}`offer``\ `{=latex}`or``\ `{=latex}`impose``\ `{=latex}`any``\ `{=latex}`terms``\ `{=latex}`on``\ `{=latex}`the`\
`Work``\ `{=latex}`that``\ `{=latex}`alter``\ `{=latex}`or``\ `{=latex}`restrict``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`or``\ `{=latex}`the`\
`recipients’``\ `{=latex}`exercise``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`rights``\ `{=latex}`granted``\ `{=latex}`hereunder.``\ `{=latex}`You``\ `{=latex}`may``\ `{=latex}`not`\
`sublicense``\ `{=latex}`the``\ `{=latex}`Work.``\ `{=latex}`You``\ `{=latex}`must``\ `{=latex}`keep``\ `{=latex}`intact``\ `{=latex}`all``\ `{=latex}`notices``\ `{=latex}`that``\ `{=latex}`refer``\ `{=latex}`to`\
`this``\ `{=latex}`License``\ `{=latex}`and``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`disclaimer``\ `{=latex}`of``\ `{=latex}`warranties.``\ `{=latex}`You``\ `{=latex}`may``\ `{=latex}`not`\
`distribute,``\ `{=latex}`publicly``\ `{=latex}`display,``\ `{=latex}`publicly``\ `{=latex}`perform,``\ `{=latex}`or``\ `{=latex}`publicly`\
`digitally``\ `{=latex}`perform``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`with``\ `{=latex}`any``\ `{=latex}`technological``\ `{=latex}`measures``\ `{=latex}`that`\
`control``\ `{=latex}`access``\ `{=latex}`or``\ `{=latex}`use``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`in``\ `{=latex}`a``\ `{=latex}`manner``\ `{=latex}`inconsistent``\ `{=latex}`with``\ `{=latex}`the`\
`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`Agreement.``\ `{=latex}`The``\ `{=latex}`above``\ `{=latex}`applies``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`as`\
`incorporated``\ `{=latex}`in``\ `{=latex}`a``\ `{=latex}`Collective``\ `{=latex}`Work,``\ `{=latex}`but``\ `{=latex}`this``\ `{=latex}`does``\ `{=latex}`not``\ `{=latex}`require``\ `{=latex}`the`\
`Collective``\ `{=latex}`Work``\ `{=latex}`apart``\ `{=latex}`from``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`itself``\ `{=latex}`to``\ `{=latex}`be``\ `{=latex}`made``\ `{=latex}`subject``\ `{=latex}`to`\
`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License.``\ `{=latex}`If``\ `{=latex}`You``\ `{=latex}`create``\ `{=latex}`a``\ `{=latex}`Collective``\ `{=latex}`Work,``\ `{=latex}`upon`\
`notice``\ `{=latex}`from``\ `{=latex}`any``\ `{=latex}`Licensor``\ `{=latex}`You``\ `{=latex}`must,``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`extent``\ `{=latex}`practicable,`\
`remove``\ `{=latex}`from``\ `{=latex}`the``\ `{=latex}`Collective``\ `{=latex}`Work``\ `{=latex}`any``\ `{=latex}`reference``\ `{=latex}`to``\ `{=latex}`such``\ `{=latex}`Licensor``\ `{=latex}`or`\
`the``\ `{=latex}`Original``\ `{=latex}`Author,``\ `{=latex}`as``\ `{=latex}`requested.``\ `{=latex}`If``\ `{=latex}`You``\ `{=latex}`create``\ `{=latex}`a``\ `{=latex}`Derivative``\ `{=latex}`Work,`\
`upon``\ `{=latex}`notice``\ `{=latex}`from``\ `{=latex}`any``\ `{=latex}`Licensor``\ `{=latex}`You``\ `{=latex}`must,``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`extent``\ `{=latex}`practicable,`\
`remove``\ `{=latex}`from``\ `{=latex}`the``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`any``\ `{=latex}`reference``\ `{=latex}`to``\ `{=latex}`such``\ `{=latex}`Licensor``\ `{=latex}`or`\
`the``\ `{=latex}`Original``\ `{=latex}`Author,``\ `{=latex}`as``\ `{=latex}`requested.`

`b.``\ `{=latex}`You``\ `{=latex}`may``\ `{=latex}`distribute,``\ `{=latex}`publicly``\ `{=latex}`display,``\ `{=latex}`publicly``\ `{=latex}`perform,``\ `{=latex}`or``\ `{=latex}`publicly`\
`digitally``\ `{=latex}`perform``\ `{=latex}`a``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`only``\ `{=latex}`under``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this`\
`License,``\ `{=latex}`and``\ `{=latex}`You``\ `{=latex}`must``\ `{=latex}`include``\ `{=latex}`a``\ `{=latex}`copy``\ `{=latex}`of,``\ `{=latex}`or``\ `{=latex}`the``\ `{=latex}`Uniform``\ `{=latex}`Resource`\
`Identifier``\ `{=latex}`for,``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`with``\ `{=latex}`every``\ `{=latex}`copy``\ `{=latex}`or``\ `{=latex}`phonorecord``\ `{=latex}`of``\ `{=latex}`each`\
`Derivative``\ `{=latex}`Work``\ `{=latex}`You``\ `{=latex}`distribute,``\ `{=latex}`publicly``\ `{=latex}`display,``\ `{=latex}`publicly``\ `{=latex}`perform,`\
`or``\ `{=latex}`publicly``\ `{=latex}`digitally``\ `{=latex}`perform.``\ `{=latex}`You``\ `{=latex}`may``\ `{=latex}`not``\ `{=latex}`offer``\ `{=latex}`or``\ `{=latex}`impose``\ `{=latex}`any`\
`terms``\ `{=latex}`on``\ `{=latex}`the``\ `{=latex}`Derivative``\ `{=latex}`Works``\ `{=latex}`that``\ `{=latex}`alter``\ `{=latex}`or``\ `{=latex}`restrict``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of`\
`this``\ `{=latex}`License``\ `{=latex}`or``\ `{=latex}`the``\ `{=latex}`recipients’``\ `{=latex}`exercise``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`rights``\ `{=latex}`granted`\
`hereunder,``\ `{=latex}`and``\ `{=latex}`You``\ `{=latex}`must``\ `{=latex}`keep``\ `{=latex}`intact``\ `{=latex}`all``\ `{=latex}`notices``\ `{=latex}`that``\ `{=latex}`refer``\ `{=latex}`to``\ `{=latex}`this`\
`License``\ `{=latex}`and``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`disclaimer``\ `{=latex}`of``\ `{=latex}`warranties.``\ `{=latex}`You``\ `{=latex}`may``\ `{=latex}`not`\
`distribute,``\ `{=latex}`publicly``\ `{=latex}`display,``\ `{=latex}`publicly``\ `{=latex}`perform,``\ `{=latex}`or``\ `{=latex}`publicly`\
`digitally``\ `{=latex}`perform``\ `{=latex}`the``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`with``\ `{=latex}`any``\ `{=latex}`technological`\
`measures``\ `{=latex}`that``\ `{=latex}`control``\ `{=latex}`access``\ `{=latex}`or``\ `{=latex}`use``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`in``\ `{=latex}`a``\ `{=latex}`manner`\
`inconsistent``\ `{=latex}`with``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`Agreement.``\ `{=latex}`The``\ `{=latex}`above`\
`applies``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`as``\ `{=latex}`incorporated``\ `{=latex}`in``\ `{=latex}`a``\ `{=latex}`Collective`\
`Work,``\ `{=latex}`but``\ `{=latex}`this``\ `{=latex}`does``\ `{=latex}`not``\ `{=latex}`require``\ `{=latex}`the``\ `{=latex}`Collective``\ `{=latex}`Work``\ `{=latex}`apart``\ `{=latex}`from``\ `{=latex}`the`\
`Derivative``\ `{=latex}`Work``\ `{=latex}`itself``\ `{=latex}`to``\ `{=latex}`be``\ `{=latex}`made``\ `{=latex}`subject``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this`\
`License.`

`c.``\ `{=latex}`If``\ `{=latex}`you``\ `{=latex}`distribute,``\ `{=latex}`publicly``\ `{=latex}`display,``\ `{=latex}`publicly``\ `{=latex}`perform,``\ `{=latex}`or``\ `{=latex}`publicly`\
`digitally``\ `{=latex}`perform``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`or``\ `{=latex}`any``\ `{=latex}`Derivative``\ `{=latex}`Works``\ `{=latex}`or``\ `{=latex}`Collective`\
`Works,``\ `{=latex}`You``\ `{=latex}`must``\ `{=latex}`keep``\ `{=latex}`intact``\ `{=latex}`all``\ `{=latex}`copyright``\ `{=latex}`notices``\ `{=latex}`for``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`and`\
`give``\ `{=latex}`the``\ `{=latex}`Original``\ `{=latex}`Author``\ `{=latex}`credit``\ `{=latex}`reasonable``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`medium``\ `{=latex}`or``\ `{=latex}`means`\
`You``\ `{=latex}`are``\ `{=latex}`utilizing``\ `{=latex}`by``\ `{=latex}`conveying``\ `{=latex}`the``\ `{=latex}`name``\ `{=latex}`(or``\ `{=latex}`pseudonym``\ `{=latex}`if`\
`applicable)``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`Original``\ `{=latex}`Author``\ `{=latex}`if``\ `{=latex}`supplied;``\ `{=latex}`the``\ `{=latex}`title``\ `{=latex}`of``\ `{=latex}`the`\
`Work``\ `{=latex}`if``\ `{=latex}`supplied;``\ `{=latex}`in``\ `{=latex}`the``\ `{=latex}`case``\ `{=latex}`of``\ `{=latex}`a``\ `{=latex}`Derivative``\ `{=latex}`Work,``\ `{=latex}`a``\ `{=latex}`credit`\
`identifying``\ `{=latex}`the``\ `{=latex}`use``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`in``\ `{=latex}`the``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`(e.g.,`\
`"French``\ `{=latex}`translation``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`by``\ `{=latex}`Original``\ `{=latex}`Author,"``\ `{=latex}`or``\ `{=latex}`"Screenplay`\
`based``\ `{=latex}`on``\ `{=latex}`original``\ `{=latex}`Work``\ `{=latex}`by``\ `{=latex}`Original``\ `{=latex}`Author").``\ `{=latex}`Such``\ `{=latex}`credit``\ `{=latex}`may``\ `{=latex}`be`\
`implemented``\ `{=latex}`in``\ `{=latex}`any``\ `{=latex}`reasonable``\ `{=latex}`manner;``\ `{=latex}`provided,``\ `{=latex}`however,``\ `{=latex}`that``\ `{=latex}`in`\
`the``\ `{=latex}`case``\ `{=latex}`of``\ `{=latex}`a``\ `{=latex}`Derivative``\ `{=latex}`Work``\ `{=latex}`or``\ `{=latex}`Collective``\ `{=latex}`Work,``\ `{=latex}`at``\ `{=latex}`a``\ `{=latex}`minimum``\ `{=latex}`such`\
`credit``\ `{=latex}`will``\ `{=latex}`appear``\ `{=latex}`where``\ `{=latex}`any``\ `{=latex}`other``\ `{=latex}`comparable``\ `{=latex}`authorship``\ `{=latex}`credit`\
`appears``\ `{=latex}`and``\ `{=latex}`in``\ `{=latex}`a``\ `{=latex}`manner``\ `{=latex}`at``\ `{=latex}`least``\ `{=latex}`as``\ `{=latex}`prominent``\ `{=latex}`as``\ `{=latex}`such``\ `{=latex}`other`\
`comparable``\ `{=latex}`authorship``\ `{=latex}`credit.`

`5.``\ `{=latex}`Representations,``\ `{=latex}`Warranties``\ `{=latex}`and``\ `{=latex}`Disclaimer`

`a.``\ `{=latex}`By``\ `{=latex}`offering``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`for``\ `{=latex}`public``\ `{=latex}`release``\ `{=latex}`under``\ `{=latex}`this``\ `{=latex}`License,`\
`Licensor``\ `{=latex}`represents``\ `{=latex}`and``\ `{=latex}`warrants``\ `{=latex}`that,``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`best``\ `{=latex}`of``\ `{=latex}`Licensor’s`\
`knowledge``\ `{=latex}`after``\ `{=latex}`reasonable``\ `{=latex}`inquiry:`

`i.``\ `{=latex}`Licensor``\ `{=latex}`has``\ `{=latex}`secured``\ `{=latex}`all``\ `{=latex}`rights``\ `{=latex}`in``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`necessary``\ `{=latex}`to``\ `{=latex}`grant`\
`the``\ `{=latex}`license``\ `{=latex}`rights``\ `{=latex}`hereunder``\ `{=latex}`and``\ `{=latex}`to``\ `{=latex}`permit``\ `{=latex}`the``\ `{=latex}`lawful``\ `{=latex}`exercise``\ `{=latex}`of`\
`the``\ `{=latex}`rights``\ `{=latex}`granted``\ `{=latex}`hereunder``\ `{=latex}`without``\ `{=latex}`You``\ `{=latex}`having``\ `{=latex}`any``\ `{=latex}`obligation``\ `{=latex}`to`\
`pay``\ `{=latex}`any``\ `{=latex}`royalties,``\ `{=latex}`compulsory``\ `{=latex}`license``\ `{=latex}`fees,``\ `{=latex}`residuals``\ `{=latex}`or``\ `{=latex}`any``\ `{=latex}`other`\
`payments;`

`ii.``\ `{=latex}`The``\ `{=latex}`Work``\ `{=latex}`does``\ `{=latex}`not``\ `{=latex}`infringe``\ `{=latex}`the``\ `{=latex}`copyright,``\ `{=latex}`trademark,``\ `{=latex}`publicity`\
`rights,``\ `{=latex}`common``\ `{=latex}`law``\ `{=latex}`rights``\ `{=latex}`or``\ `{=latex}`any``\ `{=latex}`other``\ `{=latex}`right``\ `{=latex}`of``\ `{=latex}`any``\ `{=latex}`third``\ `{=latex}`party``\ `{=latex}`or`\
`constitute``\ `{=latex}`defamation,``\ `{=latex}`invasion``\ `{=latex}`of``\ `{=latex}`privacy``\ `{=latex}`or``\ `{=latex}`other``\ `{=latex}`tortious``\ `{=latex}`injury`\
`to``\ `{=latex}`any``\ `{=latex}`third``\ `{=latex}`party.`

`b.``\ `{=latex}`EXCEPT``\ `{=latex}`AS``\ `{=latex}`EXPRESSLY``\ `{=latex}`STATED``\ `{=latex}`IN``\ `{=latex}`THIS``\ `{=latex}`LICENSE``\ `{=latex}`OR``\ `{=latex}`OTHERWISE``\ `{=latex}`AGREED``\ `{=latex}`IN`\
`WRITING``\ `{=latex}`OR``\ `{=latex}`REQUIRED``\ `{=latex}`BY``\ `{=latex}`APPLICABLE``\ `{=latex}`LAW,``\ `{=latex}`THE``\ `{=latex}`WORK``\ `{=latex}`IS``\ `{=latex}`LICENSED``\ `{=latex}`ON``\ `{=latex}`AN`\
`"AS``\ `{=latex}`IS"``\ `{=latex}`BASIS,``\ `{=latex}`WITHOUT``\ `{=latex}`WARRANTIES``\ `{=latex}`OF``\ `{=latex}`ANY``\ `{=latex}`KIND,``\ `{=latex}`EITHER``\ `{=latex}`EXPRESS``\ `{=latex}`OR`\
`IMPLIED``\ `{=latex}`INCLUDING,``\ `{=latex}`WITHOUT``\ `{=latex}`LIMITATION,``\ `{=latex}`ANY``\ `{=latex}`WARRANTIES``\ `{=latex}`REGARDING``\ `{=latex}`THE`\
`CONTENTS``\ `{=latex}`OR``\ `{=latex}`ACCURACY``\ `{=latex}`OF``\ `{=latex}`THE``\ `{=latex}`WORK.`

`6.``\ `{=latex}`Limitation``\ `{=latex}`on``\ `{=latex}`Liability.``\ `{=latex}`EXCEPT``\ `{=latex}`TO``\ `{=latex}`THE``\ `{=latex}`EXTENT``\ `{=latex}`REQUIRED``\ `{=latex}`BY`\
`APPLICABLE``\ `{=latex}`LAW,``\ `{=latex}`AND``\ `{=latex}`EXCEPT``\ `{=latex}`FOR``\ `{=latex}`DAMAGES``\ `{=latex}`ARISING``\ `{=latex}`FROM``\ `{=latex}`LIABILITY``\ `{=latex}`TO``\ `{=latex}`A`\
`THIRD``\ `{=latex}`PARTY``\ `{=latex}`RESULTING``\ `{=latex}`FROM``\ `{=latex}`BREACH``\ `{=latex}`OF``\ `{=latex}`THE``\ `{=latex}`WARRANTIES``\ `{=latex}`IN``\ `{=latex}`SECTION``\ `{=latex}`5,``\ `{=latex}`IN`\
`NO``\ `{=latex}`EVENT``\ `{=latex}`WILL``\ `{=latex}`LICENSOR``\ `{=latex}`BE``\ `{=latex}`LIABLE``\ `{=latex}`TO``\ `{=latex}`YOU``\ `{=latex}`ON``\ `{=latex}`ANY``\ `{=latex}`LEGAL``\ `{=latex}`THEORY``\ `{=latex}`FOR``\ `{=latex}`ANY`\
`SPECIAL,``\ `{=latex}`INCIDENTAL,``\ `{=latex}`CONSEQUENTIAL,``\ `{=latex}`PUNITIVE``\ `{=latex}`OR``\ `{=latex}`EXEMPLARY``\ `{=latex}`DAMAGES`\
`ARISING``\ `{=latex}`OUT``\ `{=latex}`OF``\ `{=latex}`THIS``\ `{=latex}`LICENSE``\ `{=latex}`OR``\ `{=latex}`THE``\ `{=latex}`USE``\ `{=latex}`OF``\ `{=latex}`THE``\ `{=latex}`WORK,``\ `{=latex}`EVEN``\ `{=latex}`IF``\ `{=latex}`LICENSOR`\
`HAS``\ `{=latex}`BEEN``\ `{=latex}`ADVISED``\ `{=latex}`OF``\ `{=latex}`THE``\ `{=latex}`POSSIBILITY``\ `{=latex}`OF``\ `{=latex}`SUCH``\ `{=latex}`DAMAGES.`

`7.``\ `{=latex}`Termination`

`a.``\ `{=latex}`This``\ `{=latex}`License``\ `{=latex}`and``\ `{=latex}`the``\ `{=latex}`rights``\ `{=latex}`granted``\ `{=latex}`hereunder``\ `{=latex}`will``\ `{=latex}`terminate`\
`automatically``\ `{=latex}`upon``\ `{=latex}`any``\ `{=latex}`breach``\ `{=latex}`by``\ `{=latex}`You``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this`\
`License.``\ `{=latex}`Individuals``\ `{=latex}`or``\ `{=latex}`entities``\ `{=latex}`who``\ `{=latex}`have``\ `{=latex}`received``\ `{=latex}`Derivative``\ `{=latex}`Works`\
`or``\ `{=latex}`Collective``\ `{=latex}`Works``\ `{=latex}`from``\ `{=latex}`You``\ `{=latex}`under``\ `{=latex}`this``\ `{=latex}`License,``\ `{=latex}`however,``\ `{=latex}`will``\ `{=latex}`not`\
`have``\ `{=latex}`their``\ `{=latex}`licenses``\ `{=latex}`terminated``\ `{=latex}`provided``\ `{=latex}`such``\ `{=latex}`individuals``\ `{=latex}`or`\
`entities``\ `{=latex}`remain``\ `{=latex}`in``\ `{=latex}`full``\ `{=latex}`compliance``\ `{=latex}`with``\ `{=latex}`those``\ `{=latex}`licenses.``\ `{=latex}`Sections``\ `{=latex}`1,`\
`2,``\ `{=latex}`5,``\ `{=latex}`6,``\ `{=latex}`7,``\ `{=latex}`and``\ `{=latex}`8``\ `{=latex}`will``\ `{=latex}`survive``\ `{=latex}`any``\ `{=latex}`termination``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License.`

`b.``\ `{=latex}`Subject``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`above``\ `{=latex}`terms``\ `{=latex}`and``\ `{=latex}`conditions,``\ `{=latex}`the``\ `{=latex}`license``\ `{=latex}`granted``\ `{=latex}`here`\
`is``\ `{=latex}`perpetual``\ `{=latex}`(for``\ `{=latex}`the``\ `{=latex}`duration``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`applicable``\ `{=latex}`copyright``\ `{=latex}`in``\ `{=latex}`the`\
`Work).``\ `{=latex}`Notwithstanding``\ `{=latex}`the``\ `{=latex}`above,``\ `{=latex}`Licensor``\ `{=latex}`reserves``\ `{=latex}`the``\ `{=latex}`right``\ `{=latex}`to`\
`release``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`under``\ `{=latex}`different``\ `{=latex}`license``\ `{=latex}`terms``\ `{=latex}`or``\ `{=latex}`to``\ `{=latex}`stop`\
`distributing``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`at``\ `{=latex}`any``\ `{=latex}`time;``\ `{=latex}`provided,``\ `{=latex}`however``\ `{=latex}`that``\ `{=latex}`any``\ `{=latex}`such`\
`election``\ `{=latex}`will``\ `{=latex}`not``\ `{=latex}`serve``\ `{=latex}`to``\ `{=latex}`withdraw``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`(or``\ `{=latex}`any``\ `{=latex}`other`\
`license``\ `{=latex}`that``\ `{=latex}`has``\ `{=latex}`been,``\ `{=latex}`or``\ `{=latex}`is``\ `{=latex}`required``\ `{=latex}`to``\ `{=latex}`be,``\ `{=latex}`granted``\ `{=latex}`under``\ `{=latex}`the`\
`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License),``\ `{=latex}`and``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`will``\ `{=latex}`continue``\ `{=latex}`in``\ `{=latex}`full`\
`force``\ `{=latex}`and``\ `{=latex}`effect``\ `{=latex}`unless``\ `{=latex}`terminated``\ `{=latex}`as``\ `{=latex}`stated``\ `{=latex}`above.`

`8.``\ `{=latex}`Miscellaneous`

`a.``\ `{=latex}`Each``\ `{=latex}`time``\ `{=latex}`You``\ `{=latex}`distribute``\ `{=latex}`or``\ `{=latex}`publicly``\ `{=latex}`digitally``\ `{=latex}`perform``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`or`\
`a``\ `{=latex}`Collective``\ `{=latex}`Work,``\ `{=latex}`the``\ `{=latex}`Licensor``\ `{=latex}`offers``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`recipient``\ `{=latex}`a``\ `{=latex}`license`\
`to``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`on``\ `{=latex}`the``\ `{=latex}`same``\ `{=latex}`terms``\ `{=latex}`and``\ `{=latex}`conditions``\ `{=latex}`as``\ `{=latex}`the``\ `{=latex}`license``\ `{=latex}`granted`\
`to``\ `{=latex}`You``\ `{=latex}`under``\ `{=latex}`this``\ `{=latex}`License.`

`b.``\ `{=latex}`Each``\ `{=latex}`time``\ `{=latex}`You``\ `{=latex}`distribute``\ `{=latex}`or``\ `{=latex}`publicly``\ `{=latex}`digitally``\ `{=latex}`perform``\ `{=latex}`a``\ `{=latex}`Derivative`\
`Work,``\ `{=latex}`Licensor``\ `{=latex}`offers``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`recipient``\ `{=latex}`a``\ `{=latex}`license``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`original`\
`Work``\ `{=latex}`on``\ `{=latex}`the``\ `{=latex}`same``\ `{=latex}`terms``\ `{=latex}`and``\ `{=latex}`conditions``\ `{=latex}`as``\ `{=latex}`the``\ `{=latex}`license``\ `{=latex}`granted``\ `{=latex}`to``\ `{=latex}`You`\
`under``\ `{=latex}`this``\ `{=latex}`License.`

`c.``\ `{=latex}`If``\ `{=latex}`any``\ `{=latex}`provision``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`is``\ `{=latex}`invalid``\ `{=latex}`or``\ `{=latex}`unenforceable``\ `{=latex}`under`\
`applicable``\ `{=latex}`law,``\ `{=latex}`it``\ `{=latex}`shall``\ `{=latex}`not``\ `{=latex}`affect``\ `{=latex}`the``\ `{=latex}`validity``\ `{=latex}`or``\ `{=latex}`enforceability`\
`of``\ `{=latex}`the``\ `{=latex}`remainder``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`terms``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License,``\ `{=latex}`and``\ `{=latex}`without``\ `{=latex}`further`\
`action``\ `{=latex}`by``\ `{=latex}`the``\ `{=latex}`parties``\ `{=latex}`to``\ `{=latex}`this``\ `{=latex}`agreement,``\ `{=latex}`such``\ `{=latex}`provision``\ `{=latex}`shall``\ `{=latex}`be`\
`reformed``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`minimum``\ `{=latex}`extent``\ `{=latex}`necessary``\ `{=latex}`to``\ `{=latex}`make``\ `{=latex}`such``\ `{=latex}`provision`\
`valid``\ `{=latex}`and``\ `{=latex}`enforceable.`

`d.``\ `{=latex}`No``\ `{=latex}`term``\ `{=latex}`or``\ `{=latex}`provision``\ `{=latex}`of``\ `{=latex}`this``\ `{=latex}`License``\ `{=latex}`shall``\ `{=latex}`be``\ `{=latex}`deemed``\ `{=latex}`waived``\ `{=latex}`and``\ `{=latex}`no`\
`breach``\ `{=latex}`consented``\ `{=latex}`to``\ `{=latex}`unless``\ `{=latex}`such``\ `{=latex}`waiver``\ `{=latex}`or``\ `{=latex}`consent``\ `{=latex}`shall``\ `{=latex}`be``\ `{=latex}`in`\
`writing``\ `{=latex}`and``\ `{=latex}`signed``\ `{=latex}`by``\ `{=latex}`the``\ `{=latex}`party``\ `{=latex}`to``\ `{=latex}`be``\ `{=latex}`charged``\ `{=latex}`with``\ `{=latex}`such``\ `{=latex}`waiver``\ `{=latex}`or`\
`consent.`

`e.``\ `{=latex}`This``\ `{=latex}`License``\ `{=latex}`constitutes``\ `{=latex}`the``\ `{=latex}`entire``\ `{=latex}`agreement``\ `{=latex}`between``\ `{=latex}`the``\ `{=latex}`parties`\
`with``\ `{=latex}`respect``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`Work``\ `{=latex}`licensed``\ `{=latex}`here.``\ `{=latex}`There``\ `{=latex}`are``\ `{=latex}`no`\
`understandings,``\ `{=latex}`agreements``\ `{=latex}`or``\ `{=latex}`representations``\ `{=latex}`with``\ `{=latex}`respect``\ `{=latex}`to``\ `{=latex}`the`\
`Work``\ `{=latex}`not``\ `{=latex}`specified``\ `{=latex}`here.``\ `{=latex}`Licensor``\ `{=latex}`shall``\ `{=latex}`not``\ `{=latex}`be``\ `{=latex}`bound``\ `{=latex}`by``\ `{=latex}`any`\
`additional``\ `{=latex}`provisions``\ `{=latex}`that``\ `{=latex}`may``\ `{=latex}`appear``\ `{=latex}`in``\ `{=latex}`any``\ `{=latex}`communication``\ `{=latex}`from`\
`You.``\ `{=latex}`This``\ `{=latex}`License``\ `{=latex}`may``\ `{=latex}`not``\ `{=latex}`be``\ `{=latex}`modified``\ `{=latex}`without``\ `{=latex}`the``\ `{=latex}`mutual``\ `{=latex}`written`\
`agreement``\ `{=latex}`of``\ `{=latex}`the``\ `{=latex}`Licensor``\ `{=latex}`and``\ `{=latex}`You.`

`Creative``\ `{=latex}`Commons``\ `{=latex}`is``\ `{=latex}`not``\ `{=latex}`a``\ `{=latex}`party``\ `{=latex}`to``\ `{=latex}`this``\ `{=latex}`License,``\ `{=latex}`and``\ `{=latex}`makes``\ `{=latex}`no``\ `{=latex}`warranty`\
`whatsoever``\ `{=latex}`in``\ `{=latex}`connection``\ `{=latex}`with``\ `{=latex}`the``\ `{=latex}`Work.``\ `{=latex}`Creative``\ `{=latex}`Commons``\ `{=latex}`will``\ `{=latex}`not``\ `{=latex}`be`\
`liable``\ `{=latex}`to``\ `{=latex}`You``\ `{=latex}`or``\ `{=latex}`any``\ `{=latex}`party``\ `{=latex}`on``\ `{=latex}`any``\ `{=latex}`legal``\ `{=latex}`theory``\ `{=latex}`for``\ `{=latex}`any``\ `{=latex}`damages`\
`whatsoever,``\ `{=latex}`including``\ `{=latex}`without``\ `{=latex}`limitation``\ `{=latex}`any``\ `{=latex}`general,``\ `{=latex}`special,`\
`incidental``\ `{=latex}`or``\ `{=latex}`consequential``\ `{=latex}`damages``\ `{=latex}`arising``\ `{=latex}`in``\ `{=latex}`connection``\ `{=latex}`to``\ `{=latex}`this`\
`license.``\ `{=latex}`Notwithstanding``\ `{=latex}`the``\ `{=latex}`foregoing``\ `{=latex}`two``\ `{=latex}`(2)``\ `{=latex}`sentences,``\ `{=latex}`if``\ `{=latex}`Creative`\
`Commons``\ `{=latex}`has``\ `{=latex}`expressly``\ `{=latex}`identified``\ `{=latex}`itself``\ `{=latex}`as``\ `{=latex}`the``\ `{=latex}`Licensor``\ `{=latex}`hereunder,``\ `{=latex}`it`\
`shall``\ `{=latex}`have``\ `{=latex}`all``\ `{=latex}`rights``\ `{=latex}`and``\ `{=latex}`obligations``\ `{=latex}`of``\ `{=latex}`Licensor.`

`Except``\ `{=latex}`for``\ `{=latex}`the``\ `{=latex}`limited``\ `{=latex}`purpose``\ `{=latex}`of``\ `{=latex}`indicating``\ `{=latex}`to``\ `{=latex}`the``\ `{=latex}`public``\ `{=latex}`that``\ `{=latex}`the`\
`Work``\ `{=latex}`is``\ `{=latex}`licensed``\ `{=latex}`under``\ `{=latex}`the``\ `{=latex}`CCPL,``\ `{=latex}`neither``\ `{=latex}`party``\ `{=latex}`will``\ `{=latex}`use``\ `{=latex}`the``\ `{=latex}`trademark`\
`"Creative``\ `{=latex}`Commons"``\ `{=latex}`or``\ `{=latex}`any``\ `{=latex}`related``\ `{=latex}`trademark``\ `{=latex}`or``\ `{=latex}`logo``\ `{=latex}`of``\ `{=latex}`Creative`\
`Commons``\ `{=latex}`without``\ `{=latex}`the``\ `{=latex}`prior``\ `{=latex}`written``\ `{=latex}`consent``\ `{=latex}`of``\ `{=latex}`Creative``\ `{=latex}`Commons.``\ `{=latex}`Any`\
`permitted``\ `{=latex}`use``\ `{=latex}`will``\ `{=latex}`be``\ `{=latex}`in``\ `{=latex}`compliance``\ `{=latex}`with``\ `{=latex}`Creative``\ `{=latex}`Commons’`\
`then-current``\ `{=latex}`trademark``\ `{=latex}`usage``\ `{=latex}`guidelines,``\ `{=latex}`as``\ `{=latex}`may``\ `{=latex}`be``\ `{=latex}`published``\ `{=latex}`on``\ `{=latex}`its`\
`website``\ `{=latex}`or``\ `{=latex}`otherwise``\ `{=latex}`made``\ `{=latex}`available``\ `{=latex}`upon``\ `{=latex}`request``\ `{=latex}`from``\ `{=latex}`time``\ `{=latex}`to``\ `{=latex}`time.`

`Creative``\ `{=latex}`Commons``\ `{=latex}`may``\ `{=latex}`be``\ `{=latex}`contacted``\ `{=latex}`at``\ `{=latex}`http://creativecommons.org/.`

[^1]: Hint: transporters.

[^2]: With no mention of overtime pay---our bosses seemed to think that
    ten dollars' worth of pizza was adequate compensation for four hours
    of work.

[^3]: Six rather than eight because there are *always*
    interruptions---if you can actually spend 75% of your time on the
    things you're supposed to be doing, you're a lot better at staying
    focused than most people.

[^4]: If timeslicing is bad, why are schools set up to require you to do
    it *all the time*? Doing nothing but the project course eight hours
    a day for three weeks would be more efficient. However, it would be
    harder on instructors, and would be difficult to integrate with
    courses in subjects like math and languages that take time to soak
    in.

[^5]: You might also want to check out Google's Summer of Code program,
    which pays students a few thousand dollars for working on a
    recognized open source project during their summer break.

[^6]: The scenario is that you get on an elevator with Bill Gates, and
    he says, "So, what are you working on?" You have six floors to
    convince him to fund you---what do you say?

[^7]: Joel Spolsky attributes this idea to Jim Highsmith.

[^8]: Need a citation for this

[^9]: It would be easier still if iCal, Outlook, and Google Calendar
    would all talk to one another...

[^10]: The boss of the last product group I worked in rotated developers
    into testing for a few weeks at the end of every release cycle. I
    learned more about the product I was building in those weeks than I
    learned in the rest of the year; configuring the product to work
    with databases I'd never even heard of before, and exercising
    features I only vaguely knew existed, paid dividends many times
    over.

[^11]: The best, of course, is personal integrity.

[^12]: Lisp! Lisp! All the *really* cool programmers use Lisp!

[^13]: Usually drawn up by committees packed with people who knew all
    five verses of the high school cheer.

[^14]: "You can't manage what you don't measure" is a truism in the
    business world. Unfortunately, so is, "You only get what you
    reward." If developers are rewarded for the number of lines of code
    they write, they will write overly-verbose code; if they are
    rewarded for the number of bugs they find, they won't bother to do
    any testing up front, since that would actually lower their score. I
    think metrics are valuable, but it requires a lot of maturity (and
    the ability to reflect on what they actually mean) to realize that
    value.

[^15]: Finding out who else on the team is unhappy can be the hardest
    part of the whole process, since you can't even ask the question
    without letting on that you're upset, and word will almost certainly
    get back to whoever you're asking about, who might then turn around
    and accuse you of stirring up trouble. After a couple of unhappy
    experiences of this kind, I've learned that it's best to raise the
    issue at a team meeting in front of everyone.

[^16]: It isn't uncommon to have both halves of a pair tell the
    instructor that they're doing all the work. This is one of the
    reasons I insist that students use version control to manage their
    projects: it lets me check who's actually written what.

[^17]: Many studies have shown that people tend to be more abrupt or
    confrontational in email than they are in person. If you aren't
    careful, this can easily lead to a vicious circle that only ends
    when one person or another is compared to Hitler...

[^18]: Or Trac, or Google Code, or whatever portal your team is
    using---see Section [6.9](#s:tooling-portal){reference-type="ref"
    reference="s:tooling-portal"} for more about these.

[^19]: Never, ever ship on Friday.

[^20]: Finer-grained divisions, such as a 1--10 scale, add no value:
    nobody has an algorithm for distinguishing priority 6 items from
    priority 7 items, and anyway, the grid is just to get conversation
    going.

[^21]: Something *always* goes wrong

[^22]: This term comes from a frequent scene in the original *Star Trek*
    series. Kirk: "How long 'til the engines are back on line?" Scotty:
    "Three days, captain." Kirk: "I need them in two minutes!" Scotty:
    "Och, all right."

[^23]: You will meet people who will be very critical every time one of
    your estimates is wrong. In my experience, they are no better at
    estimating than anyone else. When you point this out to them, do so
    politely.

[^24]: A religious war is one in which combatants hold very strong
    opinions precisely because there is no evidence to support either
    side.

[^25]: Where "running" means "running correctly". If the program doesn't
    have to be correct, you can write it in ten seconds or less in any
    language you like.

[^26]: He went on to become a vice president of IBM, which shows how far
    a good tool can take you.

[^27]: Its inventor, Anders Hejlsberg, went on to design C\#, which also
    shows how far a good tool can take you.

[^28]: Having to agree on *which* IDE to use may be another reason why
    some programmers resist adopting any IDE at all, since they require
    even more investment to master than editors.

[^29]: Possibly yourself two weeks from now

[^30]: Or "standards", since there are at least half a dozen variations
    in use today.

[^31]: Of which only a few percent are actually live at any time.

[^32]: Read-only because (a) giving the web server the ability to
    overwrite content in the repository would be a huge security hole,
    and (b) there's no point allowing people to write to the repository
    unless you can think of a web-based interface for editing source
    code that people will actually use.

[^33]: Like a scripting API, so that instructors can file the same
    ticket against two dozen projects in one step, or a "roll up" view
    that shows the progress several projects are making side by side.

[^34]: To *fork* a project means to create a new version of it that will
    evolve independently (i.e., to take a fork in the road). Forking
    shouldn't be done lightly, since the more projects there are, the
    less development and maintenance effort can be put into each.

[^35]: The most advanced wrinkle on this idea is Donald Knuth's
    *literate programming*, which holds that programs should be written
    in a rich notation that combines mathematical symbols with
    programming constructs, then compiled to produce human-readable and
    machine-readable versions. It's a great idea, and as Unicode becomes
    more widespread, it may well catch on. What's holding it back now is
    that debugging such programs is hard, since the code that's actually
    bears only a rough resemblance to what you actually typed in. If
    you're interested in graduate school, there's a great thesis waiting
    to be written here...

[^36]: The first version of which was written by Erich Gamma on a flight
    across the Atlantic, which just goes to show you how far you can go
    while writing a great tool.

[^37]: It's hard to do static analysis for dynamic languages like Python
    and Ruby, which is one of the reasons why compiled languages like
    C++, Java, and C\# are still more popular for very large projects.

[^38]: Eleven at present, though the number varies from term to term.

[^39]: Assuming we're generating well-formed HTML, which we should be.

[^40]: A "release log" is a file (often a spreadsheet) that records
    exactly what was shipped to whom, when.

[^41]: Every modern language has a logging facility. If you're using
    Java, for example, the de facto standard is Apache's log4j.

[^42]: Need a citation for this.

[^43]: For some reason, computer scientists often write abstracts that
    are like movie trailers or elevator pitches, rather than proper
    summaries. "We will contrast frobnication with jamframification"
    doesn't help people who have a hundred articles to skim; "We show
    that frobnication is 28% more likely to spleedle than
    jamframification under heavy load" is a lot more useful.

[^44]: The spec can be as simple as specially-flagged tickets in the bug
    database.