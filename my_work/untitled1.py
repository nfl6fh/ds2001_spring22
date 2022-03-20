#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:41:41 2022

@author: nathanlindley
"""

print('') # Story elements
userName = input('What is your name? ')
startGame = input(userName + ', would you like to play? ').lower()
if startGame == 'yes':
    print('First we\'ll start with a quiz: \nHow many oceans are there?', end = ' ')
    for i in range(2,7):
        oceans = input('Are there ' + str(i) + ' oceans? ').lower()
        if i != 5 and oceans == 'yes':
            print('Sorry, thats the wrong answer')
            break
        elif i == 5 and oceans == 'yes':
            print('Correct! Welcome aboard')
            print('What is a pirate\'s favorite letter?')
            wrongAnswer = True
            while wrongAnswer:
                riddleAnswer = input('Answer: ').lower()
                if riddleAnswer == 'r':
                    wrongAnswer = False
                else:
                    print('That\'s not quite right, try again')
            print('You may have gotten that correct, but \nI\'ve got another riddle for you now')
            print('ra2')
            wrongAnswer2 = True
            while wrongAnswer2:
                riddle2Answer = input('Answer: ').lower()
                if riddle2Answer == 'ra2':
                    wrongAnswer2 = False
                else:
                    print('That\'s not quite right, try again')
            print('Arghh you passed both of my riddles!')
            print('') # more story elements
            findTreasure = input('Would you like to help dig for the treasure? ').lower()
            if findTreasure == 'yes':
                print('We found the treasure! As a reward you can choose one item to take.')
                treasure = ['Gold Necklace','Diamond Necklace','Ruby Necklace','Saphire Necklace',
                            'Gold Coins','Gold Chalice','Jewels','Bejeweled crown','Gold Sword']
                print('Here are your options:')
                print(treasure)
                necklace = input('Would you like a necklace? ').lower()
                if necklace == 'yes':
                    necklaces = [x for x in treasure if 'Necklace' in x]
                    for i in range(len(necklaces)):
                        pick = input('Would you like ' + necklaces[i] + '? ').lower()
                        if pick == 'yes':
                            print('Sorry, that\'s what I want! pick again!')
                            necklaces.remove(necklaces[i])
                            break
                    for i in range(len(necklaces)):
                        pick = input('Would you like ' + necklaces[i] + '? ').lower()
                        if pick == 'yes':
                            print('Great choice!')
                            break
                else:
                    treasure = [x for x in treasure if 'Necklace' not in x]
                    for i in range(len(treasure)):
                        pick = input('Would you like ' + treasure[i] + '? ').lower()
                        if pick == 'yes':
                            print('Sorry, that\'s what I want! Pick again')
                            treasure.remove(treasure[i])
                            break
                    for i in range(len(treasure)):
                        pick = input('Would you like ' + treasure[i] + '? ').lower()
                        if pick == 'yes':
                            print('Great choice!')
                            break
            break
print('So long!')