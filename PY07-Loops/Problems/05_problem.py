number = int(input("Enter a number: "))
sum = 0
for i in range(1,number+1):
    sum += i
    i+=1

print("The sum is ", sum)