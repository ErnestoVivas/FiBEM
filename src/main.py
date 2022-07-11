import sys

from PyQt5 import QtWidgets, QtGui

from mainwindow import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setWindowIcon(QtGui.QIcon("fibem-icon.ico"))
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
