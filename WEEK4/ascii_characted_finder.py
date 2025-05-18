# Program to convert an ASCII code to its character

# Program Started!
print("Program Started!")  # Start message to the user

# Asking the user to type in a number for ASCII code
print("Please enter an ASCII code:")

# Reading the user's input and converting it to a positive whole number
user_input = input()  # Get input from the user
ascii_code = abs(int(user_input))  # make sure it's a positive integer even if they type something negative

# Check if the number is between 32 and 126 (printable characters)
if ascii_code in range(32, 127):  # using range to check if the code is valid
    character = chr(ascii_code)  # getting the character for the valid ASCII code
    print(f"The character represented by the ASCII code {ascii_code} is {character}.")
else:
    # If the number is not valid, show an error message
    print("Sorry, that number is outside the printable ASCII range (32–126). Try again maybe :)")

# Program Ended!
print("Program Ended!")  # End message to show we're done
