from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy

def compute_cumHisto(img, binSize=1):

    histo = np.histogram(img, binSize)
    histo = np.add.accumulate(histo[0])

    return histo


def Cdf(histo):
    K = histo.size
    n = 0
    for i in range(K):
        n += histo[i]

    P = np.zeros(K)
    c = histo[0]
    P[0] = c / n
    for i in range(K):
        c += histo[i]
        P[i] = c / n

    return P

"""
def calculate_lookup(src_cdf, ref_cdf):
    LUT = np.zeros(256)
    lookup_val = 0
    for src_pixel_val in range(len(src_cdf)):
        for ref_pixel_val in range(len(ref_cdf)):
            if ref_cdf[ref_pixel_val] >= src_cdf[src_pixel_val]:
                lookup_val = ref_pixel_val
                break
        LUT[src_pixel_val] = lookup_val
    return LUT
"""


def match_Histo(img_histo, ref_histo):

    K = img_histo.size
    PA = Cdf(img_histo)
    PR = Cdf(ref_histo)
    LUT = np.zeros(K)

    for a in range(K):
        j = K-1
        while True:
            LUT[a] = j
            j -= 1
            if j >= 0 and PA[a] <= PR[j]:
                break

    return LUT


    #img_histo . . . original histogram
    #ref_histo . . . reference histogram
    #returns the mapping function LUT to be applied to the image



def apply_LUT(img, lut):
    pass

    x, y = img.shape
    for i in range(0, x):
        for j in range(0, y):
            if img[i][j] + LUT[img[i][j]] < 255:
                img[i][j] = img[i][j] + LUT[img[i][j]]
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

    # read img
    im = Image.open("./img/bild01.jpg")
    ref = Image.open("./img/bild02.jpg")

    im =  np.array(im)
    ref =  np.array(ref)

    im = rgb2gray(im)
    ref = rgb2gray(ref)

    # compute histograms
    histo_im = compute_cumHisto(im, 64)
    histo_ref = compute_cumHisto(ref, 64)

    # compute mapping function (LUT) for matching histograms
    LUT = match_Histo(np.histogram(im, 32)[0], np.histogram(ref, 32)[0])

    print(LUT)

    # compute new image with lut
    im_new = apply_LUT(im, LUT)

    # compute new histogram of new image
    histo_new = compute_cumHisto(im_new, 64)


    # plot information
    N = histo_new.size
    x = range(N)
    width = 1

    # plot histogram of new image
    plt.figure(1)
    plt.subplot(211)
    plt.bar(x, histo_new, width, color="blue")
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

