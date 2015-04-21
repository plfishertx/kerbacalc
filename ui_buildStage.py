# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildStage.ui'
#
# Created: Sat Dec  6 12:26:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BuildStageDialog(object):
    def setupUi(self, BuildStageDialog):
        BuildStageDialog.setObjectName(_fromUtf8("BuildStageDialog"))
        BuildStageDialog.resize(716, 555)
        self.label = QtGui.QLabel(BuildStageDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(BuildStageDialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 681, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 181, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.NenginesBox = QtGui.QSpinBox(self.tab)
        self.NenginesBox.setGeometry(QtCore.QRect(210, 70, 53, 22))
        self.NenginesBox.setObjectName(_fromUtf8("NenginesBox"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 161, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.engineBox = QtGui.QComboBox(self.tab)
        self.engineBox.setGeometry(QtCore.QRect(140, 20, 151, 22))
        self.engineBox.setObjectName(_fromUtf8("engineBox"))
        self.engineBox.addItem(_fromUtf8(""))
        self.engineBox.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(340, 10, 91, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.spinBox = QtGui.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(490, 80, 53, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(470, 20, 81, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(340, 80, 151, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 141, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.payloadBox = QtGui.QComboBox(self.tab)
        self.payloadBox.setGeometry(QtCore.QRect(120, 140, 421, 22))
        self.payloadBox.setObjectName(_fromUtf8("payloadBox"))
        self.payloadBox.addItem(_fromUtf8(""))
        self.payloadBox.addItem(_fromUtf8(""))
        self.saveButton = QtGui.QPushButton(self.tab)
        self.saveButton.setGeometry(QtCore.QRect(40, 220, 79, 24))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.cancelButton = QtGui.QPushButton(self.tab)
        self.cancelButton.setGeometry(QtCore.QRect(390, 220, 79, 24))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.Add_Stage = QtGui.QWidget()
        self.Add_Stage.setObjectName(_fromUtf8("Add_Stage"))
        self.tabWidget.addTab(self.Add_Stage, _fromUtf8(""))

        self.retranslateUi(BuildStageDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BuildStageDialog)

    def retranslateUi(self, BuildStageDialog):
        BuildStageDialog.setWindowTitle(_translate("BuildStageDialog", "Dialog", None))
        self.label.setText(_translate("BuildStageDialog", "Build stage", None))
        self.label_2.setText(_translate("BuildStageDialog", "Number of Engine(s)", None))
        self.label_3.setText(_translate("BuildStageDialog", "Engine Type", None))
        self.engineBox.setItemText(0, _translate("BuildStageDialog", "None", None))
        self.engineBox.setItemText(1, _translate("BuildStageDialog", "Custom", None))
        self.label_4.setText(_translate("BuildStageDialog", "Fuel Tank(s)", None))
        self.comboBox.setItemText(0, _translate("BuildStageDialog", "Custom", None))
        self.comboBox.setItemText(1, _translate("BuildStageDialog", "None", None))
        self.comboBox.setItemText(2, _translate("BuildStageDialog", "S-IV B", None))
        self.comboBox.setItemText(3, _translate("BuildStageDialog", "S-II C", None))
        self.comboBox.setItemText(4, _translate("BuildStageDialog", "S-I C", None))
        self.label_5.setText(_translate("BuildStageDialog", "Number of Tanks:", None))
        self.label_6.setText(_translate("BuildStageDialog", "Payload", None))
        self.payloadBox.setItemText(0, _translate("BuildStageDialog", "None", None))
        self.payloadBox.setItemText(1, _translate("BuildStageDialog", "Custom", None))
        self.saveButton.setText(_translate("BuildStageDialog", "Save", None))
        self.cancelButton.setText(_translate("BuildStageDialog", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BuildStageDialog", "Stage 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Add_Stage), _translate("BuildStageDialog", "Tab 2", None))

