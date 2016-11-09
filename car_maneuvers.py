from connect import *

class CarManeuvers(object):

  def __init__(self,connection):
    self.connection = connection

  def forward(self):
    print "executing forward"
    send_command(self.connection, "forward", "0.5")

  def right(self):
    send_command(self.connection, "right", "0.5")

  def left(self):
    send_command(self.connection, "left", "0.5")

  def back_up_and_then_drive_right(self):
    print "executing back up and drive right"
    send_command(self.connection, "backwards", "0.75")
    send_command(self.connection, "right", "0.5")

  def back_up_and_then_drive_left(self):
    send_command(self.connection, "backwards", "0.75")
    send_command(self.connection, "left", "0.5")

