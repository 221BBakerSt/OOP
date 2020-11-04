class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"Student: {self.name}, {self.gender}."

class Student(Person):
    # override the parent __init__ method
    def __init__(self, name, gender, score):
        # call parent method
        super(Student, self).__init__(name, gender)
        # override parent method
        self.score = score

    # __str__() and __repr__() are both built-in functions
    # __str__() is to show to users，while __repr__() is to show to developers
    def __repr__(self):
        # self.score is int type and can't be returned, so must be transformed to a str
        return f"{self.score}"
    # for simplicity, we can just define: __repr__ = __str__


if __name__ == "__main__":
    a = Student("Tom", "male", 90)
    print(a, type(a))
    print(str(a), type(str(a)))
    # print(a) and print(str(a)) has the same result for they both call __str__ method
    # But actually the results are different if comparing type(a) and type(str(a))
    print(a == str(a)) # result: False
    """
    when printing a class, it first considers print its own __str__ return value
    if not defined, it then prints __str__ return value of its parent class
    if its parent class doesn't define a __str__ return value, then it prints __repr__ return value of its own
    if still not defined, then print __repr__ return value of its parent class
    """
    # try commenting line 6 and 7
    # the general principle is first consider __str__, then its parent's. Then consider __repr__, finally its parent's __repr__
    print(repr(a)) # if printing __repr__ directly, it only cares __repr__. __str__ won't be involved
    print(repr(a) == a.__repr__()) # True, they are the same thing


# result
# Student: Tom, male. <class '__main__.Student'>
# Student: Tom, male. <class 'str'>
# False
# 90
# True