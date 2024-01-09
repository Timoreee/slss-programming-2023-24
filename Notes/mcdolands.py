# Mcdolands order and costs bot
# Author Tim
# Nov 6 2023:
import time

print("Hello this is Mcdolands, what would you like?")
time.sleep(1)
# Define the prices of the items
burger_price = 5
fries_price = 3
tax_rate = 0.14

# Ask if the customer wants a burger
burger_choice = input("Would you like a Burger? (yes/no): ").lower().strip(",. ")
if burger_choice == "yes":
    num_burgers = 1
else:
    num_burgers = 0

# Ask if the customer wants fries
fries_choice = input("Would you like some fries? (yes/no): ").lower().strip(",. ")
if fries_choice == "yes":
    num_fries = 1
else:
    num_fries = 0

# Calculate the total cost before tax
subtotal = (num_burgers * burger_price) + (num_fries * fries_price)

# Calculate the total cost after applying tax
print(f"Total cost with tax: ${subtotal:.2f}")
