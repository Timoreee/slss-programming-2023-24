# Turtle example
# Author: Tim
# 21 Nov 2023

import turtle

# Create a turtle that can be mvoed around the screen
FORWARD_MAGNITUDE = 28


# Make a turtle object
michaelangelo = turtle.Turtle()

# Get some input from the user
print("""To give commans, type:
F - to go forward
L to turn left
R to turn right """)

# Repeat the below forever, or until the 
done = False

while not False:
    command = input("Where should I go?")
# Move the turtle around
    if command.strip(",.?! ").lower() == "f":
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command.strip(",.?! ").lower() == "l":
        michaelangelo.left(90)

    elif command.strip(",.?! ").lower() == "r":
        michaelangelo.right(90)
    elif command.strip(",.?! ").lower() == "stop":

        def draw_tree(level:int, height: int) -> None:
            """A recursive function tht draws a tree """
        done = True