'''
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

'''

import random

def game():
    print("You are playing a game...")
    score = random.randint(1,50)
    
    # Fetch the highscore

    with open("hiscore.txt") as f:
        hirescore = f.read()
        if(hirescore != ""):
            hirescore = int(hirescore)
        else:
            hirescore = 0

    print(f"Your score is {score}")
    if(score > hirescore):
        print("You have broken the Hi-score")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    else:
        print("You have not broken the Hi-score")
    return score


game()

