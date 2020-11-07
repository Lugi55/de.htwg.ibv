#!/usr/bin/env python

import glob
from skimage import io
from skimage.color import rgb2gray
from skimage.viewer import ImageViewer
import numpy as np
import matplotlib.pyplot as plt


def image_import(image_paths):
    images = []
    for path in image_paths:
        images.append(io.imread(path))
    return images

def grayscale_conversion(images):
    grayscale_images = []
    for image in images:
        grayscale_images.append(rgb2gray(image))
    return grayscale_images

def image_viewer(images, n=None):
    if n == None:
        for image in images:
            viewer = ImageViewer(image)
            viewer.show()
    else:
        viewer = ImageViewer(images[n])
        viewer.show()

def compute_histograms(images):
    histograms = []
    for image in images:
        histograms.append(np.histogram(image, bins=np.arange(256), density=True))
    return histograms


def main():
    images = image_import(glob.glob("./img/*.jpg"))
    # print(images)
    grayscale_images = grayscale_conversion(images)
    #print(grayscale_images[1])
    histograms = compute_histograms(grayscale_images)
    print(histograms)
    image_viewer(images, 3)
    image_viewer(grayscale_images, 3)

    _ = plt.hist(histograms[3], bins='auto')  # arguments are passed to np.histogram

    plt.title("Histogram with 'auto' bins")

    plt.show()
    pass

if __name__ == "__main__":
    main()
