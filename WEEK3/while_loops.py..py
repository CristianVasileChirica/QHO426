# This is a while Loop program!
# It's supposed to be a robot removing apples from a box

# First we will need to ask the user how many apples to remove
print ("How many apples should i remove?")
#Adding an empty line to be more readable
print("")

# Get the number from the user and convert it to integer
# The int() function changes the text input to a number
apple_to_remove = int(input())

# I need to keep track of how many apples we have removed so far
# Starting with zero as i haven't removed sny yet
apples_removed = 0

# Now i'm going to use a while loop
while apples_removed < apple_to_remove:
    # This message appears each time an apple is removed
    print("Removed apple.")
    print("")

    # This is how we count that we have removed another apple
    # It's like saying apple_removed = apple_removed + 1
    apples_removed += 1

# I have added an extra message, it will run after the Loop is done
print(f"All done! I removed {apples_removed} apples from the box.")
print("")
