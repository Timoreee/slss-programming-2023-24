# Chatbot
# Author: Timothy
# Date sept 20 2023

# Greet the user
print("Hello there! 🤡")
print("I'm a crude Chatbot, here to talk to you")

# Get the user's name and store it in a variable
user_name = input("So.... what's your name? ")

# Respond with the users name in a freindly way
print(f"It's good to meet you {user_name}")

# ask the user what their favourite food is
fave_food = input("First things first, what's your favourite food?")

# Make a comment about their food
# create alist of possible responses
list_of_food_responses = [
    f"Oh, I've never had {fave_food} before",
    "Mmmmm, that sounds good!",
    "I heard that that was amazing!", 
    "Okay."
    ]
# Choose one of those responses randomely
import random
randome_food_response = random.choice(list_of_food_responses)

# Print out that chosen response
print(randome_food_response)