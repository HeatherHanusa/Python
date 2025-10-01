"""
Assignment: NATO Phonetic Alphabet Dictionary
Your mission is to create a Python program that uses a dictionary to translate letters into the NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using the NATO codes.
Steps to follow:
1. Create a NATO Phonetic
Alphabet Dictionary:
Construct a dictionary in Python named nato_alphabet, where each key is a letter, and its value is corresponding NATO phonetic term.
2. Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and print the NATO phonetic term.
3. Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
4. Test Your Program:
Test the program with various inputs, ensuring it works as expected.
Example Output:
If the user inputs 'Hello':
Hotel
Echo
Lima
Lima
Oscar
"""
#1 Create a NATO Phonetic Alphabet Dictionary
nato_alphabet = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
} # I looked up the NATO phonetic alphabet online to create this dictionary.

#2 Develop the spelling program
def spell_with_nato(word):
    for letter in word.upper():
        if letter in nato_alphabet:
            print(nato_alphabet[letter])
        else:
            print(f"{letter} is not a valid letter in the NATO alphabet.")

#3 Incorporate a main function
def main():
    # Ask the user for their input
    user_input = input("Enter a word using the NATO Phonetic Alphabet: ")
    spell_with_nato(user_input)

#4 Run the program and test it
if __name__ == "__main__":
    main()