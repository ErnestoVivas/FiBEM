
'''
    This class handles the main window of FiBEM and all its respective
    functions. The objective is to create a building energy system consisting of
    a set of entities and relationships. The logic of the BES itself is handled
    in the class "building_energy_system" and is an attribute of MainWindow.
'''

from startup_dialog import StartupDialog
from add_entity_dialog import AddEntityDialog
from add_relationship_dialog import AddRelationshipDialog
from fiware_config_dialog import FiwareConfigDialog

from building_energy_system import BuildingEnergySystem

from gui import mainwindow_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        # setup window
        super().__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("FiBEM - The Fiware Building Entities Manager")

        # sub windows and dialogs
        self.startup_dialog = None
        self.add_entity_dialog = None
        self.add_relationship_dialog = None
        self.fiware_config_dialog = None

        # connect buttons to their respective functions
        self.ui.button_add_entity.clicked.connect(self.add_entity)
        self.ui.button_delete_entity.clicked.connect(self.delete_entity)
        self.ui.button_add_relationship.clicked.connect(self.add_relationship)
        self.ui.button_delete_relationship.clicked.connect(self.delete_relationship)
        self.ui.button_push_to_fiware.clicked.connect(self.push_to_fiware)

        # init bes
        self.building_energy_system = None
        self.startup_dialog = StartupDialog()
        self.startup_dialog.bes_id_set.connect(self.init_bes)
        self.startup_dialog.setWindowModality(Qt.ApplicationModal)
        self.startup_dialog.show()


    def init_bes(self, bes_id):
        self.building_energy_system = BuildingEnergySystem(bes_id)
        self.display_bes()


    def display_bes(self):
        self.ui.list_widget_entities.clear()
        self.ui.list_widget_relationships.clear()
        for entity in self.building_energy_system.entities:
            entity_data = [entity.base_attributes["type"], entity.base_attributes["id"]]
            entity_data_str = "{: <24} {: <20}".format(*entity_data)
            self.ui.list_widget_entities.addItem(QListWidgetItem(entity_data_str))
        for relationship in self.building_energy_system.relationships:
            first_entity = self.building_energy_system.entities[relationship["first_entity"]].short_id
            ref_entity = self.building_energy_system.entities[relationship["ref_entity"]].short_id
            rel_type = relationship["relationship_type"]
            rel_str = first_entity + " " + rel_type + " " + ref_entity
            self.ui.list_widget_relationships.addItem(QListWidgetItem(rel_str))

    def add_entity_to_bes(self, chosen_entity, entity_id):
        self.building_energy_system.add_entity(chosen_entity, entity_id)
        self.display_bes()


    def add_entity(self):
        self.add_entity_dialog = AddEntityDialog(self.building_energy_system)
        self.add_entity_dialog.chosen_entity.connect(self.add_entity_to_bes)
        self.add_entity_dialog.setWindowModality(Qt.ApplicationModal)
        self.add_entity_dialog.show()


    def delete_entity(self):

        # the list of entities in the guy corresponds to the order entities are
        # stored on the 'building_energy_system' object

        current_entity_index = self.ui.list_widget_entities.currentRow()
        if current_entity_index < 0:
            no_item_selected_message_box = QMessageBox()
            no_item_selected_message_box.setIcon(QMessageBox.Warning)
            no_item_selected_message_box.setText("Can not delete entity: No entity has been selected.")
            no_item_selected_message_box.setWindowTitle("No entity selected")
            no_item_selected_message_box.setStandardButtons(QMessageBox.Ok)
            answer = no_item_selected_message_box.exec()
            return
        else:
            self.building_energy_system.delete_entity(current_entity_index)     # deletes all connected relationships too
            self.display_bes()


    def delete_relationship(self):
        current_relationship_index = self.ui.list_widget_relationships.currentRow()
        if current_relationship_index < 0:
            no_item_selected_message_box = QMessageBox()
            no_item_selected_message_box.setIcon(QMessageBox.Warning)
            no_item_selected_message_box.setText("Can not delete relationship: No relationship has been selected.")
            no_item_selected_message_box.setWindowTitle("No relationship selected")
            no_item_selected_message_box.setStandardButtons(QMessageBox.Ok)
            answer = no_item_selected_message_box.exec()
            return
        else:
            self.building_energy_system.delete_relationship(current_relationship_index)
            self.display_bes()


    def add_relationship_to_bes(self, first_entity, ref_entity, relationship_type):
        self.building_energy_system.add_relationship(first_entity, ref_entity, relationship_type)
        self.display_bes()


    def add_relationship(self):
        self.add_relationship_dialog = AddRelationshipDialog(self.building_energy_system)
        self.add_relationship_dialog.new_relationship.connect(self.add_relationship_to_bes)
        self.add_relationship_dialog.setWindowModality(Qt.ApplicationModal)
        self.add_relationship_dialog.show()


    def push_to_fiware(self):
        self.fiware_config_dialog = FiwareConfigDialog(self.building_energy_system)
        self.fiware_config_dialog.setWindowModality(Qt.ApplicationModal)
        self.fiware_config_dialog.show()
