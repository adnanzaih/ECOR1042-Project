from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image

def extreme_contrast(image: Image) -> Image:
    """
    Author: Adnan Hafeez

    >>> image = load_image(choose_file())
    >>> three_tone_filter = extreme_contrast(image)
    >>> show(three_tone_filter)
    """
    new_image = copy(image)
    # filter the intensities of every component in every pixel and calculate the brightness.
    for x, y, (r, g, b) in image:
        if r >= 0 and r <= 127:
            new_red = 0
        elif r >= 128 and r <= 255:
            new_red = 255
        if g >= 0 and g <= 127:
            new_green = 0
        elif g >= 128 and g <= 255:
            new_green = 255
        if b >= 0 and b <= 127:
            new_blue = 0
        elif b >= 128 and b <= 255:
            new_blue = 255
        set_color(new_image, x, y, create_color(new_red,new_green,new_blue))
    return new_image

if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = extreme_contrast(image)
    show(new_image)
