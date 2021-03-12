#Ayesha Dassanayake T010 101180472

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image

from unit_testing import check_equal

def blue_channel(image: Image) -> Image:
    
    """
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

def test_blue() -> None:
    """
    Tests blue_channel
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
        
#Main
image = load_image(choose_file())
new_image = blue_channel(image)
show(new_image)
test_blue() 

