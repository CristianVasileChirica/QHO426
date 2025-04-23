# This Program checks if a number is even or odd
# It uses (%) modulo operator which gives us the remainder after division

# Ask the user to enter a whole number
print("Please enter a whole number.")
number = int(input()) # Convert the input to an integer

# Checking if the number is even or odd
# When we divide by 2, even numbers have a remainder of 0
# and odd numbers have a remainder of 1
if number % 2 ==0: # The % is the mofulo operator that gives us the remainder
    # This code runs if the remainder is 0 (even number)
    print(f"The number{number} is even.")
else:
   # This code runs if the remainder is not 0 (odd number)
    print(f"The number{number} is odd.")

    print(" ") # Add an empty line at the end