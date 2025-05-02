# This is a Battery Charging Simulator
# This program is showing a battery charging with ASCII asrt
# I have learned that while loops are good for repeating actions until a condition will be met!

# First, let's ask the user to how many charging bars they want
print("How many bars should be charged?")
max_bars = int(input()) # Converting the user inout to a No
print(" ")  # Adding a blank line to make the output look cleaner

# Creating a variable to keep track of how many bars are charged
# Starting with 0 since the battery hasn't started charging yet
charged_bars = 0

# The special character  █ ( Got this from solent page task)
# This Looks cooler than just using regular characters!
bar_symbol = "█"

# The while loop will run until we have changed all the bars the user asked for
while charged_bars < max_bars:
    # Adding one more bar each time through the loop
    charged_bars = charged_bars + 1 #

    # Creating the chargind display - Will make it show all bars charged so far
    charging_display = ""
    for i in range(charged_bars):
        charging_display = charging_display + bar_symbol + " "

        # Showing the current charging status
        print("Charging:", charging_display)

        # When the loop is done, the battery is fully charged
        print("\nThe battery is fully charged.")
        print(" ")