#ECOR 1042 P3 Task 2, Individual Filter

#10: posterize image filter
#Adnan Hafeez 101210710

from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image

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

if __name__ == "__main__":
    image = load_image(choose_file())
    posterized_image = posterize(image)
    show(posterized_image)
