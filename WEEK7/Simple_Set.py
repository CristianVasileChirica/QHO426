# This function creates and returns a set with observed items
def observed():
    # Create a set called observations with initial items
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}

    # Return the set (duplicates are automatically removed in sets)
    return observations


# This function runs the task by calling observed() and displaying the result
def run_task1():
    # Call the observed function and store the result in a variable
    observations_set = observed()

    # Print an empty line for spacing
    print("")

    # Display the set of observations
    print(observations_set)

    # Print another empty line for a clean ending
    print("")


# Ensure run_task1() runs only when the file is executed directly
if __name__ == "__main__":
    run_task1()
