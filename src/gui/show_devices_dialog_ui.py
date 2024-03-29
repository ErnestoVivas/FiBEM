# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_devices_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowDevicesDialog(object):
    def setupUi(self, ShowDevicesDialog):
        ShowDevicesDialog.setObjectName("ShowDevicesDialog")
        ShowDevicesDialog.resize(585, 548)
        ShowDevicesDialog.setMinimumSize(QtCore.QSize(585, 548))
        ShowDevicesDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label = QtWidgets.QLabel(ShowDevicesDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName("label")
        self.combo_box_entities = QtWidgets.QComboBox(ShowDevicesDialog)
        self.combo_box_entities.setGeometry(QtCore.QRect(100, 10, 471, 22))
        self.combo_box_entities.setObjectName("combo_box_entities")
        self.label_2 = QtWidgets.QLabel(ShowDevicesDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.list_widget_devices = QtWidgets.QListWidget(ShowDevicesDialog)
        self.list_widget_devices.setGeometry(QtCore.QRect(100, 40, 471, 151))
        self.list_widget_devices.setObjectName("list_widget_devices")
        self.text_edit_device_properties = QtWidgets.QTextEdit(ShowDevicesDialog)
        self.text_edit_device_properties.setGeometry(QtCore.QRect(100, 200, 471, 301))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.text_edit_device_properties.setFont(font)
        self.text_edit_device_properties.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_device_properties.setReadOnly(True)
        self.text_edit_device_properties.setObjectName("text_edit_device_properties")
        self.button_add_device = QtWidgets.QPushButton(ShowDevicesDialog)
        self.button_add_device.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.button_add_device.setObjectName("button_add_device")
        self.button_ok = QtWidgets.QPushButton(ShowDevicesDialog)
        self.button_ok.setGeometry(QtCore.QRect(495, 510, 75, 23))
        self.button_ok.setObjectName("button_ok")
        self.button_delete_device = QtWidgets.QPushButton(ShowDevicesDialog)
        self.button_delete_device.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.button_delete_device.setObjectName("button_delete_device")

        self.retranslateUi(ShowDevicesDialog)
        QtCore.QMetaObject.connectSlotsByName(ShowDevicesDialog)

    def retranslateUi(self, ShowDevicesDialog):
        _translate = QtCore.QCoreApplication.translate
        ShowDevicesDialog.setWindowTitle(_translate("ShowDevicesDialog", "Devices"))
        self.label.setText(_translate("ShowDevicesDialog", "Entity"))
        self.label_2.setText(_translate("ShowDevicesDialog", "Devices"))
        self.button_add_device.setText(_translate("ShowDevicesDialog", "Add"))
        self.button_ok.setText(_translate("ShowDevicesDialog", "Ok"))
        self.button_delete_device.setText(_translate("ShowDevicesDialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowDevicesDialog = QtWidgets.QDialog()
    ui = Ui_ShowDevicesDialog()
    ui.setupUi(ShowDevicesDialog)
    ShowDevicesDialog.show()
    sys.exit(app.exec_())
