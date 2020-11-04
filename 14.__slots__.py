class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("tom", 27)
# Adding a new instance attribute is allowed anytime in a dynamic language like Python
p1.gender = "male"
print(p1.gender)


class Person(object):
    mood = "happy"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # put allowed instance attributes in this tuple or list, other attributes will be forbidden.
    # notice that slots only apply to current instance attributes, not class attributes or any subclass.
    __slots__ = ("name", "age")

p = Person("tom", 27)
print(p.name, p.age, p.mood)

try:
    p.addr = "munich"
except Exception as e:
    print(e)


# result:
# male
# tom 27 happy
# 'Person' object has no attribute 'addr'