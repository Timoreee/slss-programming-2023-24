# Pumpkin Drawing
# Author: Timothy Cai
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Left eye
carver.penup()
carver.setpos(-30, 20)
carver.dot(30)

# Right Eye
carver.penup()
carver.setpos(30, 20)
carver.dot(30)

# Nose
carver.penup()
carver.setpos(0, 0)
carver.dot(10)
carver.forward(15)

# Mouth
carver.setpos(-50, -30)
carver.pendown()
carver.fd(110)
carver.color("orange", "orange")

turtle.done()