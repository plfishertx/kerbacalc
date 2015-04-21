#We build rockets!

class Part:
   def __init__(self, name, m, cost, Cd):
      self.name = name
      self.mass = m
      self.cost = cost
      self.Cd = Cd

class Payload(Part):
   def __init__(self, name, m, cost, Cd, pwrRqd):
      self.name = name
      self.m = m
      self.cost = cost
      self.Cd = Cd
      self.pwrRqd = pwrRqd

class Engine(Part):
   def __init__(self, name, m, cost, Cd, Itot, Isp, FvsT):
      self.name = name
      self.m    = m
      self.cost = cost
      self.Cd   = Cd
      self.Itot = Itot
      self.Isp  = Isp
      self.FvsT = FvsT

class Fueltank(Part):
   def __init__(self, name, mTot, cost, Cd, drymass):
      Part.__init__(name, mTot, cost, Cd)
      self.drymass = drymass

class Decoupler(Part):
   def __init__(self, name, m, cost, Cd):
      Part.__init__(name, m, cost, Cd)
      
class Stage(Part):
   def  __init__(self, parts):
      self.m = 0
      for obj in parts:
        self.m += obj.m

class Rocket:
   #Specify a list of stages in var "stages".
   def __init__(self, stages):
      print "Initialized a Rocket."
      self.stages = stages
      self.m = 0
      for eachStage in stages:
          self.m += eachStage.m

   def assembleStages(self):
       print "Ready to assemble stages!"

   def launch(self, x0, y0, v0x, v0y, a0x, a0y):
       self.x = x0
       self.y = y0
       self.vx = v0x
       self.vy = v0y
       self.ax = a0x
       self.ay = a0y

   def go(self, x, y, dt):
       halfdt = dt/2.0
       #Advance 1/2 tstep to find avg v and new acc.
       self.vx_avg = self.vx + self.ax*halfdt
       self.vy_avg = self.vy + self.ay*halfdt
       #Put acc calculation here.
       self.x  += self.vx_avg*dt
       self.y  += self.vy_avg*dt
       self.vx += self.ax*dt
       self.vy += self.ay*dt



