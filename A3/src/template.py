from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms


def compute_cumHisto(img, binSize=1):
    histo = np.histogram(img,list(range(binSize)))
    histo = np.add.accumulate(histo[0])
    return histo


def match_Histo(img_histo, ref_histo):
    pass
    return

def calculate_lookup(histo_ref, histo_im):
    LUT = np.zeros(256)
    lookup_val = 0
    for src_pixel_val in range(len(histo_ref)):
        for ref_pixel_val in range(len(histo_im)):
            if histo_im[ref_pixel_val] >= histo_ref[src_pixel_val]:
                lookup_val = ref_pixel_val
                break
        LUT[src_pixel_val] = lookup_val
    return LUT


def apply_LUT(img, lut):
    for x_pixel in range(img.shape[0]):
        for y_pixel in range(img.shape[1]):
            img[x_pixel,y_pixel] += lut[img[x_pixel,y_pixel]]
    return img



def rgb2gray(img):
    gray = copy.deepcopy(img[:,:,0])
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            gray[x,y] = img[x,y,0] * 0.299
            gray[x,y] += img[x,y,1] * 0.587
            gray[x,y] += img[x,y,2] * 0.114
    return gray


if __name__ == "__main__":

    # read img
    im = Image.open("bild01.jpg")
    ref = Image.open("bild02.jpg")

    # convert to numpy array
    im = np.array(im)
    ref = np.array(ref)

    # convert to grayscale
    im = rgb2gray(im)
    ref = rgb2gray(ref)

    # compute histograms
    histo_im = compute_cumHisto(im,256)
    histo_ref = compute_cumHisto(ref,256)

    # compute mapping function (LUT) for matching histograms
    LUT = calculate_lookup(histo_ref,histo_im)

    # compute new image with lut
    #im_new = match_histograms(im, ref)
    im_new = apply_LUT(im, LUT)


    # compute new histogram of new image
    histo_new = compute_cumHisto(im_new,256)

    # plot information
    N = histo_new.size
    x = range(N)
    width = 1

    # plot histogram of new image
    plt.figure(1)
    plt.subplot(211)
    plt.bar(x, histo_ref, width, color="blue")
    plt.xlim([0,N-1])
    # plot new img
    plt.figure(1)
    plt.subplot(212)
    plt.imshow(im_new, cmap = cm.Greys_r)

    # plot reference histogram
    plt.figure(2)
    plt.subplot(211)
    plt.bar(x, histo_ref, width, color="blue")
    plt.xlim([0,N-1])
    # plot reference image
    plt.figure(2)
    plt.subplot(212)
    plt.imshow(ref, cmap = cm.Greys_r)

    plt.show()


