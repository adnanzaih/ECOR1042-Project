#ECOR 1042 P3 Task 2, Individual Filter

# 10: three-tone image filter
#Vincent Chen 101196001
#Import all functions from Cimpl module

from Cimpl import *

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
        if colour2 ==i[0]:
            #print( i[1], i[2] , i[3])
            new_colour.append((i[1],i[2],i[3]))
        if colour3 == i[0]:
            #print( i[1], i[2] , i[3])
            new_colour.append((i[1],i[2],i[3]))
            #print (new_colour)
    three_tone_image = copy(original_image)
    for pixel in three_tone_image: #iterates over every pixel in the image and take only the green component of each pixel
        x, y, (r, g, b) = pixel
        brightness = (r + g + b) / 3 #calculates brightness
        if brightness < 85:
            c1,c2,c3 = new_colour[0]
            new_color = create_color(c1,c2,c3)
        elif brightness < 171:
            c1,c2,c3 = new_colour[1]
            new_color = create_color(c1,c2,c3)
        elif brightness < 256:
            c1,c2,c3 = new_colour[2]
            new_color = create_color(c1,c2,c3)
        set_color(three_tone_image,x,y,new_color)

    return three_tone_image

if __name__ == "__main__":
    original_image = load_image(choose_file())
    three_tone_image = three_tone(original_image,"blood","green","blue")
    show(three_tone_image)