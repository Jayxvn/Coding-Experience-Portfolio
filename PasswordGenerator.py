import string
import random

answer = ""
while (answer != "n"):
    length = int(input("Choose your password length: "))
    letters = string.ascii_letters # a-z and A-Z
    numbers = string.digits # 0-9
    symbols = string.punctuation #!@#$%^ etc.
    
    password = "".join(random.choice(letters + numbers + symbols) for _ in range(length))

    print(f"Your password is: {password}")
    
    answer = str(input("\nDo you wish to generate another (y/n)? "))
    if answer == "y":
        continue