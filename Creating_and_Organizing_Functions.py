"""
Assignment: Calculating Factorials
Objective: Write a Python program using a recursive function to calculate the factorial of a number.
A recursive is a function that calls itself to solve a problem.
Assignment Instructions:
1. Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
2. In your factorial function, first define the base: n == 1 or n == 0, where the factorial is 1.
3. For the recursive step, return n * factorial(n-1) if n>1.
4. Prompt the user for a non-negative integer and call factorial, printing the result.
"""

# Defining the function named factorial.

def factorial(n): # One paramater, n, representing the number we are calculating the factorial for.

# Define the base case:
    if n == 0 or n == 1: # Base case: if n is 0 or n is 1.
        return 1 # The factorial is 1.
    
    else: # Recursive step:
        return n * factorial(n - 1) # Return n multiplied by the factorial of (n-1).
    
# Prompt the user for a non-negative integer.

user_input = int(input("Enter a non-negative integer: ")) # Prompting the user for a non-negative number.

if user_input < 0: # Check if the input is a negative number.
    print("Please enter a non-negative integer.") # If it is a negative number.
else: # If the input is a non-negative number.
    result = factorial(user_input) # The factorial function of the users input.
    print(f"The factorial of {user_input} is {result}.") # Print the result.