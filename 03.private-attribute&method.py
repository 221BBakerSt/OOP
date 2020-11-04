class Father:
    def __init__(self):
        self.x = 50
        self.__y = 100

    def good(self):
        print("good")

    def __bad(self):
        print("bad")

    def foo(self):
        self.__bad()
        print(self.__y)

class Son(Father):
    def bar(self):
        self.__bad()
        print(self.__y)

boy = Son()

boy.good()
try:
    boy.__bad()
except Exception as e:
    # private methods won't be inherited
    print(e)
print("-------------")

print(boy.x)
try:
    print(boy.right)
except Exception as e:
    # private attributes won't be inherited
    print(e)
print("-------------")

try:
    boy.bar()
except Exception as e:
    # methods of child class can't call private methods or attributes of parent class
    print(e)

print("-------------")
# Public methods A from parent class called private methods or attributes of parent class.
# Methods of child class are able to call method A to get private methods or attributes from parent class
boy.foo()


# result:
# good
# 'Son' object has no attribute '__bad'
# -------------
# 50
# 'Son' object has no attribute 'right'
# -------------
# 'Son' object has no attribute '_Son__bad'
# -------------
# bad
# 100