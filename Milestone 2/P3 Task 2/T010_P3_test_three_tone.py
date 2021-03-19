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
    test functionality of the three tone filter. Tests tree_tone for input colours (lemon, white, blood).

    Author: Adnan Hafeez

    >>> test_green()
    '''

    # Create image with test cases
    test_image1 = create_image(6, 1) #input colors (colour1: lemon (255,255,0), colour2: white (255, 255, 255), colour3: blood (255, 0, 0)
    set_color(test_image1, 0, 0,  create_color(0, 84, 84)) #pixel brightness = 0 + 84 + 84 / 3 = 56, pixel should be set to colour1
    set_color(test_image1, 1, 0,  create_color(0, 110, 255)) # pixel brightness = 121, tone should be set to colour2
    set_color(test_image1, 2, 0,  create_color(255, 255, 255)) #pixel brightness = 255, tone should be set to colour3
    set_color(test_image1, 3, 0,  create_color(145, 75, 220)) #pixel brightness = 146, tone should be set to colour2
    set_color(test_image1, 4, 0,  create_color(121, 75, 50)) #pixel_brightness = 82, tone should be set to colour1
    set_color(test_image1, 5, 0,  create_color(0, 255, 0)) #pixel_brightness = 82, tone should be set to colour2

    # Create an image that's identical to the one a correct implementation of
    # green_channel should produce when it is passed original.
    expected_img1 = create_image(6, 1)
    set_color(expected_img1, 0, 0,  create_color(255, 255, 0))
    set_color(expected_img1, 1, 0,  create_color(255, 255, 255))
    set_color(expected_img1, 2, 0,  create_color(255, 0, 0))
    set_color(expected_img1, 3, 0,  create_color(255, 255, 255))
    set_color(expected_img1, 4, 0,  create_color(255, 255, 0))
    set_color(expected_img1, 5, 0,  create_color(255, 255, 255))


    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    three_tone1 = three_tone(test_image1,"lemon","white","blood")   #Using filter function on the original image

    for x, y, col in three_tone1: # col is the Color object for the pixel @ (x,y)
        # There's no need to unpack that object into
        # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_img1, x, y))


#Main Script
test_three_tone()