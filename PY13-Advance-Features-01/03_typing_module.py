# typing module in python - Python's typing module provides more advanced type hints, such as List, Tuple, Dict, set and Union.

from typing import List, Tuple, Dict, Set, Union

# unlike before now you can create list, tuple other stuff by declaring their type as well 

n : List[int] = [1,2,3,4,5]

n : Tuple[int] = (1,2,3,4,5)

n : Dict[str, int] = {"a": 1, "b": 2, "c": 3}

n : Set[int] = {1, 2, 3, 4, 5}

n : Union[int, str] = 1 # a variable / parameter can accept multiple types at the same time

number: Union[int, float] = 10 # here we are declaring that number can be an int or a float
print(number)

number = 10.5 # now number is a float
print(number)

number = 10 # now number is int
print(number)


# function accepts multiple types
def display(value: Union[int, str, bool]) -> None: # decalaring that this function accepts int, str and bool 
    # if we pass values of type other then these it will still run Because Union is a type hint, not strict enforcement in Python.
    print(value)

display(100)
display("Python")
display(True)
display(3.14) # no error will still run 

# Union with return type 

from typing import Union

def divide(a: int, b: int) -> Union[float, str]:
    if b == 0:
        return "Cannot divide"
    return a / b