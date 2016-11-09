import os
import sys
import threading
sys.path.insert(0, os.getcwd())
from start_server import start_server

def start_server_thread():
  server_thread = threading.Thread(target=start_server)
  threads.append(server_thread)
  server_thread.start()
