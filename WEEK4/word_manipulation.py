# Activity 3: Word Manipulation

# This function shows the word in an ASCII art box
def display_in_box(word):
    # create the top and bottom border with + and - symbols
    border = "+" + "-" * (len(word) + 2) + "+"
    print(border)
    print(f"| {word} |")  # the word is placed in the middle with padding
    print(border)
    print("")  # empty line to space it nicely


# This function converts the word to lowercase
def display_lower_case(word):
    print(word.lower())  # convert to lowercase
    print("")


# This function converts the word to uppercase
def display_upper_case(word):
    print(word.upper())  # convert to uppercase
    print("")


# This function shows the word and its mirror (reversed)
def display_mirrored(word):
    mirrored = word[::-1]  # reversing the word
    print(f"{word} | {mirrored}")
    print("")


# This function repeats the word in upper and lower case alternately
def repeat_word(word):
    # asking user how many times to repeat
    times = input("How many times do you want to display the word? ")

    # convert the input to a number safely
    if times.isdigit():  # checking if it's a number
        times = int(times)  # convert to int
        for i in range(times):
            if i % 2 == 0:
                print(word.upper())  # even turns = uppercase
            else:
                print(word.lower())  # odd turns = lowercase
    else:
        print("That was not a valid number.")
    print("")


# This function controls the program flow
def run_word_program():
    print("Welcome adventurer! You've found a mysterious map...")
    print("")

    word = input("Please enter a word: ")  # ask user for a word
    print("")  # add space after input for cleaner look

    # show options
    print("What would you like to do with the word?")
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    print("")

    # get user choice
    choice = input("Enter your choice (1-5): ")
    print("")  # spacing

    # calling the appropriate function based on user input
    if choice == "1":
        display_in_box(word)
    elif choice == "2":
        display_lower_case(word)
    elif choice == "3":
        display_upper_case(word)
    elif choice == "4":
        display_mirrored(word)
    elif choice == "5":
        repeat_word(word)
    else:
        print("Oops! That was not a valid choice.")
        print("")


# this will start the program
run_word_program()
