number = int(input("Enter a number: "))

if(number > 0):
    print("Multiplication Table of ", number)
 
    for i in range(1,11):
        print(number, "X", i, "=", number * i)
        i+=1
    
else:
    print("Please enter number greater than 0")
