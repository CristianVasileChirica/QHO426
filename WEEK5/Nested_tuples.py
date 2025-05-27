# Returns a list of teachers with tuples
def list_of_teachers():
    return [("Drishty", "Course Leader"), ("Darren", "Module Leader")]


# This function returns a list of tuples representing steps and their likelihoods
def steps():
    # Create a list called likelihoods where each item is a tuple with step name and likelihood value
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]

    # Return the full list of tuples
    return likelihoods


# This function runs the task to separate good and bad steps
def run_task3():
    # Call the steps function to get the list of step tuples
    step_data = steps()

    # Create two empty lists to store good and bad steps
    good_steps = []
    bad_steps = []

    # Print an empty line for spacing the output
    print("")

    # Loop through each tuple in step_data (which contains step name and likelihood)
    for step in step_data:
        step_name = step[0]  # Get the step name
        likelihood = step[1]  # Get the likelihood value

        # Check if the likelihood is 50 or more (bad step)
        if likelihood >= 50:
            bad_steps.append(step)  # Add to bad_steps list
        else:
            good_steps.append(step)  # Otherwise, add to good_steps list

    # Display the total number of good and bad steps
    print("Good steps: " + str(len(good_steps)) + ", Bad steps: " + str(len(bad_steps)))

    # Another empty line for a clean ending
    print("")


# Finally, call the run_task3 function to see the output when the program runs
run_task3()
