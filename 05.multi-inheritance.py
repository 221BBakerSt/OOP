# object is the superclass of all classes in python3
class Father(object):
    def __init__(self, age):
        self.age = age

    def test(self):
        print("test")

class Son(Father):
    def test1(self):
        print("test1")

class Daughter(Father):
    def test2(self):
        print("test2")

# Multi-Inheritance
class Grandson(Son, Daughter):
    def test3(self):
        # first way to call methods in superclass
        Father.test(self)
        # second way to call methods in superclass
        super().test()
        # third way to call methods in superclass
        super(Grandson, self).test()

tom = Grandson(2)
tom.test()
tom.test1()
tom.test2()
tom.test3()

# show the priority/order of inheritance, when methods/attributes of subclass overrides those of superclass
print(Grandson.__mro__)

# whether the former is an instance of the latter
print(isinstance(tom, Grandson))
# whether the former is a subclass of the latter
print(issubclass(Father, Son))


# result:
# test
# test1
# test2
# test
# test
# test
# (<class '__main__.Grandson'>, <class '__main__.Son'>, <class '__main__.Daughter'>, <class '__main__.Father'>, <class 'object'>)
# True
# False