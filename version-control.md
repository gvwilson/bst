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
has now largely been replaced by Subversion, which fixes many of CVS's flaws
(while introducing a few minor ones of its own). Alternatively, if you have
money to spend, there's Perforce, which is my personal favorite.

These three, and most others, all have the same general architecture.  The
master copy of the project resides in a *repository*, which is located on a
server. No one ever edits the repository files directly; instead, each member of
the team keeps a *working copy* on her machine. When she wants to share her work
with her teammates, she *commits* her files, which copies any changes she has
made to the repository. She can also *update* her working copy, which copies
changes other people have committed to the repository into her working copy.

What happens when two or more people change the same file at the same time? One
or the other will commit first; her changes will go into the repository. When
the second person tries to commit, though, the version control system notices
the *conflict*, and gives him three options:

1.  Throw away his work.

2.  Throw away what his teammate has done.

3.  Merge the changes, i.e., go through the conflicts and decide what to keep or
    rewrite.

Version control means never having to say you're sorry: since the repository
keeps a record of all the changes ever checked in, any developer who wants to
can *revert* to earlier versions of files.

Using a version control system is one of the things that distinguishes
professional programmers from amateurs. Yes, you can share files by mailing them
back and forth, or copying them from one laptop to another over wireless or with
a USB stick. But why would you? A version control system will do all the hard
work for you, and get it right every time.

The only drawback of version control systems is that they work best with plain
text files---most of them don't really know what to do with binary files, such
as sound clips, images, or Microsoft Word documents. When changes have been made
to a Java source file, for example, Subversion can find and display the lines
that have been edited. When you and your teammates all edit the Word version of
your final report during the same boring lecture, on the other hand, all
Subversion can do is tell you that the files have been changed---it can't find
and highlight the changes for you. This isn't really its fault: there are
hundreds of different binary file formats, and most don't come with tools for
diffing (i.e., finding differences) or merging. Still, programmers' heavy use of
version control is one of the things that keeps them in the ASCII dark ages.

{% include links.md %}
