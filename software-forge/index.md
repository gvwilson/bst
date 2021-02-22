---
---

<chap key="version-control"></chap> described how to use version control to
manage individual work, but it really comes into its own when we are working
with other people. Software forges like [GitHub][github], [GitLab][gitlab], and
[BitBucket][bitbucket] are all designed to support this, and they all provide
other tools for managing and reviewing shared information. This chapter will
look at how to use them to prepare the ground for <chap key="process"></chap>'s
discussion of software development processes.

## Using Git together

People can share work through a Git repository in one of two ways:

1.  Everyone has read and write access to a single shared repository.

2.  Everyone can read from the project's main repository, but only a few people
    can commit changes to it.  The project's other contributors <span
    g="git-fork">fork</span> the main repository to create one that they own, do
    their work in that, and then submit their changes to the main repository.

The first approach works well for teams of up to half a dozen people who are all
comfortable using Git, but if the project is larger, or if contributors are
worried that they might make a mess in the `main` branch, the second approach is
safer.

Git itself doesn't have any notion of a "main repository", but [GitHub][github]
and other software forges all encourage people to use Git as if there was one.
Suppose, for example, that Marian wants to contribute to the assignment that
Peggy is hosting on GitHub at `https://github.com/peggy/zipf`.  Marian can go to
that URL and click on the "Fork" button in the upper right corner.  GitHub
immediately creates a copy of Peggy's repository within Marian's account on
GitHub's own servers.

When the command completes, nothing has happened yet on Marian's own machine:
the new repository exists only on GitHub.  When Marian explores its history, she
sees that it contains all of the changes Peggy made.

