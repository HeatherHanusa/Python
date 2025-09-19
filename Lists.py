"""
Assignment
Welcome to your Python assignment! This task will help you practice working with lists, user input, and basic calculations. Follow the steps below.
Create a list: Start by creating a list named days that includes all seven days of the week.
Initialize an empty list: Create an empty list called steps to store the number of steps taken each day.
User input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
TOtal Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.
"""
# Created a list of days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Empty list to store steps
steps = []

# Use a loop to get user input for each day
for day in days:
    step_count = int(input(f"How many steps did you take on {day} ? "))
    steps.append(step_count)

# Daily steps display
print ("Your recorded steps")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")

# Total Steps
total_steps = sum(steps)
print(f"Total steps: {total_steps}")

# Average Steps
average_steps = total_steps / len(steps)
print(f"Average steps: {average_steps:.2f}")