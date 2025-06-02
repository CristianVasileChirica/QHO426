import json


# This function reads a JSON file and displays its contents
def read(file_path):
    # Open the JSON file and load its content
    with open(file_path) as file:
        data = json.load(file)

        # Extract and display the location name
        location = data["location"]
        print(f"Place Name: {location}")

        # Extract and display the population size
        population = data["population"]
        print(f"Population Size: {population}")
        print("")  # For spacing

        # Loop through each bot in the data and display its stats
        bots = data["bots"]
        for bot in bots:
            name = bot["name"]
            stats = bot["stats"]
            # Display the bot's name and stats in a clear format
            print(f"{name} has a strength level of {stats['strength']} and a speed level of {stats['speed']}.")
        print("")  # For spacing


# This function calls read() with the futurama.json file path
def run():
    read("futurama.json")


# Ensure run() executes only when the file is run directly
if __name__ == "__main__":
    run()
