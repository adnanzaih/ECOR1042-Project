#ECOR 1042 P3 Task 2, Filter Test Function

#10: three tone image filter testing function
#Adnan Hafeez 101210710

from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, get_color, create_image

from unit_testing import check_equal

from T010_P3_filter_three_tone import three_tone

#Test Function
def test_three_tone() -> None:
    '''
    A test function for three tone filter. Using a 6x1 pixel image as a sample to
    test functionality of the three tone filter.

    Author: Adnan Hafeez

    >>> test_green()
    '''

    # Create image with test cases

    original = create_image(4, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 110, 10))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(145, 75, 220))

    # Create an image that's identical to the one a correct implementation of
    # green_channel should produce when it is passed original.
    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 110, 0))
    set_color(expected, 2, 0,  create_color(0, 127, 0))
    set_color(expected, 3, 0,  create_color(0, 75, 0))


    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    green_image = three_tone(original)   #Using filter function on the original image

    for x, y, col in green_image: # col is the Color object for the pixel @ (x,y)
        # There's no need to unpack that object into
        # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))