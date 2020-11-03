from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def compute_Histo(img):

    pass

    return histo


def bin_Histo(img, bin=1):

    pass

    return histo


def brighten(img, offset):

    # add offset to img

    # check clamping
    pass

    return img


def get_lut(k=256):

    # create lut-table
    # which only brightens the darker pixel values (e.g. < 200)
    # bright pixel values should not change that much

    # check clamping
    pass

    return lut


def brighten_with_lut(img, lut):

    # brighten image using the lookup-table

    # check clamping
    pass

    return img


def rgb2gray(img):

    # convert to grayscale image (only one channel)
    pass

    return gray


if __name__ == "__main__":

    # read img
    im = Image.open("bild01.jpg")

    # convert to numpy array

    # convert to grayscale
    im = rgb2gray(im)

    # brighten image

    # brighten image with lut-table

    # compute histogram (with bin-size)
    histo = bin_Histo(im, 5)

    # plot histogram
    N = histo.size
    x = range(N)
    width = 1

    plt.figure(1)
    plt.subplot(211)
    plt.bar(x, histo, width, color="blue")
    plt.xlim([0,N-1])

    # plot processed img
    plt.subplot(212)
    plt.imshow(im, cmap = cm.Greys_r)

    plt.show()

