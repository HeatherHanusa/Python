"""
BMI Calculator Assignment
Objective: Create a BMI calculator that takes a user's weight and height, calculates their BMI, and categorizes it as an underweight, normal weight, overweight, or obese.
Requirements:
1. Global variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254m).
2. Main Function:
prompt the user for their weight in pounds and height in inches.
convert the inputs to metric units using global conversion constants.
calculate BMI using the formula BMI = weight / height * height).
Determine the BMI category based on standard ranges.
Display the BMI value and category.
3. Commenting
Include comments to explain ket parts of the code.
"""
# Global variables for conversion constants
pounds_to_kg = 0.453592 # 1 pound = 0.453592 kilograms
inches_to_m = 0.0254   # 1 inch = 0.0254 meters

# Main function to calculate BMI
def main():
    # Prompt the user for weight in pounds
    weight_pounds = float(input("Enter your weight in pounds: "))
    # Prompt the user for height in inches
    height_inches = float(input("Enter your height in inches: "))

    # Convert weight to kilograms
    weight_kg = weight_pounds * pounds_to_kg
    # Convert height to meters
    height_m = height_inches * inches_to_m

    # Calculate BMI using the formula BMI = weight / (height * height)
    bmi = weight_kg / (height_m * height_m)

    # Determine the BMI category based on standard ranges
    if bmi < 17.5:
        category = "Underweight"
    elif bmi < 26.5:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Display the BMI value and category
    print(f" Your BMI is {bmi:.2f}, which is considered {category}.")
# Call the main function to execute the program
main()
