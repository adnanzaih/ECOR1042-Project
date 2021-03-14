#P2 Task 2: Milestone 1’s Final Team Code
#Team 10: Vincent Chen-101196001, Adnan Hafeez-101210710, Logan DeLaat-101182975, Ayesha Dassanayake-101180472

#import all functions from Cimpl
from Cimpl import *

from unit_testing import check_equal

#Function for red filter: Logan DeLaat-101182975
def red_channel(image: Image) -> Image:
    """
    Logan DeLaat
    Returns a copy of the image in png format which only contains the red components of the original image's pixel's colour
    >>> image = load_image(choose_file())
    >>> show(red_channel(image))
    """

    copy_image = copy(image) #creates copy of image to be changed
    for x, y, (r, g, b) in image: #looks through all values of each pixel in the image
        set_color(copy_image, x, y, create_color(r,0,0))  #set the colour to only contain the red value the pixel originally had
    return copy_image

#Green filter function: Vincent Chen-101196001
def green_channel(image : Image)-> Image:
 """
 Vincent Chen
 returns a copy of the original image that now only contains the green components of each pixel
 >>>orginal_image =load_image(choosefile())
 >>>new_image = green_channel(original_image)
 >>>show(new_image)
 """
 green_image = copy(image) #Copies the original image onto variable green_image
 
 for pixel in green_image: #iterates over every pixel in the image and take only the green component of each pixel
  x, y, (r, g, b) = pixel
  new_colour = create_color( 0,g,0)
  set_color (green_image, x, y, create_color(0,g,0))
  
 return green_image #returns the filtered green image

#Function for blue filter: Ayesha Dassanayake-101180472       
def blue_channel(image: Image) -> Image:
    
    """
    Ayesha Dassanayake
    Returns a new png image containing only the blue components of the pixels in the original image
    >>> image = load_image(choose_file())
    >>> new_image = blue_channel(image)
    >>> show(new_image)
    """
    blue_img = copy(image)
    
    #removes red and green components from each pixel
    for x,y,(r,g,b) in image:
        blue = create_color(0,0,b)
        set_color(blue_img,x,y,blue)
        
    return blue_img

#Function for combined filter: Adnan Hafeez-101210710
def combine(red: Image, green: Image, blue:Image) -> Image:
    """
    Adnan Hafeez - T010 - 101210710
    Return an image that is a combination of the red, blue and green channels.
    By loading a red, green and blue filtered
    set of images in that specific order only.
    >>> red_img = load_image(choose_file())
    >>> green_img = load_image(choose_file())
    >>> blue_img = load_image(choose_file())
    >>> combined = combine(red_img, green_img, blue_img)
    >>> show(combined)
    """
    new_image = copy(red)
    for x, y, _ in red:
        red_pixel = get_color(red,x,y)
        green_pixel = get_color(green,x,y)
        blue_pixel = get_color(blue,x,y)
        combined_colors = create_color(red_pixel[0], green_pixel[1], blue_pixel[2])
        set_color(new_image, x,y, combined_colors)
    return new_image

#Test Function for red filter: Logan DeLaat-101182975
def check_red() -> None:
    """
    Logan DeLaat
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

#Test Function for green filter: Vincent Chen-101196001
def test_green() -> None:
    '''
    Vincent Chen
    A test function for green_channel. Uses a 4x1 pixel image as a sample to
    test functionality of the green filter.
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

#Test Function for blue filter: Ayesha Dassanayake-101180472
def test_blue() -> None:
    """
    Ayesha Dassanayake
    A test function for blue_channel. Uses a 4x1 pixel image as a sample to
    test functionality of the blue filter.
    >>> test_blue()
    """

    #Creates an image with 4 pixels
    original = create_image(4,1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(10, 20, 60))
    set_color(original, 2, 0,  create_color(150, 0, 150))
    set_color(original, 3, 0,  create_color(0, 81, 235))

    #Expected transformation of image
    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 60))
    set_color(expected, 2, 0,  create_color(0, 0, 150))
    set_color(expected, 3, 0,  create_color(0, 0, 235))

    #Comparing expected image to the image produced by blue_channel
    blue_img = blue_channel(original)
    for x, y, col in blue_img:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


#Test function for combined filter: Adnan Hafeez-101210710
def test_combine() -> None:
    """
    Adnan Hafeez - T010 - 101210710
    A test function for the combined filter. Utilizes a 6x1 test image for which an expected and calculated pixel value
    is obtained by applying the combine filter. The expected pixel values for each red, green, and blue image are compared
    with the calculated pixel values obtained using the combine filter. If a test passes, "PASSED" is printed, otherwise "FAILED"
    for each pixel value (x,y) respectively.
    >>> test_combine()
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


#Load image
image = load_image(choose_file())

#Main Script green
green_image = green_channel(image)
show(green_image)
print("Testing green filter:")
test_green()

#main script red
show(red_channel(image))
print("Testing red filter:")
check_red()

#main script blue
new_image = blue_channel(image)
show(new_image)
print("Testing blue filter:")
test_blue() 

#main script combine
combined = combine(red_channel(image), green_channel(image), blue_channel(image))
show(combined)
print("Testing combine filter:")
test_combine()
