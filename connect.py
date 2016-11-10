import socket

def new_connection():
    host = '192.168.2.4'
    port = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      s.connect((host, port))
      return s
    except Exception as e:
      print("Server not ready to connect")

def try_connection():
    host = '192.168.2.4'
    port = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
      s.connect((host, port))
    except Exception as e:
      print("something's wrong with ")


def send_command(connection,command,time):
    connection.send('' + command + ' ; ' + time)
    return receive_confirmation(connection)

def receive_confirmation(connection):
  received = connection.recv(20)
  return received;

def send_end_connection(connection):
  connection.send('quit')
  return

# example:
# con = new_conntection
# send_command(con,"forward",0.5)
