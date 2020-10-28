import skimage
from skimage import io
from skimage.viewer import ImageViewer
import os
import numpy
import copy


monkeyPath = os.path.join(os.getcwd(), "./img/monkey.jpg")
monkeyImage = io.imread(monkeyPath)

viewer = ImageViewer(monkeyImage)
viewer.show()


print(type(monkeyImage))
print(monkeyImage.shape)
print(type(monkeyImage[0,0,0]))

monkeyImageRED = copy.deepcopy(monkeyImage)
monkeyImageBLUE = copy.deepcopy(monkeyImage)
monkeyImageGREEN = copy.deepcopy(monkeyImage)

for x in range(monkeyImage.shape[0]):
	for y in range(monkeyImage.shape[1]):
		monkeyImageRED[x,y,1] = 0
		monkeyImageRED[x,y,2] = 0

for x in range(monkeyImage.shape[0]):
	for y in range(monkeyImage.shape[1]):
		monkeyImageBLUE[x,y,0] = 0
		monkeyImageBLUE[x,y,1] = 0

for x in range(monkeyImage.shape[0]):
	for y in range(monkeyImage.shape[1]):
		monkeyImageGREEN[x,y,0] = 0
		monkeyImageGREEN[x,y,2] = 0



viewer = ImageViewer(monkeyImageRED)
viewer.show()
viewer = ImageViewer(monkeyImageBLUE)
viewer.show()
viewer = ImageViewer(monkeyImageGREEN)
viewer.show()


def reflect(sel):
	if sel==0:
		newMonkeyImage = monkeyImage[::-1,:,:]
		viewer = ImageViewer(newMonkeyImage)
		viewer.show()
	if sel==1:
		newMonkeyImage = monkeyImage[:,::-1,:]
		viewer = ImageViewer(newMonkeyImage)
		viewer.show()


reflect(0)
reflect(1)
