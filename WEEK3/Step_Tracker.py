# The program helps to track remaining steps to target

# Asking the user for the remaining steps to the target
print("How far are we from the target?")
remaining_steps = int(input())

# Convert the imput string to a number
remaining_steps = int(remaining_steps)

#Add an empty line for a better redability
print("")

# This part is a bit tricky as i need to use range to count backwords

for steps_left in range(remaining_steps, 0, -1):
    # This will show how many steps are left
    # Using an if statement
    if steps_left ==1:
        print("1 step remaining")

        print("")

    else:
        print(f"{steps_left} steps remaining")

# Adding another empty line at the end
print("")

# Show a success message when we're done