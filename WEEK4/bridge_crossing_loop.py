# This function helps the player cross the bridge step by step
def cross_bridge(steps):
    # for every step the player takes, we show a message
    for step in range(steps):
        print("Crossed step.")  # one step done!

    # after crossing the bridge, we check how far the player went
    if steps > 5:
        print("The bridge is collapsing!")  # too far, it can't hold much longer!
    else:
        print("We must keep going!")  # not far yet, keep it up!

    print("")  # adding space to separate the two calls clearly


# Trying to cross a short bridge with only 3 steps
cross_bridge(3)

# Trying to cross a long bridge with 6 steps
cross_bridge(6)
