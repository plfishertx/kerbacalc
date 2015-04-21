# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kerbacalc3.ui'
#
# Created: Wed Dec  3 16:57:38 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(852, 740)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.calcButton = QtGui.QPushButton(self.centralwidget)
        self.calcButton.setGeometry(QtCore.QRect(360, 350, 79, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calcButton.setFont(font)
        self.calcButton.setObjectName(_fromUtf8("calcButton"))
        self.tstWidget = TestWidget(self.centralwidget)
        self.tstWidget.setGeometry(QtCore.QRect(410, 390, 441, 311))
        self.tstWidget.setStyleSheet(_fromUtf8("border-style: solid;\n"
"border-size: 2px;\n"
"border-color: black;\n"
""))
        self.tstWidget.setObjectName(_fromUtf8("tstWidget"))
        self.stagesLabel = QtGui.QLabel(self.centralwidget)
        self.stagesLabel.setGeometry(QtCore.QRect(420, 10, 421, 281))
        self.stagesLabel.setStyleSheet(_fromUtf8("background-color: blue;\n"
"color: white;\n"
""))
        self.stagesLabel.setObjectName(_fromUtf8("stagesLabel"))
        self.stageLabel = QtGui.QLabel(self.centralwidget)
        self.stageLabel.setGeometry(QtCore.QRect(10, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stageLabel.setFont(font)
        self.stageLabel.setObjectName(_fromUtf8("stageLabel"))
        self.stageBox = QtGui.QSpinBox(self.centralwidget)
        self.stageBox.setGeometry(QtCore.QRect(80, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stageBox.setFont(font)
        self.stageBox.setMinimum(1)
        self.stageBox.setObjectName(_fromUtf8("stageBox"))
        self.stageButton = QtGui.QPushButton(self.centralwidget)
        self.stageButton.setGeometry(QtCore.QRect(190, 20, 81, 31))
        self.stageButton.setObjectName(_fromUtf8("stageButton"))
        self.locationLabel = QtGui.QLabel(self.centralwidget)
        self.locationLabel.setGeometry(QtCore.QRect(10, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locationLabel.setFont(font)
        self.locationLabel.setObjectName(_fromUtf8("locationLabel"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 660, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.maxAccLCD = QtGui.QLCDNumber(self.centralwidget)
        self.maxAccLCD.setGeometry(QtCore.QRect(110, 650, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.maxAccLCD.setFont(font)
        self.maxAccLCD.setStyleSheet(_fromUtf8("color: green;\n"
"background-color: black;\n"
""))
        self.maxAccLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.maxAccLCD.setObjectName(_fromUtf8("maxAccLCD"))
        self.deltaVLCD = QtGui.QLCDNumber(self.centralwidget)
        self.deltaVLCD.setGeometry(QtCore.QRect(110, 570, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deltaVLCD.setFont(font)
        self.deltaVLCD.setStyleSheet(_fromUtf8("color: green;\n"
"background-color: black;\n"
""))
        self.deltaVLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.deltaVLCD.setObjectName(_fromUtf8("deltaVLCD"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 590, 58, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.deltaVLCD_2 = QtGui.QLCDNumber(self.centralwidget)
        self.deltaVLCD_2.setGeometry(QtCore.QRect(110, 502, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deltaVLCD_2.setFont(font)
        self.deltaVLCD_2.setStyleSheet(_fromUtf8("color: green;\n"
"background-color: black;\n"
""))
        self.deltaVLCD_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.deltaVLCD_2.setObjectName(_fromUtf8("deltaVLCD_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 520, 58, 14))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 590, 58, 14))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 660, 58, 14))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.aeroGrpBox = QtGui.QGroupBox(self.centralwidget)
        self.aeroGrpBox.setGeometry(QtCore.QRect(10, 160, 271, 131))
        self.aeroGrpBox.setObjectName(_fromUtf8("aeroGrpBox"))
        self.aeroNoneButton = QtGui.QRadioButton(self.aeroGrpBox)
        self.aeroNoneButton.setGeometry(QtCore.QRect(10, 20, 98, 19))
        self.aeroNoneButton.setObjectName(_fromUtf8("aeroNoneButton"))
        self.aeroKSPButton = QtGui.QRadioButton(self.aeroGrpBox)
        self.aeroKSPButton.setGeometry(QtCore.QRect(10, 50, 98, 19))
        self.aeroKSPButton.setObjectName(_fromUtf8("aeroKSPButton"))
        self.aeroFarnhamButton = QtGui.QRadioButton(self.aeroGrpBox)
        self.aeroFarnhamButton.setGeometry(QtCore.QRect(10, 80, 98, 19))
        self.aeroFarnhamButton.setObjectName(_fromUtf8("aeroFarnhamButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.calcButton.setText(_translate("MainWindow", "Launch", None))
        self.stagesLabel.setText(_translate("MainWindow", "stagesLabel", None))
        self.stageLabel.setText(_translate("MainWindow", "Stage:", None))
        self.stageButton.setText(_translate("MainWindow", "Build stage", None))
        self.locationLabel.setText(_translate("MainWindow", "Location:", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Kerbin", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mun", None))
        self.label.setText(_translate("MainWindow", "Max Acc:", None))
        self.label_2.setText(_translate("MainWindow", "Delta V:", None))
        self.label_3.setText(_translate("MainWindow", "Thrust/Weight", None))
        self.label_4.setText(_translate("MainWindow", "m/s", None))
        self.label_5.setText(_translate("MainWindow", "m/s^2", None))
        self.aeroGrpBox.setTitle(_translate("MainWindow", "Aerodynamics model", None))
        self.aeroNoneButton.setText(_translate("MainWindow", "None", None))
        self.aeroKSPButton.setText(_translate("MainWindow", "KSP standard", None))
        self.aeroFarnhamButton.setText(_translate("MainWindow", "Farnham", None))

from testwidget import TestWidget
