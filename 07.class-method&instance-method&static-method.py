class Person(object):

    # class attribute is available for all class objects and instance objects
    age = 0
    name = "Jack"
    
    # instance method
    def __init__(self):
        # self.age is an instance attribute, only available for instance object
        self.age = 10

    # class method differs from instance method in: decorator @classmethod, and self becomes cls, pointing to the reference of the class
    @classmethod
    def add_age(cls, new_age):
        cls.age = new_age # class method can only be called by the class

    # static method has nothing to do with the class or instance, but is able to be called by both.
    # static method has decorator @staticmethod and doesn't need self or cls. It aims to execute basic function.
    @staticmethod
    def my_staticmethod():
        print("my static method")


person1 = Person()
# if class attribute and instance attribute both include this attribute, call it from instance attribute
print(person1.age)
# if instance attribute doesn't include this attribute, then call it from class attribute
print(person1.name)

# instance attributes are unavailable for classes, so call from class attribute
print(Person.age)
print(Person.name)
print("---------------")

# both the class and the instance are able to call class method and modify class attribute
Person.add_age(20)
print(Person.age)

person1.add_age(30)
print(Person.age)
# class attribute was modified, not instance attribute
print(person1.age)

print("---------------")
# static method called by the class object
Person.my_staticmethod()
# static method called by the instance object
person1.my_staticmethod()

"""
operate class attributes/methods with class objects;
operate instance attributes/methods with instance objects;
finish basic functions with static methods.
"""
# add an extra class method:
@classmethod
def extra_cls_method(cls):
    print("this is an extra class method")

# add an extra static method:
@staticmethod
def extra_stc_method():
    print("this is an extra static method")

# bind to Person
Person.extra_cls_method = extra_cls_method
Person.extra_stc_method = extra_stc_method
# call them with the class object
Person.extra_cls_method()
Person.extra_stc_method()
# call them with the instance object
person1.extra_cls_method()
person1.extra_stc_method()


# result:
# 10
# Jack
# 0
# Jack
# ---------------
# 20
# 30
# 10
# ---------------
# my static method
# my static method
# this is an extra class method
# this is an extra static method
# this is an extra class method
# this is an extra static method