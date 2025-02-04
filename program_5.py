# Programmer: Austin Long
# Date: 2/4/2025
# Hotdog Price Calculator
import sys

# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally, a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

# declare variables
subtotal = 0.0
base_price = 0.0

# input hot dog type
hotdog_type = input("Enter the hotdog type (Hot Dog or Chili Dog): ").upper()

# determine base price from type
HOT_DOG_PRICE = 3.50
CHILI_DOG_PRICE = 4.50
if hotdog_type == "HOT DOG":
    base_price = HOT_DOG_PRICE
elif hotdog_type == "CHILI DOG":
    base_price = CHILI_DOG_PRICE
else:
    # quit if invalid input
    print("We are not offering that kind of hot dog. Please enter Hot Dog or Chili Dog.", file=sys.stderr)
    exit(1)

# Set subtotal to base price
subtotal = base_price

# Input toppings
cheese = input("Would you like cheese? (Yes or No) ").upper() == "YES"
peppers = input("Would you like peppers? (Yes or No) ").upper() == "YES"
grilled_onions = input("Would you like grilled onions? (Yes or No) ").upper() == "YES"

# Calculate extra charges based on toppings
CHEESE_PRICE = 0.50
PEPPERS_PRICE = 0.75
GRILLED_ONIONS_PRICE = 1.0
if cheese:
    subtotal += CHEESE_PRICE
if peppers:
    subtotal += PEPPERS_PRICE
if grilled_onions:
    subtotal += GRILLED_ONIONS_PRICE

# Calculate tax
TAX_RATE = 0.07
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display results to user
print("Results:")
print(f"{hotdog_type:27}${base_price:.2f}")
if cheese:
    print(f"\t + {'cheese':20}${CHEESE_PRICE:.2f}")
if peppers:
    print(f"\t + {'peppers':20}${PEPPERS_PRICE:.2f}")
if grilled_onions:
    print(f"\t + {'grilled onions':20}${GRILLED_ONIONS_PRICE:.2f}")

print()
print(f"{'Subtotal:':27}${subtotal:.2f}")
# Note: I had to look up how to do percentage formatting. Is this OK?
print(f"\t + {f'tax ({TAX_RATE:.2%})':20}${tax:.2f}")

# ANSI escape codes (https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
COLORED = '\033[95m'
RESET = '\033[0m'

print(f"{COLORED}{'Total:':27}${total:.2f}{RESET}")
