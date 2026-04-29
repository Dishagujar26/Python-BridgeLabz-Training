name = "Disha Gujar  Girl"
# check if the string has double spaces
# if "  " in name: print("The string has double spaces")
# else: print("The string does not have double spaces")

print(name.find("  ")) # find() function is used to find the index of the first occurrence of a specific substring in the string

# if the find() function returns -1, it means that the substring is not found in the string or will return the index of the first occurrence of the substring in the string if it is found.
if name.find("  ") == -1: print("The string does not have double spaces")
else: print("The string has double spaces")