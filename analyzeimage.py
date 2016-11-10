import SimpleCV
import cv2
import time
from analyzeblob import *
from car_maneuvers import *
from PIL import Image

class AnalyzeImage(object):

  def __init__(self, image_path,connection):
    self.default_command = "stop"
    self.scvImg = SimpleCV.Image(image_path)
    #adding in stop sign logic to check if speed slows down.
    #reds = self.scImg.hueDistance(color=scv.Color.RED)
    #red_stretched_image = reds.stretch(20,21)
    #red_inverted_image = red_stretched_image.invert()
    # self.red_blobs = red_inverted_image.findBlobs(minsize=3500)
    self.segmented_black_white = self.scvImg.stretch(180,181)
    self.black_white_blobs = self.segmented_black_white.findBlobs(minsize=100)
    self.car = CarManeuvers(connection)


  def runBlobFinder(self):
    if (self.black_white_blobs and (len(self.black_white_blobs) > 0)):
      self.analyzeBlobs()
    else:
      self.car.forward()
  # print x
	# print blob

  def analyzeBlobs(self):
    blobs = self.scvImg.findBlobs(minsize = 100)
    # if blobs:
    #   for blob in blobs:
    #     if blob.area() > 100:
    #       blob.draw(color=(128,0,0))
    #   self.scvImg.show()
    #   self.scvImg.show()
    #   time.sleep(2)
    #check if blocked
    for blob in self.black_white_blobs:
      print blob
      analyzed_blob = AnalyzeBlob(self.scvImg,blob)

      if analyzed_blob.isBlobBlocking():
        print "true"
        if analyzed_blob.isBlobBlockingMoreRight():
          self.car.wheels_right_back_up()
        else:
          self.car.wheels_left_back_up()
        return

      elif analyzed_blob.isBlobDetectedOnRight():
        # if analyzed_blob.blockedOnRight():
        self.car.left()
        return
      elif analyzed_blob.isBlobDetectedOnLeft():
        self.car.right()
        return
    #otherwise go forward
    self.car.forward()

#  detect blobs
#  if blobs
#    check left and check rightt
#     is blocking?
#         back up
#       else
#         turn (in correct direction)
