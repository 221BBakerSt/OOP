def func_a():
    return "this is function a"

def func_b():
    return "this is function b"

def func_c():
    return "this is function c"

def switch_case(value):
    # create a dictionary mapping case values to functions to call
    case = {"a": func_a,
            "b": func_b,
            "c": func_c}
    return case.get(value, func_c)


value = "b"
func = switch_case(value)
print(func())

print("-----------------------------")

class Switch(object):

    def visit_a(self):
        print("this is function a")

    def visit_b(self):
        print("this is function b")

    def dispatch(self, value):
        """
        Without a prefix like visit_, if values are coming from an untrusted source, 
        an attacker would be able to call any method in the class.
        """
        method_name = "visit_" + str(value)
        # get object's attribute
        method = getattr(self, method_name)
        method()

obj = Switch()
obj.dispatch("a")

# result:
# this is function b
# -----------------------------
# this is function a