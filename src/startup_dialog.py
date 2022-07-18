from gui import startup_dialog_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class StartupDialog(QtWidgets.QDialog):

    bes_id_set = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ui = startup_dialog_ui.Ui_StartupDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.line_edit_bes_id.setText("urn:ngsi_ld:my_house")
        self.ui.button_ok.clicked.connect(self.init_bes)

    def init_bes(self):
        self.bes_id_set.emit(self.ui.line_edit_bes_id.text())
        self.close()
