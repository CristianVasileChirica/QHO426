# This program compares two numbers to find which one is smaller
# We will use if, elif and else statement with the comparison operators

# Asking user for the first number
print("please enter the first number.")
first_number = float(input()) # getting text from keyboad, float() turns it into a number

# Ask user for the second number
print("please enter the second number.")
second_number = float(input()) # Storing the second number

print("") # Printing an empty line

# Now we need to check which number is smaller using comparison operators
# means less tan
# means bigger than
# == means equal to

if first_number > second_number:  # If the first number is bigger than the second
    print("The second number is the smallest!)")
elif first_number < second_number:
    print("The first number is the largest!")
else: # If we get here there must be equal
    print("Both are equal!")

print(" ") # Add a blank line at the end
