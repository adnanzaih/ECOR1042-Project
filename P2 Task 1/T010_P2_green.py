#ECOR 1042 P2 Task 1, Individual Filter and Test Function

#Team 10: Green Filter
#Vincent Chen 101196001 

#import all functions from Cimpl
from Cimpl import *

from unit_testing import check_equal

#Green filter function
def green_channel(image : Image)-> Image:
 """
 returns a copy of the original image that now only contains the green components of each pixel
 >>>orginal_image =load_image(choosefile())
 >>>new_image = green_channel(original_image)
 >>>show(new_image)
 """
 green_image = copy(image) #Copies the orginal image to variable green_image
 for pixel in green_image: #iterates over every pixel and takes only the green component of each pixel
  x, y, (r, g, b) = pixel
  new_colour = create_color( 0,g,0)
  set_color (green_image, x, y, create_color(0,g,0))
  
 return green_image

#Test Function
def test_green() -> None:  
    '''
    A test function for green_channel.
    
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
    
    green_image = green_channel(original)   #Using filter function on the original image
    
    for x, y, col in green_image: # col is the Color object for the pixel @ (x,y)
                                 # There's no need to unpack that object into
                                 # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))



#MainScript

image = load_image(choose_file())
green_image = green_channel(image)
show(green_image)
test_green()
