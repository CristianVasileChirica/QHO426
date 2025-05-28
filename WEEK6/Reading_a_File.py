# This function reads and displays a certain number of characters from the file
def display_chars(file_path, num_chars):
    # Open the file using with so it closes automatically when done
    with open(file_path) as file:
        # Read the specified number of characters
        data = file.read(num_chars)
        # Print the message with the read characters
        print("The first " + str(num_chars) + " characters are:")
        print(data)
        # Print an empty line to make output easier to read
        print("")


# This function reads and displays the first line from the file
def display_line(file_path):
    # Open the file using with so it closes automatically
    with open(file_path) as file:
        # Read the first line and remove any extra spaces or newlines
        first_line = file.readline().strip()
        # Print the message with the first line
        print("The first line is:")
        print(first_line)
        # Print an empty line to make output easier to read
        print("")


# This function reads and displays the entire content of the file
def display_text(file_path):
    # Open the file using with so it closes automatically
    with open(file_path) as file:
        # Read the full text from the file
        full_text = file.read()
        # Print the message with the full text
        print("The full text is:")
        print(full_text)
        # Print an empty line to make output easier to read
        print("")


# This function calls the other functions with "library.txt" as the file path
def run_task2():
    # Call display_chars with 5 characters to read
    display_chars("library.txt", 5)

    # Call display_line to display the first line
    display_line("library.txt")

    # Call display_text to display the entire text
    display_text("library.txt")


# This code ensures run_task2() runs only when the file is executed directly
if __name__ == "__main__":
    run_task2()
