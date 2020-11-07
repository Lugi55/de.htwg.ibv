from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
import glob


def compute_Histo(img):
    histo = np.histogram(img,bins= list(range(0,255)),normed=True)
    return histo[0]


def bin_Histo(img, bin=1):
    histo = np.histogram(img,bins= list(range(0,bin)),normed=True)
    return histo[0]


def brighten(img, offset):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y] > 255-offset:
                img[x,y] = 255
            else:
                img[x,y] += offset
    return img


def get_lut(k,p):
    if p<k:
        lut = 10
    else:
        lut = 0
    return lut


def brighten_with_lut(img,k):
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            lut = get_lut(k,img[x,y])
            if img[x,y] > 255-lut:
                img[x,y] = 255
            else:
                img[x,y] += lut
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
        im = Image.open(image)
        print('==== Pillow Image ====')
        print(im)

        # convert to numpy array
        im = np.array(im)
        print('==== Numpy Image ====')
        print(im)

        # convert to grayscale
        im = rgb2gray(im)
        print('==== Grayscale Image ====')
        print(im)

        # brighten image


        # brighten image with lut-table


        # compute histrogram (without bin-size)
        histo = compute_Histo(im)
        print('==== Histogram ====')
        print(histo)

        # compute histogram (with bin-size)
        bin_histo = bin_Histo(im, 5)
        print('==== Bin Histogram ====')
        print(bin_histo)

        # plot histogram
        N = histo.size
        x = range(N)
        width = 1

        plt.figure(image)
        plt.subplot(311)
        plt.bar(x, histo, width, color="blue")
        plt.xlim([0,N-1])

        N = bin_histo.size
        x = range(N)
        width = 1

        plt.subplot(312)
        plt.bar(x, bin_histo, width, color="red")

        # plot processed img
        plt.subplot(313)
        plt.imshow(im, cmap = cm.Greys_r)

        plt.show()

