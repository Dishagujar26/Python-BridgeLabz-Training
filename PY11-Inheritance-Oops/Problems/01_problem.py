# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, x, y):
        print("Creating a 2D vector...")
        self.x = x
        self.y = y

    def show(self):
        print(f"x: {self.x}, y: {self.y}", end=" ")


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        print("Creating a 3D vector...")
        self.z = z

    def show(self):
        super().show()
        print(f"z: {self.z}")

q = Vector3D(1, 2, 3)
q.show()