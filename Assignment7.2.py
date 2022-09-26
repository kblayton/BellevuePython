# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time


def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print() # KL - printing empty statement?


def chooseCave():
    print('Which cave will you go into? (1 or 2)')
cave = input()
	while cave == '1' or cave == '2': # KL - Indention is wrong at this point for while statement
		return cave # KL - Caves not defined (return cave). Could use else statement below to make sure they are using only 1 or 2.
	#else:
	#	print('invalid input. Please input 1 or 2')
	#	chooseCave()

def checkCave(chosenCave): # KL - indention error
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' # KL - print statement need () around string

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': # KL - while operator needs changed (While x == 'y')
	displayIntro()
	caveNumber = choosecave() # choosecave is not defined (create or function fix name)
	
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")#KL - Spelling error. pla(n)ing should be pla(y)ing