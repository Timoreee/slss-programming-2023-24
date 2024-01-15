# Counts beans
# Auor: Tim
# Jan 9

# Version 01
# Count all red pixels
# Report on the percentage of all red
# Version 0.2
# Counts al the green pixels
# Report on the percemtage of all green jellybeans

from PIL import Image

import colour_helper

GREEN_PIXEL = (0, 150, 0)

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")
red_pixels = []
green_pixels = []

# Visit every pixel in the image
for y in range (jelly_bean_img.height):
    for x in range (jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        # If that pixel is red store the location
        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "green":
            green_pixels.append((x,y))

# Create a map of found pixels
# Count every red pixel in the list
# Divide that number by the total pixels in the image

red_percentage = len(green_pixels) / (jelly_bean_img.width * jelly_bean_img.height) 

# Create a map of all red pixels
# Create a new image that is the same size as the original
original_size = (jelly_bean_img.width, jelly_bean_img.height)
green_pixel_map = Image.new("RGB", original_size)

# For every pizel in red_pixels, place a red pixel on the new image
for pixel_loc in red_pixels:
    green_pixel_map.putpixel(pixel_loc, GREEN_PIXEL)

green_pixel_map.save("green_pixel_map.jpg")

green_pixel_map.close()       
jelly_bean_img.close()

        # Display Report
print(f"Red Jelly Beans: {round(red_percentage, 2)}%")
