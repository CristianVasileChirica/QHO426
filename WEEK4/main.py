# main.py
# This is our main program launcher! It's designed to help us easily
# run all the different Python programs we've built throughout the weeks.
# Think of it as a central hub for all our coding adventures!

# --- Importing Our Weekly Modules ---
# We use 'import' to bring code from other files into this one.
# 'week1.output_tasks' tells Python: "Go into the 'week1' folder,
# and find the file named 'output_tasks.py'."
# 'as wk1_output' is a shortcut; now we can type 'wk1_output' instead of the full path!

# Imports for Week 1 programs
import week1.output_tasks as wk1_output
import week1.input_tasks as wk1_input

# Imports for Week 4 programs
# We need to import each module from the 'WEEK4' package.
# Remember: each of these files MUST have its main logic wrapped in a function!
import WEEK4.ascii_character_finder as wk4_ascii_finder
import WEEK4.boulder_escape as wk4_boulder_escape
import WEEK4.bridge_crossing_loop as wk4_bridge_crossing_loop
import WEEK4.built_in_functions as wk4_built_in_functions
import WEEK4.custom_functions as wk4_custom_functions
import WEEK4.custom_functions_nesting as wk4_custom_functions_nesting
import WEEK4.display_ladder as wk4_display_ladder
import WEEK4.identify_nesting_adventure as wk4_identify_nesting_adventure
import WEEK4.module_tasks as wk4_module_tasks
import WEEK4.Multiple_Parameters as wk4_multiple_parameters
import WEEK4.return_values as wk4_return_values
import WEEK4.word_manipulation as wk4_word_manipulation


# --- Functions for Each Week's Programs ---

def run_week_one_programs():
    """
    This function handles the menu for all programs created in Week 1.
    It asks the user which specific Week 1 task they want to run
    and then calls the appropriate function from our imported modules.
    """
    print("\n--- Welcome to Week 1 Programs! ---")
    # This loop keeps the Week 1 menu showing until the user decides to go back.
    while True:
        print("Which awesome program from 'Week 1' do you wish to launch?")
        print("[a] Simple Message (from output_tasks.py)")
        print("[b] Multiline Message (from output_tasks.py)")
        print("[c] Greet User (from input_tasks.py)")
        print("[d] Calculate Age in Future (from input_tasks.py)")
        print("[q] Go back to the Main Launcher Menu")

        # We use .lower() so that 'A' or 'a' both work, making it user-friendly!
        response = input("Enter your choice: ").lower()

        if response == "a":
            print("\n>>> Launching 'Simple Message'...")
            wk1_output.simple_message()  # Calling the function from our imported module!
        elif response == "b":
            print("\n>>> Launching 'Multiline Message'...")
            wk1_output.multiline_message()
        elif response == "c":
            print("\n>>> Launching 'Greet User'...")
            wk1_input.greet_user()
        elif response == "d":
            print("\n>>> Launching 'Calculate Age in Future'...")
            wk1_input.calculate_age_in_future()
        elif response == "q":
            print("Returning to the main menu. See you soon in Week 1!")
            break  # This 'break' statement exits the 'while True' loop, taking us back.
        else:
            print("Whoops! That wasn't a valid option. Please pick from the list (a, b, c, d, or q).")


