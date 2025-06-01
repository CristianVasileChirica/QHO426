# This function asks the user for 5 observations and returns them as a list
def observed_items():
    # Create an empty list to hold observations
    observations = []

    # Loop to collect 5 observations from the user
    for i in range(5):
        observation = input("Please enter an observation:\n")
        observations.append(observation)

    # Return the list of observations
    return observations


# This function allows the user to remove observations from the list
def remove_observations(observations):
    # Ask the user if they wish to remove observations
    while True:
        response = input("Do you wish to remove an observation (yes/no)?\n").lower()
        if response == "yes":
            # Ask what observation to remove
            remove_item = input("What observation do you wish to remove?\n")
            if remove_item in observations:
                # Remove the first occurrence of the observation
                observations.remove(remove_item)
                print("Done!")
                print("")  # For spacing
            else:
                print("That observation is not in the list.")
                print("")
        elif response == "no":
            # Exit the loop if the user says no
            break
        else:
            print("Please enter yes or no.")
            print("")


# This function runs the whole task: adding, removing, and displaying sorted observations
def run_task3():
    print("Counting observations...")
    print("")  # For spacing

    # Get the initial list of observations
    data = observed_items()

    # Allow the user to remove some observations
    remove_observations(data)

    # Sort the list of observations
    sorted_data = sorted(data)

    # Create a set to identify unique items (optional but helps with counting)
    unique_observations = set(sorted_data)

    # Display the sorted observations with their counts
    print("Observations:")
    for item in unique_observations:
        print(f"{item} observed {sorted_data.count(item)} times")

    print("")  # For spacing


# Ensure run_task3() runs only when the file is executed directly
if __name__ == "__main__":
    run_task3()
