"""
Assignment: Daily Heart Rate Tracker
In this assignment, you will create a Python program to track your daily heart rate at different times and calculate the average.
Objective:
Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements:
Define time_slots as a list with times of the day (e.g.,"Morning","Midday","Afternoon","Evening").
Use a loop to prompt the user for heart_rates to store the time slots and their cooresponding heart rates.
Calculate the average heart rate and display it.
"""
# Define time slots as a list with times of day
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Empty list to store heart rate readings
heart_rates = []

# Loop to propt reader each time slot and prompt the user for their input
for slot in time_slots:
    rate = float(input(f"Enter your heart rate (in BPM) for {slot}: "))
    heart_rates.append(rate)

# Calculate average heart rate
total = sum(heart_rates)
average = total / len(heart_rates)
print("Average heart rate today: {average:.2f} BPM.")