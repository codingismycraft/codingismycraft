# Adding descriptors to your python arsenal
October 4, 2017
![](images/descriptors.png)

Python provides a rich programming paradigm providing the ability to the programmer to express his solutions in a very concise and elegant way.  One of the python features that is not in wide use although it gives the opportunity to simplify certain pieces of code, is the <em><strong>descriptor protocol</strong></em> which is the topic of this posting.

<h5>A piece of code that needs some improvements</h5>

Let's start with a simple example of a class that can be improved by the use of descriptors.

The following class:

[python]
class Employee(object):
  def __init__(self,
                name,
                personal_email,
                work_email):
    self.name = name
    self.personal_email = personal_email
    self.work_email = work_email
[/python]

represents an employee holding the name, the personal and work emails of a person.  

Not a very useful class indeed but the problems that can be found in it can lead to an understanding
the need for descriptors.

A user of this class can instantiate persons as can be seen here:

[python]
john_doe = Employee(
  name='John Doe',
  personal_email='john.doe@work.com',
  work_email='john.doe@personal.com'
)
[/python]

This code will work fine as long as the user will be careful and pass valid data. If the user makes a mistake passing an invalid email address the code will continue its execution without giving an hint about its erroneous state; it will be later, when this object will eventually be used to send an email that it will fail due its invalid data though.  Obviously this is not a good behavior and this is why we must try to catch invalid data as early as possible and try to keep the validity of our data as high as possible.

A naive way to deal with this problem to refactor the existing code to something like the following:

[python]
import re

EMAIL_REGEX = re.compile(
  r"[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@"
  "[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})"
)


def ValidateEmail(email_address):
  if not EMAIL_REGEX.match(email_address):
    raise ValueError


class Employee(object):
  def __init__( self,
                name,
                personal_email,
                work_email):
    self.name = name
    ValidateEmail(personal_email)
    ValidateEmail(work_email)
    self.personal_email = personal_email
    self.work_email = work_email

[/python]

Passing invalid data as can be seen here:

[python]

p = Employee('test', 'test@work.com', 'test@')

[/python]

raises the following exception:

<pre>Traceback (most recent call last):
  File "employee_test.py", line 26, in 
    p = Employee('test', 'test@work.com', 'test1')
  File "employee_test", line 21, in __init__
    ValidateEmail(work_email)
  File "employee_test", line 11, in ValidateEmail
    raise ValueError
ValueError
</pre>

Although this code handles the invalid data when they are provided in the constructor, 
the user still can pass invalid values as we can see here:

[python]
p.work_email = 'test1@'
[/python]

In the line of code shown here the user is changing the work email which is accessed "directly" as an instance level attribute. 

Programmers coming from languages like C#, Java or C++ might resolve to <em><strong>accessor functions</strong></em> to solve the problem while converting the attributes to protected to avoid the user changing them directly; the same approach is also doable when using python: 

[python]
class Employee(object):
  def __init__( self,
                name,
                personal_email,
                work_email):
    self._name = name
    ValidateEmail(personal_email)
    ValidateEmail(work_email)
    self._personal_email = personal_email
    self._work_email = work_email

  def GetPersonalEmail(self):
    return self._personal_email

  def SetPersonalEmail(self, value):
    ValidateEmail(value)
    self._personal_email = value

  def GetWorkEmail(self):
    return self._work_email

  def SetWorkEmail(self, value):
    ValidateEmail(value)
    self._work_email = value

[/python]

Although an object of this class can still be changed by the outside (python does not have a mechanism similar to C++ or Java to encapsulate its private details from the user), the code prevents the user from passing invalid data to to the person object assuming that he is aware that he is not supposed to change an attribute who's name starts with an underscore (also known as protected member).

This code will work fine but it is not very pythonic in its implementation. Instead it cries about the origin of the programmer who has to be coming from a statically linked language and still retains its accent.  Although in a language like Java setters and getters consist a very common pattern that is used across the board, its implementation clearly violates the DRY principle by repeating similar lines of code, like the email validation or even the whole Set method.

