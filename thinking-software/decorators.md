# Python Decorators Basics
May 23, 2014
![](images/decorators.png)

https://www.youtube.com/watch?v=bxhuLgybIro

## Introduction to decorators

Decorators introduce a programming paradigm that is not found in statically
linked languages, like C++ or Java. Taking advantage of closures and the fact
that functions are first class citizens of python, we can easily change the
behaviour of them adding a single line of code.

If you have not used dynamic languages before, chances are that you cannot
immediately see the value of decorators but as you will learning about them
chances are that you are going to change the way you write and think about
coding, as you will discover more elegant and efficient ways to implement
things that are either very verbose or even impossible to code in traditional
statically linked languages. Although there is a small learning curve
associated with them, decorators will quickly pay back enough dividend to
justify the learning process.

A python decorator is nothing else than a callable object, receiving a callable
as a parameter and returning another callable as its return value.

We will start with the simplest possible case of a decorator, which consists of
a regular function accepting a function as its parameter, defining a nested
function taking the same parameters as the passed one, returning the nested
function to the caller.

What I have just described above, can be visualized in the following picture
which presents the basic blocks of a python decorator:

## A simple program using decorators

The following is a simple program using a decorator:


```python
#!/usr/bin/python
# A very simple decorator demonstrating the basic concept

import time
import datetime

def timestamp():
    ts = time.time()
    mask = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(ts).strftime(mask)


def add_time_stamp(foo):
    ''' add_time_stamp is a decorator accepting a function foo '''

    def inner(*args, **kargs):
        '''
        inner is the function containing the decoration
        which in this case consists of printing the timestamp
        and the calling the outer function
        '''
        print timestamp(),
        foo(*args, **kargs)
    return inner


@add_time_stamp
def show_msg(msg):
    '''
    show_msg takes a single parameter as its argument and prints
    it to the screen.

    Note hat he definition of show_msg is preceeded by @add_time_stamp
    something that is equivalent to the following:

    def show_msg(msg): print msg
    show_msg = add_time_stamp(show_msg)
    '''
    print msg

if __name__ == "__main__":
    show_msg('test')
```

Running this program from the command line, you will see the following output:

```
2014-05-15 18:04:36 test
```

As we can see, we are getting the current time-stamp followed by the string we
passed (‘test’ in our case) printed in the standard output. The implementation
of show_msg knows nothing about the time-stamp, is the decorator that is
explicitly print the time-stamp and then calls the original function.

What is interesting in this case though, is the little magic that is going on
with the use of the @add_time_stamp right before the definition of show_msg.
The “at” sign (@) that goes before the add_time_stamp is a syntactic sugar,
saying to python that we want to use the function who’s name is printed right
after it to decorate the function that will be defined in the immediately next
line!

The following lines of code:
```python
    @add_time_stamp
    def show_msg(msg):
        print msg
```

are exactly equivalent to the following:



```python
def show_msg(msg):
    print msg
 
show_msg = add_time_stamp(show_msg)
```

The use of the ampersand can be viewed as a syntactic sugar that simplifies the
way we are writing the code, making it less verbose and more expressive.
Although it might seem like a simple facility, this mechanism very useful and
in many cases changes completely the way we write code, something that will
become more evident as you start using this approach more and more..

Note that our decorator will work with any function regardless of the number of
parameters it takes, because the inner function is using the following
signature:

```python
def inner(*args, **kargs):
```

keeping itself transparent to the specific signature of the function that is
been decorated.

At this point you know enough to start writing some more useful snippets that
will use decorators in your programs, to see an example keep on reading
forward.

## Using decorators to write a generic exception handler

Let’s write a realistic example of the use of decorators trying to improve our
understanding of them.

In the following program we define a function called divide which is implement
the trivial functionality of dividing the two parameters that are passed to it:

```python
def divide(x,y):
    return x / y
```

Nothing fancy or useful of course, but enough to make apparent the use of
decorator as we will see here.

