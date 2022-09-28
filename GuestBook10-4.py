filename = "guest_book.txt"

answer = 'Yes'
while answer == 'Yes':
    with open(filename, 'a') as file_object:
        names = input("Please enter you name and it will be recorded in our guestbook!: ")
        file_object.write(names)
        answer = input("Would you like to enter another name for the guest book?: ")