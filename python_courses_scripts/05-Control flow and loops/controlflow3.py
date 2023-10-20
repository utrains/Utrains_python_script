# Python script to take a number as an input from a user and then check if it is a positive number, negative or zero.

number = input("Enter a number ")
number = int(number)
if number > 0:
    print("The number you entered is positive ")
elif number ==0:
    print("The number you entered is  zero")
else:
    print("The number you entered is negative")
