# This program helps us find our phone by asking a series of questions

# First, Let's ask the user were to look
print("Where should i look?")
# Get the user's response and store it in a variable
location = input()
print("") # Adding an empty line after user input


# Now we need to check where the user wants to look
# We'll use if-elif-else statements to handle different options

# Option is to check if the user wants to look in the bedroom
if location == "in the bedroom":
    # Ask for more specific Location within the bedroom
    print("Where in the bedroom should i look?")
    bedroom_location = input()
    print("") # Adding an empty line after user input for a better readability

    # Check the specific location in the bedroom
    if bedroom_location == " Under the bed":
        print("Found some shoes but no phone ?")
    else:
        print("Found some mess but no phone ?")

# Option 2: Checking if the user wants to look in the bathroom
elif location == "in the bathroom":
    # Ask for more specific location in the bathroom
    print("Where in the bathroom should i look?")
    bathroom_location = input()
    print("")

    # Check the specific location in the bathroom
    if bathroom_location == " In the bathtub ":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone")


# Option 3: Check if the user wants to look in the living room
elif location == "in the living room":
    # Ask Ask for a more specific location in the living room
    print("Where in the living room should i look?")
    living_room_location = input()
    print("")

    # Check specific Location in the Living room
    if living_room_location == " On the table":
        print("Yes!I found my Phone!")
    else:
        print("Found some stuff but no phone!")

# If the User enters anything else, we don't know where to look
else:
    print("")
    print("I don't know where that is but i will keep looking.")

# End of the program
print("") # Another empty line at the end of the program