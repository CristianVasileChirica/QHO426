# This program will ask what activity to perform and responds accordingly
# It shows how to use IF...ELSE statement

#Asking the user for the activity they want to perform
print("Please enter the activity you want to perform.")
activity = input () # storing the user input in a variable
print("") # Add an empty line to be more readable

# Check what activity was entered
# IF...ELSE lets us handle two different situations
if activity == "calculate": # If the activity is exactly "calculate"
    print("Performing calculations...") # This will run when activity is "calculate"
else:
    print("Performing activity...") # This will run when activity is anyrhing else

print(" ") # Add an empty line for better readability
print("Activity completed!") # This always runs, no matter what activity was
print("") # Add an empty line for better readability
