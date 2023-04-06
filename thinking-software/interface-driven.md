# Interface Driven Programming In Python
May 26, 2014
![](images/interface-driven.png)
```
If it looks like a duck, quacks like a duck and walks like a 
duck, it’s a duck
```

Probably the greatest feature of python is its dynamic nature.  By this we mean
that variable names are not bound to types and they also can be assigned at run
time, this concept is also know as duck typing and an example of it is the
following:

```python
#!/usr/bin/python
class Person(object):
        pass
 
 
def print_name(obj):
    ''' Expects obj to expose a property name'''
    print obj.name
 
p = Person()
# we add name dynamically
p.name = 'John'
 
# print name
print_name(p)
 
# we can change name from a string to anyother type
p.name = 123
 
# print name continues to work
print_name(p)
```

At this point, you should notice that the print_name function, silently is
making the assumption that obj is supporting the attribute name. Of course this
will not always be the case since we can pass any kind of a variable to the
function causing an exception to be thrown.

## It’s easier to ask forgiveness than permission

A very common solution for this kind of problem in python is the following:

```python
def print_name(obj):
    try:
        print obj.name
    except TypeError:
        pass
```

This pattern is commonly known as It’s easier to ask forgiveness than
permission. In other words we assume that the passed in object indeed supports
name and we try to use it, if it turns out that it not supported an TypeError
exception will be raised and caught allowing our program to continue to
function.

## Look before you leap

Another way to achieve similar behaviour, is to apply a technique known as Look
before you leap meaning that, we verify that an object is supporting a specific
operation before we try to use it. The following code is an example of this
technique:

```python
def print_name(obj):
    if isinstance(obj, Person):
        print obj.name

```

Another way to achieve a similar effect is the following:

```python
def print_name(obj):
    if hasattr(obj, "name"):
        print obj.name
```

## Possible Problematic Behaviour

Although the solutions we have seen so far, can allow a program to continue its
execution without breaking in case of a wrong argument, we still can see some
problematic behaviour that might cause side effects, possibly leading to bogus
behaviour.

For example, checking for the type of the passed object will ignore any other
object than Person defining name which might not be our intention. Also using
the hasattr again might lead to cases like the following:

```python
class Person(object):
    name = 'To be defined'
 
def print_name(obj):
    if hasattr(obj, "name"):
        print obj.name
 
print_name(Person)
```

The output of this snippet will be:

```
To be defined
```

while what would have seen more reasonable in this case would have been
something like this:

```python
def print_name(obj):
    if hasattr(obj, "__name__"):
        print obj. __name__
 
# do your stuff ...
```

With the following output:

```
Person
```

Another example of undesired behaviour can be demonstrated in the following example:

```python
class Person:
    def __init__(self, name):
        self._name = name
 
    def get_name(self):
        return self._name;
 
def print_name(obj):
    if isinstance(obj, Person):
        print obj.get_name()
 
 
person = Person('john')
 
# print_name will work as expected
print_name(person) 
 
# we delete name from person
del person._name    
 
# now we will have an unhandled exception!
print_name(person) 
```

## Documentation Issues

More than the problems I discussed so far as far as duck typing is going, there
are also issues with proper documentation. Given the flexibility of dynamic
typing, chances are that users of specific module will have to delve in
directly to the source code trying to understand its details and how it is
working. A developer who just started using a system, is very possible to
misuse it and even start use attributes consisting implementation details
breaking encapsulation, making the maintenance of the code difficult and error
prone.

# The problem became obvious since python’s early stages

As early as 2001, we can find proposals like: PEP 245 and PEP 246 trying to
address the problem we are discussing here.

The discussion was very long and controversial since it was about a change that
seemed not pythonic at all!

A few years latter Guido van van Rossum came with his notorious blog
posting:Interfaces or Abstract Base Classes? which led to PEP 3119 introducing
the concept of Abstract Base Classes as we use it today.

