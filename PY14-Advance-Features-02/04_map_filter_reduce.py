# Map Example - run a single fuction for each element of a list

numbers = [1,2,3,4,5,6,7,8,9,10]

square = lambda x: x * x

sqList = map(square, numbers) # map(function, iterable)
print(list(sqList))

# Map with lambda

sqList = map(lambda x: x * x, numbers)
print(list(sqList))

# Filter Example - Keeps only elements for which function returns True

def even(n):
    return n % 2 == 0

even_nums = filter(even, numbers)
print(list(even_nums))

# Filter with lambda

even_nums = filter(lambda n: n % 2 == 0, numbers)
print(list(even_nums))

# Reduce Example  - Combines all elements of a list into a single value using a function

from functools import reduce

sum = reduce(lambda x, y: x + y, numbers) # reducing a list to sum of all elements 
print(sum)

# Using reduce to get max element from a list
max = reduce(lambda x, y: x if x > y else y, numbers)
print(max)

