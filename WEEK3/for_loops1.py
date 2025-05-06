# In this program we will display ASCII mountains using a for loop


# First i will ask the user for input
print("How many mountains should i display ?")
mountain_number = int(input())

#We need to convert the input to a number, because input() gives me text
mountain_number = int(mountain_number)

# Adding a blank line to make it look better
print("")

# Telling the user what's happening
print("Displaying...")

# Adding another blank line
print("")


#Now we use for loop to print the mountain
#The number in range() is how many times the loop runs
for mountain in range(mountain_number):
    # Each mountain has 6 lines that i need to print
    # I'll print each line onr by one
    print("           __")
    print("          /  \\_  ")
    print("         /^    \\")
    print("        /  ^    \\_")
    print("      _/ ^ ^     ^\\")
    print("     /  ^     ^    \\")


    # Adding some extra blank line at the end
    print("")
    print("")


    # Telling the user we are done
    print("Done!")

