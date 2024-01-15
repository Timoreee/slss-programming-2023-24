# Functions Practice
# Author: Tim
# 24 November 2023


def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


print(print_area_of_a_square(10.5))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)

# Question 1:
# Create a function called stars()
# it takes an int as a parameter
# it returns a string of stars with the same length as the argument

def stars(num_stars: int) -> str:
    """Returns a number of stars
    
    Params:
    
    num_stars - the number of stars to return
    """

# Question 2 
# Write a function that takes three numbers
# It should return the biggest of the three numbers.
# Call it biggest_of_three()
# Don't use builtin max()function

first = int(input("please place in a number"))
second = int(input("please place in a second number"))
third = int(input("please place in a third number"))

if first > second:
    Top = first
elif first > third:
    Top = first
elif second > first:
    Top = second
elif second > third:
    Top = second
elif third >  second:
    Top = third
elif third >  first:
    Top = third

print(Top)
# Question 3 
# Write a function that creates pyramid of starss.
# call is pyramid()

pyramid = ["*", "**", "***", "****", "*****", "******", "*******", "********", "*********"]
yes = input("Do you want to build a star pyramid? ").strip(",.!? ").lower
if yes == "yes":
    for item in pyramid:
        print(f"* {item}")

