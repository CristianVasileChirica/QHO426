# This function searches the books in a file and separates sections from books
def search_books(file_path):
    # Display a message that the search is starting
    print("Searching...")

    # Create empty strings to hold sections and books
    sections = ""
    books = "Books:\n"

    # Open the file using with to make sure it closes automatically
    with open(file_path) as file:
        # Loop through each line in the file
        for line in file:
            line = line.strip()  # Remove extra spaces and newlines
            # Check if the line starts with "Section"
            if line.startswith("Section"):
                # Add the line with a newline to the sections string
                sections += line + "\n"
            else:
                # Add the line with a newline to the books string
                books += line + "\n"

    # Display a message that the search is done
    print("Done!")
    print("")  # Empty line for clarity

    # Return a single string combining sections and books with two newlines in between
    return sections + "\n\n" + books


# This function saves the data to a new file
def save(file_path, data):
    # Display a message that saving is starting
    print("Saving...")

    # Open the file for writing, creating it if it doesn't exist
    with open(file_path, "w") as file:
        # Write the data to the file
        file.write(data)

    # Display a message that saving is done
    print("Done!")
    print("")  # Empty line for clarity


# This function runs the task by calling search_books and save functions
def run_task4():
    # Call search_books with "books.txt" and save the result in data
    data = search_books("books.txt")

    # Call save with "section-books.txt" and pass data to it
    save("section-books.txt", data)


# This code makes sure run_task4() runs only when the file is executed directly
if __name__ == "__main__":
    run_task4()
