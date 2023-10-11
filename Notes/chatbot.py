# Chatbot
# Author: Timothy
# Date sept 20 2023

import random
import time


# Greet the user
print("Hello there! 🤡")
time.sleep(1.5)
print("I'm a crude Chatbot, here to talk to you")
# Get the user's name and store it in a variable
user_name = input("So.... what's your name? ")
time.sleep(1.5)

# Respond with the users name in a freindly way
print(f"It's good to meet you {user_name}")

# ask the user what their favourite food is
fave_food = input("First things first, what's your favourite food?")

# Make a comment about their food but not be terribly repetetive

#If their favourite food is sushi, reply with yum.
if fave_food == "sushi" or fave_food == "pizza":
    print("Yum! 🍣")
    print("I think I love sushi!")
elif fave_food == "Pizza" or fave_food == "pizza":
    print("🍕")
    print("good choice my good sir")
else:

    # create alist of possible responses
    list_of_food_responses = [
        f"Oh, I've never had {fave_food} before",
        "Mmmmm, that sounds good!",
        "I heard that that was amazing!", 
        "Lmao who asked."
        ]

    print(list_of_food_responses[2])

    # Choose one of those responses randomely
    import random
    randome_food_response = random.choice(list_of_food_responses)

    # Print out that chosen response
    print(randome_food_response)