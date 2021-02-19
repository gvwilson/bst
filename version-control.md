---
---

Version control is the collective memory of the project. It's what lets you move
files from one machine to another without clobbering stuff you just spent three
hours writing, and without worrying about whether you forgot an all-important
file. It's also what lets you undo your mistakes: if you spend an hour or two
going down the wrong path, and want to get back to where you were, version
control lets you do it reliably with a single command. And if all that wasn't
enough, version control lets you keep track of who did what, so that you can
allocate credit and blame where they're due.

Dozens of version control systems exist. For many years, CVS was the workhorse
of the open source world, and very popular in commercial projects as well. It
was replaced by Subversion, which fixe many of its predecessor's flaws while
introducing a few minor ones of its own. Both of these were
<g key="centralized-system">centralized systems</g>:

1.  One <g key="repository">repository</g> stored the definitive copy of the
    project's files.

1.  Nobody ever edited the contents of the main repository directly. Instead,
    everyone worked in a local copy.

1.  In order to share files with other people (or to create a backup, which
    is really just a way to share files with your future self) people would
    <g key="push">push</g> the contents of their copy to the main repository.
    To get other people's work, they would <g key="pull">pull</g> changes from
    the main repository and <g key="merge">merge</g> them with their own work.

Centralized version control systems have largely been replaced by
<g key="decentralized-system">decentralized</g> ones, and in particular by
a tool called [Git][git]. In theory, Git doesn't need a main repository;
instead, developers can merge the contents of any repository with any other one.
In practice, almost every project designates one repository as the master copy
so that everyone knows where to look to find the current state of the project.

Unfortunately, Git has a needlessly complicated interface. <cite>PerezDeRosso2013</cite>
found that even experienced users have a <g key="mental-model">mental model</g>
of how it works that contradicts its actual operation in important ways,
and each of those contradictions produces a steady stream of "what the hell?"
moments. Other distributed version control systems like [Mercurial][mercurial]
are proof that this complexity and pain are unnecessary.

> **Why can't we fix it?**
>
> If Git's interface is a problem, why can't we build a new one?
> <cite>PerezDeRosso2016</cite> tried, but as they report, the gravity of the
> existing interface is simply too powerful: as soon as people run into a
> problem and start searching online for solutions, they're thrown back into the
> world of original Git.

So why do people keep using Git? The answer these days is, "Because it's the tax
they have to pay in order to use [GitHub][github]." At the time of writing,
GitHub has over 40 million users and hosts over 28 million public repositories,
including those for many well-known open source projects. It is easily the most
popular [software forge][software-forge] in existence, and offers all of the
tools a small software team needs. Other forges exist, such as
[Bitbucket][bitbucket] and [GitLab][gitlab], but GitHub's share of the
educational market is even larger than than its share of professional
development, so if you're using anything in class, you're almost certainly using
it.

This chapter won't try to teach you Git from scratch:
[GitHub's guides][github-guides] do an excellent job of that, as does
[the Carpentries][carpentries]'s [lesson on Git][carpentries-git].
Instead, we will review the basics that we hope you have learned previous, then
look at how to use Git and GitHub to collaborate.

> **Trapped in the punchcard era**
>
> The biggest weakness of today's version control systems is that they work best
> with plain text files---most of them don't really know what to do with binary
> files, such as sound clips, images, or Microsoft Word documents. When changes
> have been made to a JavaScript source file, for example, Git can find and
> display the lines that have been edited. When you and your teammates edit the
> SVG diagrams in your final report, on the other hand, a line-by-line view
> isn't much use, and if two of you update the image you're using as a logo, all
> Git can do it tell you that there's a conflict. It doesn't have to be like
> this: programmers could build tools to compare and merge files that aren't
> backward-compatible with punchcards, and by doing so, make version control
> accessible to people whose file formats aren't stuck in the 1960s.

## A review of the basics

FIXME: add/commit; status and log; push and pull; configuration.

## A branch-based workflow

FIXME: branches; merging; rebasing; pull requests.

## Code reviews

FIXME: how to do a code review (include examples)

## Tracking issues

You probably have a to-do list somewhere. It might be scribbled in a calendar or
lab notebook, kept in a text file on your laptop, or in your head; wherever and
however you maintain it, it lists the things you're supposed to do, when they're
due, and (possibly) how urgent they are.

At its simplest, an <g key="issue-tracker">issue tracker</g> is a shared to-do
list. Ticketing systems are also called ticketing systems and bug trackers,
because most software projects use one to keep track of the bugs that developers
and users find. These days, issue trackers are almost invariably web-based. To
create a new ticket, you enter a title and a short description; the system then
assigns it a unique serial number. You can usually also specify:

-   who is responsible for the ticket (e.g., who's supposed to fix the bug, or
    test the fix, or update the documentation);

-   what kind of ticket it is (a bug report, a request for a new feature, a
    question to be answered, or some other task);

-   how important it is; and

-   when it's due.

If version control keeps track of where your project has been, your ticketing
system keeps track of where you're going. After version control, ticketing is
therefore the most essential part of a team project. Without it, you and your
teammates will have to constantly ask each other "What are you working on?",
"What am I supposed to be working on?", and "Who was supposed to do that?" Once
you start using one, on the other hand, it's easy to find out what the project's
status is: just look at the open tickets, and at those that have been closed
recently.  You can use this to create agendas for your status meetings , and to
remind yourself what you were doing three months ago when the time comes to
write your final report.

Of course, a issue tracker is only as useful as what you put into it.  If you're
describing a bug in a large application, you should include enough information
to allow someone to reproduce the problem, and someone else to figure out how
urgent the bug is, who should work on it, and what other parts of the
application might be affected by a fix. This is why industrial-strength issue
trackers like Bugzilla have upwards of two dozen fields per ticket to record:

-   what version of the software you were using;

-   what platform it was running on;

-   what you did to make it crash;

-   any data or configuration files the program relies on;

-   whatever stack traces, error reports, or log messages the program produced;

-   its severity (i.e., how much damage the bug might do);

-   its priority (how urgently the bug needs to be fixed); and

-   other tickets that might be related.

This is a lot more information than student projects require. In addition,
students are almost always working on several courses at once, and it's common
for students to have to put their team project aside for a few days to work on
assignments for other courses. For these reasons, I've found that most student
teams won't actually use anything more sophisticated than a web-base to-do list
unless they're forced to by the course's grading scheme. In that case, most come
away with the impression that tickets are something you only use when you have
to, rather than a vital team coordination tool.

{% include links.md %}
