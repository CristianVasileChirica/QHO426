# This function returns a dictionary with a short pattern
def short_pattern():
    # Create a dictionary with the sequence and occurrences
    pattern = {
        "sequence": "101",
        "occurrences": 5
    }
    # Return the dictionary
    return pattern


# This function returns a dictionary with a medium pattern
def medium_pattern():
    # Create a dictionary with the sequence and occurrences
    pattern = {
        "sequence": "111000",
        "occurrences": 25
    }
    # Return the dictionary
    return pattern


# This function returns a dictionary with a long pattern
def long_pattern():
    # Create a dictionary with the sequence and occurrences
    pattern = {
        "sequence": "1100110011001100",
        "occurrences": 50
    }
    # Return the dictionary
    return pattern


# This function runs the task: creating and displaying a dictionary of dictionaries
def run_task3():
    # Display a message to indicate that pattern analysis is starting
    print("Analysing the patterns...")
    print("")  # For spacing

    # Create the main dictionary with nested dictionaries as values
    pattern_dict = {
        "short sequence": short_pattern(),
        "medium sequence": medium_pattern(),
        "long sequence": long_pattern()
    }

    # Display each key-value pair in the dictionary
    for key, value in pattern_dict.items():
        print(f"{key}: {value}")

    print("")  # For spacing


# Ensure run_task3() runs only when the file is executed directly
if __name__ == "__main__":
    run_task3()
