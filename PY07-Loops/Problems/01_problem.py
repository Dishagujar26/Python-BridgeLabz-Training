number = int(input("Enter a number: "))

if(number > 0):
    print("Multiplication Table of ", number)

    i = 1
    while i <= 10:
        print(number, "X", i, "=", number * i)
        i+=1
    
else:
    print("Please enter number greater than 0")



if(number > 0):
    print("Reversed Multiplication Table of ", number)

    i = 10
    while i >= 1:
        print(number, "X", i, "=", number * i)
        i+=1
    
else:
    print("Please enter number greater than 0")