
# Strings are immutable, which means that they cannot be changed after they have been created.
# However, we can create a new string by slicing the original string.

name = "Harry Potter"

print(len(name)) # len() function is used to get the length of the string
print(name.endswith("Potter")) # endswith() function is used to check if the string ends with a specific substring
print(name.startswith("Harry")) # startswith() function is used to check if the string starts with a specific substring
print(name.count("r")) # count() function is used to count the number of occurrences of specific substring in the string
print(name.capitalize()) # capitalize() function is used to capitalize the first character of the string
print(name.find("Potter")) # find() function is used to find the index of the first occurrence of a specific substring in the string
print(name.lower()) # lower() function is used to convert the string to lowercase
print(name.upper()) # upper() function is used to convert the string to uppercase

print(name.replace("Harry", "Ron")) # replace() function is used to replace a specific substring with another substring in the string
print(name) # the original string is not changed because strings are immutable
print(name.replace("Harry", "Ron")) # the replace() function returns a new string with the specified substring replaced, but does not change the original string
print(name.title()) # title() function is used to convert the first character of each word in the string to uppercase and the rest to lowercase
print(name.strip()) # strip() function is used to remove any leading and trailing whitespace from the string


# Slicing is the process of extracting a portion of a string by specifying the start and end indices.
# The syntax for slicing is: string[start:end:step]
# start is the index of the first character to be included in the slice (inclusive)
# end is the index of the first character to be excluded from the slice (exclusive)


nameshort = name[0:5] # starts at 0 and ends at 5 but does not include 5    
print(nameshort)

character = name[0] # starts at 0 and ends at 1 but does not include 1
print(character)

print(name[0:5:2]) # starts at 0 and ends at 5 but does not include 5 and takes every second character
print(name[::2]) # starts at 0 and ends at the end of the string and takes every second character
print(name[1:5:2]) # starts at 1 and ends at 5 but does not include 5 and takes every second character
print(name[1:5]) # starts at 1 and ends at 5 but does not include 5
print(name[1:]) # starts at 1 and ends at the end of the string
print(name[:5]) # starts at the beginning of the string and ends at 5 but does not include 5
print(name[:]) # starts at the beginning of the string and ends at the end of the string

print(name[-1]) # starts at the end of the string and ends at the end of the string
print(name[-5:]) # starts at the end of the string and ends at the end of the string
print(name[:-5]) # starts at the beginning of the string and ends at the end of string but does not include the last 5 characters

print(name[-5:-1]) # starts at the end of the string and end at the end of the string but does not include the last character

print(name[-5:-2]) # starts at the end of the string and ends at the
