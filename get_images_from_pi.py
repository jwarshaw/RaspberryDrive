import os
import time

def get_image():
	count = 0
	while count < 3:
		os.system('scp "%s:%s" "%s"' % ('pi@192.168.2.5', 'Desktop/greg.jpg', 'greg.jpg') )
		#if pi address isn't connecting right away, need to create a key.  Use the following website to do so
		#https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md
		#replace Desktop/greg with the path.
		#replace greg with the file name
		time.sleep(0.5)
		count += 1
		#replace sleep with the amount of time needed to sleep in between getting pictures.

get_image()