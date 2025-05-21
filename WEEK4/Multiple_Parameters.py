# This function helps the player climb the collapsed bridge, now turned into a ladder
# It uses two parameters: steps_remaining and steps_crossed
def climb_ladder(steps_remaining, steps_crossed):
    # Print out the values being compared for better understanding
    print("Steps remaining:", steps_remaining)
    print("Steps crossed:", steps_crossed)

    # Now we check which number is bigger
    if steps_remaining > steps_crossed:
        # If there are more steps left than crossed, we're not close yet
        print("Still some way to go!")
    else:
        # If we've crossed more or equal steps, we're nearly done
        print("We are almost there!")


# Function calls to test our climb_ladder function
# This one should say "Still some way to go!"
climb_ladder(5, 2)

print("")  # Just a clean space between runs

# This one should say "We are almost there!"
climb_ladder(2, 5)
