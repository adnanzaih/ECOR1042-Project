#Ayesha Dassanayake T010 101180472

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image

from unit_testing import check_equal

from simple_Cimpl_filters import grayscale 

from T010_P3_filter_sepia import sepia_filter

def test_sepia() -> None:
    """
    Author: Ayesha Dassanayake
    
    Tests sepia_filter
    >>> test_sepia()
    """
    
    #Creates an image with 4 pixels
    original = create_image(4,1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(10, 20, 60))
    set_color(original, 2, 0,  create_color(180, 199, 196))
    set_color(original, 3, 0,  create_color(255, 255, 255))    
    
    #Expected transformation of image
    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0)) 
    set_color(expected, 1, 0,  create_color(33, 30, 27)) 
    set_color(expected, 2, 0,  create_color(219, 191, 162)) 
    set_color(expected, 3, 0,  create_color(255, 255, 237)) 
    
    #Comparing expected image to the image produced by sepia_filter
    sepia_img = sepia_filter(original)   
    for x, y, col in sepia_img: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))   
        
if __name__ == "__main__":
    #file = load_image(choose_file())
    #show(sepia_filter(file))
    test_sepia() 

