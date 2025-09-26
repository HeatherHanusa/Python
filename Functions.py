"""
Assignment: Create a Program to Calculate Areas
objective: Write a Python program that includes two functions - one to calculate the area of a square and another for the area of a circle.
Instructions:
1. Start with Function Definitions:
Define two functions: square and circle.
Each function should take one parameter (side for square, radius for circle).
2. Write the square function:
Calculate the area as side * side and display the result: "The area of the square is [result] square units."
3. Write the circle function:
Calculate the area using the formula: area = 3.14 * radius * radius for circle).
Display the result: "The area of the circle is [result] square units."
4. Test Your Functions:
Call square and circle with sample values.
"""
#1 Function Definition For Square
def square(side):
    area = side * side #2 Sqaure function to calculate area of square
    print(f"The area of the square is {area} square units.")

# Function Definition For Circle
def circle(radius):
    area = 3.14 * radius * radius #3 Circle function to calculate area of circle
    print(f"The area of the circle is {area} square units.")

#4 Testing the functions
square(10) #4 Example of the square function: The area of this example is 100 square units
circle(7) #4 Example of the circle function: The area of this example is 153.86 square units
