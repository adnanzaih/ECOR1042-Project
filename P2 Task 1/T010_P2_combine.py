#Import required modules.
from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    Image, get_color, create_image
from unit_testing import check_equal

def combine(red: Image, green: Image, blue:Image) -> Image:
    """Return an image that is a combination of the red, blue and green channels. By loading a red, green and blue filtered
    set of images in that specific order only.
    """
    new_image = copy(red)
    for x, y, _ in red:
        red_pixel = get_color(red,x,y)
        green_pixel = get_color(green,x,y)
        blue_pixel = get_color(blue,x,y)
        combined_colors = create_color(red_pixel[0], green_pixel[1], blue_pixel[2])
        set_color(new_image, x,y, combined_colors)
    return new_image

def test_combine() -> None:
    """
    A test function for the combined filter.
    """
    # This test function checks if combine correctly combines the R G B channels:
    # R=(0, 0, 0), G=(0, 0, 0), B=(0, 0, 0) to (0, 0, 0)  # no color
    # R=(13, 0, 0), G=(0, 0, 0), B=(0, 0, 1) to (13, 0, 1)
    # R=(255, 0, 0), G=(0, 127, 0), B=(0, 0, 127) to (255, 127, 127)
    # R=(125, 0, 0), G=(0, 73, 0), B=(0, 0, 224) to (125, 73, 224)
    # R=(254, 0, 0), G=(0, 255, 0), B=(0, 0, 255) to (254, 255, 255)
    # R=(87, 0, 0), G=(0, 13, 0), B=(0, 0, 255) to (87, 13, 255)

    # Create an red channel image with six pixels.
    red_img = create_image(6, 1)
    set_color(red_img, 0, 0,  create_color(0, 0, 0))
    set_color(red_img, 1, 0,  create_color(13, 0, 0))
    set_color(red_img, 2, 0,  create_color(255, 0, 0))
    set_color(red_img, 3, 0,  create_color(125, 0, 0))
    set_color(red_img, 4, 0,  create_color(254, 0, 0))
    set_color(red_img, 5, 0,  create_color(87, 0, 0))

    # Create an green channel image with six pixels.
    green_img = create_image(6, 1)
    set_color(green_img, 0, 0,  create_color(0, 0, 0))
    set_color(green_img, 1, 0,  create_color(0, 0, 0))
    set_color(green_img, 2, 0,  create_color(0, 127, 0))
    set_color(green_img, 3, 0,  create_color(0, 73, 0))
    set_color(green_img, 4, 0,  create_color(0, 255, 0))
    set_color(green_img, 5, 0,  create_color(0, 13, 0))

    # Create an blue channel image with six pixels.
    blue_img = create_image(6, 1)
    set_color(blue_img, 0, 0,  create_color(0, 0, 0))
    set_color(blue_img, 1, 0,  create_color(0, 0, 1))
    set_color(blue_img, 2, 0,  create_color(0, 0, 127))
    set_color(blue_img, 3, 0,  create_color(0, 0, 224))
    set_color(blue_img, 4, 0,  create_color(0, 0, 255))
    set_color(blue_img, 5, 0,  create_color(0, 0, 255))

    # Create an image that's identical to the one a correct implementation of
    # combine should produce when it is passed the red_img, green_img and blue_img as inputs.
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(13, 0, 1))
    set_color(expected, 2, 0,  create_color(255, 127, 127))
    set_color(expected, 3, 0,  create_color(125, 73, 224))
    set_color(expected, 4, 0,  create_color(254, 255, 255))
    set_color(expected, 5, 0,  create_color(87, 13, 255))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    combined_img = combine(red_img, green_img, blue_img)
    for x, y, col in combined_img: # col is the Color object for the pixel @ (x,y)
        # There's no need to unpack that object into
        # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


if __name__ == "__main__":
    #red_img = load_image(choose_file())
    #green_img = load_image(choose_file())
    #blue_img = load_image(choose_file())
    # combine images
    #combined = combine(red_img, green_img, blue_img)
    #show(combined)
    test_combine()