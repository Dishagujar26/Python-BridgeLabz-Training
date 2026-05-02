#  4. Write a program to filter a list of numbers which are divisible by 5.

number = [1,2,3,4,5,6,7,8,9,10]

num = list(filter(lambda x: x%5 == 0, number))
print(num)