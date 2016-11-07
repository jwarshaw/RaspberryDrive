from socket import *
import run_py_car as picar

def createPiReceiver():
    	serversocket = socket(AF_INET, SOCK_STREAM)
    	new_picar = picar.PiCar()
    	serversocket.bind(('',9000))
   	serversocket.listen(5)
    	while(1):
        	(clientsocket, address) = serversocket.accept()
		while(1):
        		transfer = clientsocket.recv(1024).split(';')	
			inputParser(transfer[0].strip(),float(transfer[1]),new_picar)
	
def inputParser(command,number,car):
	print 'going ' + command + ' for ' + str(number) +' seconds'
	if    command == "forward":
		car.go_forward(number)
	elif command == "backward":
		car.go_backward(number)
	elif command == "right":
		car.go_forward_right(number)
	elif command == "left":
		car.go_forward_left(number)	
	elif command == "backward right":
		car.go_backward_right(number)
	elif command == "backward left":
		car.go_backward_left(number)	
	else: 
		car.stop()
	
	
createPiReceiver()
