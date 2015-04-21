from PyQt4 import QtCore
import stine

#This file provides a list of all available payloads.

#First, declare the list that will be populated with payloads.
payloads = []

#Add each payload to the list. Payload objects have the structure:
#class Payload(QtCore.QObject):
#    def __init__(self, name, mass, cost, Cd, pwrRqd):
#       self.name = name
#       self.mass = mass
#       self.cost = cost
#       self.Cd   = Cd
#       self.pwrRqd = pwrRqd

rock = stine.Payload('rock', 1.0, 0, 0.3, 0)
payloads.append(rock)

stayPutnik = stine.Payload('stayPutnik', 10, 1.0, 0, 0)
payloads.append(stayPutnik)

n1_OgiveNoseCone = stine.Payload('N1_Ogive', 0.050, 0.50, 0.2, 0)
payloads.append(n1_OgiveNoseCone)

n2_ParabolicNoseCone = stine.Payload('N2_Parabolic', 0.050, 0.50, 0.1, 0)
payloads.append(n2_ParabolicNoseCone)

