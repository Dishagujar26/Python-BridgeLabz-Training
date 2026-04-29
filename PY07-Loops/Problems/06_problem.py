number = int(input("Enter a number: "))

fact = 1
for i in range(2,number+1):
    fact *= i
    i+=1

print("The factorial is ", fact)