emp_dict = {} # empty dictionary

# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite programming language: ")
    emp_dict[name] = language

print(emp_dict)


# if the key is same then the value will be updated with the new value. For example, if we enter the same name again with a different language, then the value of that name will be updated with the new language.
# we can have same values 