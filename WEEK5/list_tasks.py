# This is a simple Python program to practice using lists
# We're creating a list of instructions to navigate a maze

def directions():
    """
    This function creates a list of directions for navigating a maze.
    It doesn't take any input.
    It returns a list of four basic movement instructions.
    """
    # Let's start by creating an empty list to hold the directions
    steps = []

    # Now we'll add the instructions one by one
    steps.append("Move Forward")   # go straight
    steps.append("Move Backward")  # step back
    steps.append("Turn Left")      # take a left turn
    steps.append("Turn Right")     # take a right turn

    # Finally, return the full list of instructions
    return steps


def run_task1():
    """
    This function runs task 1 by calling the 'directions' function
    and printing the list it returns.
    """
    # Let's get the list of steps from our directions function
    maze_steps = directions()

    # Now let's display the steps so we can see them
    print(maze_steps)


# This part makes sure the code only runs if this file is executed directly
if __name__ == "__main__":
    run_task1()
