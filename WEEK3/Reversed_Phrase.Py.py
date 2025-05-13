# Program should begin by displaying the message below
print("What phrase do you want to see in reverse??")
print("") # Empty line for spacing

 # Reading the users response #
user_phrase = input()

# Small gap before reversing message
print("")
print("Reversing...")
print("") # Again spacing to make it clear when reading

 # The program now should use a for loop to display the phrase in reverse
# We have an empty string to store the reversed version
reserved_phrase = ""

 # We use a loop that starts from last index
# count down to 0
for i in range(len(user_phrase)-1,-1,-1):

    # We add each character to reversed_phrase
    reserved_phrase = reserved_phrase + user_phrase[i]

 #Finnly we print the reserved phrase
print("The phrase is:", reserved_phrase)