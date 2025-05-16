# This program gets a single character from the user and shows its ASCII code

# Starting message to let the user know the program is running
print("Program Started!")

# Adding a space for better readability
print("")

# Asking the user to enter just one character (like a letter, number, or symbol)
print("Please enter a standard character:")
user_input = input()  # Reading what the user types

# Another space for separation
print("")

# Now we check if the user entered exactly one character
if len(user_input) == 1:
    # If they did, we get the ASCII value using ord()
    ascii_value = ord(user_input)

    # We now show the result using f-string formatting
    print(f"The ASCII code for {user_input} is: {ascii_value}")
else:
    # If more than one character was entered, we show an error message
    print("Oops! Please enter just one single character next time.")

# Final message to show we're done
print("")
print("Program Ended!")
