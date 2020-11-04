class Animal(object):
    def eat(self):
        print("EAT")
    def drink(self):
        print("DRINK")
    def sleep(self):
        print("SLEEP")

# inherit superclass Animal
class Dog(Animal):
    def bark(self):
        print("BARK")

# inherit superclass Dog
class Snoopy(Dog):
    def talk(self):
        print("TALK")

    def bark(self):
        # override means redefine the methods in superclass. in this case, change bark to shout
        print("SHOUT")
        # first way to call methods from superclass
        Dog.bark(self)
        # second way to call methods from superclass
        super().bark()
        # third way to call methods from superclass
        super(Snoopy, self).bark()

    # delete a method from superclass
    # del Dog.bark

x = Snoopy()
x.eat()
x.talk()
print("-----")
x.bark()

# result:
# EAT
# TALK
# -----
# SHOUT
# BARK
# BARK
# BARK
