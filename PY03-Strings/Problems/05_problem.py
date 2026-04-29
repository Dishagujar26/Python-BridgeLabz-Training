# Format the string using the format() function

position = "Software Engineer"
name = "Disha"
salary = "100000"
letter = "Dear {},\nYou are selected!\n{} is the position you have been selected for.\n{} is the salary you will be receiving.\nHave a great day ahead!".format(name, position, salary)
print(letter)

# By using positional arguments

letter = "Dear {0},\nYou are selected!\n{1} is the position you have been selected for.\n{2} is the salary you will be receiving.\nHave a great day ahead!".format(name, position, salary)
print(letter)

# By using keyword arguments
letter = "Dear {name},\nYou are selected!\n{position} is the position you have been selected for.\n{salary} is the salary you will be receiving.\nHave a great day ahead!".format(name=name, position=position, salary=salary)
print(letter)
