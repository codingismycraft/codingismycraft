Falsifiability and Unit Testing
May 25, 2016
![](images/popper.png)

Without a doubt, Test Driven Development (TDD) lies in the core of my software
development approach.  I have been a very early adapter of automated testings
since my C++ and C# days and always felt very enthusiastic about their impact
on the quality of the software.

I have to admit that it was not until I became a full time python developer
that my commitment and understanding of TDD was perfected. Compared to
statically linked languages like C# or Java, the dynamic nature of python
multiplies the significance of unit testing, elevating it to one of the most
fundamental tactics for the delivery of a successful project. More than this, I
do not think that I will exaggerate if I claim that as a back end developer,
the most frequent way I can see my code in action, is simply the execution of
the test scripts.

I have spent a lot of time and effort thinking about the best practices and
patterns that can simplify testing and improve their  effectiveness in
discovering as many bogus conditions as possible.  Although there exist
preferable heuristics and coding idioms which can indeed improve the degree of
code’s testiness,  I still believe that the process of creating highly testable
software involves a lot of talent and experience on top of knowledge that can
be communicated through books or taught by a professor.

## Karl Popper and unit testing 

Aside from computer programming, the other topic I
am always fascinated about is Philosophy of Science.  Karl Popper, one of the
greatest philosophers of science ever lived, introduced us to the
Falsifiability principle, which I believe is perfectly applicable to the
concept of Test Driven Development.

Falsifiability defines the distinction between a scientific theory and
metaphysics. Based on this principle a theory is considered scientific only if
we can conceive an observation to nullify it (prove it to be wrong).

For example, a statement like “The Earth is flat” is scientific because it can
be nullified if a traveler reaches his starting point after departing from a
specific location and keep on moving towards the same direction.  The fact that
a statement is scientific, does not mean that it is correct of course.

Based on Popper’s philosophy, we can never be sure that a scientific theory is
correct as the only thing we can do with it, is to prove it wrong by executing
a successful falsifying test.

I believe that TDD constitutes a  projection of Karl Popper’s Falsifiability to
the process of developing software, as it can be viewed as a special type of a
“scientific” conjecture that needs to satisfy a collection of tests whose
purpose is  to “prove” it wrong by braking its expected behavior.

In software development we need to substitute the term “scientific theory” with
“software that works as intended” and the proposed experiments with tests that
need to be satisfied.

In the same way that we can never be certain about the absolute “truth” of a
scientific theory but the best we can do is to explain as many experiments as
possible, we can also never be sure that a specific piece of software is
completely “bug free”. The best we can do is to describe as many tests as
possible and prove that they can be served as expected without breaking the
desired behaviour.

At this point we need to clarify that, as strange as it might sound, a
successful test is the one that fails!  A failing test needs our attention, as
its existence means that we must revisit our code and resolve the related
issues something that will cause the test to pass. Our mission as developers,
is to increase the descriptiveness and comprehensiveness of our tests, trying
to cover every execution path and parameter combination that can ever occur!

# Diminishing the value of TDD is a sign of inexperience 

As a developer, there have been many times when I have been presented to some
legacy code that was clearly ill functioning and my mission was to either
refactor or rewrite it from scratch. In almost all of these cases, the legacy
platform was extremely difficult to test, as it presented a very tight coupling
among its components and external dependencies, making it impossible to write
effective and realistic tests.

A very widespread tendency among the software project managers (PMs) is to
diminish the value of testing. In their struggle to meet irrational deadlines,
PMs are focusing on delivering a working and feature rich solution, usually
underestimating its complexity and its potential for extensibility. Following
this way of delivering software, TDD is one of the practices that is usually
overlooked, as inexperienced and non technical PMs like to believe that writing
comprehensive tests is very time consuming and it does not really add lots of
business value in the final solution!

In the core of my software development philosophy, I am viewing production code
as a conjecture that is always paired with a vast array of tests that are meant
to invalidate its functionality. I think that this approach is very well
aligned with Popper’s Falsifiability and I have to admit that this analogy
works fairly well when it comes to measuring the quality of a platform.

I completely disagree with the view that the development of tests is a time
consuming and expensive process. On the contrary, investing in extensive and
well thought testing suites actually decreases the final cost of the
application when we consider bug fixes, evolution to new technologies and
adaption of new and originally unanticipated features.

## Conclusion 

Writing highly testable code requires experience, talent and knowledge of both
generic testing patterns and all of the available platform specific utilities
and tools. Possessing the ability to create testable software is one of the
most critical qualities of a master developer. Code that is easy and convenient
to test will outperform any other solution that is difficult to test, as it
will evolve easier to meet future needs, extend its life span and maximize its
cost-reward ratio.

To master the TDD process, the developer needs to reach a certain level of
maturity and cultivate the ability to transform specifications to “Popperian”
experiments expressed as simple tests, always trying to maintain the golden
ratio of coverage over cost of development.
