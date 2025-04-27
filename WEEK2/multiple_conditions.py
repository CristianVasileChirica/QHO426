# An adventure Game with multiple conditions

# First, we need to ask the user what type of adventure they would like
# The print Function shows the message to the user
print("what type of adventure should i have?")

# The input function gets text from the user and stores it in a variable
adventure_type = input()

# Always adding a line for better readability, Keeps the empty line after input
print("")

# Now we are using a if statement to make decisions based on the user's input
# The 'or' operator means " if either conditions is true"
# So if the adventure type is EITHER "scary2 OR "short", the first message will show
if (adventure_type == "scary") or (adventure_type == "short"):
    # The code will run if the adventure type is "scary" or "short"
    print("entering the dark forest!")

# The elif statement is checking if the first 'if' is False
# If the adventure_type is Either "safe" OR "long" the second message will show
elif (adventure_type == "safe") or (adventure_type == "long"):
    # This code will run if the adventure type is "safe" or "long"
    print("taking the safe route!")

# The 'else' statement runs if none of the above conditions are true
else:
    # This code will run if the adventure is not scary, short, safe , or long
    print("Not sure which route to take.")

