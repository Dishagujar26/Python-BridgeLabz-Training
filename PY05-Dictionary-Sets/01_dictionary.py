# dictionary is a collection of key value pairs 
# it is unordered, mutable and indexed
# it is defined by using curly braces {}    
# example of a dictionary

# advantages of dictionary comapre with list
# 1. faster lookups: dictionaries use a hash table to store key-value pairs,
#    which allows for faster lookups compared to lists, which require a linear search.
# 2. more efficient memory usage: dictionaries can be more memory efficient than lists,
#    especially when storing large amounts of data, as they only store the keys and values that are actually used.

my_dict = { "name": "John", 
            "age": 30, 
            "city": "New York" }
print(my_dict)   

len(my_dict)  # Output: 3

# accessing values in a dictionary
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30

# below tow lines will give the same output but the second one is more safe because if we try to access a key that does not exist in the dictionary, it will return None instead of raising a KeyError
print(my_dict["city"])  # Output: New York
print(my_dict.get("city"))  # Output: New York

# adding a new key-value pair to the dictionary
my_dict["country"] = "USA"
my_dict.add({"country": "USA"})  # this will also add the key-value pair with key "country" and value "USA" to the dictionary
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

# updating a value in the dictionary
my_dict["age"] = 31
my_dict.update({"age": 31})  # this will also update the value of age to 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# removing a key-value pair from the dictionary
del my_dict["city"]
my_dict.pop("city", None)  # this will also remove the key-value pair with key "city" if it exists, otherwise it will do nothing
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

#----------------------------------------------------------------------------------------

# looping through a dictionary
for key in my_dict:
    print(key, my_dict[key])  # Output: name John, age 31, country USA

# using the items() method to loop through a dictionary
for key, value in my_dict.items():
    print(key, value)  # Output: name John, age 31, country USA

# using the keys() method to loop through a dictionary
for key in my_dict.keys():
    print(key)  # Output: name, age, country

# using the values() method to loop through a dictionary
for value in my_dict.values():
    print(value)  # Output: John, 31, USA

#----------------------------------------------------------------------------------------

# checking if a key exists in the dictionary
if "name" in my_dict:
    print("Name exists in the dictionary")  # Output: Name exists in the dictionary

# checking if a value exists in the dictionary
if "John" in my_dict.values():
    print("John exists in the dictionary")  # Output: John exists in the dictionary

# clearing all key-value pairs from the dictionary
my_dict.clear()
my_dict = {}  # this will also clear all key-value pairs from the dictionary
print(my_dict)  # Output: {}


