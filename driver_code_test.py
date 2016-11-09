import SimpleCV as scv
from SimpleCV import Image
import cv2
import time
from start_camera import start_camera
import threading

# camera_thread = threading.Thread(target=start_camera)
# camera_thread.start()
# from get_images_from_pi import get_image, valid_image
# time.sleep(2)
# count = 0
# while (count < 50):
#   get_image(count)
#   count += 1

# exit()

image = Image('images/stop')

image.show()
image.show()
time.sleep(2)

reds = image.hueDistance(color=scv.Color.RED)
reds.show()
reds.show()
time.sleep(2)

stretch = reds.stretch(20,21)
stretch.show()
stretch.show()
time.sleep(3)


# blobs = image.findBlobs()
# if blobs:
#   for blob in blobs:
#     print "got a blob"
#     blob.draw(color=(0, 128, 0))
# image.show()
# image.show()
# time.sleep(4)






