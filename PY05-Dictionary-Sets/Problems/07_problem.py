# List conatined in a set

my_set = {8, 7, 12, "Harry", [1, 2, 3]}  # this will raise a TypeError because lists are mutable and cannot be added to a set
print(my_set)  # Output: {8, 7, 12, 'Harry'}

# The error occurs because sets in Python can only contain immutable (unchangeable) data types. 
# Lists are mutable, meaning they can be modified after they are created (e.g., you can add or remove elements from a list). 
# Since sets require their elements to be hashable (which is a property of immutable types), trying to add a list to a set will raise a TypeError. 
# In this case, the list [1, 2, 3] cannot be added to the set, resulting in the error.
