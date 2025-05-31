# This function asks the user for 7 observations and returns them as a list
def observed_items():
    # Create an empty list to hold the observations
    observations = []

    # Loop to collect 7 user inputs
    for i in range(7):
        # Prompt the user for each observation
        item = input("Please enter an observation:\n")
        # Add the input to the list
        observations.append(item)

    # Return the list of observations
    return observations


# This function counts how many times each observation was made
def run_task2():
    # Display a message that counting is starting
    print("Counting observations...")
    print("")  # Print an empty line for better spacing

    # Call observed_items to get the list of observations
    data = observed_items()

    # Create an empty set to store unique tuples of (item, count)
    observation_set = set()

    # Loop through each unique item in the list
    for item in data:
        # Create a tuple of the item and its count in the list
        count_tuple = (item, data.count(item))
        # Add the tuple to the set (duplicates will be ignored)
        observation_set.add(count_tuple)

    # Print an empty line for spacing before showing the final output
    print("")

    # Loop through the set and print how many times each unique item was observed
    for observation in observation_set:
        print(f"{observation[0]} observed {observation[1]} times.")

    # Print another empty line to clean up the output
    print("")


# Ensure run_task2() runs only when the file is executed directly
if __name__ == "__main__":
    run_task2()

