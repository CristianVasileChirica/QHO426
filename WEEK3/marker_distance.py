# This program checks how many characters (dashes) are between two markers in a string

# Asking the user to type in a sequence made of dashes and two markers
sequence = input("Please enter a sequence\n")

# Adding some space to keep things readable
print("")

# Asking the user to type which character is used as the marker
marker = input("Please enter the character for the marker\n")

# Another small gap before showing results
print("")

# We try to find where the first marker is
first_index = sequence.find(marker)

# Now we find where the second marker is
# We start looking after the first marker so we don’t count it again
second_index = sequence.find(marker, first_index + 1)

# Now we calculate the distance (how many characters are between them)
# We subtract the positions and remove 1 so we don’t count the marker itself
distance = second_index - first_index - 1

# Just in case something goes wrong (e.g., only one marker), we protect the code
# But for now we assume the user enters two markers as the task says

# Showing the final result
print(f"The distance between the markers is {distance}.")
