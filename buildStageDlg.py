from PyQt4 import QtCore, QtGui
from ui_buildStage import *
import stine
import payloads
import engines

class BuildStageDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        print "In init for BuildStageDialog class"
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_BuildStageDialog()
        self.ui.setupUi(self)
        print "StageDialog setup done."

        #Initialize stageList variable.
        self.stageList = []

        #Load list of payloads from payloads.py file.
        for aPayload in payloads.payloads:
            self.ui.payloadBox.addItem(aPayload.name)

        #Load list of engines from engines.py file.
        for anEngine in engines.engines:
            self.ui.engineBox.addItem(anEngine.name)

#        print "tab number is ", self.ui.currentIndex
        #Connect the GUI buttons to the appropriate methods.
        QtCore.QObject.connect(self.ui.payloadBox,
            QtCore.SIGNAL('currentIndexChanged(int)'), self.setPayload )

        QtCore.QObject.connect(self.ui.engineBox,
            QtCore.SIGNAL('currentIndexChanged(int)'), self.setEngine )

        QtCore.QObject.connect(self.ui.cancelButton,
            QtCore.SIGNAL('clicked()'), self.reject )

        QtCore.QObject.connect(self.ui.saveButton, 
            QtCore.SIGNAL('clicked()'),
            self.saveStage )
    #End of init

    def setPayload(self):
        print "In setPayload!"
        self.payloadName = self.ui.payloadBox.currentText()
        print "Payload is ", self.payloadName
        #payload = stine.Payload(payloadName, 1.0, 0, 0, 0)

    def setEngine(self):
        print "In setEngine!"
        self.engineName = self.ui.engineBox.currentText()
        print "Engine is ", self.engineName
        #payload = stine.Payload(payloadName, 1.0, 0, 0, 0)

    def saveStage(self):
        #Save the payload chosen for this stage.
        #payloadName = self.ui.payloadBox.currentText()
        for aPayload in payloads.payloads:
            if aPayload.name == self.payloadName:
               self.payload = aPayload
               print self.payloadName, "saved in saveStage."

        for anEngine in engines.engines:
            if anEngine.name == self.engineName:
               self.engine = anEngine
               print self.engineName, "saved in saveStage."

               
        #self.rock = stine.Payload('rock', 1.0, 0, 0, 0)
        self.partsList = [self.payload, self.engine]
        self.stage1 = stine.Stage(self.partsList)
        self.stageList = [self.stage1]
        print "stageList saved"
        print "Payload object is ", self.payload.name
        print "Engine object is ", self.engine.name


