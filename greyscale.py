# greyscale image
# Author: Tim
# Dec 19 2023

from PIL import Image
def is_white(pixel: tuple) -> str:
    average = sum(pixel) / len(pixel)
    return average >= 128

def convert_to_grayscale(im):
    pixels = list(im.get())
    new_pixels = [(255, 255, 255) if is_white(pixel) else (0, 0, 0) for pixel in pixels]

# Make new Image
     
    new_pizza = Image.new('RGB', im.size)
    new_pizza.putdata(new_pixels)

    return new_pizza    

# Open up Best Pizza image
with Image.open("./Images/best_pizza.jpg") as im:
    grayscale_im = convert_to_grayscale(im)
    # print and convert image into greyscale

grayscale_im.save("./Images/output-2.jpg")