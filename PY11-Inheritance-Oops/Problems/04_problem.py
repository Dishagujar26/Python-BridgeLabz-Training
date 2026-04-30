# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them

# a complex number has a real and imaginary part - like a+bi
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # add two complex numbers 

    def __add__(self, complex2):
        return Complex(self.real + complex2.real, self.imaginary + complex2.imaginary) # here we are returning a new complex object 
    

    # multiply two complex numbers
    
    def __mul__(self, complex2):
        real = (self.real * complex2.real) - (self.imaginary * complex2.imaginary)
        imaginary = (self.real * complex2.imaginary) + (self.imaginary * complex2.real)

        return Complex(real, imaginary)

    
    # with the str method - output will be something like <__main__.Complex object at 0x000001B3BCF10B90>
    # so we need to override it by defining our own __str__ method so that it returns something more meaningful like 1+2i

    def __str__(self): # similar toString in java
        return f"{self.real}+{self.imaginary}i" 
    
c1 = Complex(1,2) # this complex() is a constructor method of the class Complex  
c2 = Complex(3,4)
print(c1+c2) # internally c1.__sum__(c2)
print(c1*c2) # internally c1.__mul__(c2)

