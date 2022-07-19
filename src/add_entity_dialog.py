from gui import add_entity_dialog_ui

from building_energy_system import BuildingEnergySystem
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
        self.setup_choose_group_combo_box()
        self.selected_entity = 0

        # connect gui elements to functions
        self.ui.combo_box_choose_group.currentIndexChanged.connect(self.update_choose_entity_combo_box)
        self.ui.combo_box_choose_entity.currentIndexChanged.connect(self.display_entity_properties)
        self.ui.button_add_entity.clicked.connect(self.add_entity)
        self.ui.button_cancel.clicked.connect(self.cancel_add_entity)


    def setup_choose_group_combo_box(self):
        self.ui.combo_box_choose_group.addItem("Equipment")
        self.ui.combo_box_choose_group.addItem("System")
        self.ui.combo_box_choose_group.addItem("Location")
        self.ui.combo_box_choose_group.setCurrentIndex(0)
        self.update_choose_entity_combo_box()
        #self.get_selected_entity()
        #self.display_entity_properties()

    def update_choose_entity_combo_box(self):
        self.ui.combo_box_choose_entity.clear()
        group_index = self.ui.combo_box_choose_group.currentIndex()
        if group_index == 0:
            self.ui.combo_box_choose_entity.addItem("Heat_Pump")
            self.ui.combo_box_choose_entity.addItem("Electric_Boiler")
            self.ui.combo_box_choose_entity.addItem("Natural_Gas_Boiler")
            self.ui.combo_box_choose_entity.addItem("Cogeneration_Plant")
            self.ui.combo_box_choose_entity.addItem("Heat_Exchanger")
            self.ui.combo_box_choose_entity.addItem("PV_Panel")
            self.ui.combo_box_choose_entity.addItem("PVT_Panel")
            self.ui.combo_box_choose_entity.addItem("Solar_Thermal_Collector")
            self.ui.combo_box_choose_entity.addItem("Water_Heater")
            self.ui.combo_box_choose_entity.addItem("Water_Distribution")
            self.ui.combo_box_choose_entity.addItem("Valve")
            self.ui.combo_box_choose_entity.addItem("Pump")
            self.ui.combo_box_choose_entity.addItem("Radiator")
            self.ui.combo_box_choose_entity.addItem("Battery")
        elif group_index == 1:
            self.ui.combo_box_choose_entity.addItem("HVAC_System")
            self.ui.combo_box_choose_entity.addItem("Electrical_System")
            self.ui.combo_box_choose_entity.addItem("Water_System")
        elif group_index == 2:
            self.ui.combo_box_choose_entity.addItem("Room")
            self.ui.combo_box_choose_entity.addItem("Building")
            self.ui.combo_box_choose_entity.addItem("Outside")
        self.ui.combo_box_choose_entity.setCurrentIndex(0)
        self.display_entity_properties()


    def get_selected_entity(self):
        group_index = self.ui.combo_box_choose_group.currentIndex()
        entity_index = self.ui.combo_box_choose_entity.currentIndex()

        # map selected entity to lookup table
        if group_index == 0:
            self.selected_entity = entity_index
        elif group_index == 1:
            self.selected_entity = 14 + entity_index
        else:
            self.selected_entity = 17 + entity_index


    def add_entity(self):
        self.get_selected_entity()
        self.chosen_entity.emit(self.selected_entity, self.ui.line_edit_set_id.text())
        self.close()


    def cancel_add_entity(self):
        self.close()


    def display_entity_properties(self):
        self.get_selected_entity()
        current_entity_count = self.current_bes.get_entity_count(self.selected_entity)
        entity_type_str, entity_definition_str = ontology_strings.get_entity_strings(self.selected_entity)
        entity_type_str_no_prefix = ontology_strings.strip_prefix(entity_type_str)
        self.ui.line_edit_set_id.setText(f"{self.current_bes.id}:{entity_type_str_no_prefix}:{str(current_entity_count + 1).zfill(3)}")
        self.ui.line_edit_brick_type.setText(entity_type_str)
        self.ui.plain_text_edit_brick_definition.setPlainText(entity_definition_str)
