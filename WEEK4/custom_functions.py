# The function
def listen():
    # asking the user what sound they heard inside the cave
    print("What sound did you hear?")

    # taking input from the user and saving it in a variable called 'sound'
    sound = input()

    # displaying the result in a fun way by adding an exclamation mark
    print("That was a loud", sound + "!")  # we use + "!" to make it exciting


# Call function
listen()  # without this line, the function won’t actually run when the program starts
