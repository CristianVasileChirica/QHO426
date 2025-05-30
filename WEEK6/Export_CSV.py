# This function will export user-entered item data to a CSV file
def export(file_path, num_items):
    # Display message to show export process is starting
    print("Exporting...")
    print("")  # Add a blank line for better spacing

    # Open the file in append mode ("a") so we don't overwrite existing data
    with open(file_path, "a") as file:
        # Loop to collect and write data for the specified number of items
        for _ in range(num_items):
            # Ask user for item ID and store it in item_id
            item_id = input("Please enter the item id:\n")
            # Ask user for item name and store it in item_name
            item_name = input("Please enter the item name:\n")
            # Ask user for item colour and store it in item_colour
            item_colour = input("Please enter the item colour:\n")

            # Write the user input to the CSV file, formatted correctly
            file.write(f"{item_id},{item_name},{item_colour}\n")

    # Display message when export process is done
    print("")
    print("Done!")


# This function runs the export task with the desired CSV file and item count
def run():
    # Call export with the file path "exported_items.csv" and number of items to export
    export("exported_items.csv", 2)


# This code ensures run() runs only when the file is executed directly
if __name__ == "__main__":
    run()
