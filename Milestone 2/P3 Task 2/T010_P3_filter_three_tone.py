from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, get_color

def three_tone(image: Image, first_tone: str, second_tone: str, third_tone: str) -> Image:
    """
    Author: Adnan Hafeez

    >>> image = load_image(choose_file())
    >>> three_tone_filter = three_tone(image,"aqua","lemon","pink")
    >>> show(three_tone_filter)
    """
    color_lst = [("black",0,0,0),("white", 255,255,255),
                 ("blood",255,0,0), ("green",0,255,0),
                 ("blue",0,0,255), ("lemon",255, 255,0),
                 ("aqua",0,255,255),("pink",255,0,255),
                 ("gray",128,128,128)]
    new_image = copy(image)
    for color in color_lst:
        if color[0] == first_tone:
            #print("the first color is: ",color[1],color[2],color[3])
            first_tone_colors = create_color(color[1],color[2],color[3])
        if color[0] == second_tone:
            #print("the second color is: ",color[1],color[2],color[3])
            second_tone_colors = create_color(color[1],color[2],color[3])
        if color[0] == third_tone:
            #print("the third color is: ",color[1],color[2],color[3])
            third_tone_colors = create_color(color[1],color[2],color[3])

    # filter the intensities of every component in every pixel and calculate the brightness.
    for x, y, (r, g, b) in image:
        pixel_brightness = (r+b+g)/3
        if pixel_brightness >= 0 and pixel_brightness <= 84:
            set_color(new_image, x, y, first_tone_colors)
        elif pixel_brightness >= 85 and pixel_brightness <= 170:
            set_color(new_image, x, y, second_tone_colors)
        elif pixel_brightness >= 171 and pixel_brightness <= 255:
            set_color(new_image, x, y, third_tone_colors)
    return new_image

if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = three_tone(image,"aqua","lemon","blood")
    show(new_image)
