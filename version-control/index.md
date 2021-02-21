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

> **The most popular question on Stack Overflow**
>
> FIXME: the Vim editor.

FIXME: `.gitignore`

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

So far we have only used a sequential timeline with Git:
each change builds on the one before,
and *only* on the one before.
However,
there are times when we want to try things out
without disrupting our main work.
To do this, we can use \gref{branches}{git_branch} to work on separate tasks in parallel.\index{branch (in Git)}\index{Git!branch}
Each branch is a parallel timeline;
changes made on the branch only affect that branch
unless and until we explicitly combine them with work done in another branch.

We can see what branches exist in a repository using this command:\index{Git commands!branch}

```bash
$ git branch
```

```text
* master
```

When we initialize a repository,
Git automatically creates a branch called `master`.\index{Git!master branch}
It is often considered the "official" version of the repository.
The asterisk `*` indicates that it is currently active,
i.e.,
that all changes we make will take place in this branch by default.
(The active branch is like the \gref{current working directory}{current_working_directory} in the shell.)

> **Default Branches**
> 
> In mid-2020,
> GitHub changed the name of the default branch
> (the first branch created when a repository is initialized) 
> from "master" to "main."
> Owners of repositories may also change the name of the default branch. 
> This means that the name of the default branch may be different among repositories
> based on when and where it was created,
> as well as who manages it.

In the previous chapter,
we foreshadowed some experimental changes that we could try and make to `plotcounts.py`.

Making sure our project directory is our working directory,
we can inspect our current `plotcounts.py`:

```bash
$ cd ~/zipf
$ cat bin/plotcounts.py
```

```python
"""Plot word counts."""

import argparse

import pandas as pd


def main(args):
    """Run the command line program."""
    df = pd.read_csv(args.infile, header=None,
                     names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                           method='max')
    ax = df.plot.scatter(x='word_frequency',
                         y='rank', loglog=True,
                         figsize=[12, 6],
                         grid=True,
                         xlim=args.xlim)
    ax.figure.savefig(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Word count csv file name')
    parser.add_argument('--outfile', type=str,
                        default='plotcounts.png',
                        help='Output image file name')
    parser.add_argument('--xlim', type=float, nargs=2,
                        metavar=('XMIN', 'XMAX'),
                        default=None, help='X-axis limits')
    args = parser.parse_args()
    main(args)
```

We used this version of `plotcounts.py`
to display the word counts for *Dracula* on a log-log plot
(Figure \@ref(fig:git-cmdline-loglog-plot)).
The relationship between word count and rank looked linear,
but since the eye is easily fooled,
we should fit a curve to the data.
Doing this will require more than just a trivial change to the script,
so to ensure that this version of `plotcounts.py` keeps working
while we try to build a new one,
we will do our work in a separate branch.
Once we have successfully added curve fitting to `plotcounts.py`,
we can decide if we want to merge our changes back into the `master` branch.

## Creating a Branch {#git-advanced-branch-how}

To create a new branch called `fit`,
we run:

```bash
$ git branch fit
```

We can check that the branch exists by running `git branch` again:

```bash
$ git branch
```

```text
* master
  fit
```

