import os
import sys
import threading
sys.path.insert(0, os.getcwd())
from start_camera import start_camera

def start_camera_thread():
  camera_thread = threading.Thread(target=start_camera)
  threads.append(camera_thread)
  camera_thread.start()
