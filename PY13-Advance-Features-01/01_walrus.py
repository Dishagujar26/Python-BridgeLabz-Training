# Walrus operator in python is :=
# It is used to assign values to variables as part of a larger expression
# It is only available in python 3.8 and above

if (n := len([1,2,3,4,5])) > 3 :
    print(f"List is too long ({n}) elements, expected 3 or less") 

# This is equivalent to
n = len([1,2,3,4,5])
if n > 3 :
    print(f"List is too long ({n}) elements, expected 3 or less")