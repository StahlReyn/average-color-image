import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_average_color(filename, show = False):
    img = cv2.imread(filename)
    dst = filter_noise_1(img)
    print(img)

    if (show): 
        display_image(img, dst)

    value = np.mean(dst, axis=(0,1))
    return value

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

def main():
    print(get_average_color('test1.jpg'))
    print(get_average_color('test2.png'))

main()