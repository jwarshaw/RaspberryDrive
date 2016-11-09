import SimpleCV
from SimpleCV import Image
import cv2
import time
from start_camera import start_camera
import threading

# camera_thread = threading.Thread(target=start_camera)
# camera_thread.start()
# from get_images_from_pi import get_image, valid_image

# count = 0
# while (count < 10):
#   get_image(count)
#   count += 1

# exit()

image = Image('images/1.jpg')
blobs = image.findBlobs()
for blob in blobs:
  blob.draw(color=(0, 128, 0))
image.show()
image.show()
time.sleep(4)






