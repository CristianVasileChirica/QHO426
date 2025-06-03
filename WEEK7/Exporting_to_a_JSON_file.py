import json


# This function reads JSON data from a file and returns the data
def read_task2(file_path):
    # Display a message to show reading has started
    print("Reading...")

    # Open the file and load the JSON data
    with open(file_path) as file:
        data = json.load(file)

    # Display a message to show reading is done
    print("Done!")
    print("")  # For spacing

    # Return the loaded data
    return data


# This function saves JSON data to a specified file
def save(file_path, data):
    # Display a message to show exporting has started
    print("Exporting...")

    # Open the file in write mode and write the JSON data with indentation
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    # Display a message to show exporting is done
    print("Done!")
    print("")  # For spacing


# This function runs the export task by reading and then saving the data
def run_task2():
    # Calls read_task2 with "futurama.json" and store the data in json_data
    json_data = read_task2("futurama.json")

    # Call save with "exported.json" and the data to be saved
    save("exported.json", json_data)


# Ensure run_task2() executes only when the file is run directly
if __name__ == "__main__":
    run_task2()
