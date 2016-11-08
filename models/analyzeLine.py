import SimpleCV
import cv2
import time


def findBlockingBlobs(img,blobs):
		for blob in blobs:
				print blob
				print img.size()
				if blockingBlob(img,blob):
					return True
		return False
				
def blockingBlob(img,blob):
	if heightBelowThreshold(img,blob):
			if lengthSufficientToBlock(img,blob):
				return True
		

def heightBelowThreshold(img,blob):
		print blob.maxY()
		if (blob.maxY() > img.size()[1] * 0.4):
						return True

def lengthSufficientToBlock(img,blob):
		if (blob.width() > img.size()[0] * 0.55):
						return True


images = [SimpleCV.Image('test1.jpg'), SimpleCV.Image('test2.jpg'), SimpleCV.Image('test3.jpg'), SimpleCV.Image('test4.jpg'),SimpleCV.Image('test5.jpg'), SimpleCV.Image('test6.jpg')]
blobs = []

for image in images:
	segmented = image.stretch(160,161)
	blob = segmented.findBlobs(minsize=100)
	blobs.append(blob)

for x in range(len(blobs)):
	images[x].show()
	time.sleep(5)
	print x
	print blobs[x]
	print findBlockingBlobs(images[x],blobs[x])