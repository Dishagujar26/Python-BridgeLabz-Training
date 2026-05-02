# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter a number: "))

table_of_n = [n * i for i in range(1, 11)]   # list comprehension

with open("tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table_of_n)} \n")