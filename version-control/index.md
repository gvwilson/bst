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
introducing a few minor ones of its own. Both of these were <span
g="centralized-system">centralized systems</span>:

1.  One <span g="repository">repository</span> stored the definitive copy of the
    project's files.

1.  Nobody ever edited the contents of the main repository directly. Instead,
    everyone worked in a local copy.

1.  In order to share files with other people (or to create a backup, which is
    really just a way to share files with your future self) people would <span
    g="push">push</span> the contents of their copy to the main repository.  To
    get other people's work, they would download changes from the main
    repository and combine them with their own work.

Centralized version control systems have largely been replaced by <span
g="decentralized-system">decentralized</span> ones, and in particular by a tool
called [Git][git]. In theory, Git doesn't need a main repository; instead,
developers can merge the contents of any repository with any other one.  In
practice, almost every project designates one repository as the master copy so
that everyone knows where to look to find the current state of the project.

Unfortunately, Git has a needlessly complicated interface.
<cite>PerezDeRosso2013</cite> found that even experienced users have a <span
g="mental-model">mental model</span> of how it works that contradicts its actual
operation in important ways, and each of those contradictions produces a steady
stream of "what the hell?"  moments. Other distributed version control systems
like [Mercurial][mercurial] are proof that this complexity and pain are
unnecessary.

<div class="callout" markdown="1">

### Why can't we fix it?

If Git's interface is a problem, why can't we build a new one?
<cite>PerezDeRosso2016</cite> tried, but as they report, the gravity of the
existing interface is simply too powerful: as soon as people run into a problem
and start searching online for solutions, they're thrown back into the world of
original Git.

</div>

So why do people keep using Git? The answer these days is, "Because it's the tax
they have to pay in order to use [GitHub][github]." At the time of writing,
GitHub has over 40 million users and hosts over 28 million public repositories,
including those for many well-known open source projects. It is easily the most
popular <span g="software-forge">software forge</spam> in existence, and offers
all of the tools a small software team needs. Other forges exist, such as
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

<div class="callout" markdown="1">

### Trapped in the punchcard era

The biggest weakness of today's version control systems is that they work be
files, such as sound clips, images, or Microsoft Word documents. When changes >
have been made to a JavaScript source file, for example, Git can find and >
display the lines that have been edited. When you and your teammates edit the >
SVG diagrams in your final report, on the other hand, a line-by-line view >
isn't much use, and if two of you update the image you're using as a logo, all >
Git can do it tell you that there's a conflict. It doesn't have to be like >
this: programmers could build tools to compare and merge files that aren't >
backward-compatible with punchcards, and by doing so, make version control >
accessible to people whose file formats aren't stuck in the 1960s.

</div>

## A review of the basics

When I am working on a solo project or in a small team, seven commands account
for roughly 85% of my Git activity. Adding two more commands to set things up
produces a toolkit that uses Git as a file backup system.

The first step is to make sure that Git knows who we are by telling it our name
and email address:

{% include code file="config.sh" %}

Breaking this down:

-   The dollar sign `$` is a <span g="shell-prompt">shell prompt</span>.  We don't
    type that; the shell prints it to show us that it's waiting for a command.

-   Git commands are written as <code>git <em>verb</em></code>, where
    <code><em>verb</em></code> is a <span g="sub-command">sub-command</span>
    telling Git exactly what we want to do.

-   The `--global` <span g="flag">flag</span> is used to specify a value for the
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

<div class="callout" markdown="1">

### Don't mess

*Don't ever edit the files in your `.git` directory yourself.* Doing so will
have the same unpleasant result as editing a spreadsheet or an image as if it >
was a text file. If you'd like to know more about what they're for and how Git >
uses them, please see <cite>Chacon2014</cite> or <cite>Cook2019</cite>.

</div>

