from cmath import pi


filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

## Is your birthday contained in PI?

def birthdayPi():
    birthday = input("Enter your birthday, in the form of mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")

'''Giving the ability to try another date rather than closing the program.'''

tryAgain = 'yes'
while tryAgain == 'yes' or tryAgain == 'y':
    birthdayPi()

    print("Would you like try another date? Y or N?: ")
    tryAgain = input() #storing the input of the user in the variable tryAgain
    if tryAgain == 'no' or tryAgain == 'n':
        print("Thanks for playing!")
   
#print(pi_string[:52] + "...")
#print(len(pi_string))