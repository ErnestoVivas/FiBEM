from gui import add_entity_dialog_ui

# from bes_entities import heat_pump_strings
from bes_entities import electric_boiler

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


class AddEntityDialog(QtWidgets.QDialog):

    chosen_entity = pyqtSignal(int, str)

    def __init__(self, bes_id):

        # setup window
        super().__init__()
        self.ui = add_entity_dialog_ui.Ui_AddEntityDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setup_choose_entity_combo_box()
        self.bes_id = bes_id

        # connect gui elements to functions
        self.ui.button_add_entity.clicked.connect(self.add_entity)
        self.ui.button_cancel.clicked.connect(self.cancel_add_entity)
        self.ui.combo_box_choose_entity.currentIndexChanged.connect(self.display_entity_properties)


    def setup_choose_entity_combo_box(self):
        self.ui.combo_box_choose_entity.addItem("Heat_Pump")
        self.ui.combo_box_choose_entity.addItem("Electric_Boiler")
        self.ui.combo_box_choose_entity.addItem("Weather_Condition")
        self.ui.combo_box_choose_entity.setCurrentIndex(0)
        self.display_entity_properties()

    def add_entity(self):
        self.chosen_entity.emit(self.ui.combo_box_choose_entity.currentIndex(),
                                self.ui.line_edit_set_id.text())
        self.close()

    def cancel_add_entity(self):
        self.close()

    def display_entity_properties(self):
        current_entity = self.ui.combo_box_choose_entity.currentIndex()
        if current_entity == 0:
            self.ui.line_edit_brick_type.setText("ebc:Heat_Pump")
            self.ui.plain_text_edit_brick_definition.setPlainText("Heat pump definition")
        elif current_entity == 1:
            electric_boiler_count = electric_boiler.ElectricBoiler.get_entity_count()
            self.ui.line_edit_set_id.setText(self.bes_id + ":Electric_Boiler:" + str(electric_boiler_count))
            self.ui.line_edit_brick_type.setText(electric_boiler.electric_boiler_type)
            self.ui.plain_text_edit_brick_definition.setPlainText(electric_boiler.electric_boiler_definition)
