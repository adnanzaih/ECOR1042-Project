#Logan DeLaat - T010 - 101182975

from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, create_image, get_color
from T010_P3_filter_posterize import posterize

from unit_testing import check_equal

def test_posterize() -> None:
    """Author Logan DeLaat 101182975
    Tests posterize filter
    >>>test_posterize()
    """
    
    #create small image with 6 pixels to test the function
    test_image = create_image(6,1)
    set_color(test_image, 0, 0, create_color(11, 22, 33))
    set_color(test_image, 1, 0, create_color(55, 186, 201))
    set_color(test_image, 2, 0, create_color(140, 72, 33))
    set_color(test_image, 3, 0, create_color(78, 100, 254))
    set_color(test_image, 4, 0, create_color(5, 100, 69))
    set_color(test_image, 5, 0, create_color(44, 145, 119))

    #creates a small image with 6 pixels with the expected outcome to compare the test image to
    expected_image = create_image(6,1)
    set_color(expected_image, 0, 0, create_color(31, 31, 31))
    set_color(expected_image, 1, 0, create_color(31, 159, 223))
    set_color(expected_image, 2, 0, create_color(159, 95, 31))
    set_color(expected_image, 3, 0, create_color(95, 95, 223))
    set_color(expected_image, 4, 0, create_color(31, 95, 95))
    set_color(expected_image, 5, 0, create_color(31, 159, 95))

    
    #Comparing expected image to the image produced by red_channel 
    for x, y, col in posterize(test_image) : #goes through all the pixels and all their values
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y)) #gets the colour of the pixel and compares it    
        
if __name__ == "__main__":
    #file = load_image(choose_file())
    #show(sepia_posterize(file))
    test_posterize()     
