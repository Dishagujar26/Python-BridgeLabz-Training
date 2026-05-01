
# Java has many strict OOP features built into the language.
# Python supports most of them — but in a Pythonic way.

# In Java: super() calls the parent constructor.
# In Python: super().__init__() does the same.

#   Constructor Chaining means:
#   When a child class object is created, it automatically calls the parent class constructor first using super().
#   This ensures parent data is initialized before child data.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        print(f"  [Person.__init__] name={name}, age={age}")


class Employee(Person):
    def __init__(self, name, age, emp_id):

        # super().__init__() chains to Person's constructor.
        # Without this, self.name and self.age won't exist.

        super().__init__(name, age)         # Step 1: Call parent constructor
        self.emp_id = emp_id                # Step 2: Add child-specific data
        print(f"  [Employee.__init__] emp_id={emp_id}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, department):
        # Chain goes: Manager → Employee → Person
        super().__init__(name, age, emp_id) # Calls Employee.__init__
        self.department = department
        print(f"  [Manager.__init__] department={department}")


print("=" * 50)
print("1. CONSTRUCTOR CHAINING")
print("=" * 50)
print("Creating Manager object:")
m = Manager("Vikram", 40, "E101", "Engineering")
print(f"Result → {m.name}, {m.age}, {m.emp_id}, {m.department}")
# Notice: Person → Employee → Manager order of execution


# Java has a separate 'interface' keyword.
# Python has NO interface keyword — but you can SIMULATE one
# using ABC with ONLY @abstractmethod (no concrete methods).

from abc import ABC, abstractmethod
# A class can implement MULTIPLE interfaces (multiple inheritance).
# Java: class Bird implements Flyable, Swimmable
# Python: class Bird(Flyable, Swimmable)

class Flyable(ABC):                        # Interface 1
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):                      # Interface 2
    @abstractmethod
    def swim(self):
        pass

class Duck(Flyable, Swimmable):            # Implements BOTH interfaces
    def fly(self):
        return "Duck is flying!"

    def swim(self):
        return "Duck is swimming!"

class Eagle(Flyable):                      # Implements only Flyable
    def fly(self):
        return "Eagle soaring high!"


print("\n" + "=" * 50)
print("3. INTERFACES (Multiple Inheritance)")
print("=" * 50)

duck  = Duck()
eagle = Eagle()
print(duck.fly())
print(duck.swim())
print(eagle.fly())


# In Python: @staticmethod
# Static method:
#   → Belongs to the CLASS, not to any object
#   → No access to self (instance) or cls (class)
#   → Called using ClassName.method() — no object needed
#   → Used for utility/helper logic that fits inside the class

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


print("\n" + "=" * 50)
print("4. STATIC METHODS")
print("=" * 50)

# No object needed — call directly on the class
print("add(3, 4)         →", MathUtils.add(3, 4))
print("is_even(10)       →", MathUtils.is_even(10))
print("25°C in °F        →", MathUtils.celsius_to_fahrenheit(25))


# CLASS METHODS  (like Java's static factory methods)
# @classmethod receives the CLASS itself as the first argument (cls).
# Useful for: alternative constructors, factory patterns.

#   Difference from @staticmethod:
#   staticmethod → no access to class or instance
#   classmethod  → has access to the CLASS via cls

class Student:
    school_name = "Python High School"     # Class variable

    def __init__(self, name, grade):
        self.name  = name
        self.grade = grade

    @classmethod
    def from_string(cls, data_string):

        # Alternative constructor — creates a Student object
        # from a formatted string like "Ananya:10"
        # cls refers to Student class itself

        name, grade = data_string.split(":")
        return cls(name, int(grade))       # Same as Student(name, grade)

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name         # Modifies class-level variable

    def __str__(self):
        return f"{self.name} (Grade {self.grade}) | {self.school_name}"


print("\n" + "=" * 50)
print("5. CLASS METHODS")
print("=" * 50)

s1 = Student("Rohan", 9)
s2 = Student.from_string("Ananya:10")     # Alternative constructor
print(s1)
print(s2)

Student.change_school("AI Academy")       # Changes for ALL instances
print(s1)                                 # school_name updated!
print(s2)


# Java: final int MAX = 100;
# Python has NO final keyword — two common approaches:

#   a) UPPERCASE name → convention for constants (most common)
#   b) typing.Final   → type-checker enforced (modern Python)

# Python won't throw an error if you change them at runtime,
# but uppercase + Final signals "do not modify this."

from typing import Final

MAX_RETRIES: Final = 3                     # Enforced by type checkers
PI:          Final = 3.14159

class Config:
    DB_HOST: Final = "localhost"           # Class-level constant
    DB_PORT: Final = 5432
    MAX_CONN: Final = 10


print("\n" + "=" * 50)
print("6. FINAL / CONSTANTS")
print("=" * 50)
print("MAX_RETRIES →", MAX_RETRIES)
print("DB_HOST     →", Config.DB_HOST)
print("DB_PORT     →", Config.DB_PORT)


# isinstance()  (like Java's instanceof)
# Java:   if (obj instanceof Dog)
# Python: if isinstance(obj, Dog)

# isinstance() also returns True for PARENT classes —
# so a Dog object is also an instanceof Animal.

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print("\n" + "=" * 50)
print("7. isinstance() — Java's instanceof")
print("=" * 50)
print("isinstance(dog, Dog)    →", isinstance(dog, Dog))     # True
print("isinstance(dog, Animal) →", isinstance(dog, Animal))  # True (parent)
print("isinstance(dog, str)    →", isinstance(dog, str))     # False

