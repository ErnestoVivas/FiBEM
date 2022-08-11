import json
from sys import platform

from gui import show_devices_dialog_ui
from add_device_dialog import AddDeviceDialog

from building_energy_system import BuildingEnergySystem
from bes_entities import ontology_strings

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal


class ShowDevicesDialog(QtWidgets.QDialog):

    deleted_device = pyqtSignal(int, int)       # entity_id, device_id
    new_device = pyqtSignal(int, str, str, str) # entity_id, device_id, entity_name, entity_type

    def __init__(self, curr_bes, selected_entity_index):

        # setup window
        super().__init__()
        self.ui = show_devices_dialog_ui.Ui_ShowDevicesDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.current_bes: BuildingEnergySystem = curr_bes
        self.setup_entities_combo_box(selected_entity_index)

        self.add_device_dialog = None

        if (platform == "linux") or (platform == "linux2"):
            self.ui.text_edit_device_properties.setFont(QFont("DejaVu Sans Mono"))

        # connect gui elements to functions
        self.ui.combo_box_entities.currentIndexChanged.connect(self.display_entity_devices)
        self.ui.list_widget_devices.currentRowChanged.connect(self.display_device_properties)
        self.ui.button_ok.clicked.connect(self.close_dialog)
        self.ui.button_add_device.clicked.connect(self.add_device)
        self.ui.button_delete_device.clicked.connect(self.delete_device)


    def setup_entities_combo_box(self, selected_entity_index):
        for entity in self.current_bes.entities:
            self.ui.combo_box_entities.addItem(entity.base_attributes["id"])
        if selected_entity_index >= 0:
            self.ui.combo_box_entities.setCurrentIndex(selected_entity_index)
        elif self.ui.combo_box_entities.count() > 0:
            self.ui.combo_box_entities.setCurrentIndex(0)
        self.display_entity_devices()


    def display_entity_devices(self):
        self.ui.list_widget_devices.clear()
        current_entity = self.ui.combo_box_entities.currentIndex()
        for device in self.current_bes.entities[current_entity].devices:
            self.ui.list_widget_devices.addItem(QListWidgetItem(device["device_id"]))
        if self.ui.list_widget_devices.count() > 0:
            self.ui.list_widget_devices.setCurrentRow(0)
        self.display_device_properties()


    def display_device_properties(self):
        self.ui.text_edit_device_properties.clear()
        current_entity = self.ui.combo_box_entities.currentIndex()
        current_device = self.ui.list_widget_devices.currentRow()
        update_device_index = False
        if current_device >= len(self.current_bes.entities[current_entity].devices):
            print("true")
            update_device_index = True
            if len(self.current_bes.entities[current_entity].devices) == 0:
                current_device = -1
            else:
                current_device = 0

        if current_device >= 0:
            print(f"num of devices: {len(self.current_bes.entities[current_entity].devices)}, current device: {current_device}")
            self.ui.text_edit_device_properties.setText(json.dumps(self.current_bes.entities[current_entity].devices[current_device], indent=2))
        else:
            self.ui.text_edit_device_properties.setText("No devices have been found for this entity.")

        if update_device_index:
            self.ui.list_widget_devices.setCurrentRow(current_device)


    def add_device(self):
        ref_entity_id = self.ui.combo_box_entities.currentText()
        self.add_device_dialog = AddDeviceDialog(ref_entity_id)
        self.add_device_dialog.new_device.connect(self.add_device_to_bes)
        self.add_device_dialog.setWindowModality(Qt.ApplicationModal)
        self.add_device_dialog.show()


    def add_device_to_bes(self, device_id, entity_name, entity_type):
        entity_index = self.ui.combo_box_entities.currentIndex()
        self.new_device.emit(entity_index, device_id, entity_name, entity_type)
        self.display_entity_devices()


    def delete_device(self):
        entity_index = self.ui.combo_box_entities.currentIndex()
        device_index = self.ui.list_widget_devices.currentRow()
        if device_index >= 0:
            self.deleted_device.emit(entity_index, device_index)
            self.ui.list_widget_devices.takeItem(device_index)


    def close_dialog(self):
        self.close()
