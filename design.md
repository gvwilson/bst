---
---

FIXME: show ER diagrams

FIXME: show use-case maps

FIXME: explain why UML isn't useful

Building large programs with other people is different from building small
programs on your own. This section describes a few of the things that you'll
want to do in the former case that might not crop up in your regular classes.

I should confess up front that I can't tell you how to design software.  I don't
know anyone who can, either. I can *show* you by working through examples on a
whiteboard, asking rhetorical questions, and setting problems for you to think
about, but that doesn't translate well to print. If you can talk a handful of
good software designers into letting themselves be videotaped as they work
through problems on a whiteboard, please let me know---I'm sure I'd learn a lot
by watching them.

## Describing designs

I can, however, tell you a little about how to describe designs. If you watch
experienced developers drawing on the whiteboard as they're talking to one
another, you'll generally see them sketching the following:

Data structures.
:   These are blob-and-arrow pictures of the objects and containers that make up
    the program, and the references that stitch them together. The more
    experience someone has, the fewer of these they need to draw, but everyone
    falls back on them eventually (particularly during difficult debugging
    sessions).

Schemas or data models.
:   These can be fairly literal pictures of the tables in a database, possibly
    augmented with arrows to show what's a foreign key for what, or
    entity-relationship diagrams that show the things the system stores, and the
    relationships between them.

The conceptual architecture of the system.
:   This is the most important diagram of all, since it's the "big picture" view
    of how everything in the system fits together. It's also the least
    constrained, since it can include everything from specific sections of
    configuration files to class hierarchies to replicated web servers. I'll
    talk more about conceptual architectures below.

The system's physical architecture.
:   This is the files, processes, sockets, database tables, etc., that make it
    up. In most cases, this consists of a bunch of boxes representing the
    machines the application's components run on, trees showing files and
    directories, and circles showing running processes. A lot of this stuff can
    show up in the conceptual architecture as well.

The workflow architecture that shows how users accomplish things.
:   This is almost always drawn as a finite state machine. In the web world, it
    is often called a navigation diagram or roadmap; each blob represents a
    page, and the arrows connecting them show how users can navigate from one
    page to another.

With the exception of schemas and data models, all these diagrams consist of
components and connectors, i.e., things and the relationships between them. In a
physical architecture diagram, for example, the components represent machines,
processes, and files, and the connectors represent sockets and the
"reads/writes" relationship for files.

The most important diagram is the conceptual architecture, which is the "big
picture" view of how the most important pieces of the system relate to one
another. What qualifies as "important" depends on what aspect(s) of the system
you're currently concerned with. If I'm trying to explain a bug that only arises
when the application is configured incorrectly, I might draw its configuration
files, and the database tables that store user preferences, but leave out the
password database and log files entirely. If we're trying to figure out a better
load balancing strategy, on the other hand, I would draw most of what would go
into a physical architecture diagram, plus just enough of the class inheritance
hierarchy to show how the servers will load user request handlers dynamically.

The goal of these diagrams is always to help your readers, listeners, or viewers
(including yourself) understand enough of the system to be able to decide what
to do next. This is why I'm not a fan of the Unified Modeling Language
(UML). UML defines over a dozen different types of diagrams for showing the
relationships between classes, the order in which things happen when methods are
invoked, the states a system goes through when performing an action, and so on.

Hundreds of books and thousands of articles have been written about UML, and no
other notation is as well described. That's the good news; the bad news is that
in all the years I've been programming, I've only ever met one person who drew
UML diagrams of his own free will on a regular basis. I've known a handful of
other people who occasionally sketched class diagrams as part of a larger
description of a design, and that's pretty much it. When I contrast that with
blueprints in architecture, or flow diagrams in chemical engineering, the only
conclusion I can reach is that software developers don't actually find UML very
helpful.

I think there are several reasons for this, including its lack of a well-defined
semantics and the fact that UML diagrams can't be diffed and merged by version
control systems. However, since it's all that we have, in most books, likely to
be on the final exam, and might come up in an interview, it's still worth
mastering the basics.

## Getting started

