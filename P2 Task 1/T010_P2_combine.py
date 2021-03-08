from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, get_color


def combine(red: Image, green: Image, blue:Image) -> Image:
    """Return an image that is a combination of the red, blue and green channels.
    """
    new_image = copy(red)
    for x, y, _ in red:
        red_pixel = get_color(red,x,y)
        green_pixel = get_color(green,x,y)
        blue_pixel = get_color(blue,x,y)
        combined_colors = create_color(red_pixel[0], green_pixel[1], blue_pixel[2])
        set_color(new_image, x,y, combined_colors)
    return new_image


if __name__ == "__main__":
    image = load_image(choose_file())

    blue_filter = blue_channel(image)
    red_filter = red_channel(image)
    green_filter = green_channel(image)

    # combine images
    combined = combine(red_filter, green_filter, blue_filter)
    show(combined)