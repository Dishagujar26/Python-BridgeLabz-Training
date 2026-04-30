'''
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number

'''
import random

# Generate a random number
random_number = random.randint(1, 100)
guess = 0 # The user's guess
count = 0 # Number of guesses

while guess != random_number: # Loop until the user guesses the correct number
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < random_number:
        print("Higher number please")
    elif guess > random_number:
        print("Lower number please")
    count += 1

print(f"You guessed the number in {count} guess attempts!!")
