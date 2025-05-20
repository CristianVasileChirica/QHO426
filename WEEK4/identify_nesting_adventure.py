# This function asks the user what they see and responds accordingly
def identify():
    # asking the user to describe what lies ahead
    print("What lies before us?")

    # storing the answer in a variable called 'sight'
    sight = input()

    # checking what the user said (we're comparing it exactly as written)
    if sight == "a large boulder":
        # if it's a boulder, we better run!
        print("It's time to run!")
    else:
        # otherwise, it's probably nothing dangerous
        print("We will be fine.")

    print("")  # adding a line for breathing space in the output


# calling the function so it actually runs (very important!)
identify()
