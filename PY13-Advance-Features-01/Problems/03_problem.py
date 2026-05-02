#  Write a list comprehension to print a list which contains the multiplication table of a
#  user entered number.

n = int(input("Enter a number: "))

table_of_n = (n * i for i in range(1,11))
print(list(table_of_n)) # have to convert it to a list as have not use [] braces

