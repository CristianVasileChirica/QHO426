def observed_items():
    observations = []
    for i in range(5):
        observations.append(input("Pls enter the Observation-"))
    return observations

def remove_observations(observations):
    while True:
        response = input ("Do you want to remove an observation? yes/no:").strip().lower()
        if response !='yes':
            break
        item_to_remove = input ("Enter the observation to remove:")
        if item_to_remove in observations:
            observations.remove(item_to_remove)
            print(f"Removed one occurrence of {item_to_remove}'.")
        else:
            print(f'"{item_to_remove}" is not in the list of observations.")

def run_task3():
    data = observed-items()
    remove_observations(data)
    print("\nFinal sorted obesevation counts:")
    unique_items = sorted(set(data))) # SORTED RETURNS A LIST
    for item in uniques_items
