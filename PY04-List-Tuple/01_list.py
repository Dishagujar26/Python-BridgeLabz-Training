# list in python is a collection which is ordered and changeable. Allows duplicate members.
# list is defined by having values between square brackets [ ].
# creating a list

my_list = [1, 2, 3, 4, 5]
print(my_list)

# creating a list with different data types
my_list2 = [1, "Hello", 3.14, True]
print(my_list2)

# accessing list items
print(my_list[0])  # output: 1
print(my_list[1])  # output: 2

# changing list items
my_list[0] = 10
print(my_list)  # output: [10, 2, 3, 4, 5]

# adding items to a list
my_list.append(6)
print(my_list)  # output: [10, 2, 3, 4, 5, 6]

# inserting items to a list at a specific position
my_list.insert(1, 15)           
print(my_list)  # output: [10, 15, 2, 3, 4, 5, 6]

# removing items from a list
my_list.remove(15)
print(my_list)  # output: [10, 2, 3, 4, 5, 6]

print(my_list.pop(0))  # removes the item at index 0 and returns it, output: 10
print(my_list)  # output: [2, 3, 4, 5, 6]

my_list.clear()  # removes all items from the list
print(my_list)  # output: []    

# Slicing of Lists
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # output: [2, 3, 4]
print(my_list[:3])   # output: [1, 2, 3]
print(my_list[2:])   # output: [3, 4, 5
print(my_list[-3:])  # output: [3, 4, 5]

# Sorintg of Lists
my_list = [5, 2, 3, 1, 4]
print(my_list)  # output: [5, 2, 3, 1, 4]
my_list.sort()  # sorts the list in ascending order
print(my_list)  # output: [1, 2, 3, 4, 5]

# Reversing a List
my_list.reverse()  # reverses the order of the list
print(my_list)  # output: [5, 4, 3, 2, 1]


# comapare lists and string in python how are they different from each other
# lists are mutable, meaning they can be changed after they are created, while strings are immutable, meaning they cannot be changed after they are created.
# lists can contain multiple data types, while strings can only contain characters. 

list1 = [1, 2, 3]   
list2 = [1, 2, 3]
print(list1 == list2)  # output: True

string1 = "Hello"
string2 = "Hello"
print(string1 == string2)  # output: True

# lists can be nested, meaning they can contain other lists as items, while strings cannot be nested.
nested_list = [1, 2, [3, 4], 5]
print(nested_list)  # output: [1, 2, [3, 4], 5]

# lists have more built-in methods for manipulating the data, while strings have fewer built-in methods.
my_list = [1, 2, 3]
my_list.append(4)  # adds an item to the end of the list
print(my_list)  # output: [1, 2, 3, 4
my_string = "Hello"
print(my_string.upper())  # converts the string to uppercase, output: "HELLO"

# lists can be used to store and manipulate collections of data, while strings are used to store and manipulate text.
my_list = [1, 2, 3, 4, 5]
print(my_list)  # output: [1, 2, 3, 4
my_string = "Hello, World!"
print(my_string)  # output: "Hello, World!"







