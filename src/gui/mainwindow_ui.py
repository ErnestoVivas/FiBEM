# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 582)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.group_box_entities = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_entities.setMinimumSize(QtCore.QSize(120, 0))
        self.group_box_entities.setMaximumSize(QtCore.QSize(120, 16777215))
        self.group_box_entities.setSizeIncrement(QtCore.QSize(0, 0))
        self.group_box_entities.setAlignment(QtCore.Qt.AlignCenter)
        self.group_box_entities.setObjectName("group_box_entities")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.group_box_entities)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_add_entity = QtWidgets.QPushButton(self.group_box_entities)
        self.button_add_entity.setObjectName("button_add_entity")
        self.verticalLayout.addWidget(self.button_add_entity)
        self.button_parse_fmu = QtWidgets.QPushButton(self.group_box_entities)
        self.button_parse_fmu.setObjectName("button_parse_fmu")
        self.verticalLayout.addWidget(self.button_parse_fmu)
        self.button_edit_entity = QtWidgets.QPushButton(self.group_box_entities)
        self.button_edit_entity.setObjectName("button_edit_entity")
        self.verticalLayout.addWidget(self.button_edit_entity)
        self.button_delete_entity = QtWidgets.QPushButton(self.group_box_entities)
        self.button_delete_entity.setObjectName("button_delete_entity")
        self.verticalLayout.addWidget(self.button_delete_entity)
        self.button_delete_all_entities = QtWidgets.QPushButton(self.group_box_entities)
        self.button_delete_all_entities.setObjectName("button_delete_all_entities")
        self.verticalLayout.addWidget(self.button_delete_all_entities)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.group_box_entities, 0, 0, 1, 1)
        self.list_widget_entities = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_entities.setMinimumSize(QtCore.QSize(420, 0))
        self.list_widget_entities.setObjectName("list_widget_entities")
        self.gridLayout.addWidget(self.list_widget_entities, 0, 1, 1, 1)
        self.list_widget_relationships = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_relationships.setMinimumSize(QtCore.QSize(420, 0))
        self.list_widget_relationships.setObjectName("list_widget_relationships")
        self.gridLayout.addWidget(self.list_widget_relationships, 0, 2, 1, 1)
        self.group_box_relationships = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_relationships.setMinimumSize(QtCore.QSize(120, 0))
        self.group_box_relationships.setMaximumSize(QtCore.QSize(120, 16777215))
        self.group_box_relationships.setAlignment(QtCore.Qt.AlignCenter)
        self.group_box_relationships.setObjectName("group_box_relationships")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.group_box_relationships)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_add_relationship = QtWidgets.QPushButton(self.group_box_relationships)
        self.button_add_relationship.setObjectName("button_add_relationship")
        self.verticalLayout_2.addWidget(self.button_add_relationship)
        self.button_edit_relationship = QtWidgets.QPushButton(self.group_box_relationships)
        self.button_edit_relationship.setObjectName("button_edit_relationship")
        self.verticalLayout_2.addWidget(self.button_edit_relationship)
        self.button_delete_relationship = QtWidgets.QPushButton(self.group_box_relationships)
        self.button_delete_relationship.setObjectName("button_delete_relationship")
        self.verticalLayout_2.addWidget(self.button_delete_relationship)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.group_box_relationships, 0, 3, 1, 1)
        self.button_export_ontology = QtWidgets.QPushButton(self.centralwidget)
        self.button_export_ontology.setMinimumSize(QtCore.QSize(0, 30))
        self.button_export_ontology.setObjectName("button_export_ontology")
        self.gridLayout.addWidget(self.button_export_ontology, 1, 3, 1, 1)
        self.button_push_to_fiware = QtWidgets.QPushButton(self.centralwidget)
        self.button_push_to_fiware.setMinimumSize(QtCore.QSize(0, 30))
        self.button_push_to_fiware.setObjectName("button_push_to_fiware")
        self.gridLayout.addWidget(self.button_push_to_fiware, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_file_action_parse_fmu = QtWidgets.QAction(MainWindow)
        self.menu_file_action_parse_fmu.setObjectName("menu_file_action_parse_fmu")
        self.menu_file_action_quit = QtWidgets.QAction(MainWindow)
        self.menu_file_action_quit.setObjectName("menu_file_action_quit")
        self.menu_file.addAction(self.menu_file_action_parse_fmu)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_file_action_quit)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.group_box_entities.setTitle(_translate("MainWindow", "Entities"))
        self.button_add_entity.setText(_translate("MainWindow", "Add"))
        self.button_parse_fmu.setText(_translate("MainWindow", "Parse FMU"))
        self.button_edit_entity.setText(_translate("MainWindow", "Edit"))
        self.button_delete_entity.setText(_translate("MainWindow", "Delete"))
        self.button_delete_all_entities.setText(_translate("MainWindow", "Clear all"))
        self.group_box_relationships.setTitle(_translate("MainWindow", "Relationships"))
        self.button_add_relationship.setText(_translate("MainWindow", "Add"))
        self.button_edit_relationship.setText(_translate("MainWindow", "Edit"))
        self.button_delete_relationship.setText(_translate("MainWindow", "Delete"))
        self.button_export_ontology.setText(_translate("MainWindow", "Export Ontology"))
        self.button_push_to_fiware.setText(_translate("MainWindow", "Push to FIWARE"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_file_action_parse_fmu.setText(_translate("MainWindow", "Parse FMU model"))
        self.menu_file_action_quit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