What if you're starting with a blank sheet of paper (or an empty whiteboard)?
How do you describe something that doesn't exist yet? The best way to start is
to write your elevator pitch. Next, write one or two paragraph-long stories
describing how the application, feature, or library would be used. Be as
concrete as possible: instead of saying, "Allows the user to find overlaps
between their calendar and their friends' calendars," say, "The user selects one
or more of her friends' calendars (and optionally her own), and the system
displays a page showing events that two or more people are going to, color coded
to show how popular they are."

Once you have those narratives, go through and highlight the key "things" and
"relationships" you've just described. In the example above, you would highlight
"user", "friend", "calendar", "event", "page", and so on. As soon as you try to
draw a blob-and-arrow diagram showing how these are related to one another,
you'll have to start making design decisions: for example, is "friend" an
entity, or a relationship between two entities (i.e., is it a blob or an arrow)?

If, during this process, you hear yourself say, "We'll use a linked list to…"
then step back and catch your breath. Details like that do need to be worked out
at some point, but:

-   you're probably worrying about that as a way to *not* think about the bigger
    design questions (which are scarier for beginners);

-   you probably don't know enough yet about your design to make the right
    decision; and

-   you're probably a good enough coder by now that you can worry about that
    when the time comes to actually write the code. Remember, not everything
    actually needs to be designed…

