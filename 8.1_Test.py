import os

# Letting the user know what directory they are currently in
current_directory = os.getcwd()
print("Your current directory is " + str(current_directory))

# storing the file path the user chooses in the choose_directory variable
choose_directory = input("Where would you like to save this file? : ") 
filename = input("What is the name of the file you are saving? : ")

#Validating that the directory doesn't already exists. If it exists, message is displayed that states it exists. If it doesn't, the directory is created and completion message is displayed
try:
    os.mkdir(choose_directory)
except FileExistsError:
    msg = "Sorry, the directory " + choose_directory + " already exists"
    print(msg)
else:
    print("The directory at " + str(choose_directory) + " has been created")
    os.chdir = choose_directory
    print(os.getcwd())

filename = (filename + ".txt")

with open(filename, 'w') as f:
    name = input("What is your name? : ")
    address = input("What is your address? : ")
    phone_number = input("What is your phone number? : ")
    contents = f.read()
    f.write(name + ', ')
    f.write(address + ', ')
    f.write(phone_number) 
    print(contents)











