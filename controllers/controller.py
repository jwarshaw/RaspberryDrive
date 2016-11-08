import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
# import models.analyze
from models.analyze import check_blob_in_direct_path
from get_images_from_pi import get_image, valid_image
from connect import new_connection, send_command, receive_confirmation
from start_camera import start_camera
from start_server import start_server
import threading


#Start-all
  #start the camera taking pictures on camera pi
  #start the server listening on contr pi
  #start the server connection on this current server
# threads = []
# camera_thread = threading.Thread(target=start_camera)
# threads.append(camera_thread)
# camera_thread.start()
server_thread = threading.Thread(target=start_server)
server_thread.start()
print "new connection?"
# start_server()
s = new_connection()
print "connected??"
# server_thread.exit()
#Run-All.  X times do
    #retrieve image.  mage, check if its in path.
    #send instruction over server
count = 0
while (count < 100):
  get_image()
  if valid_image(os.getcwd() + "/images/gregTest.jpg"):
    instruction = check_blob_in_direct_path(os.getcwd() + "/images/gregTest.jpg")
    send_command(s, instruction, "0.5")
    receive_confirmation(s)
    count += 1

#End-all
  #Stop the camera taking pictures on the camera pi
  #close the server connection
  #Kill the server listening process

s.close()
