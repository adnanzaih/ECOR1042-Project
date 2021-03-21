#Vincent Chen T010 101196001
#Test for extreme contrast filter

from Cimpl import *
from unit_testing import check_equal
from T010_P3_extreme_contrast import extreme_contrast

    
def test_extreme_contrast() -> str:
    """
    Vincent Chen, 101196001
    A test function for extreme_contrast
    >>> test_extreme_contrast()
    """
    #create original image and set test cases
    original_image = create_image(4, 1) 
    set_color(original_image, 0, 0, create_color(128, 150, 140))
    set_color(original_image, 1, 0, create_color(0, 1, 255))
    set_color(original_image, 2, 0, create_color(100, 128, 127))
    set_color(original_image, 3, 0, create_color(127, 128, 128))
    
    # Create image with expected results
    expected_image = create_image(4, 1) 
    # Fill in the correct values in each location 
    set_color(expected_image, 0, 0, create_color(255, 255, 255))
    set_color(expected_image, 1, 0, create_color(0, 0, 255))
    set_color(expected_image, 2, 0, create_color(0, 255, 0))
    set_color(expected_image, 3, 0, create_color(0, 255, 255))
    

    #Use filter function on the original image
    filtered_image = extreme_contrast(original_image)
    
    # Comparing the transformed image returned by the filter with the expected image, one pixel at a time.  
    print("Testing extreme contrast")
    for x, y, col in filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')', col, get_color(expected_image, x, y))
        
if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = extreme_contrast(image)
    show(new_image)
    test_extreme_contrast()
