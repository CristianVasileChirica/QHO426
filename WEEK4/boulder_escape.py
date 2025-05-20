# This function asks the user what they see and gives a response based on their input
def identify():
    # asking the user what lies ahead
    print("What lies before us?")

    # storing the user's input
    response = input()

    # checking if they saw a large boulder
    if response == "a large boulder":
        print("It's time to run!")  # serious situation!
    else:
        print("We will be fine.")  # it's all good, don't panic

    print("")  # Just for spacing between function outputs


# This function gives a response based on the escape plan passed as a parameter
def escape_by(plan):
    # checking the plan and responding accordingly
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")  # too high to jump
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")  # not fast enough
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")  # fingers crossed
    else:
        print("We cannot escape that way! The boulder is in the way!")  # catch-all if plan is unknown

    print("")  # helpful space after each result


# Calling the identify function to start the adventure
identify()

# Trying different escape plans
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
