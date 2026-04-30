# Decorator in Python = a function that wraps another function to add extra behavior without changing the original function code.
# Built-in decorators -> provided by Python
# Examples: @staticmethod, @classmethod, @property

# Custom decorators -> created by programmer
# Example: @decorator

# decorator function - custom decorator function
def decorator(func):

    # wrapper function
    def wrapper():
        print("Starting...")   # before original function

        func()                 # original function call

        print("Finished...")   # after original function

    return wrapper


# apply decorator
@decorator
def greet():
    print("Hello World")


greet()

'''
greet()
 ↓
wrapper()
 ↓
Starting...
 ↓
original greet()
 ↓
Hello World
 ↓
Finished...

'''