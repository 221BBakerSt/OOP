class Item:
    def __del__(self):
        print("Item is over")


class Animal(object):

    def __init__(self, name):
        # initialisation method, will be called automatically when an object is created
        print("__init__ is called")
        self.__name = name

    def __del__(self):
        # descruction method, will be called automatically when an objected is deleted
        print(f"{self.__name} is about to be deleted")


if __name__ == "__main__":
    item1 = Item()
    item2 = item1
    
    del item1
    # since only item1 is deleted, __del__ method won't be called until all related objects are deleted
    # when the whole process ends, __del__ will be called
    # del item2 # if item2 is also deleted, __del__ will immediately be called
    print("-----------------")

    dog = Animal("Milou")
    # delete the object dog
    del dog

    cat = Animal("Tom")
    cat2 = cat
    cat3 = cat

    print("deleting cat2 now")
    del cat2
    print("deleting cat3 now")
    del cat3
    # since cat still exists, __del__won't be called until the 
    # process ends, when python interpreter clears the memory and cat is killed
    print("the process is ending soon!")


# result:
# -----------------
# __init__ is called
# Milou is about to be deleted
# __init__ is called
# deleting cat2 now
# deleting cat3 now
# the process is ending soon!
# Item is over
# Tom is about to be deleted