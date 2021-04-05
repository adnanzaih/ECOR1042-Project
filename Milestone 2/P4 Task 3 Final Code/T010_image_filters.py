#Import relevant libraries
from Cimpl import *
from simple_Cimpl_filters import grayscale
from point_manipulation import sort_points,  get_x_y_lists #import useful libraries for sorting
from math import floor
import numpy as np #for interpolation

#Logan DeLaat - T010 - 101182975
#fuction definitions
def red_channel(image: Image) -> Image:
    """
    Author Logan DeLaat
    Returns a copy of the image in png format which only contains the red components of the original image's pixel's colour
    >>> image = load_image(choose_file())
    >>> show(red_channel(image))
    """

    copy_image = copy(image) #creates copy of image to be changed
    for x, y, (r, g, b) in image: #looks through all values of each pixel in the image
        set_color(copy_image, x, y, create_color(r,0,0))  #set the colour to only contain the red value the pixel originally had      
    return copy_image

#Ayesha Dassanayake T010 101180472
def extreme_contrast(image: Image) -> Image:

    """
    Author: Ayesha Dassanayake
    
    Returns a new image changing the red, green, and blue components to their maximum or minimum values
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


#10: posterize image filter
#Adnan Hafeez 101210710
def posterize(image: Image) -> Image:
    """
    The function returns the input image modified to have a smaller number of colours than the original image.
    Applies a posterize filter to the input image.
    Author: Adnan Hafeez
    >>> image = load_image(choose_file())
    >>> posterized_image = posterize(image)
    >>> show(posterized_image)
    """
    new_image =copy(image)

    def _adjust_component(value: int) -> int:
        if value >= 0 and value <= 63:
            value = 31
        elif value >= 64 and value <= 127:
            value = 95
        elif value >= 128 and value <= 191:
            value = 159
        elif value >= 192 and value <= 255:
            value = 223
        return value

    # filter the intensities of every component in every pixel and calculate the brightness.
    for x, y, (r, g, b) in new_image:
        adjusted_r = _adjust_component(r)
        adjusted_g = _adjust_component(g)
        adjusted_b = _adjust_component(b)
        set_color(new_image, x, y, create_color(adjusted_r, adjusted_g, adjusted_b))
    return new_image


#Logan DeLaat - T010 - 101182975
def sepia_filter(image: Image) -> Image:
    """ Returns an image with a asepia filter applied meaning it is grayscale image with a yellow tint. The image is meant to look old.
    Author: Logan DeLaat
    >>>file = load_image(choose_file())
    >>>show(sepia_filter(file))
    """
    
    #call grayscale function to make the image gray
    new_image = copy(image) #can't alter original image
    g_image = grayscale(new_image)
    for x, y, (r, g, b) in g_image: #looks through all values of each pixel in the image
       
        if (r<63): #only have to compare one since all values in grayscale are the same
            set_color(g_image, x, y, create_color((r*1.1),g,(b*0.9))) #changes the images colour accordingly for a dark gray area
        elif (r>=63) and (r<=191):
            set_color(g_image, x, y, create_color((r*1.15),g,(b*0.85))) #changes the images colour accordingly for a medium gray area
        elif (r>191):
            set_color(g_image, x, y, create_color((r*1.08),g,(b*0.93))) #changes the images colour accordingly for a light gray area


    return g_image


# 10: three-tone image filter
#Vincent Chen 101196001 
def three_tone (original_image:Image, colour1:str, colour2:str, colour3:str) -> Image:
    """
    Vincent Chen, 101196001
    Returns a copy of the original image that has different colours at each 
    pixel based on the brightness at each pixel.
    If the pixel's brightness is betwen 0-84 inclusive, then the tone is set to colour1
    If the pixel's brightness is betwen 85-170 inclusive, then the tone is set to colour2
    If the pixel's brightness is betwen 171-255 inclusive, then the tone is set to colour3
    >>>original_image = load_image(choosefile())
    >>>three_tone_image = three_tone(original_image, black, gray, white)
    >>>show(three_tone_image)
    
    >>>original_image = load_image(choosefile())
    >>>three_tone_image = three_tone(original_image, blue, lemon, aqua)
    >>>show(three_tone_image)
    """
    colour_list= [("black",0,0,0), ("white",255,255,255),("blood",255,0,0),("green",0,255,0)
                ,("blue",0,0,255), ("lemon",255,255,0), ("aqua",0,255,255), ("pink",255,0,255)
                ,("gray",128,128,128)]
    new_colour = []
    for i in colour_list:
        if i[0] == colour1:
            new_colour.append((i[1],i[2],i[3]))
            #print( i[1], i[2] , i[3])

    for i in colour_list:
        if i[0] == colour2:
            #print( i[1], i[2] , i[3])
            new_colour.append((i[1],i[2],i[3]))

    for i in colour_list:
        if i[0] == colour3:
            #print( i[1], i[2] , i[3])
            new_colour.append((i[1],i[2],i[3]))
            #print (new_colour)

    three_tone_image = copy(original_image)
    for pixel in three_tone_image: #iterates over every pixel in the image and take only the green component of each pixel
        x, y, (r, g, b) = pixel
        brightness = (r + g + b) / 3 #calculates brightness
        if brightness >= 0 and brightness <= 84:
            c1,c2,c3 = new_colour[0]
            new_color = create_color(c1,c2,c3)
        elif brightness >= 85 and brightness <= 170:
            c1,c2,c3 = new_colour[1] 
            new_color = create_color(c1,c2,c3) 
        elif brightness >= 171 and brightness <= 255:
            c1,c2,c3 = new_colour[2] 
            new_color = create_color(c1,c2,c3)
        set_color(three_tone_image,x,y,new_color)
        
    return three_tone_image


#Vincent Chen 101196001 
def flip_horizontal(original_image:Image) -> Image:
    """
    Vincent Chen , 101196001
    Returns a copy of an image that is flipped along a vertical line.
    The result is an mirrored copy of original_image called h_flipped_image
    
    >>>original_image = load_image(choosefile())
    >>>h_flipped_image = flip_horizontal(original_image)
    >>>show(h_flipped_image)
    """        
    h_flipped_image= copy(original_image)
    for pixel in h_flipped_image: #iterates over every pixel in the image and take only the green component of each pixel
        x, y, (r, g, b) = pixel
        color = get_color(original_image,x,y)
        set_color(h_flipped_image,-x-1,y,color)
        
    return h_flipped_image


#Logan DeLaat - T010 - 101182975
def flip_vertical(image: Image)-> Image:
    """Returns a copy of the image that is flipped over an imaginary horizontal line in the centre of the image
    >>>file = load_image(choose_file())
    >>>show(flip_vertical(file))
    """
    
    bottom = get_height(image) #This is needed to find the total height of the image so that the distance the pixel needs to be "swapped" can be calculated. 
    copy_image = copy(image)
    for x, y, (r, g, b) in image:
        set_color(copy_image, x, (bottom-y-1), create_color(r,g,b)) #Replaces pixel's colour with the colour of the pixel equal distance away
  
    return(copy_image)


#Ayesha Dassanayake T010 101180472
def detect_edges(image: Image, threshold: int) -> Image:

    """
    Author: Ayesha Dassanayake
    
    Returns a new image with black and white pixels depending if the contrast is greater or less than the threshold
    >>> image = load_image(choose_file())
    >>> new_image = detect_edges(image,8)
    >>> show(new_image)
    """    
    
    edge_img = copy(image)

    black_pix = create_color(0,0,0)
    white_pix = create_color(255,255,255)
    
    height = get_height(edge_img) #height of the image
    
    for x,y,(r,g,b) in edge_img:
        top_pix = get_color(image,x,y) 
        rtop,gtop,btop = top_pix #colour components of the top pixel
        
        #executed if there is a bottom pixel
        if y < height - 1:
            btm_pix = get_color(image,x,y+1)
            rbtm,gbtm,bbtm = btm_pix #colour components of the bottom pixel
            
            top_avg = (rtop + gtop + btop)/3 
            btm_avg = (rbtm + gbtm + bbtm)/3
            
            contrast = abs(top_avg - btm_avg) #contrast that determines whether the pixel will be black or white
            
            if contrast > threshold:
                set_color(edge_img,x,y,black_pix) #pixel becomes black
            else:
                set_color(edge_img,x,y,white_pix) #pixel becomes white 
                
        else: 
            set_color(edge_img,x,y,white_pix) #pixel becomes white 
            
    return edge_img    


#Adnan Hafeez 101210710

def draw_curve(image: Image, color:str, pointList: list) -> (Image, list):
    """
    Author: Adnan Hafeez
    Takes an PNG and a colour name as a string parameter. Requires a list of points as a parameter or user input.
    Returns a copy of the original image with a line draw ontop of the image given the input colour and a polynomial
    fitted to the points provided by the user.
    >>> image = load_image(choose_file())
    >>> output = draw_curve(image, "lemon", pointList=None)
    >>> print(output[1])
    >>> show(output[0])
    Author: Adnan Hafeez
    """
    img_height = get_height(image)
    img_width = get_width(image)

    def _pick_color(colour:str) -> tuple:
        """
        Simple colour picking function, takes in a string name for the colour and returns a tuple of the RGB values of the
        colour.
        >>>_pick_color("blood")
        >>> (255,0,0)
        >>>_pick_color("green")
        >>> (0,255,0)
        >>>_pick_color("blacj")
        >>> (0,0,0)
        Author: Adnan Hafeez
        """
        color_lst = [("black",0,0,0),("white", 255,255,255),
                     ("blood",255,0,0), ("green",0,255,0),
                     ("blue",0,0,255), ("lemon",255, 255,0),
                     ("aqua",0,255,255),("pink",255,0,255),
                     ("gray",128,128,128)]
        for i in color_lst:
            if i[0] == colour:
                return (i[1],i[2],i[3])

    def _request_points(numPoints) -> list:
        """Interactively request points from the user if not inputted in the original function call.
        Return the points sorted in ascending order as a list.
        >>> _request_points(2) #inputs (1,1) and (2,2)
        >>> [(1,1), (2,2)]
        >>> _request_points(3) #inputs (1,1) and (2,2) and (3,4)
        >>> [(1,1), (2,2),(3,4)]
        >>> _request_points(2) #inputs (1,1) and (2,2) and (4,5)
        >>> [(1,1), (2,2),(4,5)]
        Author: Adnan Hafeez
        """
        point_list = []
        for i in range(numPoints):
            user_x_input = input("Please enter the x-coordinates of your point #({0}): ".format(i+1))
            user_y_input = input("Please enter the y-coordinates of your point #({0}): ".format(i+1))
            point_list.append((int(user_x_input),int(user_y_input)))
        return sort_points(point_list) #return point listed sorted in ascending order

    def _interpolation(points: list) -> list:
        """
        Performs a 1 degree polynomial fit if the number of points submitted by the user is 2, and a quadratic fit 
        if points are greater than 2.
        >>> _interpolation([(1,2),(3,4)])
        >>> [1. 1.]
        >>> _interpolation([(12, 102), (14, 123), (160, 210)]
        >>> [ -0.06691966  12.23991114 -35.24250278]
        >>> _interpolation([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])
        >>> [2.92038426e-17 1.00000000e+00 1.00000000e+00]
        Author: Adnan Hafeez
        """""

        if len(points) <=2:
            _deg = 1
        else:
            _deg = 2
        get_x, get_y = get_x_y_lists(points)
        return np.polyfit(get_x,get_y,_deg)

    def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
        """Solves f(x)-val = 0 for x between 0 and max_x where polycoeff contains the coefficients of f,
        using EPSILON = 1. Returns None if there is no solution between the bounds.
        >>> _exhaustive_search(640,[2.92038426e-17 1.00000000e+00 1.00000000e+00],0)
        >>> None
        >>> _exhaustive_search(640,[2.92038426e-17 1.00000000e+00 1.00000000e+00],480)
        >>> 477
        >>> _exhaustive_search(640,[0.33444816 99.66555184],480)
        >>> None
        Author: Adnan Hafeez
        """
        EPSILON = 1
        step = 1
        guess = 0
        if len(polycoeff) > 2:
            a,b,c = polycoeff
        else:
            a=0
            b, c = polycoeff
        func_sol = a*guess**2 + b*guess**1 + c - val
        while abs(func_sol) >= EPSILON and guess <= max_x:
            guess += step
            func_sol = a*guess**2 + b*guess**1 + c - val
        if guess > max_x:
            return None
        else:
            return floor(guess) #to round down into the image grid

    def _image_border_finding(image_size: list, polycoeff: list) -> list:
        """
        Takes the size of the image and interpolation coefficients of the polynomial function.
        Returns the pixels where the curve intersects the image borders.
        >>> _image_border_finding([640,480],[2.92038426e-17 1.00000000e+00 1.00000000e+00])
        [(0, 1), (477, 478)]
        >>> _image_border_finding([640,480],[ 0.33444816 99.66555184])
        [(0, 100), (640, 313)]
        >>> _image_border_finding([640,480],[[ 1.00000000e+00 -1.38076004e-14]])
        [(0, 0), (0, 0), (479, 479)]
        Author: Adnan Hafeez
        """
        #image_size[0] = image height
        #image_size[1] = image width
        intersections = []
        #check to see if crossing vertical border
        vert_left = round(np.polyval(polycoeff, 0)) #this is y value at x = 0
        vert_right = round(np.polyval(polycoeff,image_size[1]-1))  #this is y value at x = max

        horz_top = _exhaustive_search(image_size[1],polycoeff,0) #to find x we need to interpolate
        horz_bottom = _exhaustive_search(image_size[1],polycoeff,image_size[0]-1) #to find x we need to interpolate

        #these if statements are testing for the vertical bounds
        if vert_left < image_size[0] and vert_left >= 0:
            intersections += [(0,vert_left)]
        if vert_right < image_size[0] and vert_right >= 0:
            intersections += [(image_size[1],vert_right)]
        if horz_top !=None:
            intersections += [(horz_top,0)]
        if horz_bottom !=None:
            intersections += [(horz_bottom,round(np.polyval(polycoeff,horz_bottom)))]
        return sort_points(intersections)


    img_copy = copy(image)
    print("Image size (height, width)",(get_height(img_copy), get_width(img_copy)))
    if pointList == None:
        numPoints = int(input("How many numbers? (Must be greater than or equal to 2): "))
        point_list = _request_points(numPoints)
        func_coeff = _interpolation(point_list)
        point_list_border = (_image_border_finding([img_height,img_width],func_coeff))
    else:
        point_list = sort_points(pointList)
        func_coeff = _interpolation(point_list)
        point_list_border = (_image_border_finding([img_height,img_width],func_coeff))


    #draw line
    for x in range(img_width-1):
        if np.polyval(func_coeff,x) < img_height:
            y_line = floor(np.polyval(func_coeff,x))
            for y in range(y_line-4, y_line+4):
                if y>=0 and y<img_height:
                    set_color(img_copy, x,y, create_color(_pick_color(color)[0],_pick_color(color)[1],_pick_color(color)[2]))

    return (img_copy, point_list_border)


if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = extreme_contrast(image)
    show(new_image)
    
    posterized_image = posterize(image)
    show(posterized_image)    

    show(sepia_filter(image))

    three_tone_image = three_tone(image,"lemon","blood","black")
    show(three_tone_image)
    
    h_flipped_image = flip_horizontal(image)
    show(h_flipped_image)    

    #file = load_image(choose_file())
    show(flip_vertical(image))
    
    new_image = detect_edges(image,8)
    show(new_image)       
    
    output = draw_curve(image, "lemon", pointList=None)
    print(output[1])
    show(output[0])    
