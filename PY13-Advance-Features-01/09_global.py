# global variable in python is a variable that is declared outside a function and can be accessed from anywhere in the program 
# The rule is while reading them we don't need global keyword 
# but while updaing then we need to specify global variable by using global keyword 

x = 100   # global variable

def show():
    print("Inside function: ", x)


def update():
    global x # try commentin this line and see what happens
    x = 500


print("Before:", x)

show()

update()

print("After:", x)