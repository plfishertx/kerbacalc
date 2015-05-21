import sys
import numpy as np
from PyQt4 import QtCore, QtGui
from ui_kerbacalc3 import *
import random
import stine
import payloads
from buildStageDlg import *
from ui_buildStage import *
 
class GUIForm(QtGui.QMainWindow):
#This class is the top level window.
 
   def __init__(self, parent=None):
      #Initialize the super class, same as executing...
      #QtGui.QMainWindow.__init__(self,parent)
      super(GUIForm, self).__init__(parent)
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)

      #Set the inital state of the radio buttons.
      self.ui.aeroNoneButton.setChecked(1)

      #Launch the simulation when calcButton is clicked.
      QtCore.QObject.connect(self.ui.calcButton, 
                             QtCore.SIGNAL('clicked()'), 
                             self.updateGraph )

      #Call buildRocket() when stageButton is clicked.
      QtCore.QObject.connect(self.ui.stageButton,
                             QtCore.SIGNAL('clicked()'),
                             self.showBuildDlg )

   def showBuildDlg(self):
      print "Calling  BuildStageDialog from buildRocket."
      #Create the dialog box for building the rocket.
      buildDlg = BuildStageDialog(self)
      buildDlg.show()
      

      #part1 = stine.Part('rock1', 1.0, 2.0, 0.10)
      #print 'part.mass = ', part1.mass
      #partslist = [part1]
      #stage1 = stine.Stage(partslist)
      #stage2 = stine.Stage(partslist)
      #print 'stage1.mass = ', stage1.mass
      #stageList = [stage1]
      self.rocket = stine.Rocket(buildDlg.stageList)
      print "stageList is ", buildDlg.stageList
      print 'rocket.mass = ', self.rocket.m


   def updateGraph(self):
      #Launch it with initial values for pos'n, v, acc. and direction
      self.rocket.launch(0,0,0, 10.0,10.0,10.0, 0,-9.8,0, 0.0,np.pi/2.0)

      #Define params for time-diff calculation of trajectory.
      stoptime = 4.0
      Npts = 20
      dt = stoptime/Npts
      tpts = np.linspace(0, stoptime, Npts)
      vArray = np.array([0])
      yArray = np.array([0])
      print 0, tpts[0], self.rocket.y, self.rocket.vy
      for i in range( 1, len(tpts) ): 
          #Call rocket.go to advance 1 timestep.
          self.rocket.go(self.rocket.x, self.rocket.y, self.rocket.z, dt)
          print i, tpts[i], self.rocket.y, self.rocket.vy   
          vArray = np.append(vArray, self.rocket.vy)
          yArray = np.append(yArray, self.rocket.y)
      #Plot trajectory.
      self.ui.tstWidget.canvas.ax.clear()
      self.ui.tstWidget.canvas.ax.plot(tpts, yArray)
      self.ui.tstWidget.canvas.draw() 
#End of class GUIForm. 
 
if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)


   kerbWind = GUIForm()
   kerbWind.show()
   sys.exit(app.exec_())
