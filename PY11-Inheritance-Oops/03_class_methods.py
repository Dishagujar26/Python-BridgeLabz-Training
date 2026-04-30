# Decorators in Python are special functions that modify or extend the behavior of another function/method without changing its original code.
# They are written using @decorator_name above a function definition.
# Example: @staticmethod, @classmethod are built-in decorators that change how methods behave inside a class.


class Parent:
   
    def instance_method(self):
        print("self =", self)

    @classmethod
    def class_method(cls):
        print("cls =", cls)

    @staticmethod
    def static_method():
        print("No automatic argument")
      
obj = Parent()

obj.instance_method()  # gets object
Parent.class_method()  # gets class
Parent.static_method() # gets nothing

# Instance method -> uses self (object instance), Python passes object automatically; use name 'self' by convention.
# Class method -> uses @classmethod + cls (class itself), Python passes class automatically; use name 'cls' by convention (not self).
# Static method -> uses @staticmethod, Python passes nothing automatically; self/cls are not used unless you manually pass arguments.

class Employee:
    @classmethod
    def show(self):   # bad naming
        print(self)


# Understaning this code with and without @classmethod decorator 


class Parent:
    a = 1

    @classmethod
    def show(cls):
        print(cls.a)

p = Parent()
p.a = 45
p.show() 

