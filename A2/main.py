from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import copy


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
	gray = copy.deepcopy(img[:,:,0])
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			gray[x,y] = img[x,y,0] * 0.299
			gray[x,y] += img[x,y,1] * 0.587
			gray[x,y] += img[x,y,2] * 0.114
	return gray


if __name__ == "__main__":


	im = Image.open("bild05.jpg")
	im = np.array(im)
	im = rgb2gray(im)
	#im = brighten_with_lut(im, 100)
	#im = brighten(im,100)
	histo = compute_Histo(im)
	#histo = bin_Histo(im, 100)



	N = histo.size
	x = range(N)
	width = 1
	plt.figure(1)
	plt.subplot(211)
	plt.bar(x, histo, width, color="blue")
	plt.xlim([0,N-1])
	plt.subplot(212)
	plt.imshow(im, cmap = cm.Greys_r)
	plt.show()
