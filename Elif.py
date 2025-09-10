"""
Directions:
Accept a numeric grade from the user and display a letter grade. The grading scale is 90-100: A, 80-89: B, 70-79:C, 60-69: D, Below 60: F
Check to see if the number given is between 0 and 100.
"""
# Program to convert numeric grade to letter grade

# Check if grade is valid
score = int(input("Enter your numeric score (0-100): "))

# Check if grade is valid
if score < 0 or score > 100:
    print("Invalid grade. Please enter a number between 0 and 100.")

# Elif
if score >= 90:
   print("Your letter grade is A.")
elif score >= 80:
   print("Your letter grade is B.")
elif score >= 70:
   print("Your letter grade is C.")
elif score >= 60:
    print("Your letter grade is D.")
else:
    print("Your letter grade is F.")
