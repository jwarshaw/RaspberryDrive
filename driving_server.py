from socket import *
import_module(picar)

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('',9000))
    serversocket.listen(5)
    while(1):
        (clientsocket, address) = serversocket.accept()
        output = clientsocket.receive(1024)
        print output


createServer()