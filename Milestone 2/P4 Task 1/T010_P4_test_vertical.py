#Ayesha Dassanayake T010 101180472

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image

from unit_testing import check_equal

from T010_P4_filter_vertical import flip_vertical

def test_vertical() -> None:
    """
    Author: Ayesha Dassanayake
    
    Tests flip_vertical
    >>> test_vertical()
    """
    
    #Creates an image with 6 pixels
    original = create_image(1,6)
    set_color(original, 0, 0,  create_color(60, 80, 240))
    set_color(original, 0, 1,  create_color(80, 150, 200))
    set_color(original, 0, 2,  create_color(100, 100, 100))
    set_color(original, 0, 3,  create_color(20, 255, 150))    
    set_color(original, 0, 4,  create_color(0, 0, 0))
    set_color(original, 0, 5,  create_color(210, 140, 90))
            
    
    #Expected transformation of image
    expected = create_image(1, 6)
    set_color(expected, 0, 0,  create_color(210, 140, 90)) 
    set_color(expected, 0, 1,  create_color(0, 0, 0)) 
    set_color(expected, 0, 2,  create_color(20, 255, 150)) 
    set_color(expected, 0, 3,  create_color(100, 100, 100)) 
    set_color(expected, 0, 4,  create_color(80, 150, 200)) 
    set_color(expected, 0, 5,  create_color(60, 80, 240)) 
   
    #Comparing expected image to the image produced by flip_vertical
    vertical_img = flip_vertical(original)   
    for x, y, col in vertical_img: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))   
        
if __name__ == "__main__":
    #file = load_image(choose_file())
    #show(flip_vertical(file))
    test_vertical() 
