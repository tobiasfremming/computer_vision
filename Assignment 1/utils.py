import numpy as np
import matplotlib.pyplot as plt
import os


def read_im(filepath):
    im = plt.imread(filepath)
    if im.dtype == np.uint8:
        im = im.astype(float) / 255
    return im

def normalize(im):
    return (im - im.min()) / (im.max() - im.min())

def save_im(filepath, im, cmap=None):
    if im.min() < 0 or im.max() > 1:
        print(
            "Warning: The dynamic range of the image is",
            f"[{im.min()}, {im.max()}]",
            "normalizing to [-1, 1]")
        im = normalize(im)
    
    # Create directory if it doesn't exist
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.imsave(filepath, im, cmap=cmap)