In this posting we will not deal with historical aspects of ABCs (Abstract Base
Classes) nor with their non pythonic nature but we will focus in understanding
their implementation mechanics and details, so keep on reading to the next
page!

## A simple example leading to the use of an Abstract Base Class

To better understand the need of an Abstract Base Class, let’s start with a
simple example consisting of a base class called Shape which defines a single
method called get_area and a couple of its descendants called Rectangle and
Circle:

```python
class Shape(object):
    def get_area(self):
        pass
 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
 
    def get_area(self):
        return self.radius **2 * 3.14
```

This code looks good from the first glance, but as we inspect it closer we can
see some possible pitfalls. For example lets assume that we need a function
with the name find_total_area receiving a collection of shapes and returning
the total area covered by all of them, something like the following:

```python
def find_total_area(shapes):
    return sum(shape.get_area() for shape in shapes )
```

A possible use of this function could be the following:


```python
shapes = [Rectangle(10.2, 8.3), Circle(6.2)]
print find_total_area(shapes)
```

which will correctly output the following:


```
205.3616
```

## Problems with this implementation

A problem we can immediately see with the implementation of find_total_area has
to do with the user passing a list of objects not supporting the get_area
functionality. For example there might exist an Ellipse class implemented as
follows:

```python
class Ellipse:
    def __init__(self, a, b):
        self.a, self.b = a,b
 
    def calculate_area(self):
        return self.a * self.b * 3.14
```

and our user now might do something like the following:


```python
shapes = [Rectangle(10.2, 8.3), Circle(6.2), Ellipse(3,8) ]
print find_total_area(shapes)
```

As expected, in this case the find_total_area will throw an exception since the
Ellipse object does not support the get_area function…

One (not so good though!) way of fixing this problem, would had been to
re-implement the find_total_area function checking for each shape to see if it
supports the get_area functionality, as can be seen here:

```python
def find_total_area(shapes):
    def find_total_area(shapes):
    return sum(shape.get_area() for shape in shapes 
                                if hasattr(shape, 'get_area')
              )
```

Now our code will run happily without throwing any exceptions, but we still
have some problems. First of all we silently ignore the Ellipse in our
calculations and secondly we are making a silent assumption that the get_area
returns a numeric value that can be accumulated by sum. This can become a
problem for our implementation, as can be seen in the following user of our
code:

```python
shapes = [Rectangle(10.2, 8.3), Circle(6.2), Shape() ]
print find_total_area(shapes)
```

In this case, our modified version of find_total_area, will try to call the
get_area as it is implemented in Shape and of course throw an exception since
it is returning a None value that cannot be added to the areas of the other
shapes.

A better solution to our problem can be implemented by using an Abstract Base
Class, which we will see in the next page…

## Defining an Abstract Base Class

The definition of a ABC is straightforward besides the fact that is using the
not so widely concept of metaclasses. The developer does not need to understand
exactly what is happening in the background although in one of my next posts I
will talk more about metaclasses and how they can be used.

For now you can simply follow some implementation guidelines and understand
what ABCs are, strictly from the user scope of view.

Let’s now go back to our example and see how we can improve its functionality..

Our original base class looked like this:

```
class Shape(object):
    def get_area(self):
        pass
```

Assuming we are using python 2.7, to convert Shape to an ABC is as easy as follows:

```
from abc import ABCMeta, abstractmethod
 
class Shape(object):
    __metaclass__= ABCMeta
 
    @abstractmethod
    def get_area(self):
        pass
```

As you can see the necessary steps to follow are the following:

- Import ABCMeta and abstractmethod from abc
- Specify the metaclass of the class as ABCMeta
- Decorate the functions that we need to become abstract with the
  @abstractmethod decorator.

That’s it! Shape has now become an abstract class!

## How an ABC differs from any other class

An ABC cannot be instantiated directly

After defining Shape as an ABC, code like the following:

