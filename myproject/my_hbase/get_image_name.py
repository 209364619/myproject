import os
import random

image_name_list = os.listdir("I:\\hph\\all_images")
counts = len(image_name_list) - 2


def get_random_image():
    info = {}
    index = random.randint(0, counts)
    path = "I:\\hph\\all_images\\" + image_name_list[index]
    return path
