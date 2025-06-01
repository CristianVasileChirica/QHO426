# This function creates a dictionary called sequences with specific pattern items
def pattern():
    # Create a dictionary with three key-value pairs representing sequences
    sequences = {
        "Short Sequence": 3,
        "Medium Sequence": 2,
        "Long Sequence": 1
    }
    # Return the dictionary
    return sequences


# This function runs the task by calling pattern() and displaying the result
def run():
    # Call pattern() to get the dictionary and store it in a variable
    pattern_dict = pattern()

    # Print an empty line for better readability
    print("")

    # Display the dictionary with the pattern
    print(pattern_dict)

    # Print another empty line for a cleaner output
    print("")


# Ensure run() runs only when the file is executed directly
if __name__ == "__main__":
    run()
