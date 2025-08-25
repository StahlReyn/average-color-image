import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
import re

REGEX_TIME = r'.* (\d*)\..*' # something 1234.fileextension
DO_FILTER = False

def get_average_color_file(filename):
    img = cv2.imread(filename)
    return get_average_color(img)

def get_average_color_file_filtered(filename, show = False):
    img = cv2.imread(filename)
    dst = filter_noise_1(img)
    if (show): 
        display_image(img, dst)
    return get_average_color(dst)

def get_average_color(img):
    return np.mean(img, axis=(0,1))

def filter_noise_1(img):
    dst = cv2.medianBlur(img, 9)
    dst = filter_threshold(dst, 25)

    return dst

def filter_threshold(img, value):
    copy = np.copy(img)
    min = np.array([0,0,0])
    max = np.array([value,value,value])
    mask = cv2.inRange(copy, min, max)
    copy[mask>0] = (0,0,0) # change to black
    return copy

def display_image(img, dst):
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('New')
    plt.xticks([]), plt.yticks([])
    plt.show()

def get_images(path):
    imgs = glob.glob(path + "/*.png", recursive=False)

    return imgs

def get_time_from_path(path):
    match = re.search(REGEX_TIME, path)
    if match is None:
        return path
    return match.group(1)

def main():
    path = "images"
    imgs = get_images(path)

    print("time,r,g,b")
    for img in imgs:
        time = get_time_from_path(img)
        color = None
        if DO_FILTER:
            color = get_average_color_file_filtered(img)
        else:
            color = get_average_color_file(img)
        print(time + "," + str(color[0]) + "," + str(color[1]) + "," + str(color[2]))

main()