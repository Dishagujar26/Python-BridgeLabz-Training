# super() method in python inheritance
class Parent:

    def __init__(self):
        print("Parent class constructor")

    def method1(self):
        print("Parent class method1")

    def method2(self):
        print("Parent class method2")


class Child(Parent):

    def __init__(self):
        super().__init__() # parent class constructor call 
        print("Child class constructor")

    def method1(self):
        super().method1() # parent class method call
        print("Child class method1")

    def method2(self):
        super().method2() #  parent class method call
        print("Child class method2")

    def method3(self):
        print("Child class method3")


obj = Child()
obj.method1()
obj.method2()
obj.method3()

# Output:
# Parent class method1
# Child class method1
# Parent class method2
# Child class method2
# Child class method3