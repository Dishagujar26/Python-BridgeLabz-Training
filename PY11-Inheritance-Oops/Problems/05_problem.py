# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self,other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
    
    def __repr__(self): # str and repr are same but repr is used for debugging purposes in python
        return f"Vector({self.x}, {self.y}, {self.z})"
    

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

print(v1 + v2) # output: Vector(5, 7, 9)
print(v1 * v2) # output: 32