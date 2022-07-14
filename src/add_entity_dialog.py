from gui import add_entity_dialog_ui

# from bes_entities import heat_pump_strings
from building_energy_system import BuildingEnergySystem
from bes_entities import electric_boiler
from bes_entities import heat_pump
from bes_entities import natural_gas_boiler
from bes_entities import ontology_strings

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


class AddEntityDialog(QtWidgets.QDialog):

    chosen_entity = pyqtSignal(int, str)

    def __init__(self, curr_bes):

        # setup window
        super().__init__()
        self.ui = add_entity_dialog_ui.Ui_AddEntityDialog()
        self.ui.setupUi(self)
        self.current_bes: BuildingEnergySystem = curr_bes
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setup_choose_entity_combo_box()

        # connect gui elements to functions
        self.ui.button_add_entity.clicked.connect(self.add_entity)
        self.ui.button_cancel.clicked.connect(self.cancel_add_entity)
        self.ui.combo_box_choose_entity.currentIndexChanged.connect(self.display_entity_properties)


    def setup_choose_entity_combo_box(self):
        self.ui.combo_box_choose_entity.addItem("Heat_Pump")
        self.ui.combo_box_choose_entity.addItem("Electric_Boiler")
        self.ui.combo_box_choose_entity.addItem("Natural_Gas_Boiler")
        self.ui.combo_box_choose_entity.addItem("Pump")
        self.ui.combo_box_choose_entity.addItem("Radiator")
        self.ui.combo_box_choose_entity.addItem("Room")
        self.ui.combo_box_choose_entity.addItem("Building")
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
        current_entity_count = self.current_bes.get_entity_count(current_entity)
        entity_type_str, entity_definition_str = ontology_strings.get_entity_strings(current_entity)
        entity_type_str_no_prefix = ontology_strings.strip_prefix(entity_type_str)
        self.ui.line_edit_set_id.setText(self.current_bes.id + ":" + entity_type_str_no_prefix +
                                         ":" + str(current_entity_count))
        self.ui.line_edit_brick_type.setText(entity_type_str)
        self.ui.plain_text_edit_brick_definition.setPlainText(entity_definition_str)
