class Programmer:

    company = "Microsoft"
    salary = 1000000

    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def display(self):
        print(f"Employee ID: {self.emp_id} \nEmployee Name: {self.emp_name} \nEmployee Salary: {self.emp_salary} \nCompany: {self.company}")

p1 = Programmer(1, "A", 100)
p2 = Programmer(2, "B", 200)
p3 = Programmer(3, "C", 300)

list_of_programmers = [p1, p2, p3]

for programmer in list_of_programmers:
    programmer.display()

    