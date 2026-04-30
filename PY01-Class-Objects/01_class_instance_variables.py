class Employee:

    language = "python" # class variable
    salary = 1000

e1 = Employee()
e1.language = "java" # instance variable
print(e1.language, e1.salary) # output: java 1000 - instance variable has higher priority


