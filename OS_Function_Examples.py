import os # This is how you impor the os functions into python

#current_dir = os.getcwd() # This the os command to get the current working directory
#print(current_dir) # Print the current working directory

###os.chdir("Path to new default directory goes here")# chdir will let you change the default directory you are working in.  

# Writing a file to the current working directory

#with open("Test.txt", 'w') as f:
    #f.write("This is a test file")

# Listing all directories and files using os.listdir command. 

print(os.listdir())

# Making a new directory using os.mkdir 

os.mkdir("Test_Directory")

# Renaming a directory or a file use os.rename

#os.rename("Test.txt", "New_Test.txt")

#Removing a file using os.remove

#os.remove("New_Test.txt")

# Remove a directory using the os.rmdir. Directory MUST be empty or else an exception will be raised. 

#os.rmdir("New_Test")