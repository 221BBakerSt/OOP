class Person(object):
    def __new__(cls):  # cls refers to the child class of its parent class, namely Person itself
        # __new__ is about the class, other magic methods are about instances
        # it controls the instantiation of a class
        print("__new__ method")
        print("id of new class: ", id(cls))
        print("---------__new__ start--------")
        # this will be the returned value, now print it to check
        print(super(Person, cls).__new__(cls))
        print("---------__new__ over---------")
        return super(Person, cls).__new__(cls)

    def __init__(self):
        # initialisation happens after instantiation (the class creation) finishes
        print("__init__ method")

    def __del__(self):
        print("__del__ method")

    def __str__(self):
        print("__str__ method")
        return "description of this object for users"

    def __repr__(self):
        # if __str__ already exists, __repr__ won't be called
        print("__repr__ method")
        return "description of this object for developers"


if __name__ == "__main__":
    student = Person()
    """
    Three things happened in this class creation process:
    1. call __new__ method: to create the class object, and return the reference of this created class object
        since we printed it, we are able to see what it returns
    2. call __init__(self): to initialise, self is the reference of this created class objected
    3. value pass: the return value of object.__new__(cls) (what we just checked in line 8) is passed to the variable student.
    """
    print("--------------")
    print("id of Person class: ", id(Person))
    print("id of student instance: ", id(student))
    print("---------start--------")
    # Notice if we print student, the result is exactly the same as we print(object.__new__(cls)) in line 8,
    # which proves student is just a variable to store the returned value during class object creation.
    print(student)
    print("---------over---------")
    # __del__ certainly will be called when the whole process ends


# result:
# __new__ method
# id of new class:  140305633558384
# ---------__new__ start--------
# __str__ method
# description of this object for users
# __del__ method
# ---------__new__ over---------
# __init__ method
# --------------
# id of Person class:  140305633558384
# id of student instance:  4401994448
# ---------start--------
# __str__ method
# description of this object for users
# ---------over---------
# __del__ method