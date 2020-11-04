# inherit from int but define a customised class
class My_int(int):
    def __new__(cls, *args, **kwargs):
        print("__new__ method")
        return super().__new__(cls, abs(*args))


# customised class
print(My_int(-1))
# same result as built-in function abs()
print(abs(-1))
# built-in function int()
print(int(-1))

# result
# __new__ method
# 1
# 1
# -1