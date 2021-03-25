#Logan DeLaat - T010 - 101182975

from Cimpl import Image, set_color, create_color, load_image, choose_file, show, copy, get_height

def flip_veritcal(image: Image)-> Image:
    """Returns a copy of the image with that is flipped over an imaginary horizontal line in the centre of the image
    >>>file = load_image(choose_file())
    >>>show(flip_vertical(file))
    """
    
    bottom = get_height(image) #This is needed to find the total height of the image so that the distance the pixel need to be "swaped" can be caluclated. 
    copy_image = copy(image)
    for x, y, (r, g, b) in image:
        set_color(copy_image, x, (bottom-y-1), create_color(r,g,b)) #Replaces pixel's colour with the colour of the pixel equal distance away

            
    return(copy_image)
        
if __name__ == "__main__":
    file = load_image(choose_file())
    show(flip_veritcal(file))
