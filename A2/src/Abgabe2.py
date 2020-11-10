from PIL import Image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
import glob


def compute_Histo(img):
    histo = np.zeros(256)
    for val in img:
        histo[val] += 1
    return histo


def bin_Histo(img, bin=1):
    histo = np.zeros(256)
    for val in img:
        histo[val] += 1
    bin_histo = np.zeros(bin)
    histo = np.array_split(histo, bin)
    for i in range(0, bin):
        bin_histo[i] = histo[i].mean()
    # for i in range(0, bin):
        # for val in histo[i]:
            # bin_histo[i] += val
        # bin_histo[i] = int(bin_histo[i] / histo[i].size)
    return bin_histo


def brighten_with_lut(img, lut):
    print(img.shape)
    x, y = img.shape
    for i in range(0, x):
        for j in range(0, y):
            if img[i][j] + lut[img[i][j]] < 255:
                img[i][j] = img[i][j] + lut[img[i][j]]
            else:
                img[i][j] = 255
    return img


def rgb2gray(img):
    # convert to grayscale image (only one channel)
    gray = copy.deepcopy(img[:,:,0])
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            gray[x,y] = img[x,y,0] * 0.299
            gray[x,y] += img[x,y,1] * 0.587
            gray[x,y] += img[x,y,2] * 0.114
    return gray


if __name__ == "__main__":

    images = glob.glob("./img/*.jpg")

    for image in images:
        # read img
        im = io.imread(image)
        print('==== Pillow Image ====')

        # convert to numpy array
        im = np.array(im)
        print('==== Numpy Image ====')

        # convert to grayscale
        im = rgb2gray(im)
        print('==== Grayscale Image ====')

        # brighten image

        print('==== Histogram ====')
        histo = compute_Histo(im)

        lut = np.full(256, 0)
        for i in range(0, lut.size):
            lut[i] = int(1/2000*(i-255)**2)
        print(lut)

        # brighten image with lut-table
        im = brighten_with_lut(im, lut)

        # compute histrogram (without bin-size)
        histo_lut = compute_Histo(im)
        print('==== Histogram ====')

        # compute histogram (with bin-size)
        bin_histo = bin_Histo(im, 4)
        print('==== Bin Histogram ====')

        # plot histogram
        N = histo.size
        x = range(0,N)
        width = 1

        plt.figure(image)
        plt.subplot(411)
        plt.bar(x, histo, width=1, color="blue")
        plt.xlim([0,N-1])

        plt.subplot(412)
        plt.bar(x, histo_lut, width=1, color="green")

        N = bin_histo.size
        x = range(N)
        width = 1

        plt.subplot(413)
        plt.bar(x, bin_histo, width=1, color="red")

        # plot processed img
        plt.subplot(414)
        plt.imshow(im, cmap = cm.Greys_r)

        plt.show()

