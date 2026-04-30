# Inheritance in python - how many is supported in python

# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance


# Single Inheritance

class Parent:
    def method1(self):
        print("Parent class method1")

    def method2(self):
        print("Parent class method2")   

class Child(Parent):
    def method3(self):
        print("Child class method3")

obj = Child()
obj.method1()
obj.method2()
obj.method3()   


# Multiple Inheritance

class Parent1:
    def method1(self):
        print("Parent1 class method1")

    def method2(self):
        print("Parent1 class method2")
        
class Parent2:
    def method3(self):
        print("Parent2 class method3")

class Child(Parent1, Parent2):
    def method4(self):
        print("Child class method4")

obj = Child()
obj.method1()
obj.method2()
obj.method3()
obj.method4()


# Multilevel Inheritance

class GrandParent:
    def method1(self):
        print("GrandParent class method1")

class Parent(GrandParent):
    def method2(self):
        print("Parent class method2")


class Child(Parent):
    def method3(self):
        print("Child class method3")

obj = Child()
obj.method1()
obj.method2()
obj.method3()


# Hierarchical Inheritance

class Parent:
    def method1(self):
        print("Parent class method1")

class Child1(Parent):
    def method2(self):
        print("Child1 class method2")
        
class Child2(Parent):
    def method3(self):
        print("Child2 class method3")

obj1 = Child1()
obj1.method1()
obj1.method2()

obj2 = Child2()
obj2.method1()
obj2.method3()


# Hybrid Inheritance

class Parent:
    def method1(self):
        print("Parent class method1")

class Child1(Parent):
    def method2(self):
        print("Child1 class method2")
        
class Child2(Child1):
    def method3(self):
        print("Child2 class method3")

obj = Child2()
obj.method1()
obj.method2()
obj.method3()

