# Lambda in python is a function in a expression format

# lambda arguments: expression

# def double(x):
#     return x * x

double = lambda x: x * x
print(double(2))

# Lambda with three argument

sum = lambda a,b,c : a+b+c
print(sum(1,2,3)) # 6

# Lambda with multiple arguments

sum = lambda *args: sum(args)
print(sum(1,2,3,4,5))

# Conditional Lambda

even_or_odd = lambda n: "Even" if n % 2 == 0 else "Odd"

print(even_or_odd(10))
print(even_or_odd(7))

# Lambda with filter()

numbers = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda n: n % 2 == 0, numbers))
print(even)

# Lambda with map()

numbers = [1,2,3,4,5,6,7,8,9,10]

squared = list(map(lambda n: n * n, numbers))
print(squared)

# lambda returning boolean 

is_positive = lambda n: n > 0

print(is_positive(5))
print(is_positive(-2))

# lambda inside fucntion 

def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# using with sorted 

students = [
    ("Disha", 90),
    ("Rahul", 80),
    ("Ankit", 95)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)