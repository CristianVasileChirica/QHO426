import csv


# This function reads the content of a CSV file and displays headings and values
def read_csv(file_path):
    # Open the CSV file using with to make sure it closes automatically
    with open(file_path) as file:
        # Create a CSV reader object to read the file
        csv_reader = csv.reader(file)

        # Read the first line (headings) using next()
        headings = next(csv_reader)

        # Print the headings nicely
        print("Headings:")
        print(headings)
        print("")  # Empty line for spacing

        # Print a message to indicate that values will follow
        print("Values:")

        # Loop through the rest of the lines in the file
        for values in csv_reader:
            # Print each row of values
            print(values)

    # File is automatically closed when with block ends


# This function runs the task by calling read_csv with clothing.csv
def run_task1():
    # Call the read_csv function with the file path "clothing.csv"
    read_csv("clothing.csv")


# This code ensures run_task1() runs only when the file is executed directly
if __name__ == "__main__":
    run_task1()