If your instructor or one of your teammates has already created a project, you
won't use `git init`. Instead, you will use `git clone` followed by the
project's URL to get a local copy called a <span g="git-clone">clone</span>. For
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
```
```
commit d4351c4f093f60d03f303737b66b28ebb6b9ed45
Author: Greg Wilson <spanvwilson@third-bit.com>
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
    config`; the <span g="timestamp">timestamp</span> is accurate to the second,
    and includes timezone information like the `-0500` showing that I'm in
    Eastern time so that anyone in the world can tell exactly when these files
    were saved.

-   A short comment called a <span g="commit-message">commit message</span> that
    tells us what this change is all about. We will take a look in the next
    section at how to write a good commit message; for now, just remember that
    if you and your teammates have made a hundred changes to the project over
    the course of ten or twelve weeks, you're going to want something more
    informative than "Fixed stuff."

All right: what are <span g="commit">commits</span> and where do they come from? A
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

<div class="callout" markdown="1">

### The most popular question on Stack Overflow

FIXME: the Vim editor.

</div>

FIXME: explain .gitignore

We can keep track of which changes haven't yet been added and which ones have
using `git status`. If I run this command right now in this book's project I
get:

```
$ git status
```
```
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
automatically have created a bookmark called a <span
g="git-remote">remote</span> that points at the original repository. I can get a
list of remotes like this:

```
$ git remote -v
```
```
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

The counterpart of `git push` is `git pull`. It <span g="git-pull">pulls</g>
changes from the remote repository and merges them into your local copy:

```
$ git pull origin main
```

Pushing and pulling changes allows you and your teammates to synchronize your
work. They're also very useful operations if you're working on your own and
using two or more computers (such as a personal laptop and your school's
servers).

<div class="callout" markdown="1">

### Clean and build

Many instructors require learners to submit work by committing it to a Git
repository. One way to check that what works for you will work for whoever is >
grading it is to clone a fresh copy of the project in a temporary directory >
and make sure that everything builds and runs there. Doing that will tell you >
if you or one of your teammates has forgotten to commit a key file. In an >
advanced course, you might be asked to do this automatically every time >
someone commits changes; we'll explore this in <span c="tooling"></span>.

</div>

## A branch-based workflow

So far we have only used a sequential timeline with Git: each change builds on
the one before, and *only* on the one before.  However, there are times when we
want to try things out without disrupting our main work.  To do this, we can use
<span g="git-branch">branches</span> to work on separate tasks in parallel.
Each branch is a parallel timeline; changes made on the branch only affect that
branch unless and until we explicitly combine them with work done in another
branch.

We can see what branches exist in a repository like this:

```
$ git branch
```
```
* main
```

When we initialize a repository,
Git automatically creates a branch called `master`;
most people now rename this to `main` by running:

```
$ git branch -m main
```

{: .continue}
immediately after running `git init`.
The `main` branch is often considered the "official" version of the repository.
The asterisk `*` indicates that it is currently active,
i.e.,
that all changes we make will take place in this branch by default.
(The active branch is like the <span g="cwd">current working directory</span> in the shell.)

To create a new branch called `homework3`,
we run:

```
$ git branch homework3
```

The name of the branch should indicate what we plan to do in it,
just like the names of files and variables indicate what they're for.
We can check that the branch exists by running `git branch` again:

```
$ git branch
```
```
* main
  homework3
```

Our branch is there,
but the `*` shows that we are still in the `main` branch.
(By analogy,
creating a new directory doesn't automatically move us into that directory.)
To switch to our new branch we use the `checkout` command:

```
$ git checkout homework3
$ git branch
```
```
  main
