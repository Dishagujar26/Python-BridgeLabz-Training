# enumerate() in Python is used when you want both index and value while looping.
# It returns an enumerate object, which is an iterator that contains tuples of index and value - pairs in the form (index, value).

my_list = ["apple", "banana", "cherry", "date", "elderberry"]

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# By default indexing starts at 0, but can be changed using start parameter.

for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")

# With the enumerate function manually we would have to do like this 

for i in range(len(my_list)):
    print(f"Index: {i}, Value: {my_list[i]}")