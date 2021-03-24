#ECOR 1042 P3 Task 2, Individual Filter

# 10: Vertical flip filter
#Vincent Chen 101196001 

#Import all functions from Cimpl module
from Cimpl import *

def flip_vertical(orginal_image:Image)-> Image:
    """
    Vincent Chen , 101196001
    Returns a copy of an image that is flipped along a horizontal line.
    The result is an upside-down copy of original_image called v_flipped_image
    
    >>>original_image = load_image(choosefile())
    >>>three_tone_image = flip_vertical(original_image)
    >>>show(v_flipped_image)
    """
    #v_flipped_image= copy(original_image)
    #width = get_width(original_image)
    #height = get_height(original_image)
    #for y in range(height):
        #y_flip = height-(y+1)
        #for x in range(width):
            #color = get_color(original_image,x,y)
            #set_color(v_flipped_image,x,y_flip,color)
            
    v_flipped_image= copy(original_image)
    for pixel in v_flipped_image: #iterates over every pixel in the image and take only the green component of each pixel
        x, y, (r, g, b) = pixel
        color = get_color(original_image,x,y)
        set_color(v_flipped_image,x,-y-1,color)   
    return v_flipped_image
            
if __name__ == "__main__":
    original_image = load_image(choose_file())
    v_flipped_image = flip_vertical(original_image)
    show(v_flipped_image)
        
