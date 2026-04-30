class VectorPrint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # to print the vector as 7i + 8j + 10k
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    

vector1 = VectorPrint(7, 8, 10)
print(vector1)