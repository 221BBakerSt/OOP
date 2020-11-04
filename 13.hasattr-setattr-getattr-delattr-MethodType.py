class Person(object):
    class_attr = 10

    def __init__(self):
        self.instance_attr = 20

    def think(self):
        pass


tom = Person()
# equivalent to print(tom.class_attr)
print(getattr(tom, "class_attr"))

# equivalent to print(tom.instance_attr)
print(getattr(tom, "instance_attr"))

# set a new class attribute, equivalent to Person.age = 30
setattr(Person, "age", 30)

# set a new instance attribute, equivalent to tom.score = 40
setattr(tom, "score", 40)

# equivalent to print(Person.age)
print(getattr(Person, "age"))

# equivalent to print(tom.score)
print(getattr(tom, "score"))

# instance tom also has attribute age in class Person
print(hasattr(tom, "age"))

# class Person doesn't have attribute score, which belongs to instance tom
print(hasattr(Person, "score"))

# delete class attribute age
delattr(Person, "age")

# both class Person and instance tom don't have attribute age now
print(hasattr(tom, "age"))

# get attribute salary from instance tom, if it doesn't exist, set this attribute
getattr(tom, "salary", setattr(tom, "salary", 50))
print(tom.salary)

def talk(self):
    """
    define a function and bind it to an instance's method
    """
    return f"{self} talks"

from types import MethodType
# MethodType(function, instance)
tom.talk = MethodType(talk, tom)

# instance tom now has this method, but Person doesn't.
print(hasattr(Person, "talk"))
print(hasattr(tom, "talk"))
print(tom.talk())

# dict of all attributes of class Person
print(Person.__dict__)

# dict of all attributes of instance tom
print(tom.__dict__)


# result:
# 10
# 20
# 30
# 40
# True
# False
# False
# 50
# False
# True
# <__main__.Person object at 0x10b571ad0> talks
# {'__module__': '__main__', 'class_attr': 10, '__init__': <function Person.__init__ at 0x10b51f320>, 'think': <function Person.think at 0x10b505b00>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
# {'instance_attr': 20, 'score': 40, 'salary': 50, 'talk': <bound method talk of <__main__.Person object at 0x10b571ad0>>}
