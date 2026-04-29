 
# set is a collection which is unordered, unchangeable*, and unindexed.
# set is defined by using curly braces {} or the set() function.
# example of a set

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4
len(my_set)  # Output: 5

# adding an element to a set
my_set.add(6)
my_set.update({6})  # this will also add the element 6 to the set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# clear a set
my_set.clear()
my_set = set()  # this will also create an empty set
print(my_set)  # Output: set()
my_set = {1, 2, 3, 4, 5}

# copy a set
my_set_copy = my_set.copy()
print(my_set_copy)  # Output: {1, 2, 3, 4, 5}

# removing an element from a set
my_set.remove(3)
my_set.discard(3)  # this will also remove the element 3 from the set if it exists, otherwise it will do nothing
my_set.pop()  # this will remove and return an arbitrary element from the set, but since sets are unordered, we cannot predict which element will be removed
my_set.pop(3)  # this will also remove the element 3 from the set if it exists, otherwise it will do nothing
print(my_set)  # Output: {1, 2, 4, 5, 6}

# checking if an element is in a set    
print(4 in my_set)  # Output: True
print(3 in my_set)  # Output: False

# looping through a set
for element in my_set:
    print(element)  # Output: 1, 2, 4, 5, 6

# set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union of two sets
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}
print(my_set.union(set2))  # this will also return the union of set1 and set2

# intersection of two sets  
print(set1 & set2)  # Output: {3}
print(my_set.intersection(set2))  # this will also return the intersection of set1 and set2

# difference of two sets
print(set1 - set2)  # Output: {1, 2}
print(my_set.difference(set2))  # this will also return the difference of set1 and set2

# symmetric difference of two sets          
print(set1 ^ set2)  # Output: {1, 2, 4, 5}  
print(my_set.symmetric_difference(set2))  # this will also return the symmetric difference of set1 and set2



