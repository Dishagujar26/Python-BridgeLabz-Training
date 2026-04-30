class Employee:

    company = "Capgemini" # class variable common to all objects of the class

    # initializer method __init__ is called when an object of the class is created. It is used to initialize the attributes (instance variables) of the object
    # Dunder method in python starts and ends with two underscores
    
    def __init__(self, emp_id, emp_name, emp_salary): # instance variables emp_id, emp_name, emp_salary
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def display(self):
        print(f"Employee ID: {self.emp_id} \nEmployee Name: {self.emp_name} \nEmployee Salary: {self.emp_salary} \nCompany: {self.company}")


# obejects and classes in python - objects are instances of a class and classes are templates for creating objects

emp1 = Employee(1, "A", 100)
emp2 = Employee(2, "B", 200)

emp1.display()
emp2.display()

print(Employee.company)