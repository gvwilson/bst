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
introducing a few minor ones of its own. Both of these were <g
key="centralized-system">centralized systems</g>:

1.  One <g key="repository">repository</g> stored the definitive copy of the
    project's files.

1.  Nobody ever edited the contents of the main repository directly. Instead,
    everyone worked in a local copy.

1.  In order to share files with other people (or to create a backup, which
    is really just a way to share files with your future self) people would
    <g key="push">push</g> the contents of their copy to the main repository.
    To get other people's work, they would <g key="pull">pull</g> changes from
    the main repository and <g key="merge">merge</g> them with their own work.

Centralized version control systems have largely been replaced by <g
key="decentralized-system">decentralized</g> ones, and in particular by a tool
called [Git][git]. In theory, Git doesn't need a main repository; instead,
developers can merge the contents of any repository with any other one.  In
practice, almost every project designates one repository as the master copy so
that everyone knows where to look to find the current state of the project.

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
look at how to use Git and GitHub to collaborate. We will show the commands as
if you were typing them on the command line; if you are a beginner, we recommend
that you use a graphical interface like [GitKraken][gitkraken] or the one that
comes with your IDE. These GUIs are all layered on top of the commands we are
going to discuss, so they (should) all work the same way.

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

When I am working on a solo project or in a small team, seven commands account
for roughly 85% of my Git activity. Adding two more commands to set things up
produces a toolkit that uses Git as a file backup system.

The first step is to make sure that Git knows who we are by telling it our name
and email address:

```
$ git config --global user.name "Peggy Springsteen"
$ git config --global user.email "peggy@wolframhart.org"
```

Breaking this down:

-   The dollar sign `$` is a <g key="shell-prompt">shell prompt</g>.  We don't
    type that; the shell prints it to show us that it's waiting for a command.

-   Git commands are written as <code>git <em>verb</em></code>, where
    <code><em>verb</em></code> is a <g key="sub-command">sub-command</g> telling
    Git exactly what we want to do.

-   The `--global` <g key="flag">flag</g> is used to specify a value for the
    command in the same way that parameters are used to pass values to
    functions. In this case, we're telling Git that we want to configure things
    globally (i.e., for every project we have on this computer). We can also
    configure things repository-by-repository if we want to have a different
    name or email address for different projects.

-   `user.name` is the thing we want to configure. There are a lot of these;
    we can use `git config --list` to display them.

-   Finally, we specify the values that we want `user.name` and `user.email` to
    have. We wrap these in quotes because they contain spaces and the `@`
    symbol, which might otherwise confuse the shell.

