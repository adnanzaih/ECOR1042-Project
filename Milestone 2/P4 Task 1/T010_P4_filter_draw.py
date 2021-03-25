#Adnan Hafeez 101210710

from Cimpl import choose_file, load_image, show, Image, copy, create_color, set_color, get_color, create_image,\
    get_width,get_height
from point_manipulation import sort_points,  get_x_y_lists
import numpy as np


def draw_curve(image: Image, color:str, pointList: list) -> (Image, list):
    """

    Author: Adnan Hafeez
    :param image:
    :return:
    """

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
            user_x_input = input("Please enter the x-coordinates of your point #({0}) ".format(i+1))
            user_y_input = input("Please enter the y-coordinates of your point #({0}) ".format(i+1))
            point_list.append((int(user_x_input),int(user_y_input)))
        return sort_points(point_list) #return point listed sorted in ascending order

    def _interpolation(points: list, deg: int) -> list:
        if deg <=2:
            _deg = 1
        elif deg > 2:
            _deg = 2
        get_x, get_y = get_x_y_lists(points)
        return np.polyfit(get_x,get_y,_deg)



    img_copy = copy(image)
    print("Image size (height, width)",(get_height(img_copy), get_width(img_copy)))
    numPoints = int(input("How many numbers? (Must be greater than or equal to 2)"))
    point_list = _request_points(numPoints)
    print(_interpolation(point_list, numPoints))

    return (img_copy, point_list)

if __name__ == "__main__":
    image = load_image(choose_file())
    output = draw_curve(image,"aqua", pointList=None)
    print(output[1])
    show(output[0])



