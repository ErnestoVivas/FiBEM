import json

from gui import show_devices_dialog_ui

from building_energy_system import BuildingEnergySystem
from bes_entities import ontology_strings

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
#from PyQt5.QtCore import pyqtSignal


class ShowDevicesDialog(QtWidgets.QDialog):

    def __init__(self, curr_bes):

        # setup window
        super().__init__()
        self.ui = show_devices_dialog_ui.Ui_ShowDevicesDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.current_bes: BuildingEnergySystem = curr_bes
        self.setup_entities_combo_box()

        # connect gui elements to functions
        self.ui.combo_box_entities.currentIndexChanged.connect(self.display_entity_devices)
        self.ui.list_widget_devices.currentRowChanged.connect(self.display_device_properties)
        self.ui.button_ok.clicked.connect(self.close_dialog)


    def setup_entities_combo_box(self):
        for entity in self.current_bes.entities:
            self.ui.combo_box_entities.addItem(entity.base_attributes["id"])


    def display_entity_devices(self):
        self.ui.list_widget_devices.clear()
        current_entity = self.ui.combo_box_entities.currentIndex()
        for device in self.current_bes.entities[current_entity].devices:
            self.ui.list_widget_devices.addItem(QListWidgetItem(device["device_id"]))


    def display_device_properties(self):
        self.ui.text_edit_device_properties.clear()
        current_entity = self.ui.combo_box_entities.currentIndex()
        current_device = self.ui.list_widget_devices.currentRow()
        if current_device >= 0:
            self.ui.text_edit_device_properties.setText(json.dumps(self.current_bes.entities[current_entity].devices[current_device], indent=2))


    def close_dialog(self):
        self.close()
