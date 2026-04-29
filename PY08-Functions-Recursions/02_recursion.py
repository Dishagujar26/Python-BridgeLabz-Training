
# Recursion is a function that calls itself.
# Recursion is a useful tool for solving problems that can be broken down into smaller subproblems.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5)) 

# How does recursion work?
# The function calls itself until it reaches the base case.
# The base case is the condition when the function stops calling itself.


