n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))
n5 = int(input("Enter the fifth number: "))
n6 = int(input("Enter the sixth number: "))

my_marks_tuple = (n1, n2, n3, n4, n5, n6)
print(my_marks_tuple)

print("The highest mark is:", max(my_marks_tuple))
print("The lowest mark is:", min(my_marks_tuple))
print("The average mark is:", sum(my_marks_tuple) / len(my_marks_tuple))

print("The number of marks entered is:", len(my_marks_tuple))
print("The marks in sorted order are:", sorted(my_marks_tuple))