"""
Assignment: Simple Interest Calculator
Objective:
Write a Python function named calculate_interest that computes and returns simple interest based on given parameters.
Background
Simple interest is calculated using the formula:
simple interest = (principal * rate of interest * Time) / 100
Function Requirements
A main function should control the logic of the program
Create and call a function should be named calculate_interest.
It should take three parameters that you get from the user:
1. Principal - The initial amount
2. Rate - The annual interest rate (percentage)
3. Time - The investment duration in years.
Use the return keyword to send back the computed interest to a variable in the main function.
Print the result using formatted strings in the main function.
Example
If you call calculate_interest(1000, 5, 2), the function should return 100 as the simple interest.
Task instructions
1. Define the function calculate_interest with appropriate parameters.
2. Apply the formula to calculate the simple interest.
3. Return the calculated interest.
4. Print the result using an f-string:
print(f"The simple interest for $(principal:,.2f) at {rate}% over {time} years is ${interest:,.2f).")
"""
#1 Define the function calculate_interest with appropriate parameters.
def calculate_interest(principal, rate, time):
    #2 Apply the formula to calculate the simple interest.
    interest = (principal * rate * time) / 100
    #3 Return the calculated interest.
    return interest
# The user input and main function logic for this assignment.
def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time in years: "))

# calculate_interest function
    interest = calculate_interest(principal, rate, time)

#4 Print the result using an f-string:
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")

if __name__ == "__main__": # Running the program
    main()