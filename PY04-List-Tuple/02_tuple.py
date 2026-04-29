# list and tuple are both data structures in Python that can store multiple items. However, there are some key differences between them:
# 1. Mutability: Lists are mutable, meaning they can be modified after they are created, while tuples are immutable, meaning they cannot be modified after they are created.
# 2. Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses
# 3. Performance: Tuples are generally faster than lists because they are immutable and have a smaller memory footprint.

# creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# creating a tuple with different data types
my_tuple2 = (1, "Hello", 3.14, True)
print(my_tuple2)

# accessing tuple items
print(my_tuple[0])  # output: 1
print(my_tuple[1])  # output: 2

# changing tuple items (this will raise an error because tuples are immutable)
my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# adding items to a tuple (this will raise an error because tuples are immutable)
my_tuple.append(6)  # AttributeError: 'tuple' object has no attribute 'append'

# inserting items to a tuple at a specific position (this will raise an error because tuples are immutable)
my_tuple.insert(1, 15)  # AttributeError: 'tuple' object has no attribute 'insert'

# removing items from a tuple (this will raise an error because tuples are immutable)           
my_tuple.remove(15)  # AttributeError: 'tuple' object has no attribute 'remove'

# slicing of tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # output: (2, 3, 4)
print(my_tuple[:3])   # output: (1, 2, 3)
print(my_tuple[2:])   # output: (3, 4, 5)
print(my_tuple[-3:])  # output: (3, 4, 5)

# Tuple of single element 
my_tuple = (1,)  # note the comma after the single element
print(my_tuple)  # output: (1,)

# Tuple and string comparison
# Tuples can contain multiple data types, while strings can only contain characters.    
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(tuple1 == tuple2)  # output: True
string1 = "Hello"
string2 = "Hello"
print(string1 == string2)  # output: True

# methods available for tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(2))  # output: 1 (counts the number of occurrences of the value 2 in the tuple)
print(my_tuple.index(3))  # output: 2 (returns the index of the first occurrence of the value 3 in the tuple

# len() - returns the number of items in the tuple
print(len(my_tuple))  # output: 5
# max() - returns the largest item in the tuple
print(max(my_tuple))  # output: 5
# min() - returns the smallest item in the tuple
print(min(my_tuple))  # output: 1


# Unpacking of tuples 
my_tuple = (1, 2, 3)
a, b, c = my_tuple  # unpacking the tuple into individual variables
print(a)  # output: 1
print(b)  # output: 2
print(c)  # output: 3

