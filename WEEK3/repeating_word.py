# This program prints "Hi" as many times as characters in user's phrase
from binascii import crc_hqx

from numpy import character

print ("Please enter a phrase :")
user_phrase = input() # Storing what user types

# Using Len() function to count how many characters are in the phrase
character_count = len(user_phrase)
# Keeping track on how many times I've printed "Hi"
times_printed = 0

#While loop will run until we've "Hi" enough times
while times_printed < character_count:
    print("Hi", end="")
    times_printed = times_printed + 1

print() # New line at the end