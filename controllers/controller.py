import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
import analyzeLine
import runAnalyzeLine
from runAnalyzeLine import runAnalyzeLines
from analyzeLine import findBlockingBlobs
from get_images_from_pi import get_image, valid_image
from connect import new_connection, send_command, receive_confirmation,send_end_connection
from start_camera import start_camera
from start_server import start_server
import threading

def start_server_thread():
	server_thread = threading.Thread(target=start_server)
	server_thread.start()
	return;

def start_camera_thread():
	camera_thread = threading.Thread(target=start_camera)
	camera_thread.start()
	return;

#Start-all
#start the server listening on contr pi
start_server_thread()
#start the camera taking pictures on camera pi
start_camera_thread()
# Sleep to make sure server connects
sleep(7)
#start the server connection on this current server
s = new_connection()

#Run-All.
count = 0
while (count < 20):
  instruction = "forward"
  #retrieve image.
  get_image()
  if valid_image(os.getcwd() + "/gregTest.jpg"):
  	#Blog Detection
    in_way = runAnalyzeLines(os.getcwd() + "/gregTest.jpg")
    if (in_way == True):
      instruction = "stop"
  	#send instruction over server
    send_command(s, instruction, "0.5")
    #confirmation that instruction was received
    receive_confirmation(s)
    print instruction
  count += 1

#End-all
#Camera exits automatically automatically
#Close the Server Connection on the Pi-Controller End
send_end_connection(s)
#Kill the server listening process
s.close()
#exit out of controller
exit()
