# Thoughts About Software Quality…
May 20, 2014
![](images/longetivity.png)
## Longevity and number of users are the two most dominant characteristics of
high quality software This might sound a bit axiomatic but it has to be true:
software that remains alive while still expanding the number of it users as
time goes on, is the epitome of good software; anything else that can possibly
be used as quality metric is more of an implementation detail and should be
viewed like the vehicle rather than the destination.

Take for example software like LINUX, Apache Web Server of vi! Although solving
a different problem, each of these represents high quality solutions, since
they have been around for so many years and used by millions of users.

Regardless of any technical characteristic and implementation details, software
that meats these two requirements, longevity and wide use base should by
definition be considered as high quality; any other related aspect is just
indicative and can never change the verdict that is dictated by them.

Obviously, this definition is influenced by a very strong opinion that is
viewing software as the solution to very specific and well defined problems and
not as some sort of an abstract concept, that needs to be solved following the
appropriate algorithms, patterns and methodologies.

## You can never be sure in advance about the quality of the software you
developed Based in the definition as stated above, we can never be sure in
advance about the quality of some software we have just developed and only time
will reveal it.

This might seem a little oxymoron, since in most of the cases, we as
developers, tend to be believe that we now everything about our creations and
think that we can easily classify them as good, average or bad. I don’t think
so. Software is such a complicated concept, that even those who build it cannot
provide an accurate estimate about how it is going to evolve and serve its
clients.

Each time I am completing a solution, I always stay with the impression that I
would have definitely implemented it in a somehow better way now that I know
more about it! I also believe that this should be the case with any other
developer and I am not the only one in this boat!

I think that the essence of successful software development is exactly to
minimize this kind of afterthoughts (I am also sure that you will never be able
to completely eliminate them though!).

Although this might be the topic of another posting, I believe that the
reasoning behind the phenomenon of always having the impression that you could
have done something in a better way, had you re-implemented the solution again,
has to be related with the fact that software development, is still not pure
engineering and science but also contains a lot of aspects of a craft. Talent
and experience are way more important when it comes to programming than in
other classical engineering task.

## The ingredients of high quality software Of course, what I have already say
so far, should never be interpreted as that the design and implementation
specific details are irrelevant!

Quite the opposite is the truth!

Exactly in the implementation concepts and the design approach lies the
possibility of a solution to be proven high quality!

The applied design and implementation principles, although by themselves cannot
guarantee the quality of the software, the will certainly influence it and to a
large extend determine it. The best way to discover the best characteristics to
be used, is to examine software that has been proven successful, standing the
test of time and try to adapt them based in the nature of our domain and the
most important of them are the following:

### Platform neutrality

Software that is decoupled from any external technologies seem to be easier to
use and evolve.  By external technologies, we can refer to anything that our
code interacts with and can be the operating system, the data base, the
messaging broker and anything else. Somebody can even make the point that even
the programming language itself, is an external dependency and decide to
implement his code in such a way that can be translated to several programming
languages!

### Modularity

A consequence of platform neutrality, is modularity which allows for easy
replacement of specific components with other who complying to the expected
contracts still are implemented in a completely different way, something that
can be done for performance or interoperability reasons.

### Backwards compatibility

Newer versions should be very careful about their existing clients and should
strive for as complete as possible backwards compatibility. The most probable
timing for a piece of software to loose a user is when it moves to a newer
version breaking his code base and expecting him to modify his code base to
achieve forward compatibility. Although there might be cases where breaking
backwards compatibility could be justified, in most of the cases something like
this should be avoided.

### Easiness of integration

The ability of software to be a good player within its ecosystem, complying to
standards and common conventions, is very important as time goes by and the
domain becomes more mature attracting more solutions that need to exchange data
and functionality. A ‘closed’ system, which has no hooks to its environment is
just a matter of time to become obsolete, no matter how complete and successful
will be upon its birth.

### Easiness of use

Obviously, easiness of use is a characteristic of successful software as it
increases the chances of massive adoption. Besides that, easiness of use can
easily be added to software that already complies to the concepts of modularity
and platform neutrality but there are cases where it becomes the most important
quality. At this point, I want to make it clear, that by easiness of use, I am
referring both to the end user who will interact with the software by some GUI
and the programmer who will use the code base to develop in top of it.

### Ability to solve to completely different problems than the original

A consequence of most of the above characteristics, is the inherent ability of
a piece of software to be used in ways that the original developer had no idea
about.

## It is still a judgement call Of course, this does not imply a blind adoption
of every concept and methodology that is widely considered as an ingredient of
high quality software!

There are a lot of judgement calls that the developer will have to make, during
the design and implementation faces and it is up to his expertise to deviate
from the rules when he thinks that this the way to go.

## Conclusion Endurance to time and wide user base is the most dominant
characteristic of high quality software and our main goal as developers should
be to achieve both of them. Studying successful software we can reach
conclusions about the principles we should use although personal judgements,
talent and experience should also play a very important role to our decisions.
