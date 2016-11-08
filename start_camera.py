import os

def start_camera():
    os.system('ssh "%s" "%s" "%s" "%s" "%s"' % ('pi@192.168.2.5', 'nohup', 'python', 'RaspberryDrive/views/takePicture.py', '&'))
    return
# start_camera()

