#Vincent Chen 101196001 

#Import all functions from Cimpl module
from Cimpl import *

def flip_horizontal(orginal_image:Image)-> Image:
    """
    Vincent Chen , 101196001
    Returns a copy of an image that is flipped along a vertical line.
    The result is an mirrored copy of original_image called h_flipped_image
    
    >>>original_image = load_image(choosefile())
    >>>three_tone_image = flip_horizontal(original_image)
    >>>show(h_flipped_image)
    """
    #v_flipped_image= copy(original_image)
    #width = get_width(original_image)
    #height = get_height(original_image)
    #for y in range(height):
        #y_flip = height-(y+1)
        #for x in range(width):
            #color = get_color(original_image,x,y)
            #set_color(v_flipped_image,x,y_flip,color)
            
    h_flipped_image= copy(original_image)
    for pixel in h_flipped_image: #iterates over every pixel in the image and take only the green component of each pixel
        x, y, (r, g, b) = pixel
        color = get_color(original_image,x,y)
        set_color(h_flipped_image,-x,y,color)   
    return h_flipped_image
            
if __name__ == "__main__":
    original_image = load_image(choose_file())
    h_flipped_image = flip_horizontal(original_image)
    show(h_flipped_image)
