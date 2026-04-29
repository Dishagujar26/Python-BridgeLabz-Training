a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("a is the greatest number")
elif(b>a and b>c and b>d):
    print("b is the greatest number")
elif(c>a and c>b and c>d):
    print("c is the greatest number")
elif(d>a and d>b and d>c):
    print("d is the greatest number")
else:
    print("All numbers are equal")

