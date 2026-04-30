# Operator overloading means giving special meaning to operators
# like +, -, *, >, < for user-defined objects.

# Why do we need it? Normally operators work on built-in types:
# 10 + 20 = 30
# "Hi" + "Bro" = "HiBro" But for our own class objects, Python doesn't know what + should do. Operator overloading lets us define that behavior.

# How do we perform it?
# By using special methods (magic / dunder methods)
# __add__()  -> +
# __sub__()  -> -
# __mul__()  -> *
# __gt__()   -> >
# __lt__()   -> <
# __eq__()   -> ==


class Student:
    def __init__(self, marks):
        self.marks = marks

    # overload + operator
    def __add__(self, other):
        return self.marks + other.marks


s1 = Student(50)
s2 = Student(60)

print(s1 + s2)   # calls s1.__add__(s2)

class Number:
    def __init__(self, x):
        self.x = x

    def __gt__(self, other):
        return self.x > other.x


n1 = Number(10)
n2 = Number(5)

print(n1 > n2)