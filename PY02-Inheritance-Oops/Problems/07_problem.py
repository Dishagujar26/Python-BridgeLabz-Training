#  Override the __len__() method on vector of problem 5 to display the dimension of the
#  vector

class Vector:
    def __init__(self,list):
        self.list = list
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
 
    # print(len(v1)) - this will give error (without overriding the __len__()) as it is not defined we have to override the below method such that it returns the length of the vector 
    # for varibale length we have to store the vector in list and then find the length of the list 
    def __len__(self):
        return len(self.list)

v1 = Vector([1,2,3]) # pass vector as list 
print(len(v1)) 