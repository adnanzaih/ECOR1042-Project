from Cimpl import *
from simple_Cimpl_filters import *

def sepia_filter(image: Image) -> Image:
    """ Returns an image with a asepia filter applied meaning it is grayscale image with a yellow tint. The image is meant to look old.
    >>>
    >>>
    >>>
    """
    
    #call grayscale function to make the image gray
    g_image = grayscale(image)
    for x, y, (r, g, b) in image: #looks through all values of each pixel in the image
       
        if (r<63): #only have to compare one since all values in grayscale are the same
            set_color(g_image, x, y, create_color((r*1.1),g,(b*0.9))) #changes the images colour accordingly for a dark gray area
        elif (r>=63) and (r<=191):
            set_color(g_image, x, y, create_color((r*1.15),g,(b*0.85))) #changes the images colour accordingly for a medium gray area
        elif (r>191):
            set_color(g_image, x, y, create_color((r*1.08),g,(b*0.93))) #changes the images colour accordingly for a light gray area


    return g_image

file = load_image(choose_file())
show(sepia_filter(file))

