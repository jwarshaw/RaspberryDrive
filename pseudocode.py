



def driveforward(time)
  FOR each second in time
    goforward(1)
    IF isblocked?
      return false

def isblocked?
  IF checkcamera() && checkproximity()
    return true
  ELSE
    return false

def goforward(time):
  FOR the length of time
    sendgoforwardsignaltocar()

def gobackward(time):
  FOR the length of time
    sendgobackwardsignaltocar()

def maneuverright(backuptime,rightime):
  gobackward(backuptime)
  goright(righttime)

def checkcamera()

def checkproximity()



