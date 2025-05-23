# Display the first item i.e. apple
print("apple")  # Just showing an example from the task description

# Update the second item i.e. replace banana with berry
# This is just an illustration, not part of the task code
# So no need to include fruits list from the original example

# Remove the third item i.e. removes cherry
# Not doing this here because we're focusing on movement paths

# Function to create and return a path of movements
def movements():
    # This function builds a path using a list
    # The list has directions and steps, taking turns
    path = [
        "Move Forward", 10,  # First move: go forward 10 steps
        "Move Backward", 5,  # Then back up 5 steps
        "Move Left", 3,      # Slide left for 3 steps
        "Move Right", 1      # Finally move right for 1 step
    ]
    return path  # Send the list back to the caller


# Function to run the task and display the formatted movement instructions
def run_task2():
    print("Moving...")  # Starting message

    path_instructions = movements()  # Call the other function to get our path

    # We loop through the list using steps of 2, because we want to pair direction and steps
    for i in range(0, len(path_instructions), 2):
        direction = path_instructions[i]      # This grabs the movement direction (a string)
        steps = path_instructions[i + 1]      # This grabs the step count (a number)

        # We now print the instruction in the format asked by the task
        print(f"{direction} for {steps} steps")


# Call the main function to test it
run_task2()
