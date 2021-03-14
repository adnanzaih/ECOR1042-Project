from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image

from simple_Cimpl_filters import grayscale

def sepia_filter(image: Image) -> Image:
    """
    Author: Adnan Hafeez

    Sepia Tinting

    >>> image = load_image(choose_file())
    >>> three_tone_filter = sepia_filter(image)
    >>> show(three_tone_filter)
    """
    new_image = copy(image)
    grayscaled_img = grayscale(new_image)
    # filter the intensities of every component in every pixel and calculate the brightness.
    for x, y, (r, g, b) in grayscaled_img:
        if g < 63:
            b = b*0.9
            r = 1.1*r
        elif g >= 63 and g <= 191:
            b = b*0.85
            r = 1.15*r
        elif g > 191:
            b = b*0.93
            r = 1.08*r
        set_color(grayscaled_img, x, y, create_color(r,g,b))
    return grayscaled_img

if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = sepia_filter(image)
    show(new_image)
