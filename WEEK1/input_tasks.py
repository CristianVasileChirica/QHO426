# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# Ask for age,
print("How old are you (in years)?")
age = int(input())

#Ask for height
print("How tall are you (in meters)?")
height = float(input())

#Ask for weight
print("How much do you weigh (in kilograms)?")
weight = float(input())

# Calculate BMI
bmi = weight / (height ** 2)# Using power operator to square the height
formatted_bmi = "{:.1f}".format(bmi)# Format to show 1 decimal place

# Display BMI result
print(f"{name} you are {age} years old and your bmi is {formatted_bmi}.")

# Display a robot box with eyes
print("###########")
print("#  O   O  #")
print("#    #    #")
print("###########")