# This function will draw the ladder steps using the number we give it
# We call this a parameter - like passing ingredients into a recipe

def display_ladder(steps):
    # looping through each step the user asked for
    for step in range(steps):
        print("| |")       # side of the ladder
        print("***")       # the rung of the ladder


# This function talks to the user and asks for a number
# Then it uses that number to build the ladder by calling the other function

def create_ladder():
    print("How many steps remain?")  # asking user for the number of steps
    steps_input = input()            # taking the input as text (string)

    # making sure we turn the input into a number so we can use it in a loop
    steps_number = int(steps_input)  # converting string to an integer

    print("")  # adding a small empty space to separate input from output visually

    display_ladder(steps_number)     # calling the function that draws the ladder


# this line makes sure our code runs the create_ladder function
# without this, nothing will happen unless we type create_ladder() ourselves
create_ladder()
