# Method overriding in python 
# When a child class has the SAME method name as the parent,
# the child's version REPLACES the parent's version.


class Animal:
    def speak(self):
        print("Some animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")


a = Animal()
d = Dog()
c = Cat()

a.speak()   # → Some animal makes a sound.  (uses parent method)
d.speak()   # → Dog says: Woof!             (uses Dog's overridden method)
c.speak()   # → Cat says: Meow!             (uses Cat's overridden method)

# KEY POINT:
# All three objects call speak(), but each runs a DIFFERENT version.
# Python picks the method based on which class the object belongs to.
# This behavior is called POLYMORPHISM.