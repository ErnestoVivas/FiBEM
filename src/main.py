import sys

from PyQt5 import QtWidgets

from mainwindow import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
