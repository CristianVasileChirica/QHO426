# The program asks about what book types and responds to adventure books

# An IF statement is used to make a decision based on the boo type

# Asking the User for the type of book
print("What type of book is this?!")
book_type = input() # Getting the book type from the user and store it in a variable
print("") # Adding an empty line to be better readable

# Checking if the book is an adventure one
# The IF statement will check a condition and tuns the code if the condition id True
if book_type == "Adventure": # The == mens is equal to
    print("I like Adventure books!") # This line will only run if book_type is "Adventure"
    print("") # Another empty line for better readability

# This code is not indented, i will run regardless of the book type
print("Finished reading book!")
print("") # Empty line for better readability