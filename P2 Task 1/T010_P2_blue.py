from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, get_color


def blue_channel(image: Image) -> Image:
    """Return a blue filtered copy of image; that is, an image that is showing only the blue color of the original image.

    >>> image = load_image(choose_file())
    >>> inverted = invert(image)
    >>> show(inverted)
    """
    new_image = copy(image)
    # filter the intensities of every component in every pixel.
    for x, y, (r, g, b) in image:
        blue = create_color(0,0,b)
        set_color(new_image, x, y, blue)
    return new_image

if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = blue_channel(image)
    show(new_image)