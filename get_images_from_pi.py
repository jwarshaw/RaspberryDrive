import os
from PIL import Image

def get_image(count):
  scp_command = 'scp pi@192.168.2.5:Desktop/gregTest.jpg ' + 'images/' + str(count) + '.jpg'
  os.system(scp_command)
  return
	# os.system('scp pi@192.168.2.5:Desktop/gregTest.jpg gregTest.jpg')

	#if on a new computer and the pi address isn't connecting right away, need to create a key.  Use the following website to do so
	#https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md

def valid_image(path):
	try:
		Image.open(path)
	except IOError:
		return False
	return True
