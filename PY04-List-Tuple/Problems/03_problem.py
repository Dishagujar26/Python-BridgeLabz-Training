# check that a type can not be changed in python
my_string = "Hello"

print(my_string)  # output: Hello
my_string[0] = "h"  # TypeError: 'str' object does not support item assignment
