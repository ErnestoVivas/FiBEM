# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\fiware_config_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FiwareConfigDialog(object):
    def setupUi(self, FiwareConfigDialog):
        FiwareConfigDialog.setObjectName("FiwareConfigDialog")
        FiwareConfigDialog.resize(495, 301)
        FiwareConfigDialog.setMinimumSize(QtCore.QSize(495, 301))
        FiwareConfigDialog.setMaximumSize(QtCore.QSize(495, 301))
        self.label = QtWidgets.QLabel(FiwareConfigDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(FiwareConfigDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FiwareConfigDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 111, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FiwareConfigDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FiwareConfigDialog)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 111, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FiwareConfigDialog)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 111, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(FiwareConfigDialog)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 111, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(FiwareConfigDialog)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 111, 21))
        self.label_9.setObjectName("label_9")
        self.line_edit_url = QtWidgets.QLineEdit(FiwareConfigDialog)
        self.line_edit_url.setGeometry(QtCore.QRect(150, 40, 331, 21))
        self.line_edit_url.setObjectName("line_edit_url")
        self.line_edit_api_key = QtWidgets.QLineEdit(FiwareConfigDialog)
        self.line_edit_api_key.setGeometry(QtCore.QRect(150, 130, 251, 21))
        self.line_edit_api_key.setObjectName("line_edit_api_key")
        self.line_edit_fiware_service = QtWidgets.QLineEdit(FiwareConfigDialog)
        self.line_edit_fiware_service.setGeometry(QtCore.QRect(150, 70, 331, 21))
        self.line_edit_fiware_service.setObjectName("line_edit_fiware_service")
        self.line_edit_fiware_service_path = QtWidgets.QLineEdit(FiwareConfigDialog)
        self.line_edit_fiware_service_path.setGeometry(QtCore.QRect(150, 100, 331, 21))
        self.line_edit_fiware_service_path.setObjectName("line_edit_fiware_service_path")
        self.combo_box_time_zone = QtWidgets.QComboBox(FiwareConfigDialog)
        self.combo_box_time_zone.setGeometry(QtCore.QRect(150, 160, 251, 21))
        self.combo_box_time_zone.setObjectName("combo_box_time_zone")
        self.line_edit_mqtt_topics_file = QtWidgets.QLineEdit(FiwareConfigDialog)
        self.line_edit_mqtt_topics_file.setGeometry(QtCore.QRect(150, 190, 251, 21))
        self.line_edit_mqtt_topics_file.setObjectName("line_edit_mqtt_topics_file")
        self.button_open_mqtt_topics_file = QtWidgets.QPushButton(FiwareConfigDialog)
        self.button_open_mqtt_topics_file.setGeometry(QtCore.QRect(410, 190, 71, 21))
        self.button_open_mqtt_topics_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_open_mqtt_topics_file.setObjectName("button_open_mqtt_topics_file")
        self.line_edit_grafana_config_file = QtWidgets.QLineEdit(FiwareConfigDialog)
        self.line_edit_grafana_config_file.setGeometry(QtCore.QRect(150, 220, 251, 21))
        self.line_edit_grafana_config_file.setObjectName("line_edit_grafana_config_file")
        self.button_open_grafana_config_file = QtWidgets.QPushButton(FiwareConfigDialog)
        self.button_open_grafana_config_file.setGeometry(QtCore.QRect(410, 220, 71, 21))
        self.button_open_grafana_config_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_open_grafana_config_file.setObjectName("button_open_grafana_config_file")
        self.button_ok = QtWidgets.QPushButton(FiwareConfigDialog)
        self.button_ok.setGeometry(QtCore.QRect(325, 260, 75, 23))
        self.button_ok.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(FiwareConfigDialog)
        self.button_cancel.setGeometry(QtCore.QRect(405, 260, 75, 23))
        self.button_cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_cancel.setObjectName("button_cancel")
        self.button_random_api_key = QtWidgets.QPushButton(FiwareConfigDialog)
        self.button_random_api_key.setGeometry(QtCore.QRect(410, 130, 71, 21))
        self.button_random_api_key.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_random_api_key.setObjectName("button_random_api_key")

        self.retranslateUi(FiwareConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(FiwareConfigDialog)

    def retranslateUi(self, FiwareConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        FiwareConfigDialog.setWindowTitle(_translate("FiwareConfigDialog", "Post Entities to FIWARE"))
        self.label.setText(_translate("FiwareConfigDialog", "Enter FIWARE connection parameters:"))
        self.label_3.setText(_translate("FiwareConfigDialog", "URL"))
        self.label_4.setText(_translate("FiwareConfigDialog", "API key"))
        self.label_5.setText(_translate("FiwareConfigDialog", "FIWARE service"))
        self.label_6.setText(_translate("FiwareConfigDialog", "FIWARE service path"))
        self.label_7.setText(_translate("FiwareConfigDialog", "Time zone"))
        self.label_8.setText(_translate("FiwareConfigDialog", "MQTT topics file"))
        self.label_9.setText(_translate("FiwareConfigDialog", "Grafana config file"))
        self.button_open_mqtt_topics_file.setText(_translate("FiwareConfigDialog", "open"))
        self.button_open_grafana_config_file.setText(_translate("FiwareConfigDialog", "open"))
        self.button_ok.setText(_translate("FiwareConfigDialog", "Ok"))
        self.button_cancel.setText(_translate("FiwareConfigDialog", "Cancel"))
        self.button_random_api_key.setText(_translate("FiwareConfigDialog", "random"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FiwareConfigDialog = QtWidgets.QDialog()
    ui = Ui_FiwareConfigDialog()
    ui.setupUi(FiwareConfigDialog)
    FiwareConfigDialog.show()
    sys.exit(app.exec_())
