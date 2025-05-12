#  Word character program

# First we ask the user to enter a word
print("What word do you see?")
print("") # Empty line just to look a bit better

# Getting the user input
user_word = input()

print("")

# Letting the user know we're starting character by character display
print("Display index positions ...")
print("") # Empty line

# Now we use a for loop to go through each character
# The variable 'i' represents the index position in the word
for i in range(0, len(user_word), 1):

    # Then print both the index and the character
    print("index", 1, ":", user_word[i])

    # After the loop we printe Done!
    print("")
    print("Done!")
