from gui import add_entity_dialog_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


class AddEntityDialog(QtWidgets.QDialog):

    chosen_entity = pyqtSignal(int)

    def __init__(self):

        # setup window
        super().__init__()
        self.ui = add_entity_dialog_ui.Ui_AddEntityDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setup_choose_entity_combo_box()

        # connect buttons to functions
        self.ui.button_add_entity.clicked.connect(self.add_entity)
        self.ui.button_cancel.clicked.connect(self.cancel_add_entity)


    def setup_choose_entity_combo_box(self):
        self.ui.combo_box_choose_entity.addItem("Heat_Pump")
        self.ui.combo_box_choose_entity.addItem("Weather_Condition")
        self.ui.combo_box_choose_entity.setCurrentIndex(0)

    def add_entity(self):
        self.chosen_entity.emit(self.ui.combo_box_choose_entity.currentIndex())
        self.close()

    def cancel_add_entity(self):
        self.close()