A copy of a repository is a clone just like the ones you have created earlier;
it's just hosted on the forge's servers instead of your laptop.  In order to
start working on the project, Marian needs a clone of *their* repository (not
Peggy's) on their own computer.  We will modify Marian's prompt to include their
desktop user ID (`marian`) and working directory (initially `~`) to make it
easier to follow what's happening:

```
marian:~ $ git clone https://github.com/marian/homework5.git
```

This command creates a new directory with the same name as the project, i.e.,
`homework5`.  When Marian goes into this directory and runs `ls` and `git log`,
she sees all of the project's files and history:

```
marian:~ $ cd bst
marian:~/bst $ ls
```

```
marian:~/bst $ git log --oneline -n 4
```

Marian also sees that Git has automatically created a remote for their
repository that points back at their repository on GitHub:

```
marian:~/bst $ git remote -v
```

```
origin  https://github.com/marian/bst.git (fetch)
origin  https://github.com/marian/bst.git (push)
```

Marian can pull changes from their fork and push work back there, but needs to
do one more thing before getting the changes from Peggy's repository:

```
marian:~/bst $ git remote add upstream https://github.com/peggy/bst.git
marian:~/bst $ git remote -v
```
```
origin      https://github.com/marian/bst.git (fetch)
origin      https://github.com/marian/bst.git (push)
upstream    https://github.com/peggy/bst.git (fetch)
upstream    https://github.com/peggy/bst.git (push)
```

Marian has called their new remote `upstream` because it points at the
repository theirs is derived from.  She could use any name, but `upstream` is a
nearly universal convention.

With this remote in place, Marian is finally set up.  Suppose, for example, that
Peggy has modified the project's `README.md` file to add Marian as a
contributor.  (Again, we show Peggy's user ID and working directory in her
prompt to make it clear who's doing what):

```
# BST

Our homework project

## Contributors

- Peggy
- Marian
```

Peggy commits her changes and pushes them to *her* repository on GitHub:

```
peggy:~/bst $ git commit -a -m "Adding Marian as a contributor"
peggy:~/bst $ git push origin main
```

Peggy's changes are now on her desktop and in her GitHub repository but not in
either of Marian's repositories (local or remote).  Since Marian has created a
remote that points at Peggy's GitHub repository, though, she can easily pull
those changes to their desktop:

```
marian:~/bst $ git pull upstream main
```

Pulling from a repository owned by someone else is no different than pulling
from a repository we own.  In either case, Git merges the changes and asks us to
resolve any conflicts that arise.  The only significant difference is that, as
with `git push` and `git pull`, we have to specify both a remote and a branch:
in this case, `upstream` and `main`.

Marian can now get Peggy's work, but how can Peggy get Marian's?  She could
create a remote that pointed at Marian's repository on GitHub and periodically
pull in Marian's changes, but that would lead to chaos, since we could never be
sure that everyone's work was in any one place at the same time.  Instead,
almost everyone uses <span g="pull-request">pull requests</span>.  A pull
request is essentially a note saying, "Someone would like to merge branch A of
repository B into branch X of repository Y".  The pull request does not contain
the changes, but instead points at two particular branches.  That way, the
difference displayed is always up to date if either branch changes.

But a pull request can store more than just the source and destination branches:
it can also store comments people have made about the proposed merge.  Users can
comment on the pull request as a whole, or on particular lines, and mark
comments as out of date if the author of the pull request updates the code that
the comment is attached to.  Complex changes can go through several rounds of
review and revision before being merged, which makes pull requests the review
system we all wish journals actually had.

To see this in action, suppose Marian wants to add their email address to
`README.md`.  She creates a new branch and switch to it:

```
marian:~/bst $ git checkout -b adding-email
```

{: .continue}
then makes a change and commit it:

```
marian:~/bst $ git commit -a -m "Adding my email address"
```

```
marian:~/bst $ git diff HEAD~1
```

Marian's changes are only in her local repository.  She cannot create a pull
request until those changes are on GitHub, so she pushes her new branch to her
repository on GitHub:

```
marian:~/bst $ git push origin adding-email
```

When Marian goes to her GitHub repository in the browser, GitHub notices that
she has just pushed a new branch and asks her if she wants to create a pull
request.  When Marian clicks on the button, GitHub displays a page showing the
default source and destination of the pull request and a pair of editable boxes
for the pull request's title and a longer comment.

If she scrolls down, Marian can see a summary of the changes that will be in the
pull request.  Whe she clicks "Create Pull Request", Git gives it a unique
serial number.  This pull request is displayed in Peggy's repository rather than
Marian's since it is Peggy's repository that will be affected if the pull
request is merged.

Clicking on the "Pull requests" tab in Peggy's repository brings up a list of
PRs and clicking on the pull request link itself displays its details.  Marian
and Peggy can both see and interact with these pages, though only Peggy has
permission to merge.

Since there are no conflicts, GitHub will let Peggy merge the PR immediately
using the "Merge pull request" button.  She could also discard or reject it
without merging using the "Close pull request" button.  Instead, she clicks on
the "Files changed" tab to see what Marian has changed.

If Marian changes `README.md`, commits, and pushes to her branch while the pull
request is open, the pull request is immediately updated.  As explained above, a
PR is a note asking that two branches be merged, so if either end of the merge
changes, the PR updates automatically.

If Peggy has merged several pull requests, Marian can update her desktop
repository by pulling from her `upstream` repository (i.e., Peggy's repository):

```
marian:~/bst $ git checkout main
marian:~/bst $ git pull upstream main
```

Finally, Marian can their those changes back to the `main` branch in her own
repository on GitHub:

```
marian:~/bst $ git push origin main
```

All four repositories are now synchronized. If there are any conflicts along the
way, Peggy and Marian can resolve them just as they would resolve conflicts
between branches in a single repository.  GitHub and other forges do allow
people to merge conflicts through their browser-based interfaces, but doing it
on our desktop means we can use our favorite editor to resolve the conflict.  It
also means that if the change affects the project's code, we can run everything
to make sure it still works.

But what if Marian or someone else merges another change while Peggy is
resolving this one, so that by the time she pushes to her repository there is
another, different, conflict?  In theory this cycle could go on forever; in
practice, it reveals a communication problem that Peggy (or someone) needs to
address.  If two or more people are constantly making incompatible changes to
the same files, they should discuss who's supposed to be doing what, or
rearrange the project's contents so that they aren't stepping on each other's
toes.

## Code reviews

There's no point creating pull requests if they are all merged as-is. The reason
they exist is to allow <span g="code-review">code review</span>.  One study
after another since the mid-1970s has proven that code review is the most
cost-effective way to find bugs in software <cite>Cohen2010</cite>. It is also
the most effective way to share knowledge between team members: if you read
someone else's code, you have a chance to learn all the things that you didn't
know to ask and they didn't realize they should tell you.

There are lots of guides online for doing code reviews, most of them based on
their authors' personal experience. A notable exception is the [SmartBear
guide][smartbear-code-review], which draws on a large study of code review in
industry. The rules below present some of their findings with modifications for
students' situations.

Have the instructor do a demonstration review.
:   Even if you have done code reviews before, you may not know what's expected
    for this class. The instructor can show you by putting up some sample code
    and going through it, thinking aloud as they notice things worth commenting
    on so that you have an idea of how much detail they expected.

Review at most 200 lines of a code at a time.
:   The [SmartBear guide][smartbear-code-review] recommends reviewing at most
    400 lines at a time, which should take 60-90 minutes. You will probably get
    there eventually, but in our experience it's better to start with something
    smaller and work up to that.

    A corollary of this rule is that no pull request should be more than 200
    lines long. If one is, the odds are that reviewers won't be able to hold it
    all in their head at once (<chap key="thinking-learning"></chap>) and so
    will miss things.

Authors should clean up code before review.
:   If the person creating the pull request goes through and adds some more
    comments, cleans up some variable names, and does a bit of refactoring
    (<chap key="design"></chap>), they won't just make reviewing easier: the
    odds are very good that they will find and fix a few problems on their own.

Use checklists.
:   <cite>Gawande2011</cite> popularized the idea that using checklists improves
    results even for experts.  If you are new to code reviews, ask the
    instructor for a list of the dozen most common problems to check for.
    (Anything more than that is likely to be overhwelming.) If you and your
    teammates have been working together for a while, look at your own code
    reviews and make a list of the things that keep coming up.  Having the list
    will make you more aware of the issues while you're coding, which in turn
    will make you less likely to keep making the same mistakes.

Follow up.
:   The author of the code doesn't have to accept every suggestion, but should
    have a better reason than "I don't want to" for rejecting any of them.
    GitHub and other platforms allow people to create discussion threads for
    each comment, and will mark threads as being out of date when the pull
    request is updated. Whoever did the review should then scan the changes to
    make sure their points have been addressed, and to give themselves a chance
    to learn a few more things from the author.

Don't tolerate rudeness.
    Most code review guidelines say, "Be respectful."  The problem is that if
    you are, you probably don't need to be told that, and if you're not, a
    written rule probably isn't going to change your behavior. What *will*
    change behavior is teammates defending the victims of rudeness by telling
    the offender, "That's not how we speak to each other."
    <cite>Dobbin2019</cite> (summarized in <cite>Dobbin2020</cite>) found that
    training people how to be good <span g="ally">allies</span> was more
    effective at reducing abuse than most of the other things companies do;
    we'll explore this more in <chap key="legalities"></chap>.

So what does a code review actually look like? Here's a short Python program
that searches for duplicated files (i.e., ones that have exactly the same
content). The listing below shows the comments I left when reviewing it.

{% include code file="dup.py" %}

| Line(s) | Comment |
| ------- | ------- |
| 02      | Add a <span g="docstring">docstring</g> describing the program. |
| 03      | Put imports in alphabetical order. |
| 07      | Use a set instead of a list for faster lookup. |
| …       | One entry per line will be easier to read. |
| 09      | `SENSES` isn't used anywhere: delete. |
| 12      | Add a docstring describing this function. |
| 12-22   | Use `argparse` to handle options. |
| 12-22   | Put option handling in its own function. |
| 17      | Print error message to `sys.stderr`. |
| 33      | Add a docstring describing this function. |
| 34-39   | Use `any` instead of a loop to check this. |
| 41      | <span g="magic-number">Magic number</span> 10. |
| 41      | Provide option to control progress reporting. |
| 47      | Use `'rb'` to read files as binary. |
| 57      | Add a docstring describing this function. |
| 60      | Why `paths.pop()`? |

## Tracking issues

You probably have a to-do list somewhere. It might be scribbled in a calendar or
lab notebook, kept in a text file on your laptop, or in your head; wherever and
however you maintain it, it lists the things you're supposed to do, when they're
due, and (possibly) how urgent they are.

At its simplest, an <span g="issue-tracker">issue tracker</span> is a shared
to-do list. Ticketing systems are also called ticketing systems and bug
trackers, because most software projects use one to keep track of the bugs that
developers and users find. These days, issue trackers are almost invariably
web-based. To create a new ticket, you enter a title and a short description;
the system then assigns it a unique serial number. You can usually also specify:

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
