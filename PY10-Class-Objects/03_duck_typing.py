class Cat:
    def speak(self):
        print("Meoww")

class Dog:
    def speak(self):
        print("Bhow Bhow")

animals = [Cat(), Dog()]

for a in animals:
    a.speak()

