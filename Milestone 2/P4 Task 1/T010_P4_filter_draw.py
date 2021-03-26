#Adnan Hafeez 101210710

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image,\
    get_width,get_height
from point_manipulation import sort_points,  get_x_y_lists
from math import floor
import numpy as np


def draw_curve(image: Image, color:str, pointList: list) -> (Image, list):
    """

    Author: Adnan Hafeez
    :param image:
    :return:
    """
    img_height = get_height(image)
    img_width = get_width(image)

    def _pick_color(colour:str) -> tuple:
        color_lst = [("black",0,0,0),("white", 255,255,255),
                     ("blood",255,0,0), ("green",0,255,0),
                     ("blue",0,0,255), ("lemon",255, 255,0),
                     ("aqua",0,255,255),("pink",255,0,255),
                     ("gray",128,128,128)]
        for i in color_lst:
            if i[0] == colour:
                return (i[1],i[2],i[3])

    def _request_points(numPoints) -> list:
        point_list = []
        for i in range(numPoints):
            user_x_input = input("Please enter the x-coordinates of your point #({0}): ".format(i+1))
            user_y_input = input("Please enter the y-coordinates of your point #({0}): ".format(i+1))
            point_list.append((int(user_x_input),int(user_y_input)))
        return sort_points(point_list) #return point listed sorted in ascending order

    def _interpolation(points: list) -> list:
        if len(points) <=2:
            _deg = 1
        else:
            _deg = 2
        get_x, get_y = get_x_y_lists(points)
        return np.polyfit(get_x,get_y,_deg)

    def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
        """Solves f(x)-val = 0 for x between 0 and max_x where polycoeff contains the coefficients of f,
        using EPSILON = 1. Returns None if there is no solution between the bounds
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

        :param image_size: [img_height, img_width]
        :param polycoeff:
        :return:
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
    point_list = (_image_border_finding([img_height,img_width],func_coeff))

    #draw line
    for x in range(img_width-1):
        if np.polyval(func_coeff,x) < img_height:
            y_line = floor(np.polyval(func_coeff,x))
            for y in range(y_line-2, y_line+3):
                if y>=0 and y<img_height:
                    set_color(img_copy, x,y, create_color(_pick_color(color)[0],_pick_color(color)[1],_pick_color(color)[2]))

    return (img_copy, point_list)

if __name__ == "__main__":
    image = load_image(choose_file())
    output = draw_curve(image,"blood", pointList=None)
    print(output[1])
    show(output[0])



