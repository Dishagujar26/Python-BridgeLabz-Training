number = int(input("Enter a number: "))

def sum_of_natural_number(n):
    if n == 1:
        return 1

    return n + sum_of_natural_number(n - 1)

print("The sum of natural numbers is:", sum_of_natural_number(number))
print(f"The sum of 1 to {number} is: {sum_of_natural_number(number)}")