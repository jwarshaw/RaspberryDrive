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
  stretch = reds.stretch(20,21)
  invert = stretch.invert()
  blobs = invert.findBlobs(minsize=2000)
  if blobs:
    for blob in blobs:
      print blob.area()
      blob.draw(color=(0, 128, 0))
  invert.show()
  invert.show()
  time.sleep(3)

image = Image('images/0.jpg')
x = 0
while (x < 40):
  image = Image('images/'+ str(x) + '.jpg')
  detect_stop_sign(image)
  print x
  x +=1

exit()





