---
---

## Including Everyone

FIXME: allyship from a legal and moral standpoint

## Licensing

A license dictates how project materials can be used and redistributed.  If the
license or a publication agreement makes it difficult for people to contribute,
the project is less likely to attract new members, so the choice of license is
crucial to the project's long-term sustainability.

<div class="callout" markdown="1">

### Open except...

Projects that are only developing software may not have any problem making
everything open.  Teams working with sensitive data, on the other hand, must >
be careful to ensure that what should be private isn't inadvertently shared.  >
In particular, people who are new to Git (and even people who aren't) >
occasionally add raw data files containing personal identifying information to >
repositories.  It's possible to rewrite the project's history to remove things >
when this happens, but that doesn't automatically erase copies people may have >
in forked repositories.

</div>

Every creative work has some sort of license; the only question is whether
authors and users know what it is and choose to enforce it.  Choosing a license
for a project can be complex, not least because the law hasn't kept up with
everyday practice.  FIXME lightweight intro while <cite>Lindberg2008</cite> is a
deeper dive for those who want details.  Depending on country, institution, and
job role, most creative works are automatically eligible for intellectual
property protection.  However, members of the team may have different levels of
copyright protection.  For example, students and faculty may have a copyright on
the research work they produce, but university staff members may not, since
their employment agreement may state that what they create on the job belongs to
their employer.

To avoid legal messiness, every project should include an explicit license.
This license should be chosen early, since changing a license can be
complicated.  For example, each collaborator may hold copyright on their work
and therefore need to be asked for approval when a license is changed.
Similarly, changing a license does not change it retroactively, so different
users may wind up operating under different licensing structures.

<div class="callout" markdown="1">

### Leave it to the professionals

Don't write your own license.  Legalese is a highly technical language, and
words don't mean what you think they do.

</div>

To make license selection for code as easy as possible, GitHub allows us to
select one of several common software licenses when creating a repository.  The
Open Source Initiative maintains [a list][osi-license-list] of <span
g="open-license">open licenses</span>, and [choosealicense.com][choose-license]
will help us find a license that suits our needs.  Some of the things we need to
think about are:

1.  Do we want to license the work at all?

1.  Is the content we are licensing source code?

1.  Do we require people distributing derivative works to also distribute their code?

1.  Do we want to address patent rights?

1.  Is our license compatible with the licenses of the software we depend on?

1.  Do our institutions have any policies that may overrule our choices?

1.  Are there any copyright experts within our institution who can assist us?

Unfortunately, GitHub's list does not include common licenses for data or
written works like papers and reports.  Those can be added in manually, but it's
often hard to understand the interactions between multiple licenses on different
kinds of material <cite>Almeida2017</cite>.

Just as the project's Code of Conduct is usually placed in a root-level file
called `CONDUCT.md`, its license is usually put in a file called `LICENSE.md`
that is also in the project's root directory.

### Software

In order to choose the right license for our software, we need to understand the
difference between two kinds of license.  The <span g="mit-license">MIT
License</span> and its close sibling the <span g="bsd-license">BSD
License</span> say that people can do whatever they want to with the software as
long as they cite the original source, and that the authors accept no
responsibility if things go wrong.  The <span g="gpl">GNU Public License</span>
(GPL) gives people similar rights, but requires them to share their own work on
the same terms:

> You may copy, distribute and modify the software as long as you track
> changes/dates in source files.  Any modifications to or software including
> (via compiler) GPL-licensed code must also be made available under the GPL
> along with build and install instructions.
>
> --- [tl;dr][tldr-gpl]

In other words, if someone modifies GPL-licensed software or incorporates it
into their own project, and then distributes what they have created, they have
to distribute the source code for their own work as well.

The GPL was created to prevent companies from taking advantage of open software
without contributing anything back.  The last thirty years have shown that this
restriction isn't necessary: many projects have survived and thrived without
this safeguard.  We therefore recommend that projects choose the MIT license, as
it places the fewest restrictions on future action.

<div class="callout" markdown="1">

### First, do no harm

The <span g="hippocratic-license">Hippocratic License</span> is a newer license
that is quickly becoming popular.  Where the GPL requires people to > share
their work, the Hippocratic License requires them to do no harm.  More >
precisely, it forbids people from using the software in ways that violate the >
[Universal Declaration of Human Rights][udhr].  We have learned the hard way >
that software and science can be mis-used; adopting the Hippocratic License is >
a small step toward preventing this.

</div>

### Data and reports

The MIT license, the GPL, and the Hippocratic License are intended for use with
software.  When it comes to data and reports, the most widely used family of
licenses are those produced by [Creative Commons][creative-commons].  These have
been written and checked by lawyers and are well understood by the community.

The most liberal option is referred to as <span g="cc0">CC0</span> where the "0"
stands for "zero restrictions".  This puts work in the public domain, i.e.,
allows anyone who wants to use it to do so however they want with no
restrictions.  CC-0 is usually the best choice for data, since it simplifies
aggregate analysis involving datasets from different sources.  It does not
negate the scholarly tradition and requirement of citing sources; it just
doesn't make it a legal requirement.

The next step up from CC-0 is the Creative Commons--Attribution license, usually
referred to as <span g="cc-by">CC-BY</span>. This allows people to do whatever
they want to with the work as long as they cite the original source.  This is
the best license to use for manuscripts: we want people to share them widely but
also want to get credit for our work.

Other Creative Commons licenses incorporate various restrictions, and are
usually referred two using the two-letter abbreviations listed below:

- ND (no derivative works) prevents people from creating modified versions of
    our work.  Unfortunately, this also inhibits translation and reformatting.

- SA (share-alike) requires people to share work that incorporates ours on the
    same terms that we used.  Again, it is fine in principle but in practice
    makes aggregation and recombination difficult.

- NC (no commercial use) does *not* mean that people cannot charge money for
    something that includes our work, though some publishers still try to imply
    that in order to scare people away from open licensing.  Instead, the NC
    clause means that people cannot charge for something that uses our work
    without our explicit permission, which we can give under whatever terms we
    want.

## Intellectual Property

FIXME: who owns what a student produces and why?

## Employment

FIXME: what rights do you have (or what myths can we dispel)?

## Ten Simple Rules for Being Fired

These rules are based on [my experience with DataCamp][thirdbit-datacamp] and on
the experiences of friends and colleagues there and at other companies.

1. Insist on a record of all conversations.
:   The biggest mistake you can make is to assume good faith on the part of
    those who fired you.  In most jurisdictions you have a right to record any
    phone calls you are part of, and if that feels too confrontational, insist
    on communicating by email.  If they insist on communicating by phone or
    video call, follow up immediately with an email summary and make sure you
    send a copy to your personal account.

2. Pause before speaking, posting, or tweeting.
:   If possible, have someone you trust look everything over before you say it
    or send it.  (Don't use someone who still works for the company, even if
    they are your closest friend: it puts them in a legally and morally
    difficult position.)

3. Keep your public statements brief.
:   People may care, but most won't care as much as you do.  A simple recitation
    of facts is usually damning enough.

4. If you want to correct something online, add a timestamped amendment.
:   Don't just take it down or edit it: if you do, you will be accused of
    rewriting history, and muddied waters only help whoever fired you.  Also, be
    prepared for them to dig through everything you've ever said online and
    re-post parts selectively to discredit you.

5. Speak directly to all the issues rather than omitting or ignoring things you'd rather not discuss.
:   Your honesty is your greatest asset, and it's hypocritical to criticize your
    opponents for spin or selective reporting if you're doing it too,

6. Don't sign any agreement that might prevent you from speaking about moral or legal concerns,
:   or make sure the agreement explicitly excludes your concerns before signing
    it.  (And yes, it's very privileged of me to be able to say this: someone
    whose immigration status, essential health benefits, or family income is
    being threatened may not have a choice.  That is why I think people who do
    have a choice also have an obligation to fight.)

7. Don't cite the law unless a lawyer tells you to.
:   The law probably doesn't mean what you think it means, and they almost
    certainly do have lawyers on their side who will seize on any mis-statement
    or mistake you make.

8. Don't try to get them to acknowledge that they were wrong.
:   Whatever happened probably wouldn't have if they were the sort of people who
    could do that.

9. Go for long walks.
:   Or cook some healthy meals, or pick up the guitar you haven't touched in
    years---anything that requires you to focus on something else for a while.
    This isn't just for your mental health: exhausted people make poor
    decisions, and you need to be at the top of your game.

10. Remember that it's OK to cry.
:   And that other people do care about you.