def run_week_four_programs():
    """
    This function handles the menu for all programs created in Week 4.
    It prompts the user to select a program and then executes the corresponding function.
    """
    print("\n--- Welcome to Week 4 Programs! ---")
    while True:
        print("Which exciting program from 'Week 4' do you wish to launch?")
        print("[a] ASCII Character Finder")
        print("[b] Boulder Escape")
        print("[c] Bridge Crossing Loop")
        print("[d] Built-in Functions Demo")
        print("[e] Custom Functions Demo")
        print("[f] Custom Functions Nesting Demo")
        print("[g] Display Ladder")
        print("[h] Identify Nesting Adventure")
        print("[i] Module Tasks (Placeholder)") # If module_tasks has a run function
        print("[j] Multiple Parameters Demo")
        print("[k] Return Values Demo")
        print("[l] Word Manipulation")
        print("[q] Go back to the Main Launcher Menu")

        response = input("Enter your choice: ").lower()

        if response == "a":
            print("\n>>> Launching 'ASCII Character Finder'...")
            wk4_ascii_finder.run_ascii_character_finder() # Assuming this is the function name
        elif response == "b":
            print("\n>>> Launching 'Boulder Escape'...")
            wk4_boulder_escape.run_boulder_escape()
        elif response == "c":
            print("\n>>> Launching 'Bridge Crossing Loop'...")
            wk4_bridge_crossing_loop.run_bridge_crossing_loop() # You'll need to define this function
        elif response == "d":
            print("\n>>> Launching 'Built-in Functions Demo'...")
            wk4_built_in_functions.run_built_in_functions_demo() # Define this
        elif response == "e":
            print("\n>>> Launching 'Custom Functions Demo'...")
            wk4_custom_functions.run_custom_functions_demonstration() # Define this
        elif response == "f":
            print("\n>>> Launching 'Custom Functions Nesting Demo'...")
            wk4_custom_functions_nesting.run_custom_functions_nesting_demo() # Define this
        elif response == "g":
            print("\n>>> Launching 'Display Ladder'...")
            wk4_display_ladder.run_display_ladder() # Define this
        elif response == "h":
            print("\n>>> Launching 'Identify Nesting Adventure'...")
            wk4_identify_nesting_adventure.run_identify_nesting_adventure() # Define this
        elif response == "i":
            print("\n>>> Launching 'Module Tasks'...")
            # If module_tasks.py has a function to run its main logic
            wk4_module_tasks.run_module_tasks() # Define this
        elif response == "j":
            print("\n>>> Launching 'Multiple Parameters Demo'...")
            wk4_multiple_parameters.run_multiple_parameters_demo() # Define this
        elif response == "k":
            print("\n>>> Launching 'Return Values Demo'...")
            wk4_return_values.run_return_values_demo() # Define this
        elif response == "l":
            print("\n>>> Launching 'Word Manipulation'...")
            wk4_word_manipulation.run_word_manipulation() # Define this
        elif response == "q":
            print("Returning to the main menu. Fantastic job with Week 4!")
            break
        else:
            print("Invalid choice for Week 4. Please pick from the list (a-l or q).")


# --- The Grand Launcher's Main Function ---

def run_main_launcher():
    """
    This is the core function of our program launcher.
    It presents the main menu to the user, allowing them to choose
    which week's programs they want to explore and run.
    """
    print("\n=============================================")
    print(" Welcome to the Python Program Launcher! ")
    print(" Your one-stop shop for all our coding adventures! ")
    print("=============================================")

    # This loop keeps the main launcher running until the user decides to quit.
    while True:
        print("\n--- Main Launcher Menu ---")
        print("What Python journey would you like to embark on today?")
        print("[1] Explore 'Week 1' Programs")
        print("[2] Discover 'Week 4' Programs") # New option for Week 4
        # As you progress, you'd add more options here for new weeks!
        # print("[3] Journey into 'Week 5' Programs (Coming Soon!)")
        print("[q] Quit the Program Launcher")

        user_choice = input("Enter your selection: ").lower()

        if user_choice == "1":
            run_week_one_programs()  # Call the function dedicated to Week 1's menu.
        elif user_choice == "2":
            run_week_four_programs() # Call the new function for Week 4's menu.
        elif user_choice == "q":
            print("\nFarewell! Thanks for using the Program Launcher. Happy coding!")
            break  # This breaks out of the main 'while True' loop, ending the program.
        else:
            print("Hmm, that's not a recognized option. Please enter '1', '2', or 'q'.")


# --- The Entry Point of Our Program ---
# This is a standard Python practice!
# 'if __name__ == "__main__":' means: "If this 'main.py' file is the one
# that was directly executed (not imported by another file), then run the code below."
# This is perfect for our launcher, as we want it to start when we run main.py.
if __name__ == "__main__":
    run_main_launcher()