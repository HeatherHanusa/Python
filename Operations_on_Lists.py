"""
Assignment: Ticket Sales
Objective: Develop a program to manage ticket sales for an event.
Assignment Steps:
1. Create a list representing 20 seats, numbered 1 to 20.
2. Display the list of avaliable seats to the customer
3. Prompt the customer to select a seat from the list of avaliable seats and display the updated list.
4. Remove the selected seat from the list of avaliable seats and display the updated list.
5. Id the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
6. Ensure the program gracefully handles all scenarios and is user-friendly.
"""
# Created a list of seats numbered 1 to 20
seats = list(range(1,21))
# Avaliable seats for customer
print("Avaliable Seat:", seats)
# Prompt the customer to select a seat
choice = int(input("Please select a seat from the avaliable seats: "))
# Remove sold seats from the list and update the list
if choice in seats:
    seats.remove(choice)
    print("Seat", choice, "has been successfully purchased.")
else:
    print("Invalid choice or already sold seat. Please try again!")