# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_entity_dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEntityDialog(object):
    def setupUi(self, AddEntityDialog):
        AddEntityDialog.setObjectName("AddEntityDialog")
        AddEntityDialog.resize(375, 238)
        self.label = QtWidgets.QLabel(AddEntityDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddEntityDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddEntityDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.label_3.setObjectName("label_3")
        self.combo_box_choose_entity = QtWidgets.QComboBox(AddEntityDialog)
        self.combo_box_choose_entity.setGeometry(QtCore.QRect(100, 20, 261, 21))
        self.combo_box_choose_entity.setObjectName("combo_box_choose_entity")
        self.line_edit_set_id = QtWidgets.QLineEdit(AddEntityDialog)
        self.line_edit_set_id.setGeometry(QtCore.QRect(100, 50, 261, 21))
        self.line_edit_set_id.setObjectName("line_edit_set_id")
        self.line_edit_brick_type = QtWidgets.QLineEdit(AddEntityDialog)
        self.line_edit_brick_type.setGeometry(QtCore.QRect(100, 80, 261, 21))
        self.line_edit_brick_type.setAutoFillBackground(True)
        self.line_edit_brick_type.setReadOnly(True)
        self.line_edit_brick_type.setObjectName("line_edit_brick_type")
        self.plain_text_edit_brick_definition = QtWidgets.QPlainTextEdit(AddEntityDialog)
        self.plain_text_edit_brick_definition.setGeometry(QtCore.QRect(100, 110, 261, 81))
        self.plain_text_edit_brick_definition.setReadOnly(True)
        self.plain_text_edit_brick_definition.setBackgroundVisible(True)
        self.plain_text_edit_brick_definition.setObjectName("plain_text_edit_brick_definition")
        self.label_4 = QtWidgets.QLabel(AddEntityDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.label_4.setObjectName("label_4")
        self.button_add_entity = QtWidgets.QPushButton(AddEntityDialog)
        self.button_add_entity.setGeometry(QtCore.QRect(210, 200, 75, 23))
        self.button_add_entity.setObjectName("button_add_entity")
        self.button_cancel = QtWidgets.QPushButton(AddEntityDialog)
        self.button_cancel.setGeometry(QtCore.QRect(290, 200, 75, 23))
        self.button_cancel.setObjectName("button_cancel")

        self.retranslateUi(AddEntityDialog)
        QtCore.QMetaObject.connectSlotsByName(AddEntityDialog)

    def retranslateUi(self, AddEntityDialog):
        _translate = QtCore.QCoreApplication.translate
        AddEntityDialog.setWindowTitle(_translate("AddEntityDialog", "Add Entity"))
        self.label.setText(_translate("AddEntityDialog", "Entity"))
        self.label_2.setText(_translate("AddEntityDialog", "Id"))
        self.label_3.setText(_translate("AddEntityDialog", "Brick type"))
        self.label_4.setText(_translate("AddEntityDialog", "Brick definition"))
        self.button_add_entity.setText(_translate("AddEntityDialog", "Add"))
        self.button_cancel.setText(_translate("AddEntityDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddEntityDialog = QtWidgets.QDialog()
    ui = Ui_AddEntityDialog()
    ui.setupUi(AddEntityDialog)
    AddEntityDialog.show()
    sys.exit(app.exec_())