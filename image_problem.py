import colour_helper


# Solutions to Questions and Images
# Auth: Tim
# Dec 20 2023


# Question 1: Binarizing an image
def binarize(filename: str) -> None:
    with Image.open(filename) as im:
     # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):
                pixel = (im.getpixel(x, y))

            if colour_helper.is_light(pixel):

        # if this pixel is light
            # Replace pixel to white
                im.putpixel(x, y), colour_helper.WHITE_PIXEL()
            else:
        # if it isn't
            # Replace with black pixel
                im.putpixel(x, y), colout_helper.BLACK_PIXEL()
                
        Save theImage.save("./Images/binarized.jpg")

def image_to_greyscale(filename:)

binarize("beach.jpg")