<h5>Improving the code using a descriptor</h5>

Let's start the refactoring of the Person class by introducing the following class that wraps the implementation details of an email object:

[python]
class Email(object):
  """Descriptor class used to hold an email address."""

  def __init__(self):
    self.pool = {}

  def __get__(self, instance, owner):
    return self.pool.get(instance, 0)

  def __set__(self, instance, email_address):
    if not EMAIL_REGEX.match(email_address):
      raise ValueError
    self.pool[instance] = email_address
[/python]

The Email class as defined here implements a couple of "magic" methods with the names __get__ and __set__ which as we will shortly see give some special functionality to the way python is going to process calls to them.

The following is an <a href="https://docs.python.org/2.7/reference/datamodel.html">extract</a> from the official python's documentation which describes these methods:
<blockquote>
<h5>Implementing Descriptors</h5>
The following methods only apply when an instance of the class containing the method (a so-called descriptor class) appears in an owner class (the descriptor must be in either the owner’s class dictionary or in the class dictionary for one of its parents). In the examples below, “the attribute” refers to the attribute whose name is the key of the property in the owner class’ __dict__.

<strong>object.__get__(self, instance, owner)</strong>

Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). owner is always the owner class, while instance is the instance that the attribute was accessed through, or None when the attribute is accessed through the owner. This method should return the (computed) attribute value or raise an AttributeError exception.

<strong>object.__set__(self, instance, value)</strong>

Called to set the attribute on an instance instance of the owner class to a new value, value.

<strong>object.__delete__(self, instance)</strong>

Called to delete the attribute on an instance instance of the owner class.</blockquote>
As you can see, I have also implemented the initializer of the Email class adding a <strong>pool</strong> instance level attribute that we will now see why it is needed.

Having the Email descriptor, let's go ahead and rewrite the Person class:

[python]
import re

EMAIL_REGEX = re.compile(
  r"[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@"
  "[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})"
)


def ValidateEmail(email_address):
    if not EMAIL_REGEX.match(email_address):
        raise ValueError


class Email(object):
    """Descriptor class used to hold an email address."""
    
    def __init__(self):
        self.pool = {}

    def __get__(self, instance, owner):
        return self.pool.get(instance, 0)

    def __set__(self, instance, email_address):
        if not EMAIL_REGEX.match(email_address):
            raise ValueError
        self.pool[instance] = email_address


class Employee(object):
    personal_email = Email()
    work_email = Email()

    def __init__(self, name, personal_email, work_email):
        self.name = name
        self.personal_email = personal_email
        self.work_email = work_email

[/python]

Passing an invalid email address raises an exception:

[python]
try:
    johnDoe = Employee(
      name='John Doe',
      personal_email='john.doe@personal.com',
      work_email='john.doe@',
    )
except ValueError:
    print 'Failed to assign email.'
[/python]

The following code creates two employees:

[python]
johnDoe = Employee(
  name='John Doe',
  personal_email='john.doe@personal.com',
  work_email='john.doe@work.com',
)


mikeSmith = Employee(
  name='Mike Smith',
  personal_email='mike.smith@personal.com',
  work_email='mike.smith@work.com',
)
[/python]

We can use them as follows:

[python]
print johnDoe.personal_email
print mikeSmith.personal_email
[/python]

and get the following output:
<pre>john.doe@personal.com
mike.smith@personal.com
</pre>
At this point we need to understand what exactly is happening here. The Employee class is defining the two email attributes as class level objects but reading closer the code above, we can see that the corresponding variables are been accessed at the instance level; for example when we execute the following code:

[python]
johnDoe.personal_email='mike.smith@personal.com'
[/python]

we expect to access the <strong>personal_email</strong> attribute of the johnDoe object which will be assigned with the <strong>mike.smith@personal.com</strong> value. If this is the case, then the <strong>personal_email</strong> variable must be of string (str) type but clearly this is not the case, since if the following assignment:

