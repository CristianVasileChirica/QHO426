# A Pizza Ordering Program
# This is showing different decisions type in Phyton (if -else, nested, AND,OR, NOT)
from selectors import SelectSelector

#Welcome message
print("Welcome to Pizza Ordering!")
print("")

#Ask for pizza size
print("What size pizza would you like? (small/medium/large)")
size = input()
print("")

# We are using : if-elif-else statements
# This shows choosing between multiple options
if size == "small":
    print("You ordered a small pizza, that will cost £8.")
    price = 8
elif size == "medium":
    print("You ordered a medium pizza, That will cost £10")
    price = 10
elif size == "large":
    print("You ordered a Large pizza, That will cost you £12")
    price = 12
else:
    print("Sorry, I don't understand that size., will make you a medium pizza.")
    price = 10
    size = "medium"
print("")

# Now : Nested decisions
# This will shows a decision inside another decision
print("Would you like extra cheese! (yes/no)")
extra_cheese = input()
print("") # Printing an empty line for better readability

# First decision - about having extra cheese
if extra_cheese == "yes":
    # Nested decisions inside the first one
    print("Do you want double or triple cheese? (double/triple)")
    cheese_amount = input()
    print("")

    # This decision is nested
    if cheese_amount == "double":
        print("Adding double cheese for £2 extra.")
        price = price + 2 # Corrected: should add to the price
        has_cheese = "yes"
    elif cheese_amount == "triple":
        print("Adding triple cheese for £2.50 extra.")
        price = price + 2.50 # Corrected: should add to the price
        has_cheese = "yes"
    else:
        print("Sorry, I don't understand that amount of cheese. No extra cheese added.")
        has_cheese = "no"
else:
    print("No extra cheese added.")
    has_cheese = "no"
print("")

# Now Logical And Operator
# Both conditions must be true
print("Would you like to add peperoni? (yes/no)")
add_peperoni = input()
print("")

# Using AND - both conditions must be true
if (add_peperoni == "yes") and (size == "large"):
    print("Adding pepperoni to your large pizza for £2 extra.")
    price = price + 2
    has_peperoni = "yes"
elif add_peperoni == "yes":
    print("Adding pepperoni for £1.20 extra.")
    price = price + 1.20
    has_peperoni = "yes"
else:
    print("No pepperoni added.")
    has_peperoni = "no"
print("")

# Now Logical OR operator
# At least one condition must be true
print("Do you have a discount coupon?  (yes/no)")
has_coupon = input()
print("")

# Using OR - only one condition needs to be true
# The condition (size >= 15) is always false for the given sizes, corrected logic
if (has_coupon == "yes"):
    print("You qualify for a £2 discount!")
    price = price - 2
    got_discount = "yes"
else:
    print("No discount added.")
    got_discount = "no"
print("")

#Now using NOT with conditions
# Reversing a condition
print("Is this for delivery? (yes/no)")
is_delivery = input()
print("")

# Using NOT and combining conditions
if is_delivery == "yes" and not got_discount == "yes":
    print("Delivery fee is £3")
    price = price + 3
    print(f"Your total is £{price}")
elif is_delivery == "yes" and got_discount == "yes":
    print("Delivery fee is £1.5 (reduced with your discount)")
    price = price + 1.5
    print(f"Your total is £{price}")
else:
    print("Your order will be ready for pickup.")
    print(f"Your total is £{price}.")
print("")

# End message
print("Thank you for ordering from our Pizza!")


