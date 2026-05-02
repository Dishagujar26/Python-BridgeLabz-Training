# List comprehensions - short way of creating a list 

list = [1,2,3,4,5]

squared_list = []

# for iteam in list:
#    squared_list.append(iteam * iteam)

# the above can be simplified using list comprehensions

squared_list = [iteam * iteam for iteam in list]
# [expression for item in iterable]
print(squared_list)

even = []

for i in list:
    if i % 2 == 0:
        even.append(i)

# the above can be simplified using list comprehensions

even = [i for i in list  if i % 2 == 0]
# [expression for item in iterable if condition]
print(even)

'''

[i for i in numbers if i % 2 == 0]
 ↑      ↑             ↑
store   loop         filter

'''