[python]
johnDoe.personal_email='mike.smith@'
[/python]

is raising an exception.

<strong>Delving into the descriptor mechanism </strong>

From the example we have seen so far, we have see a way to eliminate the repeated chunks of code that are needed to validate an email address field; still we need to understand a little better how this code is working as some non standard functionality has to be happening for this code to execute properly.

The first thing we should notice is the implementation of the get / set methods as they appear in the Email class. Their signatures are the following:
<pre>__get__(self, instance, owner)
    
__set__(self, instance, email_address)
</pre>
In both cases what can the first argument (instance) refer to?

The use of the "instance" for the attribute name should make it easy to understand that it is referring to an object that is already created in the memory.

What happens behind the scenes, is that when python is calling one of the get / set, it passes to it an object; in our example, the object that is passed will always be of type Employee and it will be the object that we called the getter or the setter from. Reading closely to the implementation of the Email class, we see that upon initialization we add to the object a dictionary (pool) which holds the corresponding email values based on the Employee object.

Instead of the email values to be stored directly in an Employee object, they are stored in a class level attribute (you can think of it as a static variable) which maps the instance to the corresponding value.

<h5>Removing a possible memory leak</h5>

The implementation of Email as it appears above greatly simplifies our original code but it can result to a nasty memory leak that we need to fix. First lets verify the problem by running the following code:

[python]
def CreateSomeEmployees():
    """Simply creates two employess.
    
    Used to detect memory leaks.
    """
    johnDoe = Employee(
      name='John Doe',
      personal_email='john.doe@personal.com',
      work_email='john.doe@work.com',
    )


    mikeSmith = Employee(
      name='Mike Smith',
      personal_email='mike.smith@personal.com',
      work_email='mike.smith@work.com',
    )
    
print 'Personal emails in memory: %d' % (
    len(Employee.__dict__['personal_email'].pool)
)   
CreateSomeEmployees()

print 'Personal emails in memory: %d' % (
    len(Employee.__dict__['personal_email'].pool)
)   
CreateSomeEmployees()

print 'Personal emails in memory: %d' % (
    len(Employee.__dict__['personal_email'].pool)
)   

[/python]

The output of this code will be the following:
<pre>Personal emails in memory: 0
Personal emails in memory: 2
Personal emails in memory: 4
</pre>
Note that each time we call CreateSomeEmployess we have two new Employee objects created that are going out of scope when the function exits. Despite this though, we can see that although the objects are going out of scope, the pool dictionary that leaves in the Email class retains a reference to it resulting to a memory leak that hopefully is very easy to fix.

To assure that out of scope objects are removed from the pool we need to use a <strong>WeakKeyDictionary</strong> instead of the standard dictionary that we are using so far.

The following is an &lt;ahttps://docs.python.org/2.7/library/weakref.html"&gt;extract from the official python's documentation which WeakKeyDictionary:
<blockquote>
<h5>class weakref.WeakKeyDictionary([dict])</h5>
Mapping class that references keys weakly. Entries in the dictionary will be discarded when there is no longer a strong reference to the key. This can be used to associate additional data with an object owned by other parts of an application without adding attributes to those objects. This can be especially useful with objects that override attribute accesses.</blockquote>
The final code looks like this:

[python]
import re
from weakref import WeakKeyDictionary

EMAIL_REGEX = re.compile(
  r"[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@"
  "[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})"
)


def ValidateEmail(email_address):
    """Validates an email_address:
    
    Raises:
       ValueError: If the email is invalid.
    """
    if not EMAIL_REGEX.match(email_address):
        raise ValueError