* homework3
```

We haven't made any changes since switching to the `fit` branch,
so at this point `main` and `fit` are at the same point in the repository's history.
Commands like `ls` and `git log` therefore show that the files and history haven't changed.

<div class="callout" markdown="1">

### Where branches are saved

Git saves every version of every file in the repository's `.git` directory.
When we switch from one branch to another, it copies files out of there and >
rearranges directories to restore that state of the world.

</div>

Why go to all this trouble?  Because it allows us to work on several things at
once without stepping on our own toes, just as putting variables inside objects
and classes allows us to ignore the details of *this* when we're working on
*that*. For example, if we are close to finishing homework assignment 3 but want
to get an early start on assignment 4, we can create a new branch from `main`
called `homework4` and start setting things up in there.
When we are done, we can <span g="git-merge">merge</span> the state of one
branch back into another. Merging doesn't change the source branch, but once
it's done, all of the changes made there are in the destination branch.

To see what the differences are between two branches, we use `git diff` with
those branches' names:

```
$ git diff homework3..main
```

{: .continue}
More generally, we can use `git diff` to compare any two states of the
repository, including old versions with current ones:

```
$ git diff HEAD~3..HEAD
```

Once we're sure we actually want to merge changes, we do so like this:

```
$ git merge homework3 main
```

Git automatically creates a new commit to represent the merge.  If we now run
`git diff main..homework3`, Git doesn't print anything because there aren't any
differences to show.

Once we merge the changes from `homework3` into `main` there is no need to keep
the `homework` branch, so we can delete it:

```
$ git branch -d fit
```
```
Deleted branch homework3 (was 1577404).
```

Merging `homework3` into `main` went smoothly because there were no conflicts
between the two branches, but if we are going to use branches, we must learn how
to merge <span g="git-conflict">conflicts</g>.  These occur when a line has been
changed in different ways in two separate branches or when a file has been
deleted in one branch but edited in the other.

If the file `README.md` has been changed in both `main` and `homework4`,
`git diff` will show the conflict:

```
$ git diff homework4..main
```

When we try to merge `homework4` into `main`, Git doesn't know which of these
changes to keep:

```
$ git merge docs main
```

After we run this command, Git has put both sets of changes into `README.md`,
but has marked which came from where:

```
$ cat README.md
```

The lines from `<<<<<<< HEAD` to `=======` are what was in `main`, while the
lines from there to `>>>>>>> docs` show what was in `homework4`.  If there were
several conflicting regions in the same file, Git would mark each one this way.

We have to decide what to do next: keep the `main` changes, keep those from
`homework4`, edit this part of the file to combine them, or write something new.
Whatever we do, we must remove the `>>>`, `===`, and `<<<` markers.  Once we are
done, we can add the file and commit the change like we would any other edit:

```
$ git add README.md
$ git commit -m "Merging README additions"
```

Our branch's history will now show a single sequence of commits with the `main`
changes on top of the earlier `homework4` changes:

```
$ git log --oneline -n 4
```

If we want to see what happened, we can add the `--graph` option to `git log`:

```
$ git log --oneline --graph -n 4
```

At this point we can delete the `homework` branch or switch back to it and do
some more work.  Each time we switch to it, we merge changes *from* `main`
*into* `homework4`, do our editing (while switching back to `main` or other
branches as needed to work on the code), and then merge *from* `homework4` *to*
`main` once the documentation is updated.

Branches can be confused, but this workflow will help you keep track of what you
are doing:

1.  `git checkout main` to make sure you are in the `main` branch.

2.  `git checkout -b name-of-feature` to create a new branch.  *Always* create a
    branch when making changes, since you never know what else might come up.
    The branch name should be as descriptive as a variable name or filename
    would be.

3.  Make your changes.  If something occurs to you along the way---for example,
    if we are writing a new function and realize that the documentation for some
    other function should be updated---*don't* do that work in this branch.
    Instead, commit our changes, switch back to `main`, and create a new branch
    for the other work.

4.  When the new feature is complete, use `git merge` to get any changes you
    merged into `main` after creating `name-of-feature` and resolve any
    conflicts.  This is an important step: you want to test that everything
    works while you are in your feature branch, not in `main`.

5.  Finally, switch back to `main` and `git merge name-of-feature main` to merge
    your changes into `main`.  You should not have any conflicts, and all of
    your tests should pass.

Most experienced developers use this
<span g="branch-per-feature-workflow">branch-per-feature workflow</span>,
but what exactly is a "feature"?
These rules make sense for small projects:

1.  Anything cosmetic that is only one or two lines long can be done in `main`
    and committed right away.  "Cosmetic" means changes to comments or
    documentation: nothing that affects how code runs, not even a simple
    variable renaming.

2.  A pure addition that doesn't change anything else is a feature and goes into
    a branch.  For example, if you are adding a feature to the user interfaces,
    that should be done on its own branch because it might take several tries to
    get right, and you might interrupt yourself to fix things you discover along
    the way.

3.  Every bug fix is also done in a separate branch

The hardest thing about using a branch-per-feature workflow is sticking to it
for small changes.  As the first point in the list above suggests, most people
are pragmatic about this on small projects; on large ones, where dozens of
people might be committing, even the smallest and most innocuous change needs to
be in its own branch so that it can be reviewed (which we discuss below).

<div class="callout" markdown="1">

### Rebasing

One way to make the history of a repository easier to read is to squash several
consecutive commits into one.  This is called <span
g="git-rebase">rebasing</span>, and can be done using:

```
$ git rebase -i START
```

where `START` identifies the commit *before* the ones you want to start merging
(i.e., the last one *not* to modify). Rebasing can go wrong in a lot > of
confusing ways, particularly if you have merged changes from another branch >
into the one you're squashing, so we recommend that you avoid it for >
schoolwork.

</div>
