from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, get_color


def green_channel(image: Image) -> Image:
    """Return a green filtered copy of image; that is, an image that is showing only the green color of the original image.

    >>> image = load_image(choose_file())
    >>> inverted = invert(image)
    >>> show(inverted)
    """
    new_image = copy(image)
    # filter the intensities of every component in every pixel.
    for x, y, (r, g, b) in image:
        green = create_color(0,g,0)
        set_color(new_image, x, y, green)
    return new_image


if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = green_channel(image)
    show(new_image)