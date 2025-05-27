# Returns a tuple with names of teachers
def teachers():
    return ("Prins", "Darren")


# This function will find the minimum and maximum from a tuple of likelihoods
def likelihood_min_max():
    # Here we create a tuple with some likelihood values for steps falling
    likelihoods = (50, 38, 27, 99, 4)

    # Find the smallest value (minimum) using the min() function
    smallest = min(likelihoods)

    # Find the largest value (maximum) using the max() function
    largest = max(likelihoods)

    # We return both values as a tuple because we need to give back two numbers
    return (smallest, largest)


# This function runs the task and displays the results nicely
def run_task2():
    # Call the likelihood_min_max function and store the result in min_max_result
    min_max_result = likelihood_min_max()

    # Print an empty line for better readability
    print("")

    # Display the results with clear text, accessing each value from the tuple
    print("Minimum likelihood of falling: " + str(min_max_result[0]) + "%")
    print("Maximum likelihood of falling: " + str(min_max_result[1]) + "%")

    # Another empty line for a clean end of output
    print("")


# Finally, call the run_task2 function to see the results when the program runs
run_task2()
