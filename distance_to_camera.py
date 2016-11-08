# Import image library necessary for file
import SimpleCV
import sys
from SimpleCV import Image

def check_image(image_path):
	#Find file by path and import.  File currently resides in same directory.
	image = Image(image_path)
	# grey = image.grayscale()

	instruction = "go"
	array_bounds_possible_widths = [image.width / 4, image.width / 4 * 3]
	shapes_pic_attributes = image.size()

	shapes_pic_size = shapes_pic_attributes[0] * shapes_pic_attributes[1]
	# dist = img.colorDistance(SimpleCV.Color.Black).dilate(2)
	blobs = image.findBlobs()

	#check if the blob is in the middle 1/2 of screen and is too high
	for blob in blobs[:-1]:
		# print blob.contains()

		if (blob.coordinates()[0] > array_bounds_possible_widths[0] and blob.coordinates()[0] < array_bounds_possible_widths[1]) and (blob.height() > image.height / 5 and blob.coordinates()[1] > image.height / 5 * 2):
			# print grey.height
			print blob.coordinates()[1]
			print "Blob is in the way!!"
			blob.draw(color=(255,0,0))
			instruction = "stop"

	# Display the blob until you click on the left side of the picture.
	#display = SimpleCV.Display()
	#while display.isNotDone():
		#image.show()
		##\#if display.mouseLeft:
			#break

	return instruction
