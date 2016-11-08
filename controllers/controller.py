import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
from models import analyzeLine
# from models.analyze import findBlockingBlobs
from models.analyzeLine import findBlockingBlobs
from get_images_from_pi import get_image, valid_image
from connect import new_connection, send_command, receive_confirmation,send_end_connection
from start_camera import start_camera
from start_server import start_server
import threading



#Start-all
threads = []
#start the server listening on contr pi
server_thread = threading.Thread(target=start_server)
threads.append(server_thread)
server_thread.start()
#Sleep for testing
sleep(2)
#start the camera taking pictures on camera pi
camera_thread = threading.Thread(target=start_camera)
threads.append(camera_thread)
camera_thread.start()
# Sleep to make sure server connects
sleep(5)
#start the server connection on this current server
s = new_connection()

#Run-All.  X times do
    #retrieve image.  #Blog Detection
    #send instruction over server
count = 0
while (count < 20):
  instruction = "forward"
  get_image()
  if valid_image(os.getcwd() + "/images/gregTest.jpg"):
    in_way = check_blob_in_direct_path(os.getcwd() + "/images/gregTest.jpg")
    if (in_way == True):
      instruction = "stop"
    send_command(s, instruction, "0.5")
    receive_confirmation(s)
    count += 1
    sleep(0.5)

# #End-all
#   #Stop the camera taking pictures on the camera pi -- still needs to be implemented
#   #close the server connection
send_end_connection(s)
#   #Kill the server listening process
s.close()
exit()
