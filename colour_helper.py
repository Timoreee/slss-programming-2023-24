# Colour Helper
# Author: Tim
# 13 December 2023

# Do you need help with colours?
# This is for you!


def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 250 and r < 32 and b < 32:
        return "green"
    if g < 25 and b < 25 and r > 150:
        return "red"
    if g >= 80 and b < 20 and r < 20:
        return "jelly_bean_green"



def is_light(pixel: tuple) -> bool:
    """ Return true if pixel is light"""

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + blue+ green) / 3
    if average >= 128:
        return True
    else:
        return False


input

black_pixel = (0, 0, 0)
dark_grey_pixel = (127, 127, 127)
light_grey_pixel = (128, 128, 128)
white_pixel = (255, 255, 255)

print(is_light(black_pixel))  # False
print(is_light(dark_grey_pixel))  # False
print(is_light(light_grey_pixel))  # True
print(is_light(white_pixel))  # True

