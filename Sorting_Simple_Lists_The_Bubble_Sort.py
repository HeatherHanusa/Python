"""
Assignment:
Task:
1. Prompt the user to enter a five names.
2. Store the names in a list.
3. Sort the list using the Bubble Sort algorithm.
4. Print both the sorted and reversed lists.
Submission:
Save your program in a .py file and upload it to GitHub. Submit the GitHub link on canvas. Include comments in your code explaining your logic.
"""
# Prompt the user to enter five names
names = []
# Store the names in a list
for i in range(5):
    name=input("Enter name: ")
    names.append(name.lower()) # Lower case names

# Sort the names in a Bubble Sort algorithm
swapped = True # This tracks if a swap was made
while swapped: # Continue looping until no swaps occur
    swapped = False # Resets the swapped flag
    for i in range(len(names)-1): # Compare elements in the list
        if names[i] > names[i+1]:
            names[i], names[i+1] = names[i+1], names[i]
            swapped = True # A swap was made

# Sorted lists
print("Sorted names:", names)

# Reversed lists
names.reverse()
print("Reversed list", names)