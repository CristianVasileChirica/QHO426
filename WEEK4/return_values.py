# This function adds the two weights together and gives us the total
# We use 'return' to send that result back to whoever called this function
def sum_weights(weight_person, weight_inventory):
    total = weight_person + weight_inventory  # adding both weights together
    return total  # returning the result so it can be used elsewhere


# This function calculates the average by using the sum function we made above
# It's like teamwork between functions! They help each other.
def calc_avg_weight(weight_person, weight_inventory):
    total = sum_weights(weight_person, weight_inventory)  # using the result from the first function
    average = total / 2  # dividing by 2 because we have 2 items (person and inventory)
    return average  # sending back the average


# This function is in charge of talking to the user and deciding what to do
# It has no parameters because it handles everything inside

def run():
    print("What is the weight of the person?")
    person_input = input()  # taking input from the user

    print("What is the weight of their inventory?")
    inventory_input = input()  # taking second input from user

    # turning the text inputs into actual numbers
    weight_person = int(person_input)
    weight_inventory = int(inventory_input)

    print("")  # just adding some breathing space in the output

    print("What would you like to calculate (sum or average)?")
    choice = input()  # letting the user decide which result they want

    print("")

    # checking what the user typed and acting accordingly
    if choice == "sum":
        result = sum_weights(weight_person, weight_inventory)
        print("The sum of weights is", result, ".")
    elif choice == "average":
        result = calc_avg_weight(weight_person, weight_inventory)
        print("The average weight is", result, ".")
    else:
        print("Sorry, I didn't understand. Please type 'sum' or 'average'.")


# Run the program
run()
