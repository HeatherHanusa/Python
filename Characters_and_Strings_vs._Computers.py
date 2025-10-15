"""
Assignment: ASCII Value Finder
At the end of this lesson, students will be able to:
Convert a character to its ASCII value using Python.
Convert an ASCII value back to a character.
Implement input validation using loops and error handling.
Step-by-Step Instructions
Start Your Python Script:
Open your Python environment and start a new script.
Use a main() function to organize your code.
Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:
Ensure the user enters preisely one character.
Use len() to check input length.
Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Example:
ascii_value = ord(user_input)
Display the Resut:
Print the ASCII value to the user.
Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 32 and 127.
Use a try-except blcok to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
Example:
character = chr(ascii_input)
Test Your Program:
Run your script and try various characters and ASCII values.
Submit Your Work:
Upload your script to GitHub.
Submit a link to your repository.
"""
# Start your Python Script:
def main():
# Prompting the user for a single character
    user_input = input("Please enter a single character: ")

# Make sure the user enters only one character
    if len(user_input) == 1:
        print(f"You entered: {user_input}")
# Convert to ASCII Value
        ascii_value = ord(user_input)
        print(f"The ASCII value of {user_input} is {ascii_value}.")
    else:
        print("Error: Please enter only one character.")

# Use a try_except block to handle invalid inputs
    try:
      ascii_input = int(input("Enter a number between 32 and 127: "))
      if 32 <= ascii_input <= 127:
        character = chr(ascii_value)
        print(f"The character for ASCII value {ascii_input} is {character}.")
      else:
          print("Number must be between 32 and 127.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
   main()