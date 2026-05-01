# Method Overloading means: same method name, but works
# differently depending on the NUMBER of arguments passed.
#
# Python does NOT support overloading natively.
# We simulate it using DEFAULT PARAMETER VALUES.


class Calculator:

    def add(self, a, b=0, c=0):
        # b and c have default values of 0. So the caller can pass 1, 2, or 3 arguments.
        # Python will use 0 for any argument not provided. This simulates method overloading.
        result = a + b + c
        print(f"Result = {result}")


calc = Calculator()

calc.add(5)           # → Result = 5    (only a is passed, b=0, c=0)
calc.add(5, 3)        # → Result = 8    (a and b passed, c=0)
calc.add(5, 3, 2)     # → Result = 10   (all three passed)

# KEY POINT:
# Same method 'add()' handles 1, 2, or 3 arguments.
# This is how Python SIMULATES method overloading.
# The method name stays the same, behavior changes with input.