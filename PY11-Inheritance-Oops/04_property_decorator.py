# @property is a built-in decorator that lets you use a method like an attribute (variable).

class Employee:
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus

    @property
    def total_salary(self):
        return self.salary + self.bonus


e1 = Employee(50000, 10000)

print(e1.total_salary)   # no ()

# Example: @classmethod + @property + @property.setter

class Employee:

    # Class variable (shared by all objects)
    a = 10

    def __init__(self):
        self.fname = ""
        self.lname = ""


    # CLASS METHOD -> cls refers to the class itself, not object
    # Used to access/modify class variables
    @classmethod
    def show(cls):
        print(f"The class attribute a is: {cls.a}") 


    # PROPERTY GETTER -> Makes method behave like a variable
    # We can access it as: e.name  (without brackets)
    @property
    def name(self):
        return f"{self.fname} {self.lname}"


    # PROPERTY SETTER -> Runs automatically when we assign value:
    # e.name = "Harry Khan"
    #
    # Internally Python calls this setter method. It receives "Harry Khan" in value
    @name.setter
    def name(self, value):

        # split(" ") converts:
        # "Harry Khan" -> ["Harry", "Khan"]

        # first word goes into fname
        self.fname = value.split(" ")[0]

        # second word goes into lname
        self.lname = value.split(" ")[1]


e = Employee()


# Change class variable (better done as Employee.a = 45)
e.a = 45


# Calls setter automatically Internally: e.name("Harry Khan")
# fname = Harry
# lname = Khan
e.name = "Harry Khan"


# Directly printing stored values
print(e.fname)      # Harry
print(e.lname)      # Khan


# Calls getter automatically Internally:
# e.name -> calls @property method
print(e.name)       # Harry Khan


e.show()


# SUMMARY:
# @classmethod -> works with class using cls
# @property -> getter, access method like variable
# @property.setter -> setter, assign like variable but method runs internally