Once you have a diagram---any kind of diagram---you should start iterating
around it. Pick one open problem (such as "how will users control who can see
their calendars?"), think of a way to solve it ("they can mark them as 'public',
or invite specific people to view them"), figure out how to implement your
solution, then revisit any previous decisions that your most recent decisions
affect. Design is a very cyclic process: every time you add or change one thing,
no matter how small, you may need to go back and re-design other things.

There are two traps here for the inexperienced. The first is *analysis
paralysis*, in which you find yourself revisiting issues over and over again
without ever making any decisions that stick. The second is the *already
invented here* syndrome, in which someone (possibly you) says, "Look, we've
already made a decision about that, let's not reopen the debate." Either can
sink a project; together, they show why it's so hard to teach design, since what
I'm basically saying is, "Argue enough, but not too much." Helpful, isn't it?

## Design for testability

When most developers hear the word "design", they think about either the
application's structure or its user interface. If you don't think about how
you're going to test your application while you're designing it, though, the
odds are very good that you'll build something that can't (or cannot easily) be
tested. Conversely, if you *design for test*, it'll be a lot easier to check
whether your finished application actually does what it's supposed to.

For example, let's consider a typical three-tier web site that uses the
Model-View-Controller (MVC) design pattern. The model, which is stored in a
relational database, is the data that the application manipulates, such as
purchase orders and game states. The controller layer encapsulates the
application's business rules: who's allowed to cancel games while they're in
progress, how much interest to add on out-of-province orders, and so
on. Finally, the view layer translates the application's state into HTML for
display to the user.

This architecture presents (at least) three challenges from the point of view of
testing:

1.  Unit testing libraries like JUnit (and its clones in other languages) aren't
    built to handle this: as the word "library" implies, they're made up of code
    that's meant to be called *within* a process. Despite the ubiquity of
    multi-process applications, most debuggers and testing libraries cannot
    track "calls" *between* processes.

2.  Configuring a test environment is a pain: you have to set up a database
    server, clear the browser's cache, make sure the right clauses are in your
    Apache configuration file, and so on.

3.  Running tests is slow. In order to ensure that tests are independent, you
    have to create an entirely new fixture for each test. This means
    reinitializing the database, restarting the web server, and so on, which can
    take several seconds *per test*. That translates into an hour or more for a
    thousand tests, which is pretty much a guarantee that developers won't run
    them routinely while they're coding, and might not even run them before
    checking changes in.

The first step in fixing this is to get rid of the browser and web server. One
way to do this is to replace the browser with a script that generates HTTP
requests as multi-line strings and passes them to a "fake CGI" library via a
normal function call. After invoking our actual program, the fake CGI library
passes the text of an HTTP response back to our script, which then checks that
the right values are present (about which more in a moment). The "fake CGI"
library's job is to emulate the environment the web app under test would see if
it was being invoked as a CGI by Apache: environment variables are set, standard
input and output are replaced by string I/O objects, and so on, so that the web
app has no (easy) way of knowing that it's being invoked via function call,
rather than being forked.

Why go through this rigmarole? Why not just have a top-level function in the web
app that takes a URL, a dictionary full of header keys and values, and a string
containing the POST data, and check the HTML page it generates? The answer is
that structuring our tests in this way allows us to run them both in this test
harness, and against a real system. By replacing the fake CGI adapter with code
that sends the HTTP request through a socket connected to an actual web server,
and reads that server's response, we can check that our application still does
what it's supposed to when it's actually deployed. The tests will run much more
slowly, but that's OK: if we've done our job properly, we'll have caught most of
the problems in our faked environment, where debugging is much easier to do.

Now, how to check the result of the test? We're expecting HTML, which is just
text, so why not store the HTML page we want in the test and do a string
comparison? The problem with that literal approach is that every time we make
any change at all to the format of the HTML, we have to rewrite every test that
produces that page. Even something as simple as introducing white space, or
changing the order of attributes within a tag, will break string comparison.

A better strategy is to add unique IDs to significant elements in the HTML page,
and only check the contents of those elements. For example, if we're testing
login, then somewhere on the page there ought to be an element like this:

```
<div id="currentuser">Logged in as <strong>gvwilson</strong>
(<a href="http://www.example.org/logout">logout</a>
|
<a href="http://www.example.org/preferences">preferences</a>)
</div>
```

We can find that pretty easily with an *XPath* query, or by crawling the DOM
tree produced by parsing the HTML ourselves. We can then move the `div` around
without breaking any of our tests; if we were a little more polite about
formatting its internals (i.e., if we used something symbolic to highlight the
user name, and trusted CSS to do the formatting), we'd be in even better shape.

We've still only addressed half of our overall problem, though: our web
application is still talking to a database, and reinitializing it each time a
test runs is sloooooooow.

We can solve this by moving the database into memory. Most applications rely on
an external database server, which is just a long-lived process that manages
data on disk. An increasingly-popular alternative is the *embedded* database, in
which the database manipulation code runs inside the user's application as a
normal library. Berkeley DB (now owned by Oracle) and SQLite (still open source)
are probably the best known of these; their advocates claim they are simpler to
build and faster to run, although there are lots of advantages to using servers
as well.

The advantage of embedded databases from a testing point of view is that they
can be told to store data in memory, rather than on disk. This would be a silly
thing to do in a production environment (after all, the whole point of a
database is that it persists), but in a testing environment, it can speed things
up by a factor of a thousand or more, since the hard drive never has to come
into play. The cost of doing this is that you have to either commit to using one
database in both environments, or avoid using the "improvements" that different
databases have added to SQL.

Once these changes have been made, the application zips through its tests
quickly enough that developers actually will run the test suite before checking
in changes to the code. The downside is the loss of *fidelity*: the system we're
testing is a close cousin to what we're deploying, but not exactly the
same. However, this is a good economic tradeoff: we may miss a few bugs because
our fake CGI layer doesn't translate HTTP requests exactly the same way Apache
and Python's libraries do, but we catch (and prevent) a lot more by making
testing cheap.

This example just scratches the surface of designing for testability. If you
want to go further you can add some or all of the following:

1.  Scriptable interfaces to the product, so that we can drive it more
    easily with automation.

1.  Logging of activities within the program.

1.  Monitoring of the internals of the application via another window or
    output over the network.

1.  Clearer error/exception messages, including unique identifiers for
    specific points in the code, or *which* damn file was not found.

## Keeping track

If your project is run like most, you're going to submit your work several times
over the course of the term. That means it's important for you to keep track of
exactly what version you're working on at any time, where it came from, and
where it's going.

The usual way to do this is with *version numbers*. If you see a number like
"6.2.3.1407" attached to a piece of software, it generally means:

-   major version 6

-   minor version 2

-   patch 3

-   build 1407

The major version number is only incremented when significant changes are
made. In practice, "significant" means "changes that make it impossible for
older versions to read the new version's data or configuration files". In
practice, major version numbers are often under the control of the marketing
department---if a competitor releases a new major version, we'd pretty much have
to as well.

Minor version numbers are what most people think of as releases. If you've added
a few new features, changed part of the GUI, etc., you increment the minor
version number so that your customers can talk intelligently about which version
they have.

Patches are things that don't have their own installers. If, for example, you
need to change one HTML form, or one DLL, you will often just mail that out to
customers, along with instructions about where to put it, rather than creating a
new installer. You should still give it a number, though, and make an entry in
your release log[^40].

The build number is incremented every time you create a new version of the
product for QA to test. Build numbers are never reset, i.e. you don't go from
5.2.2.1001 to 6.0.0.0, but from 5.2.2.1001 to 6.0.0.1002, and so on. Build
numbers are what developers care about: they're often only matched up with
version numbers after the fact (i.e. you create build #1017, QA says, "It looks
good," so you say, "All right, this'll be 6.1.0," and voila, you have
6.1.0.1017.)

Finally, groups will sometimes identify pre-releases as "beta 1", "beta 2", and
so on, as in "6.2 beta 2". Again, this label is usually attached to a particular
build after the fact---you wait until QA (or whoever) says that build #1017 is
good enough to send out to customers, then tag it in version control.

A four-part numbering scheme is more than you need for an undergraduate
course. You can probably get away with just two numbers: one to identify the
assignment the software was submitted for, and another to identify the files
that went into that "release".

## Logging

Something else you can design into your system to make your life easier later on
is *logging*. This is the grown-up way to debug with print statements. Instead
of writing:

```python
def extrapolate(basis, case):
    print "entering extrapolate..."
    trials = count_basis_width(basis)
    if not trials:
        print "...no trials!"
        raise InvalidDataException("no trials")
    print "...running", len(trials), "trials"
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    print "...exiting extrapolate with", result
```

you use your language's logging library like this:

```python
from logging import error, debug

def extrapolate(basis, case):
    debug("entering extrapolate...")
    trials = count_basis_width(basis)
    if not trials:
        warning("...no trials!")
        raise InvalidDataException("no trials")
    debug(f"...running {len(trials)} trials")
    result = run_trial(trials[0])
    for t in range(1, len(trials)):
        result = max(result, run_trial(trials[i]))
    debug(f"...exiting extrapolate with {result}"}
```

At first glance, this is just more verbose. The benefit, though, is that your
messages are now divided into two classes. If you want to get all the messages,
you put:

```python
logging.basicConfig(level=logging.DEBUG)
```

somewhere near the start of your program. `DEBUG` identifies the least important
messages in your program---the ones you probably only want to see when you're
trying to figure out what's gone wrong. In order, the more important levels (in
Python's logging framework---other libraries define these slightly differently)
are `INFO`, `WARNING`, `ERROR`, and `CRITICAL`. If you only want messages at the
`WARNING` level and above, you change the configuration to:

```python
logging.basicConfig(level=logging.WARNING)
```

so that `DEBUG` and `INFO` messages aren't printed.

A logging library allows you to control how much your program tells you about
its execution by making one change, in one place. It also means that you can
leave these messages in your code, even when you release it. No more commenting
out `print` statements, only to add them back in later. (And no more
inappropriately-worded messages that *weren't* commented out popping up in the
middle of demos.)

But wait, there's more. Logging libraries also let you control where your
messages are sent. By default, they go to the screen, but you can send them to a
file instead simply by changing the configuration:

```python
logging.basicConfig(level=logging.ERROR,
                    filename="/tmp/mylog.txt",
                    filemode="append")
```

This is handy if it takes your program a while to get to the point where the
error occurs. It's also handy if you don't know whether your program contains an
error or not: if you leave logging turned on every time you run it, then
whenever it does something unexpected (like crashing), you will have at least
some idea of what it was doing beforehand.

Most logging libraries also support *rotating files*, i.e., they will write to
`log.1` on the first day, `log.2` on the second day, and so on until they reach
(for example) `log.7`, then wrap around and overwrite `log.1`. Web servers and
other long-lived programs are usually set up to do this so that they don't fill
up the disk with log information.

Finally, logging libraries can send output to mail servers, cell phones, web
servers, and Lava Lamps to notify system administrators when something
`CRITICAL` happens. You can also define message categories, like "database
operations" or "login and logout", and then tell the logging library to only
save specific kinds of messages. It's all straightforward to set up, and once
it's in place, it gives you a lot more insight into what your program is
actually doing.
