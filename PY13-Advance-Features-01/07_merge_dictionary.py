# Introduced in Python 3.9+ merge operator |

student1 = {
    "name": "Disha",
    "age": 22
}

student2 = {
    "city": "Bhopal",
    "course": "Python"
}

result = student1 | student2

print(result)

'''
original dictionary are unchanged 
{
 'name': 'Disha',
 'age': 22,
 'city': 'Bhopal',
 'course': 'Python'
}

'''
# Duplicate key case 

a = {"name": "Disha"}
b = {"name": "Rahul"}

print(a | b) # output: {'name': 'Rahul'} right side will override left side 

# Update merge operator |= merge into existing dictionary
# modifies original dictionary

student = {
    "name": "Disha"
}

student |= {
    "age": 22
}

print(student)

# duplicate key 

a = {"x": 1}
a |= {"x": 100}

print(a) # {'x': 100} 