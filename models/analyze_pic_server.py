import analyze
from analyze import check_blob_in_direct_path
import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
from get_images_from_pi import get_image, get_image_x_times
from connect import new_connection, send_command

#controller action
#start a server
#10 times do:
  #get image, check if its in path.
  #send instruction over server
  #sleep, do it again

count = 0
s = new_connection()
while (count < 10):
  get_image()
  instruction = check_blob_in_direct_path(os.getcwd() + "/images/greg.jpg")
  send_command(s, instruction, "1")
  count += 1
  sleep(1)

s.close()
