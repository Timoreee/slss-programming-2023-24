# A robot puppy that finds the center of the ball in the image
# Author: Tim
# Jan 12 2023

from PIL import Image
img = './Images/Red Ball.jpeg'
def find_mid(img):

    # Read image
    image = Image.open(img)

    # Convert the image 
    image_rgb = image.convert('RGB')

    # Set the RGB values for red color
    red_color = (255, 0, 0)
    # Find red pixel

    red = []
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = image_rgb.getpixel((x, y))
            if all(val >= 200 for val in pixel) and pixel[0] == 255:  # Red
                red.append((x, y))

    # Calculate the center of the red pixels (assuming it's the ball)
    if red:
        mid_x = sum(x for x, _ in red) // len(red)
        mid_y = sum(y for _, y in red) // len(red)
        return mid_x, mid_y
    
mid = find_mid(img)
print(f"Center of the red ball: ({mid[0]}, {mid[1]})")