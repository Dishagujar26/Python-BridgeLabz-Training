number = int(input("Enter a number: "))

if number >= 2:
    for i in range(2, int(number**0.5) + 1 ):
        if number % i == 0 :
            print("not a prime ")
            break
    else:
        print("it is a prime")
else:
    print("not a prime ")