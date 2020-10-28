import skimage as sk
import skimage.io
import skimage.viewer
import numpy as np
import copy

path_to_img: str = "monkey.jpg"

class img:
	def __init__(self, path: str):
		self.__buffer: np.ndarray = sk.io.imread(path)

	def __str__(self) -> str:
		return str(type(self.__buffer)) + ", " + str(type(self.__buffer[0, 0, 0])) + ", " + str(self.__buffer.shape)

	def _get_buffer(self) -> np.ndarray:
		return self.__buffer
	
	def _set_buffer(self, buf: np.ndarray) -> None:
		self.__buffer = buf
	
	def display(self) -> None:
		sk.viewer.ImageViewer(self.__buffer).show()
	
	def width(self) -> int:
		return self.__buffer.shape[0]

	def height(self) -> int:
		return self.__buffer.shape[1]

def flip(im: img, horizontal = False) -> img:
	ret: img = copy.deepcopy(im)
	if horizontal is False:
		ret._set_buffer(ret._get_buffer()[::-1,:,:])
	else:
		ret._set_buffer(ret._get_buffer()[:,::-1,:])
	return ret

def extract_channel(im: img, ch_name: str) -> img:
	ret: img = copy.deepcopy(im)
	tmp: np.ndarray = ret._get_buffer()

	for x in range(0, ret.width()):
		for y in range(0, ret.height()):
			color: np.ndarray = tmp[x,y]
			if ch_name == "red":
				color[1] = 0
				color[2] = 0
			if ch_name == "green":
				color[0] = 0
				color[2] = 0
			if ch_name == "blue":
				color[0] = 0
				color[1] = 0
			tmp[x, y] = color
	ret._set_buffer(tmp)
	return ret

def main() -> None:
	test_image: img = img(path_to_img)
	test_image.display()
	flip(test_image).display()
	flip(test_image, True).display()
	extract_channel(test_image, "red").display()
	extract_channel(test_image, "green").display()
	extract_channel(test_image, "blue").display()
	print(str(test_image))

if __name__ == "__main__":
	main()