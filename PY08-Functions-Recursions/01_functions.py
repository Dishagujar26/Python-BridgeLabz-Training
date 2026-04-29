# what is a function in python ? 

# a function is a block of code that is used to perform a specific task.
# a function can be called by using its name followed by parentheses.
# a function can also accept arguments, which are values that are passed to the function when it is called.
# a function can also return a value, which is the value that is returned by the function when it is called.

# syntax
# def function_name(parameters):
#     statement(s)

# example   

def add(a, b):  
    return a + b

print(add(2, 3))

# average function 
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    return (a + b + c) / 3

# calling a function is the same as calling a variable
print(avg)

#  Write a program to greet a user with “Good day” using functions. 
def greet():
    print("Good day")

# mutiple calls of the same function
greet()
greet()

# Tpes of function in python
# 1. Built-in functions - functions that are built into python such as print(), input(), len(), etc.
# 2. User-defined functions - functions that are defined by the user for example add(), avg(), greet() etc.

# fucntions with parameters 
def add(a, b):
    return a + b

print(add(2, 3))

# fucntions with default parameters
def add(a, b=10):
    return a + b

print(add(2)) # value for a is passed and value for b is default
print(add(2, 3)) # value for a is passed and value for b is passed, the default value is ignored

# fucntions with variable length arguments
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))

# fucntions with keyword arguments
def add(**kwargs):
    print(kwargs) # output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print(type(kwargs)) # output: <class 'dict'>
    print(kwargs.values()) # output: dict_values([1, 2, 3, 4, 5])
    return sum(kwargs.values())

print(add(a=1, b=2, c=3, d=4, e=5))




