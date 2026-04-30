# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animal:
    def __init__(self, name):
        print("Animal created")
        self.name = name

class Pets(Animal):
    def __init__(self, name):
        print("Pets created")
        super().__init__(name)

class Dog(Pets):
    def __init__(self, name):
        print("Dog created")
        super().__init__(name)

    def bark(self):
         print(f"{self.name} is barking")
    
d = Dog("Shiro")
d.bark()