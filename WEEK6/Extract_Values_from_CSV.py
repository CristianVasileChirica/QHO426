import csv


# This function extracts the names of clothing items from the CSV file
def extract(file_path):
    # Display message that extraction is starting
    print("Extracting...")
    print("")  # Empty line for spacing

    # Create an empty string to store the clothing names
    names = ""

    # Open the file using with to ensure it closes automatically
    with open(file_path) as file:
        # Create a csv_reader object to read the file
        csv_reader = csv.reader(file)

        # Skip the headings line using next()
        headings = next(csv_reader)

        # Loop through each remaining line in the CSV file
        for values in csv_reader:
            # Extract the clothing name (second column in the CSV)
            clothing_name = values[1]

            # Add the clothing name and a newline character to names string
            names += clothing_name + "\n"

    # Display message that extraction is done and show extracted names
    print("Done! The extracted items are as follows:")
    print(names)  # Print names with newlines already included


# This function runs the task by calling extract with clothing.csv
def run_task2():
    # Call extract function with the file path "clothing.csv"
    extract("clothing.csv")


# This code ensures run_task2() runs only when the file is executed directly
if __name__ == "__main__":
    run_task2()
