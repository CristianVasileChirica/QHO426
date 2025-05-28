# This function searches through the lines in a given file
def search(file_name):
    # Display a message to show that the search is starting
    print("Searching...")
    print("")  # Empty line for better spacing

    # Open the file using with to ensure it closes automatically
    with open(file_name) as file:
        # Loop through each line in the file
        for line in file:
            # Remove any extra spaces or newline characters from the line
            location = line.strip()
            # Print the message with the location information
            print("Looked in " + location + ".")

    # Display a message to show that the search has finished
    print("")
    print("...Done!")


# This function runs the task by calling search() with "library.txt"
def run_task3():
    # Call the search function with the file name "library.txt"
    search("library.txt")


# This code ensures run_task3() runs only when the file is executed directly
if __name__ == "__main__":
    run_task3()
