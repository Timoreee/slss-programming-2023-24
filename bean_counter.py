# Counts beans
# Author: Tim
# Jan 9

# Version 01
# Count all red pixels
# Report on the percentage of all red
# Version 0.2
# Counts al the green pixels
# Report on the percemtage of all green jellybeans

from PIL import Image
red_ball_center = './Images/Red Ball.jpeg'

def find_ball_center(red_ball_center):
    # Read the image
    image = Image.open(red_ball_center)
    # Convert the image into RGB
    rgb_image = image.convert('RGB')
    # Set the RGB values for red color
    red_color = (255, 0, 0)
    # Find red pixels
    red_pixels = []
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = rgb_image.getpixel((x, y))
            if all(val >= 200 for val in pixel) and pixel[0] == 255:  # Red color with some tolerance
                red_pixels.append((x, y))
    # Find the center
    if red_pixels:
        center_x = sum(x for x, _ in red_pixels) // len(red_pixels)
        center_y = sum(y for _, y in red_pixels) // len(red_pixels)
        return center_x, center_y
    else:
        return None
    
center = find_ball_center(red_ball_center)

print(f"The center of the red ball is: ({center[0]}, {center[1]})")