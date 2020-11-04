class Student(object):

    # @property decorator turns a method to an attribute
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must be between 0 -- 100")
        self.__score = value

s = Student()
s.score = 90 # normally score should be a method
print(s.score) # result: 90

class Person(object):

    # birth is modifiable because it has a setter
    @property # equivalent to a getter method
    def birth(self):
        return self.__birth

    @birth.setter # equivalent to a setter method
    def birth(self, value):
        self.__birth = value

    # age is only readable
    @property # equivalent to a getter method
    def age(self):
        return 2020 - self.__birth

m = Person()
m.birth = 1980
print(m.age) # result: 40


class Exam(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        # score now is only readable because no setter
        return self._score

e = Exam(90)
print(e.score)


# another example：
class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height
    
s = Screen()
s.width = 2
s.height = 5
print(s.width) # result: 2
print(s.height) # result: 5
print(s.resolution) # result: 10


# turn methods to attributes
class Foo(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    # the former is a getter method, the latter is a setter method
    x = property(getNum, setNum)

foo1 = Foo()
# if it's not set, just print the initial attribute
print(foo1.x) # result: 100
foo1.x = 50
print(foo1.x) # result: 50
