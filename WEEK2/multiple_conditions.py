# Dark Forest Adventure Program using Logical AND operator

# Asking the user what they are hearing and storing their response
print("What did yiu hear?")
sound = input()

# Adding a blank line for better readability
print("")

# Asking the user what they saw and store their response
print("What did you see?")
sight = input()

# Add a blank line for readability
print("")

#Check if Both conditions are true using the AND operator
# Both conditions they must be true for the if statement to execute
if (sound == "grrr") and (sight == "two red eyes"):
    # This runs if both conditions are true
    print("There is a scary creature. I should get out of here!")
else:
    # This runs if any condition is false
    print("I am a little scared but i will continue.")
    print("")

