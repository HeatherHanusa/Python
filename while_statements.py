"""
Assignment
Write the program "99 Bottles of beer on the Wall" using a while loop. Be mindful to change the word 'bottles' to 'bottle' when down to the last one. You must do the full 99 bottles; the sample shows the last 3 versus.
"""
#Countdown from 99 to 0
count = 99

while count > 0:  # This makes the loop stop at 0
    word_now = "bottle" if count == 1 else "bottles"
    next_count = count - 1
    if next_count == 1: # This is for the numbers 1 to 0
        print(f"{count} bottle of beer on the wall")
        print(f"{count} bottle of beer")
        print("Take one down and pass it around,")
        print(last_line)
        last_line = "No more bottles of beer on the wall!"
    else: # This is for the numbers 99 to 2
        print(f"{count} bottles of beer on the wall")
        print(f"{count} bottles of beer")
        print("Take one down and pass it around,") 
        print("no more bottles of beer on the wall!")
        word_next = "bottle" if next_count == 1 else "bottles"
        last_line = f"{next_count} {word_next} of beer on the wall!"
    if count - 1 == 1:
        last_line = "1 bottle of beer on the wall!"
    count -= 1  # <- This makes the loop start to count down

