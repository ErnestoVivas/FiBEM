from gui import add_device_dialog_ui
from dynamic_device_attrs_widget import DynamicDeviceAttrsWidget

from bes_entities import ontology_strings

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal


class AddDeviceDialog(QtWidgets.QDialog):

    new_device = pyqtSignal(str, str, str)

    def __init__(self, ref_entity_id):
        super().__init__()
        self.ui = add_device_dialog_ui.Ui_AddDeviceDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # setup generic ui elements
        self.ui.line_edit_device_id.setText("<enter_device_id>")
        self.ui.line_edit_entity_name.setText(f"{ref_entity_id}:<device_id>")
        self.setup_entity_types_combo_box()
        self.dynamic_device_attrs_widget = DynamicDeviceAttrsWidget()
        self.ui.scroll_area_dynamic_device_attrs.setWidget(self.dynamic_device_attrs_widget)

        # connect buttons to functions
        self.ui.button_ok.clicked.connect(self.add_device_to_bes)
        self.ui.button_cancel.clicked.connect(self.cancel)


    def setup_entity_types_combo_box(self):
        for device in ontology_strings.device_definitions:
            self.ui.combo_box_entity_type.addItem(device)


    def add_device_to_bes(self):
        device_id = self.ui.line_edit_device_id.text()
        entity_name = self.ui.line_edit_entity_name.text()
        entity_type = self.ui.combo_box_entity_type.currentText()
        self.new_device.emit(device_id, entity_name, entity_type)
        self.close()


    def cancel(self):
        self.close()
