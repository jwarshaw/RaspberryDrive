from connect import *

class CarManeuvers(object):

  def __init__(self,connection):
    self.connection = connection

  def forward(self):
    print "executing forward"
    send_command(self.connection, "forward", "0.5")

  def right(self):
    print "executing right"
    send_command(self.connection, "right", "9.85")

  def left(self):
    print "executing left"
    send_command(self.connection, "left", "0.85")

  def back_up_then_right(self):
    print "executing back up and drive right"
    send_command(self.connection, "left", "0.1")
    send_command(self.connection, "backward", "0.6")


  def back_up_then_left(self):
    print "executing back up and drive left"
    send_command(self.connection, "right", "0.1")
    send_command(self.connection, "backward", "0.6")
    #

