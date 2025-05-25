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

# Function to create and return the list of movement directions
def directions():
    # This function will build a list of steps (directions only)
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps  # Send the list back

# Function to display menu with indexed directions
def menu():
    print("Please select a direction:")  # Starting prompt
    steps_list = directions()  # Get the list of directions
    print("")  # Extra space for readability
    for index in range(len(steps_list)):
        direction = steps_list[index]  # Get direction at current index
        print(f"{index}: {direction}")  # Print index and direction
    print("")  # Extra space after listing

# Function to run task 3
def run_task3():
    menu()  # Simply call the menu function

# Now we can call run_task3() to test the output
run_task3()
