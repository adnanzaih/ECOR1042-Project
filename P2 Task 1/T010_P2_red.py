#Logan DeLaat - T010 - 101182975

from Cimpl import *
from unit_testing import *

#fuction definitions
def red_channel(image: Image) -> Image:
    """
    Author Logan DeLaat
    Returns a copy of the image in png format which only contains the red components of the original image's pixel's colour
    >>> image = load_image(choose_file())
    >>> show(red_channel(image))
    """

    copy_image = copy(image) #creates copy of image to be changed
    for x, y, (r, g, b) in image: #looks through all values of each pixel in the image
        set_color(copy_image, x, y, create_color(r,0,0))  #set the colour to only contain the red value the pixel originally had      
    return copy_image
    
#testing function



def check_red() -> None:
    """
    Author Logan DeLaat
    Tests the red_channel function to make sure the result is the same as expected
    >>>check_red() 
    """
    #create small image with 6 pixels to test the function
    test_image = create_image(6,1)
    set_color(test_image, 0, 0, create_color(11, 22, 33))
    set_color(test_image, 1, 0, create_color(55, 0, 133))
    set_color(test_image, 2, 0, create_color(14, 72, 33))
    set_color(test_image, 3, 0, create_color(78, 100, 2))
    set_color(test_image, 4, 0, create_color(0, 0, 1))
    set_color(test_image, 5, 0, create_color(44, 77, 66))

    #creates a small image with 6 pixels with the expected outcome to compare the test image to
    expected_image = create_image(6,1)
    set_color(expected_image, 0, 0, create_color(11, 0, 0))
    set_color(expected_image, 1, 0, create_color(55, 0, 0))
    set_color(expected_image, 2, 0, create_color(14, 0, 0))
    set_color(expected_image, 3, 0, create_color(78, 0, 0))
    set_color(expected_image, 4, 0, create_color(0, 0, 0))
    set_color(expected_image, 5, 0, create_color(44, 0, 0))

    
    #Comparing expected image to the image produced by red_channel 
    for x, y, col in red_channel(test_image) : #goes through all the pixels and all their values
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y)) #gets the colour of the pixel and compares it
    
#main script
file = load_image(choose_file())
show(red_channel(file))
check_red()
