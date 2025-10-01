"""
Assignment: Adding Exception Handling
Objective: Enhance a basic Python program by implementing try and except statements to handle errors in user input, focusing on data type errors.
Starting Code:
# Simple Python program to calculate the square of a number
def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}")
    square_number()
Instructions:
1. Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
2. Identify Potential Errors: Consider errors that might occur with non-numeric input.
3. Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect dats types with an error message.
4. Test Your Code: Ensure the exception handling works correctly with various inpits.
5. GitHub Upload: Upload your py file to GitHub and hand in the link.
    """
# Simple Python program to calculate the square of a number.
def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2 # This line may raise a ValueError if input is not a valid integer.
    print(f"The square of {number} is {squared_number}")
    square_number() # Understanding the code: Reviewing the provided Python script.

# Using the try and except blocks to catch a ValueError.
def square_number():
    try:
        number = input("Enter a number to square: ")
        square_number = int(number) ** 2
        print(f"The square of {number} is {square_number}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calling the function to execute the program.
square_number()