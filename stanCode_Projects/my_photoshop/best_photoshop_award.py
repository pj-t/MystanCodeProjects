"""
File: best_photoshop_award.py
Name: Baron
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 0.975

BLACK_PIXEL = 113


def main():
    """
    Idea：Jeery is a secret programmer of gundam.
    """
    fig = SimpleImage('image_contest/jerry.jpeg')
    bg = SimpleImage('image_contest/jerry_bg.jpeg')
    bg.make_as_big_as(fig)
    bg.show()
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    """
    : param1 fig: SimpleImage, the original image
    : param2 bg: SimpleImage, the background image
    : return fig: SimpleImage, the green screen pixels are replaced by pixels of background image
    """

    for x in range(bg.width):
        for y in range(bg.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue) // 3
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue
            if fig_pixel.green > avg * THRESHOLD and total > BLACK_PIXEL:
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