```
some_shape = Shape()
```

will fail to execute throwing the following TypeError:

```
TypeError: Can't instantiate abstract class Shape
with abstract methods get_area
```

An ABC is meant to serve only as a base class leaving the implementation of its
abstract members to its descendants. This does not mean that an ABC cannot
contain implementation details, in other words we can define members of the ABC
as in any other class, assuming that they are not decorated by the
abstractmethod (or absractproperty that we will see later) decorators.

### An ABC is forcing its descendants to implement its abstract parts

A descendant of an ABC is forced to implement its abstract parts. Code like the
following:

```
class BogusShape(Shape):
    pass
 
b = BogusShape()
```

Will fail with the following exception:

```
TypeError: Can't instantiate abstract class BogusShape with 
abstract methods get_area
```

Note that the TypeError exception will be thrown at the time we will try to
instantiate BogusShape. In other languages like C++ or Java the error condition
would had been caught at compile time.

## Defining descendants of an ABC

A descendant of an ABC needs to implement all of its abstract parts. Failure to
do so will cause an exception to be thrown at run time. For example the
following two classes are valid implementers of the ABC Shape:

```
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
 
    def get_area(self):
        return self.radius **2 * 3.14
```

As you can see, there is nothing specific to the fact that the base class in an ABC.

Using this approach our original code can be written as follows:

```
#!/usr/bin/python
 
from abc import ABCMeta, abstractmethod
 
class Shape(object):
    __metaclass__= ABCMeta
 
    @abstractmethod
    def get_area(self):
        pass
 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
 
    def get_area(self):
        return self.radius **2 * 3.14
 
 
class Ellipse:
    def __init__(self, a, b):
        self.a, self.b = a,b
 
    def get_area(self):
        return self.a * self.b * 3.14
 
 
def find_total_area(shapes):
    return sum(shape.get_area() for shape in shapes 
                                if isinstance(shape, Shape))
 
shapes = [Rectangle(10.2, 8.3), Circle(6.2), Ellipse(8,12)]
print find_total_area(shapes)
```

An interesting feature of ABCs is that if we want Ellipse to be considered as a
Shape as well, it is possible to do even without deriving from Shape, as long
it implements get_area. This can be accomplished by adding the following line
of code:

```
Shape.register(Ellipse)
```

Now our program becomes:

```
#!/usr/bin/python
 
from abc import ABCMeta, abstractmethod
 
class Shape(object):
    __metaclass__= ABCMeta
 
    @abstractmethod
    def get_area(self):
        pass
 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
 
    def get_area(self):
        return self.radius **2 * 3.14
 
 
class Ellipse:
    def __init__(self, a, b):
        self.a, self.b = a,b
 
    def get_area(self):
        print 'Ellipse get_area was called!'
        return self.a * self.b * 3.14
 
def find_total_area(shapes):
    return sum(shape.get_area() for shape in shapes 
                                if isinstance(shape, Shape))
 
shapes = [Rectangle(10.2, 8.3), Circle(6.2), Ellipse(8,12)]
print find_total_area(shapes)
 
Shape.register(Ellipse)
 
print find_total_area(shapes)
```

The output of our program now, will be the following:

```
205.3616
Ellipse get_area was called!
506.8016
```

As you can see, the Ellipse.get_area was now called even if Ellipse does not
derives from Shape, since we called the register function of the ABC.

## Conclusion
Abstract base classes can be used to customize type checking whenever something
like this is preferable over the classical pythonic duck typing.

We can use this technique in cases where we want to favour code extensibility
based in loose coupled components, that will be developed by many developers
who do not necessary have a deep understanding of the code details and prefer
to view specific components as black boxes that they interact with using well
defined interface-based contracts.

Another argument in favour of ABCs based design has to do with the improved
documentation which can become higher level, encapsulating as many
implementation details as possible from the user of the component allowing for
easier code changes and testing.














