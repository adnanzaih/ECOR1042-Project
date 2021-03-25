#Adnan Hafeez 101210710

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image
from unit_testing import check_equal
from T010_P4_filter_horizontal import flip_horizontal

def test_horizontal() -> None:
    """
    A test function for horizontal flip filter. Using a 6x1 pixel image as a sample to
    test functionality.

    Author: Adnan Hafeez
    >>> test_horizontal()
    """

    #Creates an image with 4 pixels
    original = create_image(6,1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(10, 20, 60))
    set_color(original, 2, 0,  create_color(180, 199, 196))
    set_color(original, 3, 0,  create_color(255, 255, 255))
    set_color(original, 4, 0, create_color(255, 255, 255))
    set_color(original, 5, 0, create_color(124, 45, 0))


    #Expected transformation of image
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(124, 45, 0))
    set_color(expected, 1, 0,  create_color(255, 255, 255))
    set_color(expected, 2, 0,  create_color(255, 255, 255))
    set_color(expected, 3, 0,  create_color(180, 199, 196))
    set_color(expected, 4, 0, create_color(10, 20, 60))
    set_color(expected, 5, 0, create_color(0, 0, 0))

    #Comparing expected image to the image produced by sepia_filter
    img = flip_horizontal(original)
    for x, y, col in img:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

if __name__ == "__main__":
    #file = load_image(choose_file())
    #show(sepia_filter(file))
    test_horizontal()

