"""# This program will ask what activity to perform and responds accordingly based on what they have entered
# It shows how to use IF...ELSE statement to make decisions in our program

#Asking the user for the activity they want to perform
print("Please enter the activity you want to perform.")
activity = input () # storing the user input in a variable
print("") # Add an empty line to be more readable

# Check what activity was entered and if it's "calculate"
# IF...ELSE lets us handle two different situations
if activity == "calculate": # Checking If the activity is exactly "calculate"
    print("Performing calculations...") # This will run when activity is "calculate"
else:
    print("Performing activity...") # This will run when activity is anyrhing else

print(" ") # Add an empty line for better readability
print("Activity completed!") # This always runs, no matter what activity was
print("") # Add an empty line for better readability"""

# This program will help a robot to navigate through a maze
# It will show how to use if...elif...else statements to handle multiple choices

# First, we need to ask the user which direction the robot should move
print("Towords which direction should i go(up, down, left or right)?")
direction = input() # This will save the user's answer in a variable called "directions"

# Now we will check which direction was chosen
# We'll use if, elif, and else to handle all possible directions
if direction == "up": # checking if the direction chosed by the user is "up"
      # this will run if the direction typed by the user is "up"
      print("I am moving in a upward direction!")
elif direction == "down": # Checking if the direction is "down"
        # This will run if the direction typed by the user is "down"
        print("I am moving in a downward direction!")
elif direction == "left": # checking if the direction is "left"
        # This will work if the user types "left"
        print("I am moving in a left direction!")
elif direction == "right": # Checking if the direction typed by the user is "right"
        #thsi will run if the user typed "right"
        print("I am moving in a right direction!")
else:
    # This will run if the input user uses doesn't match any of the above
    print(" I do not understand the direction!")

    # Empty line added
    print("")
