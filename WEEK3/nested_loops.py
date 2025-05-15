# nested_loops.py
# This program asks the user how many rows and columns they want,
# and then shows a grid of ASCII emoji :-) based on that.

# First, we greet the user and ask them for input

# Asking the user how many rows they want
rows = int(input("How many rows should I have?\n"))

# Adding an empty line for spacing before next question
print("")

# Asking the user how many columns they want
cols = int(input("How many columns should I have?\n"))

# Adding some space before showing the emoji grid
print("")
print("Here I go:")
print("")

# This is the outer loop – it runs once for each row the user wants
for r in range(rows):
    # This inner loop runs once for each column in that row
    for c in range(cols):
        # We print a smiley face and stay on the same line
        print(":-)", end=" ")
    # After finishing one full row of smileys, we go to a new line
    print()

# Adding a space after the grid before ending message
print("")
# A nice way to show the user that the grid is complete
print("Done!")