Now that Git knows who we are, let's set up our project. If we are starting from
scratch, we create a directory, go into it, and run `git init`. This may or may
not print out some messages depending on what version of Git you have and how
much of its output your GUI shows (if you're using one). Regardless of that,
this command creates a sub-directory called `.git` inside your project
directory. That special sub-directory is what makes something a project: it
contains all of the administrative data that Git uses to keep track of what
files you have and how they've changed.

> **Don't mess**
>
> *Don't ever edit the files in your `.git` directory yourself.*  Doing so will
> have the same unpleasant result as editing a spreadsheet or an image as if it
> was a text file. If you'd like to know more about what they're for and how Git
> uses them, please see <cite>Chacon2014</cite> or <cite>Cook2019</cite>.

If your instructor or one of your teammates has already created a project, you
won't use `git init`. Instead, you will use `git clone` followed by the
project's URL to get a local copy called a <g key="git-clone">clone</g>. For
example, if you want a clone of this book, you can do this:

```
$ git clone https://github.com/gvwilson/bst.git
```

{: .continue}
This will create a directory with the same name as the project, create a `.git`
sub-directory inside it, and download the project's history so that you can
start work.

Regardless of how you create your repository, you can use `git log` to look at
its history. If I run this command right now for this book, I get:

```
$ git log
commit d4351c4f093f60d03f303737b66b28ebb6b9ed45
Author: Greg Wilson <gvwilson@third-bit.com>
Date:   Fri Feb 19 09:48:37 2021 -0500

    Opening section of version control.

commit 80d38a8cbf650431fe4719ec768bd890e00c7431
Author: Greg Wilson <gvwilson@third-bit.com>
Date:   Thu Feb 18 11:21:00 2021 -0500

    Teams

commit 6e30bd5e5af2c3491f25f014c03d5e9ff5c79879
Author: Greg Wilson <gvwilson@third-bit.com>
Date:   Wed Feb 17 20:48:04 2021 -0500

    Moving a section

...
```

Each entry has:

-   A line labeled `commit` followed by a large hexadecimal number.  This number
    is a unique label for the state of the project's files at that point in
    time.  if we want to refer to a particular version of our project, we can
    use this or the first half-dozen digits (such as `6e30bd`) so long as the
    latter is unambiguous.

-   Two lines showing who saved the state of the project and when. The name and
    email address in the `Author` field are the ones we set up with `git
    config`; the <g key="timestamp">timestamp</g> is accurate to the second, and
    includes timezone information like the `-0500` showing that I'm in Eastern
    time so that anyone in the world can tell exactly when these files were
    saved.

-   A short comment called a <g key="commit-message">commit message</g> that
    tells us what this change is all about. We will take a look in the next
    section at how to write a good commit message; for now, just remember that
    if you and your teammates have made a hundred changes to the project over
    the course of ten or twelve weeks, you're going to want something more
    informative than "Fixed stuff."

All right: what are <g key="commit">commits</g> and where do they come from? A
commit is a snapshot of the project at a particular moment in time; we create
them using a command like:

```
$ git commit -m "Made the status bar display the user name"
```

{: .continue}
Here, `commit` is the verb and the `-m` (short for "message") flag is followed
by the comment we want to save in the log.

If we only use `git commit`, though, nothing will happen. We need to tell Git
which files we want to save in the commit, which we do using `git add`:

```
$ git add version-control.md _data/glossary.yml
```

{: .continue}
One way to think about this is that `git add` puts things in a box to be
shipped, while `git commit` actually sends the package. Git requires us to do
this in two steps because we might change our mind about what we want to store:
for example, we might `git add` a file, then realize we need to make a few more
edits, `git add` it again, and then `git commit`. Alternatively, we might add a
bunch of files, then realize that some of them (like editor backup files or
temporary files created by the compiler) shouldn't be saved, so we take them out
before committing.

We can keep track of which changes haven't yet been added and which ones have
using `git status`. If I run this command right now in this book's project I
get:

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   _includes/links.md
	modified:   bibliography.md
	modified:   version-control.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   version-control.md
```

{: .continue}
The first paragraph titled "Changes to be committed" tells me which files I have
asked Git to save using `git add`. The second paragraph, "Changes not staged for
commit", shows that I have modified `version-control.md` (this chapter) since I
last asked Git to save a snapshot. Both paragraphs tell me that I can use `git
restore` with or without the `--staged` flag to put a file back the way it was
if I decide I don't want to save the changes I've made.

I can also use `git restore` to recover an old version of a file from any
previous commit. Being able to do this was the original motivation for version
control systems, and is still one of the main reasons people use them. For
example, if I want to get the version of this file from two days ago, I can use
`git log` to find the commit ID `2be70844`, and then run:

```
$ git restore --source 2be70844 version-control.md
```

{: .continue}
I can also count backward from where I am now.  The most recent commit has the
special symbolic name `HEAD`; the expression `HEAD~1` means "the one before it",
while `HEAD~2` goes back two commits and so on. Regardless of how I specify what
I want, restoring an old version doesn't erase any of the ones I have saved
since then: the project's history stays intact.

Finally, I should make sure there's a second physical copy of my work so that if
my drive fails or my laptop is stolen I don't lose everything I've done. If I
created the repository by cloning something on GitHub, then Git will
automatically have created a bookmark called a <g key="git-remote">remote</g>
that points at the original repository. I can get a list of remotes like this:

```
$ git remote -v
origin	https://github.com/gvwilson/bst (fetch)
origin	https://github.com/gvwilson/bst (push)
```

{: .continue}
The `-v` flag (short for "verbose") tells Git to print more than just the
remote's name. The remote itself is called `origin`, and Git lists two URLs for
it because in theory you can download (or "fetch") from one and upload (or
"push") to another. Sane people don't do this.

If I want to save everything I've done locally on GitHub, I push my changes:

```
$ git push origin main
```

{: .continue}
The verb is `push`; the word `origin` identifies where I want to send things,
and the word `main` identifies the branch I'm on.  We'll discuss branches in the
next section, but for now, you can run `git branch` to see which ones you have
and which one you're working in.

The counterpart of `git push` is `git pull`. It gets updates from the remote
repository and merges them into your local copy:

```
$ git pull origin main
```

Pushing and pulling changes allows you and your teammates to synchronize your
work. They're also very useful operations if you're working on your own and
using two or more computers (such as a personal laptop and your school's
servers).

> **Clean and build**
>
> Many instructors require learners to submit work by committing it to a Git
> repository. One way to check that what works for you will work for whoever is
> grading it is to clone a fresh copy of the project in a temporary directory
> and make sure that everything builds and runs there. Doing that will tell you
> if you or one of your teammates has forgotten to commit a key file. In an
> advanced course, you might be asked to do this automatically every time
> someone commits changes; we'll explore this in <chap key="tooling"></chap>.

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