Our branch is there,
but the asterisk `*` shows that we are still in the `master` branch.
(By analogy,
creating a new directory doesn't automatically move us into that directory.)
As a further check,
let's see what our repository's status is:

```bash
$ git status
```

```text
On branch master
nothing to commit, working directory clean
```

To switch to our new branch we can use the `checkout` command\index{Git commands!checkout}
that we first saw in Chapter \@ref(git-cmdline):

```bash
$ git checkout fit
$ git branch
```

```text
  master
* fit
```

In this case,
we're using `git checkout` to check out a whole repository,
i.e., switch it from one saved state to another.

We should choose the name to signal the purpose of the branch,
just as we choose the names of files and variables to indicate what they are for.
We haven't made any changes since switching to the `fit` branch,
so at this point `master` and `fit` are at the same point in the repository's history.
Commands like `ls` and `git log` therefore show that the files and history haven't changed.

> **Where Are Branches Saved?**
>
> Git saves every version of every file in the `.git` directory\index{Git!.git directory}
> that it creates in the project's root directory.
> When we switch from one branch to another,
> it replaces the files we see with
> their counterparts from the branch we're switching to.
> It also rearranges directories as needed
> so that those files are in the right places.

> **Why Branch?**
>
> Why go to all this trouble?
> Imagine we are in the middle of debugging a change like this
> when we are asked to make final revisions
> to a paper that was created using the old code.
> If we revert `plotcount.py` to its previous state we might lose our changes.
> If instead we have been doing the work on a branch,
> we can switch branches,
> create the plot,
> and switch back in complete safety.

We could proceed in three ways at this point:

1.  Add our changes to `plotcounts.py` once again in the `master` branch.
2.  Stop working in `master` and start using the `fit` branch for future development.
3.  \gref{Merge}{git_merge} the `fit` and `master` branches.

The first option is tedious and error-prone;
the second will lead to a bewildering proliferation of branches,
but the third option is simple, fast, and reliable.\index{Git commands!merge}\index{merge (in Git)}
To start,
let's make sure we're in the `master` branch:

```bash
$ git checkout master
$ git branch
```

```text
  fit
* master
```

We can now merge the changes in the `fit` branch into our current branch
with a single command:

```bash
$ git merge fit
```

```text
Updating ddb00fb..1577404
Fast-forward
 bin/plotcounts.py   |  70 ++++++++++++++++++++++++++++++++++++++
                           +++++++++++++++++++++++++++++++
 results/dracula.png | Bin 23291 -> 38757 bytes
 2 files changed, 70 insertions(+)
```

Merging doesn't change the source branch `fit`,
but once the merge is done,
all of the changes made in `fit` are also in the history of `master`:

```bash
$ git log --oneline -n 4
```

```text
1577404 (HEAD -> master, fit) Adding Moreno-Sanchez et al (2016)
        reference
38c209b Added fit to word count data
ddb00fb (origin/master) removing inverse rank calculation
7de9877 ignoring __pycache__
```

Note that Git automatically creates a new commit (in this case, `1577404`)
to represent the merge.
If we now run `git diff master..fit`,
Git doesn't print anything
because there aren't any differences to show.

Now that we have merged all of the changes from `fit` into `master`
there is no need to keep the `fit` branch,
so we can delete it:

```bash
$ git branch -d fit
```

```text
Deleted branch fit (was 1577404).
```

> **Not Just the Command Line**
>
> We have been creating, merging, and deleting branches on the command line,
> but we can do all of these things using [GitKraken][gitkraken],
> [the RStudio IDE][rstudio-ide],
> and other GUIs.
> The operations stay the same;
> all that changes is how we tell the computer what we want to do.

## Handling Conflicts {#git-advanced-conflict}

A \gref{conflict}{git_conflict} occurs\index{Git!conflict}\index{conflict!in Git}
when a line has been changed in different ways in two separate branches
or when a file has been deleted in one branch but edited in the other.
Merging `fit` into `master` went smoothly
because there were no conflicts between the two branches,
but if we are going to use branches,
we must learn how to merge conflicts.

To start,
use `nano` to add the project's title to
a new file called `README.md` in the `master` branch,
which we can the view:

```bash
$ cat README.md
```

```text
# Zipf's Law
```

```bash
$ git add README.md
$ git commit -m "Initial commit of README file"
```

```text
[master 232b564] Initial commit of README file
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

Now let's create a new development branch called `docs`
to work on improving the documentation for our code.
We will use `git checkout -b` to create a new branch and switch to it
in a single step:

```bash
$ git checkout -b docs
```

```text
Switched to a new branch 'docs'
```

```bash
$ git branch
```

```text
* docs
  master
```

On this new branch,
let's add some information to the README file:

```text
# Zipf's Law

These Zipf's Law scripts tally the occurrences of words in text
files and plot each word's rank versus its frequency.
```

```bash
$ git add README.md
$ git commit -m "Added repository overview"
```

```text
[docs a0b88e5] Added repository overview
 1 file changed, 3 insertions(+)
```

In order to create a conflict,
let's switch back to the `master` branch.
The changes we made in the `docs` branch are not present:

```bash
$ git checkout master
```

```text
Switched to branch 'master'
```

```bash
$ cat README.md
```

```text
# Zipf's Law
```

Let's add some information about the contributors to our work:

```text
# Zipf's Law

## Contributors

- Amira Khan <amira@zipf.org>
```

```
$ git add README.md
$ git commit -m "Added contributor list"
```

```text
[master 45a576b] Added contributor list
 1 file changed, 4 insertions(+)
```

We now have two branches,
`master` and `docs`,
in which we have changed `README.md` in different ways:

```bash
$ git diff docs..master
```

```diff
diff --git a/README.md b/README.md
index f40e895..71f67db 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,5 @@
 # Zipf's Law
 
-These Zipf's Law scripts tally the occurrences of words in text
-files and plot each word's rank versus its frequency.
+## Contributors
+
+- Amira Khan <amira@zipf.org>
```

When we try to merge `docs` into `master`,
Git doesn't know which of these changes to keep:

```bash
$ git merge docs master
```

```text
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

If we look in `README.md`,
we see that Git has kept both sets of changes,
but has marked which came from where:

```bash
$ cat README.md
```

```text
# Zipf's Law

<<<<<<< HEAD
## Contributors

- Amira Khan <amira@zipf.org>
=======
These Zipf's Law scripts tally the occurrences of words in text
files and plot each word's rank versus its frequency.
>>>>>>> docs
```

The lines from `<<<<<<< HEAD` to `=======` are what was in `master`,
while the lines from there to `>>>>>>> docs` show what was in `docs`.
If there were several conflicting regions in the same file,
Git would mark each one this way.

We have to decide what to do next:\index{Git!resolve conflict}\index{resolve conflict (in Git)}
keep the `master` changes,
keep those from `docs`,
edit this part of the file to combine them,
or write something new.
Whatever we do,
we must remove the `>>>`, `===`, and `<<<` markers.
Let's combine the two sets of changes
so the resulting file reads:

```text
# Zipf's Law

These Zipf's Law scripts tally the occurrences of words in text
files and plot each word's rank versus its frequency.

## Contributors

- Amira Khan <amira@zipf.org>
```

We can now add the file and commit the change,
just as we would after any other edit:

```bash
$ git add README.md
$ git commit -m "Merging README additions"
```

```text
[master 55c63d0] Merging README additions
```

Our branch's history now shows a single sequence of commits,
with the `master` changes on top of the earlier `docs` changes:

```bash
$ git log --oneline -n 4
```

```text
55c63d0 (HEAD -> master) Merging README additions
45a576b Added contributor list
a0b88e5 (docs) Added repository overview
232b564 Initial commit of README file
```

If we want to see what really happened,
we can add the `--graph` option to `git log`:

```bash
$ git log --oneline --graph -n 4
```

```text
*   55c63d0 (HEAD -> master) Merging README additions
|\  
| * a0b88e5 (docs) Added repository overview
* | 45a576b Added contributor list
|/  
* 232b564 Initial commit of README file
```

At this point we can delete the `docs` branch:

```bash
$ git branch -d docs
```

```text
Deleted branch docs (was a0b88e5).
```

Alternatively,
we can keep using `docs` for documentation updates.
Each time we switch to it,
we merge changes *from* `master` *into* `docs`,
do our editing
(while switching back to `master` or other branches as needed
to work on the code),
and then merge *from* `docs` *to* `master`
once the documentation is updated.

> **Remember to Push**
>
> If you are using a remote repository,
> don't forget to use `git push`
> to keep your version on GitHub up to date
> with your local version.


What is the best way to incorporate branching into our regular coding practice?
If we are working on our own computer,
this workflow will help us keep track of what we are doing:

1.  `git checkout master` to make sure we are in the `master` branch.

2.  `git checkout -b name-of-feature` to create a new branch.
    We *always* create a branch when making changes,
    since we never know what else might come up.
    The branch name should be as descriptive as a variable name or filename would be.

3.  Make our changes.
    If something occurs to us along the way---for example,
    if we are writing a new function and realize that
    the documentation for some other function should be updated---we do *not*
    do that work in this branch just because we happen to be there.
    Instead,
    we commit our changes,
    switch back to `master`,
    and create a new branch for the other work.

4.  When the new feature is complete,
    we `git merge master name-of-feature`
    to get any changes we merged into `master` after creating `name-of-feature`
    and resolve any conflicts.
    This is an important step:
    we want to do the merge and test that everything still works in our feature branch,
    not in `master`.

5.  Finally,
    we switch back to `master` and `git merge name-of-feature master`
    to merge our changes into `master`.
    We should not have any conflicts,
    and all of our tests should pass.

Most experienced developers use this
\gref{branch-per-feature workflow}{branch_per_feature_workflow},\index{branch-per-feature workflow (in Git)}\index{Git!branch-per-feature workflow}
but what exactly is a "feature"?
These rules make sense for small projects:

1.  Anything cosmetic that is only one or two lines long
    can be done in `master` and committed right away.
    Here,
    "cosmetic" means changes to comments or documentation:
    nothing that affects how code runs, not even a simple variable renaming.

2.  A pure addition that doesn't change anything else is a feature and goes into a branch.
    For example,
    if we run a new analysis and save the results,
    that should be done on its own branch
    because it might take several tries to get the analysis to run,
    and we might interrupt ourselves to fix things that we discover aren't working.

3.  Every change to code that someone might want to undo later in one step is a feature.
    For example,
    if a new parameter is added to a function,
    then every call to the function has to be updated.
    Since neither alteration makes sense without the other,
    those changes are considered a single feature and should be done in one branch.

The hardest thing about using a branch-per-feature workflow is sticking to it for small changes.
As the first point in the list above suggests,
most people are pragmatic about this on small projects;
on large ones,
where dozens of people might be committing,
even the smallest and most innocuous change needs to be in its own branch
so that it can be reviewed (which we discuss below).

FIXME: branches; merging; rebasing; pull requests


So far we have used Git to manage individual work,
but it really comes into its own when we are working with other people.
We can do this in two ways:

1.  Everyone has read and write access to a single shared repository.

2.  Everyone can read from the project's main repository,
    but only a few people can commit changes to it.
    The project's other contributors \gref{fork}{git_fork} the main repository\index{Git!fork a repository}\index{fork (in Git)}
    to create one that they own,
    do their work in that,
    and then submit their changes to the main repository.

The first approach works well for teams of up to half a dozen people
who are all comfortable using Git,
but if the project is larger,
or if contributors are worried that they might make a mess in the `master` branch,
the second approach is safer.

Git itself doesn't have any notion of a "main repository",
but \gref{forges}{forge} like [GitHub][github],
[GitLab][gitlab],
and [BitBucket][bitbucket] all encourage people
to use Git in ways that effectively create one.
Suppose,
for example,
that Sami wants to contribute to the Zipf's Law code that
Amira is hosting on GitHub at `https://github.com/amira-khan/zipf`.
Sami can go to that URL and click on the "Fork" button in the upper right corner
(Figure \@ref(fig:git-advanced-fork-button)).
GitHub immediately creates a copy of Amira's repository within Sami's account on GitHub's own servers.

```{r git-advanced-fork-button, echo=FALSE, fig.cap="Forking a repository."}
knitr::include_graphics("figures/git-advanced/fork-button.png")
```

When the command completes,
the setup on GitHub now looks like Figure \@ref(fig:git-advanced-after-fork).
Nothing has happened yet on Sami's own machine:
the new repository exists only on GitHub.
When Sami explores its history,
they see that it contains all of the changes Amira made.

```{r git-advanced-after-fork, echo=FALSE, fig.cap="Repositories on GitHub after forking."}
knitr::include_graphics("figures/git-advanced/after-fork.png")
```

A copy of a repository is called a \gref{clone}{git_clone}.\index{Git!clone a repository}\index{clone (in Git)}
In order to start working on the project,
Sami needs a clone of *their* repository (not Amira's) on their own computer.
We will modify Sami's prompt to include their desktop user ID (`sami`)
and working directory (initially `~`)
to make it easier to follow what's happening:\index{Git commands!clone}

```bash
sami:~ $ git clone https://github.com/sami-virtanen/zipf.git
```

```text
Cloning into 'zipf'...
remote: Enumerating objects: 64, done.
remote: Counting objects: 100% (64/64), done.
remote: Compressing objects: 100% (43/43), done.
remote: Total 64 (delta 20), reused 63 (delta 19), pack-reused 0
Receiving objects: 100% (64/64), 2.20 MiB | 2.66 MiB/s, done.
Resolving deltas: 100% (20/20), done.
```

This command creates a new directory with the same name as the project,
i.e., `zipf`.
When Sami goes into this directory and runs `ls` and `git log`,
they see that all of the project's files and history are there:

```bash
sami:~ $ cd zipf
sami:~/zipf $ ls
```

```text
README.md       bin             data             results
```

```bash
sami:~/zipf $ git log --oneline -n 4
```

```text
55c63d0 (HEAD -> master, origin/master, origin/HEAD) 
        Merging README additions
45a576b Added contributor list
a0b88e5 Added repository overview
232b564 Initial commit of README file
```

Sami also sees that Git has automatically created a \gref{remote}{git_remote} for their repository\index{Git!remote}\index{remote (in Git)}
that points back at their repository on GitHub:

```bash
sami:~/zipf $ git remote -v
```

```text
origin  https://github.com/sami-virtanen/zipf.git (fetch)
origin  https://github.com/sami-virtanen/zipf.git (push)
```

Sami can pull changes from their fork and push work back there,
but needs to do one more thing before getting the changes from Amira's repository:

```bash
sami:~/zipf $ git remote add upstream
              https://github.com/amira-khan/zipf.git
sami:~/zipf $ git remote -v
```

```text
origin      https://github.com/sami-virtanen/zipf.git (fetch)
origin      https://github.com/sami-virtanen/zipf.git (push)
upstream    https://github.com/amira-khan/zipf.git (fetch)
upstream    https://github.com/amira-khan/zipf.git (push)
```

Sami has called their new remote `upstream` because it points at the repository
theirs is derived from.\index{Git!upstream repository}\index{upstream repository (in Git)}
They could use any name,
but `upstream` is a nearly universal convention.

With this remote in place,
Sami is finally set up.
Suppose,
for example,
that Amira has modified the project's `README.md` file to add Sami as a contributor.
(Again, we show Amira's user ID and working directory in her prompt to make it clear who's doing what):

```text
# Zipf's Law

These Zipf's Law scripts tally the occurrences of words in text
files and plot each word's rank versus its frequency.

## Contributors

- Amira Khan <amira@zipf.org>
- Sami Virtanen
```

Amira commits her changes and pushes them to *her* repository on GitHub:

```bash
amira:~/zipf $ git commit -a -m "Adding Sami as a contributor"
```

```text
[master 35fca86] Adding Sami as a contributor
 1 file changed, 1 insertion(+)
```

```bash
amira:~/zipf $ git push origin master
```

```text
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 315 bytes | 315.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/amira-khan/zipf.git
   55c63d0..35fca86  master -> master
```

Amira's changes are now on her desktop and in her GitHub repository
but not in either of Sami's repositories (local or remote).
Since Sami has created a remote that points at Amira's GitHub repository,
though,
they can easily pull those changes to their desktop:

```bash
sami:~/zipf $ git pull upstream master
```

```text
From https://github.com/amira-khan/zipf
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 55c63d0..35fca86
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
```

Pulling from a repository owned by someone else
is no different than pulling from a repository we own.
In either case,
Git merges the changes and asks us to resolve any conflicts that arise.
The only significant difference is that,
as with `git push` and `git pull`,
we have to specify both a remote and a branch:
in this case,
`upstream` and `master`.

## Pull Requests {#git-advanced-pull-requests}

Sami can now get Amira's work,
but how can Amira get Sami's?
She could create a remote that pointed at Sami's repository on GitHub
and periodically pull in Sami's changes,
but that would lead to chaos,
since we could never be sure that everyone's work was in any one place at the same time.
Instead,
almost everyone uses \gref{pull requests}{pull_request}.\index{pull request (in Git)}\index{Git!pull request}
They aren't part of Git itself,
but are supported by all major online \gref{forges}{forge}.

A pull request is essentially a note saying,
"Someone would like to merge branch A of repository B into branch X of repository Y".
The pull request does not contain the changes,
but instead points at two particular branches.
That way,
the difference displayed is always up to date
if either branch changes.

But a pull request can store more than just the source and destination branches:
it can also store comments people have made about the proposed merge.
Users can comment on the pull request as a whole,
or on particular lines,
and mark comments as out of date
if the author of the pull request updates the code that the comment is attached to.
Complex changes can go through several rounds of review and revision
before being merged,
which makes pull requests the review system we all wish journals actually had.

To see this in action,
suppose Sami wants to add their email address to `README.md`.
They create a new branch and switch to it:

```bash
sami:~/zipf $ git checkout -b adding-email
```

```text
Switched to a new branch 'adding-email'
```

then make a change and commit it:

```bash
sami:~/zipf $ git commit -a -m "Adding my email address"
```

```text
[adding-email 3e73dc0] Adding my email address
 1 file changed, 1 insertion(+), 1 deletion(-)
```

```bash
sami:~/zipf $ git diff HEAD~1
```

```diff
diff --git a/README.md b/README.md
index e8281ee..e1bf630 100644
--- a/README.md
+++ b/README.md
@@ -6,4 +6,4 @@ and plot each word's rank versus its frequency.
 ## Contributors
 
 - Amira Khan <amira@zipf.org>
-- Sami Virtanen
+- Sami Virtanen <sami@zipf.org>
```

Sami's changes are only in their local repository.
They cannot create a pull request until those changes are on GitHub,
so they push their new branch to their repository on GitHub:

```bash
sami:~/zipf $ git push origin adding-email
```

```text
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 315 bytes | 315.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'adding-email' on GitHub by visiting:
remote:   https://github.com/sami-virtanen/zipf/pull/new/adding-email
remote: 
To https://github.com/sami-virtanen/zipf.git
 * [new branch]      adding-email -> adding-email
```

When Sami goes to their GitHub repository in the browser,
GitHub notices that they have just pushed a new branch
and asks them if they want to create a pull request
(Figure \@ref(fig:git-advanced-after-sami-pushes)).

```{r git-advanced-after-sami-pushes, echo=FALSE, fig.cap="Repository state after Sami pushes."}
knitr::include_graphics("figures/git-advanced/after-sami-pushes.png")
```

When Sami clicks on the button,
GitHub displays a page showing the default source and destination of the pull request
and a pair of editable boxes for the pull request's title and a longer comment
(Figure \@ref(fig:git-advanced-pull-request-start)).

```{r git-advanced-pull-request-start, echo=FALSE, fig.cap="Starting a pull request."}
knitr::include_graphics("figures/git-advanced/open-pull-request.png")
```

If they scroll down,
Sami can see a summary of the changes that will be in the pull request
(Figure \@ref(fig:git-advanced-pull-request-summary)).

```{r git-advanced-pull-request-summary, echo=FALSE, fig.cap="Summary of a pull request."}
knitr::include_graphics("figures/git-advanced/open-pull-request-detail.png")
```

The top (title) box is autofilled with the previous commit message,
so Sami adds an extended explanation to provide additional context
before clicking on "Create Pull Request"
(Figure \@ref(fig:git-advanced-pull-request-fill-in)).
When they do,
GitHub displays a page showing the new pull request,
which has a unique serial number
(Figure \@ref(fig:git-advanced-pull-request-new)).
Note that this pull request is displayed in Amira's repository rather than Sami's
since it is Amira's repository that will be affected if the pull request is merged.

```{r git-advanced-pull-request-fill-in, echo=FALSE, fig.cap="Filling in a pull request."}
knitr::include_graphics("figures/git-advanced/fill-in-pull-request.png")
```

```{r git-advanced-pull-request-new, echo=FALSE, fig.cap="Creating a new pull request."}
knitr::include_graphics("figures/git-advanced/new-pull-request.png")
```

Amira's repository now shows a new pull request
(Figure \@ref(fig:git-advanced-pull-request-viewing)).
Clicking on the "Pull requests" tab brings up a list of PRs
(Figure \@ref(fig:git-advanced-pull-request-list))
and clicking on the pull request link itself displays its details
(Figure \@ref(fig:git-advanced-pull-request-details)).
Sami and Amira can both see and interact with these pages,
though only Amira has permission to merge.

```{r git-advanced-pull-request-viewing, echo=FALSE, fig.cap="Viewing a pull request."}
knitr::include_graphics("figures/git-advanced/viewing-new-pull-request.png")
```

```{r git-advanced-pull-request-list, echo=FALSE, fig.cap="Listing pull requests."}
knitr::include_graphics("figures/git-advanced/pr-list.png")
```

```{r git-advanced-pull-request-details, echo=FALSE, fig.cap="Details of pull requests."}
knitr::include_graphics("figures/git-advanced/pr-details.png")
```

Since there are no conflicts,
GitHub will let Amira merge the PR immediately using the "Merge pull request" button.
She could also discard or reject it without merging using the "Close pull request" button.
Instead,
she clicks on the "Files changed" tab to see what Sami has changed
(Figure \@ref(fig:git-advanced-pull-request-changes)).

```{r git-advanced-pull-request-changes, echo=FALSE, fig.cap="Viewing changes to files."}
knitr::include_graphics("figures/git-advanced/pr-changes.png")
```

If she moves her mouse over particular lines,\index{Git!pull request!reviewing}\index{reviewing (Git pull request)}\index{code review!pull request}
a white-on-blue cross appears near the numbers to indicate that she can add comments
(Figure \@ref(fig:git-advanced-pull-request-comment-marker)).
She clicks on the marker beside her own name and writes a comment:
She only wants to make one comment rather than write a lengthier multi-comment review,
so she chooses "Add single comment"
(Figure \@ref(fig:git-advanced-pull-request-write-comment)).
GitHub redisplays the page with her remarks inserted
(Figure \@ref(fig:git-advanced-pull-request-pr-with-comment)).

```{r git-advanced-pull-request-comment-marker, echo=FALSE, fig.cap="A GitHub comment marker."}
knitr::include_graphics("figures/git-advanced/pr-comment-marker.png")
```

```{r git-advanced-pull-request-write-comment, echo=FALSE, fig.cap="Writing a comment on a pull request."}
knitr::include_graphics("figures/git-advanced/pr-writing-comment.png")
```

```{r git-advanced-pull-request-pr-with-comment, echo=FALSE, fig.cap="Viewing a comment on a pull request."}
knitr::include_graphics("figures/git-advanced/pr-with-comment.png")
```

While Amira is working,
GitHub has been emailing notifications to both Sami and Amira.
When Sami clicks on the link in their email notification,
it takes them to the PR and shows Amira's comment.
Sami changes `README.md`,
commits,
and pushes,
but does *not* create a new pull request or do anything to the existing one.\index{Git!pull request!updating}
As explained above,
a PR is a note asking that two branches be merged,
so if either end of the merge changes,
the PR updates automatically.

Sure enough,
when Amira looks at the PR again a few moments later she sees Sami's changes
(Figure \@ref(fig:git-advanced-pull-request-pr-with-fix)).
Satisfied,
she goes back to the "Conversation" tab and clicks on "Merge".
The icon at the top of the PR's page changes text and color to show that the merge was successful
(Figure \@ref(fig:git-advanced-pull-request-successful-merge)).

```{r git-advanced-pull-request-pr-with-fix, echo=FALSE, fig.cap="A pull request with a fix."}
knitr::include_graphics("figures/git-advanced/pr-with-fix.png")
```

```{r git-advanced-pull-request-successful-merge, echo=FALSE, fig.cap="After a successful merge."}
knitr::include_graphics("figures/git-advanced/pr-successful-merge.png")
```

To get those changes from GitHub to her desktop repository,
Amira uses `git pull`:

```bash
amira:~/zipf $ git pull origin master
```

```text
From https://github.com/amira-khan/zipf
 * branch            master     -> FETCH_HEAD
Updating 35fca86..a04e3b9
Fast-forward
 README.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

To get the change they just made from their `adding-email` branch into their `master` branch,
Sami could use `git merge` on the command line.
It's a little clearer,
though,
if they also use `git pull` from their `upstream` repository (i.e., Amira's repository)
so that they're sure to get any other changes that Amira may have merged:

```bash
sami:~/zipf $ git checkout master
```

```text
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
```

```bash
sami:~/zipf $ git pull upstream master
```

```text
From https://github.com/amira-khan/zipf
 * branch            master     -> FETCH_HEAD
Updating 35fca86..a04e3b9
Fast-forward
 README.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

Finally,
Sami can push their changes back to the `master` branch
in their own remote repository:

```bash
sami:~/zipf $ git push origin master
```

```text
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/sami-virtanen/zipf.git
   35fca86..a04e3b9  master -> master
```

All four repositories are now synchronized.

## Handling Conflicts in Pull Requests {#git-advanced-pr-conflict}

Finally,
suppose that Amira and Sami have decided to collaborate more extensively on this project.
Amira has added Sami as a collaborator to the GitHub repository.
Now Sami can make contributions directly to the repository,
rather than via a pull request from a forked repository.

Sami makes a change to `README.md` in the `master` branch on GitHub.
Meanwhile, Amira is making a conflicting change to the same file in a different branch.\index{Git!pull request!conflict}
When Amira creates her pull request,
GitHub will detect the conflict and report that the PR cannot be merged automatically
(Figure \@ref(fig:git-advanced-pr-conflict)).

```{r git-advanced-pr-conflict, echo=FALSE, fig.cap="Showing a conflict in a pull request."}
knitr::include_graphics("figures/git-advanced/pr-conflict.png")
```

Amira can solve this problem with the tools she already has.
If she has made her changes in a branch called `editing-readme`,
the steps are:

1.  Pull Sami's on the `master` branch of the GitHub repository
    into the `master` branch of her desktop repository.

2.  Merge *from* the `master` branch of her desktop repository
    *to* the `editing-readme` branch in the same repository.

3.  Push her updated `editing-readme` branch to her repository on GitHub.
    The pull request from there back to the `master` branch of the main repository
    will update automatically.

GitHub and other forges do allow people to merge conflicts
through their browser-based interfaces,
but doing it on our desktop means we can use our favorite editor to resolve the conflict.
It also means that if the change affects the project's code,
we can run everything to make sure it still works.

But what if Sami or someone else merges another change
while Amira is resolving this one,
so that by the time she pushes to her repository
there is another, different, conflict?
In theory this cycle could go on forever;
in practice,
it reveals a communication problem that Amira (or someone) needs to address.
If two or more people are constantly making incompatible changes to the same files,
they should discuss who's supposed to be doing what,
or rearrange the project's contents so that they aren't stepping on each other's toes.

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
