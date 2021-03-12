#Logan DeLaat - T010 - 101182975

from Cimpl import *
from unit_testing import *

#fuction definitions
def red_channel(image: Image) -> Image:
    """
    Returns a copy of the image in png format which only contains the red components of the original image's pixel's colour
    >>> image = load_image(choose_file())
    >>> show(red_channel(image))
    """

    copy_image = copy(image)
    for x, y, (r, g, b) in image:
        set_color(copy_image, x, y, create_color(r,0,0))        
    return copy_image
    
#testing function



def check_red() -> None:
    """
    Tests the red_channel function to make sure the result is the same as expected
    >>>check_red()
    """
    #create small image with 6 pixels to check
    test_image = create_image(6,1)
    set_color(test_image, 0, 0, create_color(11, 22, 33))
    set_color(test_image, 1, 0, create_color(55, 0, 133))
    set_color(test_image, 2, 0, create_color(14, 72, 33))
    set_color(test_image, 3, 0, create_color(78, 100, 2))
    set_color(test_image, 4, 0, create_color(0, 0, 1))
    set_color(test_image, 5, 0, create_color(44, 77, 66))

    
    expected_image = create_image(6,1)
    set_color(expected_image, 0, 0, create_color(11, 0, 0))
    set_color(expected_image, 1, 0, create_color(55, 0, 0))
    set_color(expected_image, 2, 0, create_color(14, 0, 0))
    set_color(expected_image, 3, 0, create_color(78, 0, 0))
    set_color(expected_image, 4, 0, create_color(0, 0, 0))
    set_color(expected_image, 5, 0, create_color(44, 0, 0))

    
    #Comparing expected image to the image produced by red_channel 
    for x, y, col in red_channel(test_image) : 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y))
    
#main script
file = load_image(choose_file())
show(red_channel(file))
check_red()
