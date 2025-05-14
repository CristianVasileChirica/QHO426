# letter_printer.py
# This program prints each letter of a phrase on a separate line

# Ask the user for their phrase
print("What phrase do you want to see?")
user_phrase = input()

# Add a blank line for better formatting
print(" ")

# Let the user know we're processing their input
print("outputting...")

# Add a blank line before showing the results
print("")

# Print a message before showing the letters
print("The phrase is: ")

# Here we use the 'in' membership operator to go through each character
# This is easier than using indexes because we don't need to track position
# The variable 'letter' will hold each character one by one as we go through the phrase
for letter in user_phrase:
    # Print each letter on its own line
    # I don't need to add line breaks because print() adds them automatically
    print(letter)