from gui import dynamic_device_attrs_widget_ui

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QFont


class DynamicDeviceAttrsWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = dynamic_device_attrs_widget_ui.Ui_DynamicDeviceAttrsWidget()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
