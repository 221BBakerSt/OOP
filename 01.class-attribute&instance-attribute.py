class Tool(object):

    # class attributes are available for all instances
    num = 0

    # instance method
    def __init__(self, name):
        # instance attribute
        self.name = name
        # operate class attribute
        Tool.num += 1

tool1 = Tool("chrome")
tool2 = Tool("safari")
tool3 = Tool("firefox")

print(Tool.num) # result: 3