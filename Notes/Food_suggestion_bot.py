# Food Suggestion Bot
# Author: Timothy
# 6 october 2023

# a bot that asks the user what their favourite food is. Based on the food,
# it will classify the type/genre/cuisine of the food, then give a restaurant suggestion
import time
import random

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello there, I am your personal food bot and I am here to guide you through your cuisine journey!")
time.sleep(1.5)
fave_food = input("First things first of coruse, what is tyour favourite food?")
time.sleep(1)

# Italion cuisine
italion_food = ["pasta","tiramisu", "canneloni"]
american_food = ["burger","hot dog", "pancakes", "Waffles"]
# Add another type of cuisine our bot should know
# if they input an answer with italian food
#  suggest an italian restaurant
if fave_food.lower().strip("!,.?") in italion_food:
    print(" So I see that you like Italian food")
    time.sleep(0.5)
    print("I personally suggest broli kitchen then")
    time.sleep(1)
    print("Here is the address")
    print("186-8180 No 2 Rd, Richmond, BC V7C 5K1")
elif fave_food.lower().strip("!,.?") in american_food:
    print(" So I see that you like American food")
    time.sleep(0.5)
    print("I personally suggest LA grill then")
    time.sleep(1)
    print("Here is the address")
    print("186-8180 No 2 Rd, Richmond, BC V7C 5K1")
else:
    print("Sorry I don't seem to have that type of food in my database")
    time.sleep(1)
    print("thus, I cannot give you a suggestion")