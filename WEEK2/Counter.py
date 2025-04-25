# This program will count how many even and odd numbers the user has entered

# First, we  need variables to count even and odd numbers
# These are like little boxes that store numbers
even_counter = 0  # Starts at 0 because we haven't counted any even numbers yet
odd_counter = 0   # Starts at 0 because we haven't counted any odd numbers yet

# Now will ask for the first number
print("Please enter the first whole number.")
first_number = int(input())  # Gets what the user types and makes it a whole number

# Checking  if the first number is even or odd
# When we divide by 2, if there is no remainder (0), means it's even!
if first_number % 2 == 0:  # The '%' symbol gives the remainder after division
 even_counter = even_counter + 1  # Adding 1 to the even counter
else:
    odd_counter = odd_counter + 1    # Adding 1 to the odd counter

# Now for the second number
print("Please enter the second whole number.")
second_number = int(input())

# Checking if the second number is even or odd
if second_number % 2 == 0:
    even_counter = even_counter + 1
else:
    odd_counter = odd_counter + 1

# And finally the third number
print("Please enter the third whole number.")
third_number = int(input())

# Checking if the third number is even or odd
if third_number % 2 == 0:
    even_counter = even_counter + 1
else:
    odd_counter = odd_counter + 1

# Adding  a blank line before showing the result for a better look
print("")

# Showing the results!
print(f"There were {even_counter} even and {odd_counter} odd numbers.")

# Adding a blank line at the end, for a better look
print(" ")