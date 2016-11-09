import SimpleCV as scv
from SimpleCV import Image
import cv2
import time
from start_camera import start_camera
import threading

def take_50_pictures():
  camera_thread = threading.Thread(target=start_camera)
  camera_thread.start()
  from get_images_from_pi import get_image, valid_image
  time.sleep(2)
  count = 0
  while (count < 50):
    get_image(count)
    count += 1

def detect_stop_sign(image):
  reds = image.hueDistance(color=scv.Color.RED)
  stretched_image = reds.stretch(20,21)
  inverted_image = stretched_image.invert()
  blobs = inverted_image.findBlobs(minsize=3500)
  if blobs:
    return True #means there is an obstruction
  return False

image = Image('images/0.jpg')
x = 5
while (x < 7):
  print x
  image = Image('images/stop'+ str(x) + '.jpg')
  detect_stop_sign(image)
  x +=1

exit()





