class Woman:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        # create a method to call attributes if it satisfies some conditions
        if self.age < 40:
            return self.age
        else:
            return "It is a secret!"


susan = Woman(35)
print(susan.get_age())
# so we don't call susan.age directly to protect this attribute
# but if we want, the attribute is still accessible
print(susan.age)

lisa = Woman(42)
print(lisa.get_age())
print(lisa.age)
print("------------")

class Woman:
    def __init__(self, age):
        self.__age = age

    def __ask(self):
        # create a private method to call private attributes
        if self.__age < 40:
            return self.__age
        else:
            return "It is a secret!"

    def age(self):
        # create a public method to call private method
        return self.__ask()


susan = Woman(42)
print(susan.age())
# private attributes won't be shown directly
print(susan.age)
try:
    print(susan.__age)
except Exception as e:
    print("Exception: ", e)

# force to visit private method
print(susan._Woman__ask())
# force to visit private attribute
print(susan._Woman__age)
#_Class__object is called "name mangling"，
# to prevent subclass from accidently overriding private methods or attributes of its superclass


# result:
# 35
# 35
# It is a secret!
# 42
# ------------
# It is a secret!
# <bound method Woman.age of <__main__.Woman object at 0x10dfd78d0>>
# Exception:  'Woman' object has no attribute '__age'
# It is a secret!
# 42