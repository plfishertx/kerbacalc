import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(350,250)
    w.move(300,300)
    w.setWindowTitle('SimpleTitle')
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


