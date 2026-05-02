# isinstance() is used to check whether an object belongs to a particular class/type.

a = 10
print(isinstance(a, int)) # True

b = "Hello"
print(isinstance(b, str)) # True

c = [1, 2, 3]
print(isinstance(c, list)) # True

d = (1, 2, 3)
print(isinstance(d, tuple)) # True

print(isinstance("hello", (int, float))) # False

# isinstance() with Union type hinting + enforcing strict type checking

from typing import Union

def show(value: Union[int | str | bool]) -> None: # new syntax | instead of , for Union
    if isinstance(value, Union[int, str, bool]):
        print(value)
    else:
        raise TypeError(f"Expected int, str or bool, but got {type(value)}")
        # raise is a keyword in Python that is used to manually raise an exception - stop execution and raise an error 
        # when Python executes that line, it creates an exception object and throws it.

show(10)
show("Hello")
show(True)

# show(3.14) # TypeError: Expected int, str or bool, but got float
# If you raise and don't catch it with try/except, program immediately stops (unless some outer caller catches it).

'''
raise ValueError("Wrong value")
raise TypeError("Wrong type")
raise KeyError("Key missing")
raise IndexError("Index out of range")
raise ZeroDivisionError("Cannot divide by zero") 

common built-in exceptions for error handling

'''

# Type() and isinstance() [runtine checker]

class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(type(d) == Dog)          # True
print(type(d) == Animal)       # False

print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True