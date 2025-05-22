# module_tasks.py
# This program creates a number guessing game using the random module
# My first program using imported modules!

# Import the random module so we can generate random numbers
# I'll use 'import random' instead of abbreviating it since I'm still learning
import random


def play_guess_the_number():
    # This function contains the main game logic
    # First, I need to get the minimum value from the user
    print("Please enter the minimum value:")
    min_value = input()
    min_value = int(min_value)  # Convert to integer

    # Next, get the maximum value from the user
    print("Please enter the maximum value:")
    max_value = input()
    max_value = int(max_value)  # Convert to integer

    # Generate a random number between min and max (inclusive)
    # I'll use randint because it includes both endpoints
    secret_number = random.randint(min_value, max_value)

    # Tell the user what range we're thinking of
    print(f"I am thinking of a number between {min_value} and {max_value}. Can you guess what it is?")

    # Start the guessing loop
    # I'll use a while loop because I don't know how many guesses it will take
    user_guess = None  # Initialize the guess variable

    while user_guess != secret_number:
        # Get the user's guess
        user_guess = input()
        user_guess = int(user_guess)  # Convert to integer

        # Check if the guess is correct
        if user_guess == secret_number:
            # They got it right! Break out of the loop
            break
        elif user_guess < secret_number:
            # Their guess is too low
            print("Your guess is too low.")
        elif user_guess > secret_number:
            # Their guess is too high
            print("Your guess is too high.")

        # Ask them to try again (unless they got it right)
        print("Try again:")

    # They guessed correctly, so congratulate them
    print("Congratulations! You guessed my number!")


# Call the function to start the game
# This is where the program actually begins
play_guess_the_number()