If the divide function is called with y equalling 0 obviously it will throw an
exception as we can see here:

```python
#!/usr/bin/python
 
def divide(x,y):
    return x / y
 
print divide(8,0)
```

Running this program will result to the following output:

```
Traceback (most recent call last):
  File "./junk1.py", line 6, in 
    print 8/0
ZeroDivisionError: integer division or modulo by zero
```

The obvious way to fix this behaviour is to catch this exception showing some
message to the user:

```python
#!/usr/bin/python
 
def divide(x,y):
    try:
        a = x/y
        return x / y
    except Exception as ex:
        print ex
 
print divide(8,0)
```

To make our example more realistic, lets assume that we need another function
requiring similar exception catching behaviour, something like this:

```python
#!/usr/bin/python
 
def print_file(filename):
    try:
        f = open(filename)
        print f.read()
    except Exception as ex:
        print ex
 
def divide(x,y):
    try:
        a = x/y
        return x / y
    except Exception as ex:
        print ex
 
print_file('nonexistent_file')
```

In this case, assuming nonexistent_file indeed does not exist, we except to see
the following output when we run the program:

```
[Errno 2] No such file or directory: 'nonexistent_file'

```

Sure, we have a working program that can handle possible exceptions reasonably
well but as you can see the same code needed to handle them is repeated in both
functions. The use of a simple decorator can make our code more expressible and
easier to understand and this is how this can be done:

```python
#!/usr/bin/python
 
def handle_exceptions(foo):
    def inner(*args, **kargs):
        try:
            foo(*args, **kargs)
        except Exception as ex:
            print ex
    return inner
 
@handle_exceptions
def print_file(filename):
    f = open(filename)
    print f.read()
 
@handle_exceptions
def divide(x,y):
    a = x/y
    return x / y
 
print_file('nonexistent_file')
```

Note, how our code is now cleaner as the print_file and divide functions are no
longer polluted with the exception handling logic which is now implemented in a
decorator making our code easier to read and understand.

One question that arises here, is what if did not want one of the functions to
actually display the exception message? How in other words we can customize the
decorator passing to it additional parameters to alter its behaviour? This will
be the topic of the next example that you can read in the following page.

## Adding parameters to decorators

In the previous page we simplified our code by using a decorator to handle
exceptions keeping clear the implementation of a function. This is a great
improvement over repeating the same code over and over for each function we
write but someone might make the case that this solution is very generic and we
might need more control over the implementation of the decorator to specify its
behaviour.

This can be accomplished by a decorator with parameters which is slightly more
complicated than a parameter-less one and it can be done by nesting our current
decorator within a higher level function which will now become the real
decorator.

Continuing our example, let’s assume that we can solve our problem by using a
boolean called that will either make our handler to print the message or not.
Based on this our decorator should now look like this:

```python
def handle_exceptions(foo):
    def inner(*args, **kargs):
        try:
            foo(*args, **kargs)
        except Exception as ex:
            if print_message:
            print ex
    return inner
return handle_exceptions
```

Now, the decorator part for our functions should change to the following:

```python
@handle_exceptions_ex(True)
def print_file(filename):
```

and
```python
@handle_exceptions_ex(True)
def divide(x,y):
```
 
the whole program should look like this now:

```python
#!/usr/bin/python
 
def handle_exceptions_ex(print_message):
    def handle_exceptions(foo):
        def inner(*args, **kargs):
            try:
                foo(*args, **kargs)
            except Exception as ex:
                if print_message:
                print ex
        return inner
    return handle_exceptions
 
@handle_exceptions_ex(True)
def print_file(filename):
    f = open(filename)
    print f.read()
 
@handle_exceptions_ex(True)
def divide(x,y):
    a = x/y
    return x / y
 
print_file('nonexistent_file')
```

In this posting we covered the basics of python decorators. There are more
advanced uses of them that we will talk about in the next postings.





