# Brightness adjustment program

# Display message to ask the user for brightness level
print("What level of brightness is required?")
print("")  # Empty line for spacing

# Getting user input and convert it into an integer number
# I'm going to 'user_brightness'
user_brightness = int(input())

# Print a message to show we're starting the adjustment
print("\nAdjusting brightness...\n")

# Start the Loop from 2 up the user brightness Level + 1
# We want even numbers only: 2, 4, 6, etc.
for light_level in range(2, user_brightness + 1, 2,):

    # Printing the brightness Level using symbols multiplied by the number
    # We show how many * based on the current light_level
    print("Brightness Level:", "*" * light_level)
    print("")  # Empty line for spacing

# When done, we how a final message
print("\nComplete!")
