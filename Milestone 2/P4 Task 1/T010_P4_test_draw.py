from T010_P4_filter_draw import draw_curve
from Cimpl import *
from unit_testing import check_equal

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
         
                
    

    


if __name__ == "__main__":
    test_draw_curve()
