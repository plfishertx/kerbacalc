#class Location(QObject):
#   def __init__(self, g):
#       self.g = g
import physConst

class Planet():
   def __init__(self, name, mass, R, g, a, apoap, periap, inc, ecc, lonAsc,
                lonPeriHel, T):
      self.name = name
      self.mass = mass
      self.R    = R
      self.g    = g
      self.a    = a
      self.apoap= apoap
      self.periap = periap
      self.inc = inc
      self.ecc = ecc
      self.lonAsc = lonAsc
      self.lonPeriHel = lonPeriHel
      self.T = T

   def orbitalV(r):
      return(math.sqrt(physConst.G*self.mass/r))

#Planet data in meters, kg, sec, and degrees.
planetList = [
             {'name':'Earth', 'mass':5.972E24, 'R':6.371E06, 'g':9.80,
              'a':1.49598E11, 'apoap':1.5210E11, 'periap':1.4709E11,  
              'inc':0.00005,'ecc':0.0167, 'lonAsc':-11.26064, 'lonPeriHel':102.94719, 
              'T':3.1558118E7},
             {'name':'Kerbin', 'mass':5.2915793E22, 'R':6.00E5, 'g':9.81,
              'a':1.3599840256E10, 'apoap':1.3599840256E10, 'periap':1.3599840256E10, 
              'inc':0, 'ecc':0, 'lonAsc':0, 'lonPeriHel':0, 
              'T':9.203545E6},
             {'name':'Mun', 'mass':9.76E20, 'R':2.0E5, 'g':1.63,
              'a':1.2E7, 'apoap':1.2E7, 'periap':1.2E7, 'inc':0, 
              'ecc':0, 'lonAsc':0, 'lonPeriHel':0, 
              'T':138984},
             {'name':'Minmus', 'mass':2.6457897E19, 'R':6.0E4, 'g':0.491,
              'a':4.7E7, 'apoap':4.7E7, 'periap':4.7E7, 'inc':6.0, 
              'ecc':0, 'lonAsc':78, 'lonPeriHel':38, 
              'T':1077311},
             {'name':'Moon', 'mass':7.34767309E22, 'R':1.7381E6, 'g':1.62,
              'a':3.844E8, 'apoap':4.055E8, 'periap':3.633E8, 'inc':5.145, 
              'ecc':0.0549, 'lonAsc':0, 'lonPeriHel':0, 
              'T':2.3606208E6}
             ]
planets = []
for world in planetList:
    planets.append( Planet(world['name'], world['mass'], world['R'], world['g'],
               world['a'], world['apoap'], world['periap'], world['inc'],
               world['ecc'], world['lonAsc'], world['lonPeriHel'], world['T']) )

for a in planets:
    print a.name, a.g, 'm/s^2  ', 365.256*a.T/3.1558118E7, 'days'

print "Big G is ", physConst.G



