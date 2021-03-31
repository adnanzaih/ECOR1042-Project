from T010_image_filters import *
from Cimpl import *
import string
from typing import List

def batch_analysis(filename: str) -> None:
    infile = open(filename, "r")
    word_list_new = []
    for line in infile:
        word_list = line.split()
        for word in word_list:
            if word != '':
                word_list_new += [word]
        print(line)
        load_img = load_image(word_list_new[0])
        for filter in range(len(line)-2):
            load_img = filter_array(load_img, line[filter+2])
        show(load_img)
        save_as(load_img, word_list_new[1])
        word_list_new = [] #reset the line to empty
    infile.close()
    # Now build the list of distinct words.
    word_list_new = list(word_list)
    return word_list_new


def filter_array(image: Image, filter_id: str) -> Image:
    if filter_id == "3":
        image = three_tone(image,"aqua","blood","lemon")
    if filter_id == "X":
        image = extreme_contrast(image)
    if filter_id == "T":
        image = sepia_filter(image, )
    if filter_id == "P":
        image = posterize(image)
    if filter_id == "E":
        image = detect_edges(image,15)
    if filter_id == "V":
        image = flip_vertical(image)
    if filter_id == "H":
        image = flip_horizontal(image)
    return image

command_sequence = batch_analysis('sample.txt')