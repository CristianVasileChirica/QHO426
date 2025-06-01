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


# This function displays all the keys in the dictionary on separate lines
def display_keys(data):
    print("Keys:")  # Section header
    for key in data.keys():
        print(key)
    print("")  # Empty line for spacing


# This function displays all the values in the dictionary on separate lines
def display_values(data):
    print("Values:")  # Section header
    for value in data.values():
        print(value)
    print("")  # Empty line for spacing


# This function displays key-value pairs in the format "key: value"
def display_items(data):
    print("Pairs:")  # Section header
    for key, value in data.items():
        print(f"{key}: {value}")
    print("")  # Empty line for spacing


# This function runs the task: calls pattern and displays keys, values, and pairs
def run():
    # Call pattern() to get the dictionary and store it in pattern_dict
    pattern_dict = pattern()

    # Display the original dictionary
    print("Dictionary:")
    print(pattern_dict)
    print("")  # Empty line for spacing

    # Call the functions to display keys, values, and pairs
    display_keys(pattern_dict)
    display_values(pattern_dict)
    display_items(pattern_dict)


# Ensure run() runs only when the file is executed directly
if __name__ == "__main__":
    run()
