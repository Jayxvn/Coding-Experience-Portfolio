Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> answer = " "
... while(answer != "n"):
...     cgpa = 0.0
...     gpa = 0.0
...     total_gpa = 0.0
...     credits = 0.0
...     i = 0
...     previous_gpa = 0.0
...     previous_credits = 0.0
...     total_credits = 0.0
... 
...     previous_gpa = float(input("What is your previous GPA (if you don't have one, type 0)? "))
...     previous_credits = float(input("How many credits do you already have (if you don't have any, type 0)? "))
... 
...     total_gpa = previous_gpa * previous_credits
...     total_credits = previous_credits
... 
...     classes = int(input("How many classes are you taking this semester? "))
... 
...     for i in range(1, classes + 1):
...         gpa = float(input(f"What is your grade in class {i} (in 4.0 format): "))
...         credits = float(input("How many credits do you have in this class? "))
...         total_gpa += gpa * credits
...         total_credits += credits
... 
...     cgpa = total_gpa / total_credits
...     
...     print(f"Your cumulative GPA is now: {round(cgpa, 3)}")
... 
...     answer = str(input("Do you wish to calculate again? (y/n) "))
...     if answer == "y":
