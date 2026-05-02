# Python's module execution control

def show():
    print("Hello World")

print("this will run as we it is outside of the if block- " \
"run when direclty called also when called from any import statement")

if __name__== "__main__":
    print("this block is only executed when directly called not from any import statement")
    print("here you put code that you don't want to be executed from any import statement")
    show()
    print(__name__) # this prints the name of the module
