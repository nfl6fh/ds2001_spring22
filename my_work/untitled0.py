"""
    Name:
    Collaborators: 
    COSC-010
    Subtraction Game Lab

    In this game, the user selects an integer between 10 and 30. This
    number represents the starting number of matches. The user and the
    then alternate removing 1 or 2 matches. The object of the game is 
    to avoid removing the last match. The computer will play without
    much strategy, generally just choosing 1 or 2 at random.
"""
import random
import time
delay = 0

print("Welcome to the Subtraction Game!")



"""

Insert code here to allow user to select before computer each turn

"""

playing = True
while playing:
    badInput = True
    while badInput:
        try:
            n = int(input("Enter the starting number of matches (between 10 and 30) "))
            if n >= 10 and n <= 30:
                badInput = False
        except:
            badInput = True
    remaining = n
    inGame = True
    while inGame:
        badInput = True
        while badInput:
            try:
                userInput = int(input('Enter either 1 or 2 '))
                if userInput == 1 or userInput == 2:
                    badInput = False
            except:
                badInput = True
        remaining -= userInput
        print("...And of the original", n, "matches, now there are", remaining, "left")
        if remaining <= 0:
            print('You lost')
            inGame = False
            break
        elif remaining == 1:
            print('You win!')
            inGame = False
            break
        time.sleep(delay * 2)
        computerChoice = random.choice([1, 2])
        remaining -= computerChoice 
        print("...The computer chooses", computerChoice)
    playAgain = input('Would you like to play again? (y/n) ').lower()
    if playAgain == 'n':
        playing = False

"""

Insert code here to deal with the result of computer making its choice

"""

        
print("Thank you for playing. Goodbye.")    