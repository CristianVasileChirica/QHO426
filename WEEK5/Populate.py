# This function creates and returns a list of directions
def directions():
    # Create a list of steps
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps  # Return the list


# This function will show a menu, get user input, and return the selected direction
def menu_and_input():
    print("Please select a direction:")  # Show menu title

    # Call the directions function and store the list
    steps_list = directions()

    # Display each direction with its index number
    for index in range(len(steps_list)):
        print(f"{index}: {steps_list[index]}")

    # Get user input - we assume user enters a valid integer for simplicity
    choice = int(input())  # Get the number from user

    # Return the selected direction based on the index they provided
    return steps_list[choice]


# This function will run the main task 4 logic
def run_task4():
    route = []  # Create an empty list to store the escape route
    print("Working out escape route...")  # Start message

    # Do this 5 times - get directions from the user and add to the route
    for _ in range(5):  # Use underscore because we don't need the loop variable
        direction_chosen = menu_and_input()  # Call menu_and_input to get a direction
        route.append(direction_chosen)  # Add the chosen direction to the route list
        print("")  # Add an empty line for better readability after each selection

    # Show the complete escape route
    print(f"Escape route: {route}")


# This part makes the program run if we run this script directly
if __name__ == "__main__":
    run_task4()
