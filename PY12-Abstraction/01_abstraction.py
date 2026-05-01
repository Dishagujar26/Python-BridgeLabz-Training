# abstraction in python means showing only essential details and hiding internal implementation.
# In Python, abstraction is mainly achieved using the built-in module Python abc (Abstract Base Class).

# import ABC and abstractmethod from Python's built-in abc module
# abc = Abstract Base Class module
# It helps us create abstract classes (classes that act like blueprints/rules)
from abc import ABC, abstractmethod


# Create an abstract class named Animal
# (ABC) means Animal is now an Abstract Base Class
# Abstract class = a class used only for defining rules
# Usually we don't create objects of abstract classes directly
class Animal(ABC):


    # @abstractmethod is a decorator - "Any child class inheriting Animal MUST implement this method"
    @abstractmethod
    def sound(self):
        # empty method body / placeholder
        # Parent class only declares the method
        # Child class will provide actual implementation
        pass


# Dog class inherits Animal class
class Dog(Animal):


    # Since Animal has abstract method sound(),
    # Dog MUST implement sound()
    # Otherwise Python will give error
    def sound(self):
        print("Bark")


# Creating object of Dog class
# This is allowed because Dog implemented all abstract methods
d = Dog()


# Calling Dog's sound method
d.sound()      # Output: Bark