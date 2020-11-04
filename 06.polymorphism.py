class Person(object):
    def hello(self):
        print("hello person")

class Man(Person):
    def hello(self):
        print("hello man")

def say_hello(person):
    person.hello()

a = Person()
b = Man()

# Encapsulation, inheritance, and polymorphism are the 3 main characteristics of OOP!

# Collecting multiple functions and variables, public or private, in a box called class.
# Public parts are accessible and private parts are inaccessible from outside. This is encapsulation.

"""
When we hit "ctrl + c":
In an editor, it means copy.
In a terminal, it means abort the current task.
The same event happening to different objects leads to different result.
"""

say_hello(a) # result: hello person
say_hello(b) # result: hello man
"""
Polymorphism is different operations with different instances with the same interface.
When defining a calling function, we are unsure which method will be called, from superclass or subclass, until runtime.
When a subclass is added, we only need to make sure the outside calling function is correct, and don't care how it is called.

It complies with "open-closed principle": open for extension, but closed for modification.
Open for extending new subclasses, but closed for modifying methods in base class.

For dynamic programming language like Python, it's not a must to pass a subclass of the base class to the outside calling function.
We only need to make sure we pass an object with the same interface. In this case, the interface is hello() method.
"""
