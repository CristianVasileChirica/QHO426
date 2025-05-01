# Here we are making a robot avoid obstacles using while loops

# First i need to ask the user how many obstacles to avoid
print  ("How many obstacles should i avoid? ")

  #Here we are getting the input from the user and converted it to a number
obstacle_to_avoid = int(input())

  # Adding a blank line to make the output look cleaner
print("")

 # Setting up a counter to keep a track of how many obstacles we've avoided
 # It starts at 0 because we haven't avoided any yet
obstacles_avoided = 0

#Now we are using the while loop to run until we've avoided all obstacles
while obstacles_avoided < obstacle_to_avoid:
    # First print "Avoiding..." but don't go to next line because end=""
    print("Avoiding...", end="")

#Increase our counter by 1 since we're avoiding an obstacle now
    obstacles_avoided = obstacles_avoided + 1

#This f-String lets you put variable right in the text
    print(f" Done! {obstacles_avoided} obstacles avoided.")

#Adding another blank line to separate the final message
print("")

# Let the user know we're all done!
print("All obstacles have been avoided.")

   #I added a little extra message to make my program special
print("Robot safety protocol complete!")