class Calculator:

    # constructor method with default value for num2   
    def __init__(self, num1, num2=None):
        self.num1 = num1
        self.num2 = num2


    # operations needing two numbers
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2


    # operations needing one number
    def square(self):
        return self.num1 * self.num1

    def cube(self):
        return self.num1 * self.num1 * self.num1

    def square_root(self):
        return self.num1 ** 0.5

    def cube_root(self):
        return self.num1 ** (1/3)

    def factorial(self):
        fact = 1
        for i in range(1, self.num1 + 1):
            fact *= i
        return fact


# Example
c1 = Calculator(5)
print(c1.square())       # 25
print(c1.factorial())    # 120

c2 = Calculator(10, 3)
print(c2.add())          # 13
print(c2.subtract())     # 7