#Ayesha Dassanayake T010 101180472

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color

def extreme_contrast(image: Image) -> Image:

    """
    Author: Ayesha Dassanayake
    
    Returns a new png image changing the red, green, and blue components to their maximum or minimum values
    >>> image = load_image(choose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)
    """    
    
    contrast_img = copy(image)
    
    #goes through each pixel and sets their colour components to their maximum or minimum values
    for x,y,(r,g,b) in image:
        if r >= 0 and r <= 127:
            new_red = 0
        elif r > 127 and r <= 255:
            new_red = 255
        
        if g >= 0 and g <= 127:
            new_green = 0
        elif g > 127 and g <= 255:
            new_green = 255
        
        if b >= 0 and b <= 127:
            new_blue = 0
        elif b > 127 and b <= 255:
            new_blue = 255                
            
        contrast = create_color(new_red,new_green,new_blue)
        set_color(contrast_img,x,y,contrast)
        
    return contrast_img    

if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = extreme_contrast(image)
    show(new_image)