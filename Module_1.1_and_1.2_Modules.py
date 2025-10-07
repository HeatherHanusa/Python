"""
Assignment: Number Guessing Game
In this assignment, you will create a Python program that generates a random number between 1 and 100.
Your program should allow the user to guess the number, and provide feedback on how close their guess is to the actual number.

Assignment Objectives:
Use the random module to generate a random number
Implement a while loop to allow continuous guessing until the correct number is guessed.
Use the abs() function to determine the difference between the guess and the actual number.
Provide feedback based on the proximity of the guess to the actual number:
If the difference is within 5, print "Very Hot".
If the difference is within 15, print "Hot".
If the difference is within 25, print "Cool"
If the difference is more than 25, print "Cold".
Make sure to call the main function!
After completing the program, upload it to your GitHub repository.
Submit the link to your GitHub repository in Canvas.
"""
# Import the random module that will generate the random number
import random

def main():
    # Generating a number between 1 and 100 randomly.
    number = random.randint(1, 100)
    print("Can you guess the number I am thinking of between 1 and 100?") # Question for the user

# The variable that the user uses to guess
    guess = None

# Looping continues until the number is guessed
    while guess != number:
    # Where the user can guess
        guess = int(input("Enter your guess: "))

# Calculating the difference between the guess and the actual number.
        difference = abs(number - guess)

# Feedback for the user if they are close to guessing the number or not.
        if difference == 0:
            print("Correct! You guessed the right number!")
        elif difference <= 5:
            print("Very Hot")
        elif difference <= 15:
            print("Hot")
        elif difference <= 25:
            print("Cool")
        else:
            print("Cold")
# Making sure the main function runs the program
if __name__ == "__main__":
    main()