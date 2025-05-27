import os


# This function retrieves and displays the current working directory and its contents
def cwd():
    # Get the current working directory path using os.getcwd()
    path = os.getcwd()

    # Display the current working directory in a friendly format
    print(f"The current working directory is {path}")

    # Print an empty line for better output spacing
    print("")

    # Display the message about the directory's contents
    print("The directory contains the following files:")

    # Loop through each file/folder in the current directory and display its name
    for file in os.listdir(path):
        print(file)


# This function runs the task by calling cwd() after a "Processing..." message
def run():
    # Display a processing message so the user knows the program is working
    print("Processing...")

    # Print an empty line for clarity
    print("")

    # Call the cwd() function to display directory info
    cwd()


# Finally, call the run() function to execute the program when the file runs
run()
