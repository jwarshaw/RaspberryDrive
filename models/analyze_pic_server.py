import analyze
from analyze import check_blob_in_direct_path
import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
from get_images_from_pi import get_image, get_image_x_times, valid_image
from connect import new_connection, send_command, receive_confirmation

#controller action
#start a server
#x times do:
  #get image, check if its in path.
  #send instruction over server
  #sleep, do it again

count = 0
s = new_connection()
while (count < 100):
  get_image()
  if valid_image(os.getcwd() + "/images/gregTest.jpg"):
    instruction = check_blob_in_direct_path(os.getcwd() + "/images/gregTest.jpg")
    send_command(s, instruction, "0.5")
    receive_confirmation(s)
    count += 1

s.close()
