# This program will calculate the sum of the first 100 numbers


# Displaying initial message to let the user know what we're doing
print("Calculating the sum of the first 100 numbers...")
print("") # Adding a blank line for better readability

# Creating our variables
current_number = 1   # We start counting from 1
total_sum = 0 # This will hold our final answer

# We will use the while loop for adding numbers from 1 to 100
while current_number <= 100: # This will keep going until we reach 100
    total_sum = total_sum + current_number # Adding our current number to our total
    current_number = current_number + 1 # Move to the next one

print("...Done! The answer is " + str(total_sum) + ".")

print("") # Adding an empty line

