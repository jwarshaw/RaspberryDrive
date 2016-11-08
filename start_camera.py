import os

def start_camera():
  os.system('ssh "%s" "%s" "%s"' % ('pi@192.168.2.5', 'python', 'RaspberryDrive/views/takePicture.py') )

start_camera()
