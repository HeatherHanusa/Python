"""
Assignment: Create and Use Tuples
Now, let's practice using tuples. Imagine you're planning the classes for a programming certificate. You need to list out six classes. 
Here's what you need to do:

1. Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
2. Weite a program that uses a for loop to print each class in the tuple.
3. Use the len function to print how many courses are in the tuple.
Make sure to use a main function for this program.
"""
# Create a tuple named programming_classes.
programming_classes = (
    'Intro to Python', 
    'Advanced Python', 
    'Database Essentials', 
    'Web Development Basics', 
    'Data Structures in Python', 
    'Web Design Fundamentals'
) # The six programming classes.

# Use a for loop to print each class in the tuple.
print ("Programming Classes:")
for course in programming_classes:
    print(course)

# Print each class in the tuple.
print("\nTotal number of courses:", len(programming_classes)) # Use the len function to print how many courses are in the tuple.

# Main Function.
if __name__ == "__main__":
    pass