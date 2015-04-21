from PyQt4 import QtCore
import stine

#This file provides a list of all available engines.

#First, declare the list that will be populated with engines.
engines = []

#Add each engine to the list. Engine objects have the structure:
#class Engine(QtCore.QObject):
#    def __init__(self, name, mass, cost, Cd, Itot, Isp):
#       self.name = name
#       self.mass = mass
#       self.cost = cost
#       self.Cd   = Cd
#       self.Itot = Itot   Total Impulse in newton-sec
#       self.Isp  = Isp    Specific Impulse in seconds.
#       self.FvsT = FvsT   File containing thrust curve vs time.
B6_4 = stine.Engine('Estes B6-4', 0.00624, 1.0, 0.1, 5.0, 81.76, 'None')
engines.append(B6_4)

C6_3 = stine.Engine('Estes C6-3', 0.0125, 1.0, 0.1, 10, 81.76, 'None')
engines.append(C6_3)

D12_3 = stine.Engine('Estes D12-3', 0.0249, 1.0, 0.1, 20, 81.86, 'None')
engines.append(D12_3)

F1= stine.Engine('Rocketdyne F1', 9115, 1.5E6, 0.1, 1.117E09, 263, 'None')
engines.append(F1)

