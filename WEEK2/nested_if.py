# This program helps classify books based on their cover type
# It shows how to put one decision inside another decision (nested if)

# First we will ask the user what type of cover the book has
print("What type of cover does the book have?")
cover_type = input()  # This will save what the user types
print(" ")  # Adding an empty line to make it look nicer

# Now we need to check what kind of cover it is
if cover_type == "soft":  # The == checks if cover_type equals "soft"
    # This code only runs if the cover is soft!

    # Now I need to ask a second question about the binding
    print("Is the book perfect-bound?")
    binding = input()  # Save the user's answer
    print(" ")  # Another empty line

    # This is a nested if - it's inside the first if statement
    # It only runs if the cover is already "soft"
    if binding == "yes":
        # This will run if cover is soft AND binding is "yes"
      print("Soft cover, perfect bound books are very popular!")
    else:
        # This runs if cover is soft BUT binding is NOT "yes"
        print("Soft covers with coils or stitches are great for short books")

else:
    # This code runs if the cover is NOT "soft"
    print("Books with hard covers are a bit more expensive!")
