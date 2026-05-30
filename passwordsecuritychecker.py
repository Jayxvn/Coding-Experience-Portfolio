# Awesome password security checker man

import string

# Start loop
answer = "y"
while(answer != "n"):

# Declaring variables
    points = 0
    password = str(input("Please input your password: "))

# Defining password blacklist
    banned_passwords = ["password", "123456", "abcdefg", "qwerty", "admin", "letmein"]
    
# Check if password is in the blacklist, or send back to beginning to rethink your choices
    if password in banned_passwords:
        print("DO NOT USE THAT PASSWORD BRO")
        continue
    
# Check password length
    if len(password) < 8:
        print("Your password isn't even long enough gang... ")
    elif len(password) >= 15:
        points += 2
    elif len(password) >= 12:
        points += 1

# Check any uppercases
    if any(char.isupper() for char in password):
        points += 1

# Check any lowercases
    if any(char.islower() for char in password):
        points += 1

# Check any digits
    if any(char.isdigit() for char in password):
        points += 1

# Check any symbols
    if any(char in string.punctuation for char in password):
        points += 1

# Judge based on points
    if points <= 2:
        print("You have a weak password.")
    elif points <= 4:
        print("You have a decent password.")
    else:
        print("You have a strong password!")

# Back to top of loop
    while True:
        answer = str(input("Would you like to try another password (y/n)? "))
        if answer != "y" and answer != "n":
            print("What?")
        else:
            break
