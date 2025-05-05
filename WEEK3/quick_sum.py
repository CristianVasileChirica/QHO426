# This adds up number that the user will enter

# First, we asked how many number they want to add
how_many = input ("How many numbers should I sum up?\n")
how_many = int(how_many) # Convert to integer

# Create a variable to store the total
total = 0

# We will use a counter to keep track of which number we are on
current_number = 1

# Loop to get all the number from the user
while current_number <= how_many:
    # Ask for each number
    number = input(f"Please enter number{current_number} of {how_many}:\n")
    number = float(number) # Converting to number, handling decimals too

    # Add it to our total
    total = total + number

    # Move to the next number
    current_number = current_number + 1

    # Show the answer
    print(f"The answer is {total}.")
    print("")
