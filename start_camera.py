import os

def start_camera():
  os.system('"%s:%s" "%s" "%s"' % ('pi@19 2.168.2.5', 'Desktop/gregTest.jpg', 'gregTest.jpg', os.getcwd() + '/images') )

