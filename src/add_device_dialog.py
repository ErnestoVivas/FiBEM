from gui import add_device_dialog_ui
from dynamic_device_attrs_widget import DynamicDeviceAttrsWidget

from bes_entities import ontology_strings

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QFont


class AddDeviceDialog(QtWidgets.QDialog):

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

    def setup_entity_types_combo_box(self):
        for sensor in ontology_strings.sensor_definitions:
            self.ui.combo_box_entity_type.addItem(sensor)
        self.ui.combo_box_entity_type.insertSeparator(self.ui.combo_box_entity_type.count())
        for property in ontology_strings.calculated_properties_definitions:
            self.ui.combo_box_entity_type.addItem(property)
        self.ui.combo_box_entity_type.insertSeparator(self.ui.combo_box_entity_type.count())
        for command in ontology_strings.command_definitions:
            self.ui.combo_box_entity_type.addItem(command)
