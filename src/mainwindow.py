
'''
    This class handles the main window of FiBEM and all its respective
    functions. The objective is to create a building energy system consisting of
    a set of entities and relationships. The logic of the BES itself is handled
    in the class "building_energy_system" and is an attribute of MainWindow.
'''

from add_entity_dialog import AddEntityDialog

from gui import mainwindow_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        # setup window
        super().__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # sub dialogs
        self.add_entity_dialog = None


        # connect buttons to their respective functions
        self.ui.button_add_entity.clicked.connect(self.add_entity)


    def add_entity_to_bes(self, chosen_entity):
        print(chosen_entity)
        if chosen_entity == 0:
            pass
        elif chosen_entity == 1:
            pass

    def add_entity(self):
        self.add_entity_dialog = AddEntityDialog()
        self.add_entity_dialog.chosen_entity.connect(self.add_entity_to_bes)
        self.add_entity_dialog.setWindowModality(Qt.ApplicationModal)
        self.add_entity_dialog.show()
