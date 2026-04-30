# Example: Difference between instance method call and class-level call

class Employee:

        language = "python"
        salary = 1000

        # Dunder method in python starts and ends with two underscores
        def __init__(self):
              print("Employee object created")

        # This is an instance method
        # 'self' represents the object that calls this method - it can be changed to anything you want to represent the object
        def get_info(self):
            print(f"Employee Language: {self.language} \nEmployee Salary: {self.salary}")

        # static method - no need to pass self parameter as it is not an instance method 
        @staticmethod
        def greet():
              print("Good Morning")
        

# Creating an object (instance) of Employee
e1 = Employee()


# Calling method using object

# Python automatically passes 'e1' as the self argument
# Internally, Python treats this as:
# Employee.get_info(e1) So this works fine

e1.get_info()
e1.greet() # static method can be called using object as well as class name

# Calling instance method using class name 

# Here, Python does NOT automatically pass any object. Internally, Python treats this as: Employee.get_info()
# But get_info() expects one argument: self, Since nothing is passed, it throws an error

# Employee.get_info()      # Uncommenting this line will generate:
# TypeError: get_info() missing 1 required positional argument: 'self'


# Correct way to call using class name. Pass an object manually as self

Employee.get_info(e1)      # This works