class Email(object):
    """Descriptor class used to hold an email address."""
    
    def __init__(self):
        """Initialized the object.
        
        Attrs:
            pool: (WeakKeyDictionary) Maps object instance to a
            corresponding email address.
        """
        self.pool = WeakKeyDictionary()

    def __get__(self, instance, owner):
        """Called when the user is accessing a class level instance
        of type Email.
        
        For example assuming the following class:
        
            class Employee(object):
                email = Email()

        and an instance of it:
          
            employee = Employee()
        
        the following assigment
        
            x = employee.email
          
        will call this method.
        
        Args:
            instance: (python object) the python object having a class
            level attribute of type Email.
            
            owner: The type of the calling object.  Not used here.
        
        Returns:
            (string) The email as it exists in the pool. 
        """
        return self.pool.get(instance, 0)

    def __set__(self, instance, email_address):
        """Called when the user sets the value of a class level
        instance of type Email.
        
        For example assuming the following class:
        
            class Employee(object):
                email = Email()

        and an instance of it:
          
            employee = Employee()
        
        the following assigment
        
            employee.email = 'first.lastname@some_server.com'
          
        will call this method.
        
        Raises:
            ValueError: When passed an invalid email address
        
        Args:
            instance: (python object) the python object having a class
            level attribute of type Email.
            
            email_address: The value to assign.
        """
        if not EMAIL_REGEX.match(email_address):
            raise ValueError
        self.pool[instance] = email_address


class Employee(object):
    """Used to demo the use of descriptors."""
    
    personal_email = Email()
    work_email = Email()

    def __init__(self, name, personal_email, work_email):
        self.name = name
        self.personal_email = personal_email
        self.work_email = work_email

[/python]

Now if we run the code that caused the link before:

[python]
print 'Personal emails in memory: %d' % (
    len(Employee.__dict__['personal_email'].pool)
)   
CreateSomeEmployees()

print 'Personal emails in memory: %d' % (
    len(Employee.__dict__['personal_email'].pool)
)   
CreateSomeEmployees()

print 'Personal emails in memory: %d' % (
    len(Employee.__dict__['personal_email'].pool)
)   
[/python]

we are getting the following output:
<pre>Personal emails in memory: 0
Personal emails in memory: 0
Personal emails in memory: 0
</pre>
showing that the memory leaks have disappeared.

<h5>Lookup Chain for attribute retrieval</h5>

To understand how the descriptor is called, we need to know the binding sequence that is followed by python when an attribute name is dereferenced.  

The following code

[python]
the_obj = TheClass()
print the_obj.the_attribute_name
[/python]

creates and object of type <strong>TheClass</strong> with the name <strong>the_obj</strong>.


The second line retrieves the value of the attribute called name and prints it to the standard output; the syntax used is a syntactic sugar that hides the following chain of sequential lookup:

1. Start from the <strong>instance</strong> level.

If the object (<strong>the_obj</strong> in our example) has a entry with the name the_attribute_name in its __dict__ use this.  This means that if the following line of code is successful return it as the value of the attribute:

<pre>
the_obj.__dict__['the_attribute_name']
</pre>

If not, continue the lookup.

2. Continue the lookup using the type of the object (<strong>TheClass</strong> in our example).  Similarly to the previous step, if the following line of code is successful return it as the value of the attribute:

<pre>
type(the_obj).__dict__['the_attribute_name']
</pre>

3. If the attribute name is not resolved at this point, the lookup chain will continue searching all the parent classes (using the MRO sequence) for a matching attribute.

4. If the attribute was not found raise an exception.

<h5>Conclusion</h5>

Although python descriptors are not widely used by application developers, they consist a powerful mechanism that is used from library writers to achieve an elegant and easy to use way to create declarative and concise code.  Descriptors can become useful in any kind of interaction with a property of an object; they can centralize the interaction with the state of an object and share functionalities like data validation, logging or encapsulation improving the code reuse, maintainability and readability of the produced code.  Getting familiar and adopting the use of descriptors, not only enriched the arsenal of the programmer with a powerful technique but also increases the understanding of python and dynamic programming in general.

<hr>
