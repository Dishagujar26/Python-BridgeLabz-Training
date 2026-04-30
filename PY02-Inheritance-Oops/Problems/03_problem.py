# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:
    salary = 0
    increment = 1.5

    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salary_after_increment(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = ((salary/self.salary)-1)*100

        # new_salary = old_salary * (1 + increment/100)
        # old_salary = new_salary / (1 + increment/100)
        # increment = ((new_salary / old_salary) - 1) * 100
        

e = Employee(10000, 10) 
print(e.salary_after_increment) # calls salary_after_increment() method
e.salary_after_increment = 15000 # calls salary_after_increment.setter
print(e.increment)
