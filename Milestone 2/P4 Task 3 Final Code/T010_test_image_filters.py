from T010_image_filters import extreme_contrast, posterize, sepia_filter, three_tone, flip_horizontal, flip_vertical, detect_edges, draw_curve

from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, create_image, get_color

from unit_testing import check_equal





    
def test_extreme_contrast() -> None:
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
        



def test_three_tone() -> None:
    '''
    A test function for three tone filter. Using a 6x1 pixel image as a sample to
    test functionality of the three tone filter. Tests tree_tone filter for input colours (lemon, white, blood).
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
    set_color(expected_img1, 0, 0,  create_color(255, 255, 0)) #colour1
    set_color(expected_img1, 1, 0,  create_color(255, 255, 255)) #colour2
    set_color(expected_img1, 2, 0,  create_color(255, 0, 0)) #colour 3
    set_color(expected_img1, 3, 0,  create_color(255, 255, 255)) #colour 2
    set_color(expected_img1, 4, 0,  create_color(255, 255, 0)) #colour 1
    set_color(expected_img1, 5, 0,  create_color(255, 255, 255)) #colour 1


    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    three_tone1 = three_tone(test_image1,"lemon","white","blood")   #Using filter function on the original image

    for x, y, col in three_tone1: # col is the Color object for the pixel @ (x,y)
        # There's no need to unpack that object into
        # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_img1, x, y))

def test_draw_curve():
        
    #if the polynomial [0,2,0] was entered
    """
    Vincent Chen 101196001 
    tests the draw curve function
    >>>test_draw_curve()    
    """
    print ("Testing draw cruve")
        
    test_image_color = create_color(255,255,255) 
        
    original = create_image(9,9,test_image_color) #Create a 9x9 pixel image
        
    expected = create_image(9,9,test_image_color) #Create the expected image that the draw_curve function will return
        
    set_color(expected,0,0, create_color(255,0,0))
    set_color(expected,0,1, create_color(255,0,0))
    set_color(expected,0,2, create_color(255,0,0))
    set_color(expected,0,3, create_color(255,0,0))
        
    set_color(expected,1,0, create_color(255,0,0))
    set_color(expected,1,1, create_color(255,0,0))
    set_color(expected,1,2, create_color(255,0,0))
    set_color(expected,1,3, create_color(255,0,0))
    set_color(expected,1,4, create_color(255,0,0))
    
    set_color(expected,2,0, create_color(255,0,0))
    set_color(expected,2,1, create_color(255,0,0))   
    set_color(expected,2,2, create_color(255,0,0))
    set_color(expected,2,3, create_color(255,0,0))
    set_color(expected,2,4, create_color(255,0,0))
    set_color(expected,2,5, create_color(255,0,0))
    set_color(expected,2,6, create_color(255,0,0))
    
    set_color(expected,3,1, create_color(255,0,0))
    set_color(expected,3,2, create_color(255,0,0)) 
    set_color(expected,3,3, create_color(255,0,0))   
    set_color(expected,3,4, create_color(255,0,0))
    set_color(expected,3,5, create_color(255,0,0))
    set_color(expected,3,6, create_color(255,0,0))
    set_color(expected,3,7, create_color(255,0,0))
    set_color(expected,3,8, create_color(255,0,0))
    
    
    set_color(expected,4,3, create_color(255,0,0))
    set_color(expected,4,4, create_color(255,0,0)) 
    set_color(expected,4,5, create_color(255,0,0))
    set_color(expected,4,6, create_color(255,0,0))
    set_color(expected,4,7, create_color(255,0,0))
    set_color(expected,4,8, create_color(255,0,0))
        
    border_list = [(0,0),(0,0),(4,8)] #Expected borders that draw_curve function will return
           
    returned_tuple = draw_curve(original,"blood",[(0,0),(4,8)]) #Draw curve returns a tuple index 1 is the image, and index 2 are the borders
    curve_image = returned_tuple[0]
    curve_border = returned_tuple[1]
    for x,y,col in curve_image:   # col is the Color object for the pixel @ (x,y)
        check_equal("Checking pixel @(" + str(x) + "," + str(y) + ")" , col,get_color(expected,x,y))
        
    for i in range(len(border_list)):
        check_equal("Checking border No." +str(i+1)+ " @ x-coordinate:",border_list[i][0],curve_border[i][0])
        check_equal("Checking border No." +str(i+1)+ " @ y-coordinate:",border_list[i][1],curve_border[i][1])
         
                
    

def test_edge() -> None:
    """Author Logan DeLaat 101182975
    Tests edge detection filter
    >>>test_edge()
    """
    
    #Creates a small image with 6 pixels to test the function.
    test_image = create_image(3,2)
    set_color(test_image, 0, 0, create_color(11, 22, 33))
    set_color(test_image, 1, 0, create_color(55, 186, 201))
    set_color(test_image, 2, 0, create_color(140, 72, 33))
    set_color(test_image, 0, 1, create_color(78, 100, 254))
    set_color(test_image, 1, 1, create_color(5, 100, 69))
    set_color(test_image, 2, 1, create_color(44, 145, 119))

    #Creates a small image with 6 pixels with the expected outcome to compare the test image to.
    expected_image = create_image(3,2)
    set_color(expected_image, 0, 0, create_color(0, 0, 0))
    set_color(expected_image, 1, 0, create_color(0, 0, 0))
    set_color(expected_image, 2, 0, create_color(255, 255, 255))
    set_color(expected_image, 0, 1, create_color(255, 255, 255))
    set_color(expected_image, 1, 1, create_color(255, 255, 255))
    set_color(expected_image, 2, 1, create_color(255, 255, 255))    


    
    #Comparing expected image to the image produced by red_channel 
    for x, y, col in detect_edges(test_image, 25) : #goes through all the pixels and all their values
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y)) #gets the colour of the pixel and compares it    
        
        
        
def test_horizontal() -> None:
    """
    A test function for horizontal flip filter. Using a 6x1 pixel image as a sample to
    test functionality against an expected image array given as expected.
    Author: Adnan Hafeez
    >>> test_horizontal()
    """

    #Creates an image with 4 pixels
    original = create_image(6,1) #create image to be tested
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(10, 20, 60))
    set_color(original, 2, 0,  create_color(180, 199, 196))
    set_color(original, 3, 0,  create_color(255, 255, 255))
    set_color(original, 4, 0, create_color(255, 255, 255))
    set_color(original, 5, 0, create_color(124, 45, 0))


    #Expected transformation of image
    expected = create_image(6, 1) #create expected image
    set_color(expected, 0, 0,  create_color(124, 45, 0))
    set_color(expected, 1, 0,  create_color(255, 255, 255))
    set_color(expected, 2, 0,  create_color(255, 255, 255))
    set_color(expected, 3, 0,  create_color(180, 199, 196))
    set_color(expected, 4, 0, create_color(10, 20, 60))
    set_color(expected, 5, 0, create_color(0, 0, 0))

    #Comparing expected image to the image produced by sepia_filter
    img = flip_horizontal(original)
    for x, y, col in img:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



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
        


#Main Script

if __name__ == "__main__":
    test_extreme_contrast()
    test_posterize()
    test_sepia()
    test_three_tone()
    test_draw_curve()
    test_edge()
    test_horizontal()
    test_vertical()