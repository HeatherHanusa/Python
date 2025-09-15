"""
signment: Basic Logical Operations with Integers
In this exercise, you will practice using logical operators (and, or, not) in Python.
Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.
"""
# This code demonstates the use of and in Python
integer = (float(input("Enter an integer: ")))
integer2 = (float(input("Enter another integer: ")))
integer3 = (float(input("Enter one more integer: ")))
if integer > integer2 and integer > integer3:
    print(f"{integer} is the largest number.")
elif integer2 > integer and integer2 > integer3:
    print(f"{integer2} is the largest number.") 
else:
    print(f"{integer3} is the largest number.")
# This code above is the and operator
if integer < integer2 or integer < integer3:
    print(f"{integer} is the smallest number.")
elif integer2 < integer and integer2 < integer3:
    print(f"{integer2} is the smallest number.")
else:
    print(f"{integer3} is the smallest number.")
# This code above is the or operator
if not integer > integer2:
    print(f"{integer} is not greater than {integer2}.")
else:
    print(f"{integer} is greater than {integer2}.")
# This code above is the not operator