import random # built in module 

'''
1 for snake
-1 for water
0 for gun 

'''
computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youdict = {'s':1,'w':-1,'g':0}
reversedict = {1:'Snake',-1:'Water',0:'Gun'}

you = youdict[youstr]

# By now we have 2 number (computer and you)

print(f"You chose: {reversedict[you]}\nComputer chose: {reversedict[computer]}")

if(you == computer):
    print("The game is a draw")
else:
    if((you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1)):
        print("You won!!")
    else:
        print("You lost!!")
 