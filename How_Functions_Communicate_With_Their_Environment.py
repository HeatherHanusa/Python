"""
Assignment: Your Own Madlib
Objective:
Develop a Python-based Madlib based on a song of your choice. The program should collect at least 9 different pieces
of information from the user and incorporate them into the song using named arguments. The goal is to practive using
fuunctions, user input, and string manipulation in Python.
Important note:
Choose any some you like for your Midlab, but remember, no Rickrolling! Be creative and respectful in your song choice.
Task:
1. Select a song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with innapropriate or offensive content.
2. Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, objectives, nouns, places, etc.
3. Write the function:
Define a function named custom_song that takes at least 8 parameters corresponding to the variables you have identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
4. Collect user input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
5. Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function.
"""
# Step 1: Select a somg
# The duck song by Bryant Oden

# Step 2: Identify Variables
input_animal = input("Enter an animal: ")
input_drink = input("Enter a drink: ")
input_gender = input("Enter a gender: ")
input_fruit = input("Enter a fruit: ")
input_temperature = input("Enter a temperature: ")
input_cup = input("Enter a type of cup: ")
input_walk = input("Enter a type of walk: ")
input_time = input("Enter day, month, or year: ")

# step 3: write the function
print ("\n\n")
print (f" The {input_animal} walked in to the {input_drink} stand")
print (f" And he said to the {input_gender} runnin' the stand")
print (f" Hey (bam bam bam) got any {input_fruit}?")
print (f" The {input_gender} said no, we just sell {input_drink}")
print (f" But it's {input_temperature}, and it's fresh, and it's all home-made!")
print (f" Can I get you a {input_cup}?")
print (f" The {input_animal} said, I'll pass.")
print (f" Then he {input_walk} away, {input_walk} {input_walk}.")
print (f" Then he {input_walk} away, {input_walk} {input_walk}.")
print (f" Then he {input_walk} away, {input_walk} {input_walk}.")
print (f" Till the very next {input_time} (bom, bom, bom, bom, bom, babom)")
