# This program calculates BMI (Body Mass Index)

# Asking the user for their name
print("What is your name?")
name = input()  # input() gets text from the user

# Asking for age and convert it to number
print("How old are you (in years)?")
age = int(input())  # int() changes text to a number

# Asking for height and convert it to decimal number
print("How tall are you (in meters)?")
height = float(input())  # float() changes text to decimal number

# Asking for weight and convert it to decimal number
print("How much do you weigh (in kilograms)?")
weight = float(input())

# Calculate BMI using the formula: weight divided by height squared
# The ** symbol means "to the power of" - so height ** 2 is height squared
bmi = weight / (height ** 2)

# Making the BMI show only one decimal place

formatted_bmi = "{:.1f}".format(bmi)

# Showing the final result with the person information
print(f"{name} you are {age} years old and your bmi is {formatted_bmi}.")

