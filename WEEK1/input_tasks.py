# This program will display a game health status using symbols

# Asking the user for number of lives
print("Please enter the number of lives.")
lives = int(input())  # Convert input to a whole number
print(" ")  # Printing a empty line for space

# Asking the user to input energy levels
print("Please enter the energy level.")
energy = int(input())  # Converting input to a whole number
print(" ")  # Printing an empty line for space

# Asking the user what is their shield level
print("Please enter the shield level.")
shield = int(input())  # Converting input to a whole number
print(" ")  # Printing an empty line for space

# Letting the user know the health has been set
print("Health has been set.")
print(" ")  # Printing an empty line for space

# Creating the health display using string operators
# The * operator repeats a string a specified number of times
# Example: "♥" * 3 creates "♥♥♥"

# Displaying lives using heart symbols
print("Lives:  " + "♥" * lives)

# Displaying energy using diamond symbols
print("Energy: " + "♦" * energy)

# Displaying shield using diamond symbols
print("Shield: " + "♦" * shield)

# Code completed