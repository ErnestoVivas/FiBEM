
'''
This class handles the main window of FiBEM and all its respective
functions. The objective is to create a building energy system consisting of
a set of entities and relationships. The logic of the BES itself is handled
in the class "building_energy_system" and is an attribute of MainWindow.
'''

from sys import platform

from startup_dialog import StartupDialog
from parse_fmu_dialog import ParseFmuDialog
from add_entity_dialog import AddEntityDialog
from show_devices_dialog import ShowDevicesDialog
from add_relationship_dialog import AddRelationshipDialog
from fiware_config_dialog import FiwareConfigDialog

from building_energy_system import BuildingEnergySystem
from bes_entities import ontology_strings

from gui import mainwindow_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox, QFileDialog


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        # setup window
        super().__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("FiBEM - The Fiware Building Entities Manager")

        # determine system type (important for fonts...)
        self.platform = "Windows"
        if (platform == "linux") or (platform == "linux2"):
            self.platform == "linux"
            self.ui.list_widget_entities.setFont(QFont("DejaVu Sans Mono"))
            self.ui.list_widget_relationships.setFont(QFont("DejaVu Sans Mono"))

        # sub windows and dialogs
        self.startup_dialog = None
        self.parse_fmu_dialog = None
        self.add_entity_dialog = None
        self.show_devices_dialog = None
        self.add_relationship_dialog = None
        self.fiware_config_dialog = None

        # connect buttons to their respective functions
        self.ui.button_add_entity.clicked.connect(self.add_entity)
        self.ui.button_delete_entity.clicked.connect(self.delete_entity)
        self.ui.button_parse_fmu.clicked.connect(self.parse_fmu)
        self.ui.button_devices.clicked.connect(self.show_devices)
        self.ui.button_add_relationship.clicked.connect(self.add_relationship)
        self.ui.button_get_relationships_auto.clicked.connect(self.get_relationships_auto)
        self.ui.button_delete_relationship.clicked.connect(self.delete_relationship)
        self.ui.button_delete_all_entities.clicked.connect(self.clear_all)
        self.ui.button_export_json.clicked.connect(self.export_json)
        self.ui.button_export_ontology.clicked.connect(self.export_ontology)
        self.ui.button_push_to_fiware.clicked.connect(self.push_to_fiware)

        # connect menu items to functions
        self.ui.menu_file_action_new.triggered.connect(self.make_new_bes)
        self.ui.menu_file_action_open.triggered.connect(self.import_bes)
        self.ui.menu_file_action_save.triggered.connect(self.bes_save)
        self.ui.menu_file_action_save_as.triggered.connect(self.bes_save_as)
        self.ui.menu_file_action_export_json.triggered.connect(self.export_json)
        self.ui.menu_file_action_export_ontology.triggered.connect(self.export_ontology)
        self.ui.menu_file_action_post_to_fiware.triggered.connect(self.push_to_fiware)
        self.ui.menu_file_action_quit.triggered.connect(self.exit_application)

        self.ui.menu_edit_action_parse_fmu.triggered.connect(self.parse_fmu)
        self.ui.menu_edit_action_add_entity.triggered.connect(self.add_entity)
        self.ui.menu_edit_action_add_relationship.triggered.connect(self.add_relationship)
        self.ui.menu_edit_action_get_relationships_auto.triggered.connect(self.get_relationships_auto)
        self.ui.menu_edit_action_devices.triggered.connect(self.show_devices)
        self.ui.menu_edit_action_delete_entity.triggered.connect(self.delete_entity)
        self.ui.menu_edit_action_delete_relationship.triggered.connect(self.delete_relationship)
        self.ui.menu_edit_action_clear_all.triggered.connect(self.clear_all)


        # init bes
        self.bes_save_file_name = ""
        self.building_energy_system = None
        self.startup_dialog = StartupDialog()
        self.startup_dialog.bes_id_set.connect(self.init_bes)
        self.startup_dialog.setWindowModality(Qt.ApplicationModal)
        self.startup_dialog.show()


    def make_new_bes(self):
        self.startup_dialog = StartupDialog()
        self.startup_dialog.bes_id_set.connect(self.reset_bes)
        self.startup_dialog.setWindowModality(Qt.ApplicationModal)
        self.startup_dialog.show()


    def init_bes(self, bes_id):
        self.building_energy_system = BuildingEnergySystem(bes_id)
        self.display_bes()


    def reset_bes(self, new_bes_id):
        self.building_energy_system.reset_bes_new_id(new_bes_id)
        self.display_bes()


    def import_bes(self):
        import_file_name, check = QFileDialog.getOpenFileName(self, "Import", "", "Config file (*.cfg)")
        if check:
            with open(import_file_name, "r") as import_file:
                imported_bes = import_file.readlines()
                i = 0
                for line in imported_bes:
                    line = line.rstrip("\n")
                    if (i == 0) and (not(line == "# FiBEM save file")):
                        print("got here")
                        return

                    splitted_line = line.split(" ")
                    if i == 1:
                        new_bes_id = splitted_line[2]
                        self.reset_bes(new_bes_id)
                    else:
                        type = splitted_line[0]
                        if type == "#Entity":
                            entity_type = splitted_line[1]
                            entity_id = splitted_line[2]
                            entity_type_numeric = ontology_strings.entity_value_from_string[entity_type]
                            self.add_entity_to_bes(entity_type_numeric, entity_id)
                        elif type == "#Relationship":
                            first_entity = int(splitted_line[1])
                            ref_entity = int(splitted_line[2])
                            relationship_type = splitted_line[3]
                            self.add_relationship_to_bes(first_entity, ref_entity, relationship_type)
                    i += 1


    def parse_fmu(self):
        fmu_file_name, check = QFileDialog.getOpenFileName(self, "Open FMU file", "", "FMU file (*.fmu)")
        if check:
            self.parse_fmu_dialog = ParseFmuDialog(fmu_file_name)
            self.parse_fmu_dialog.parsed_entities.connect(self.set_entities_from_fmu)
            self.parse_fmu_dialog.setWindowModality(Qt.ApplicationModal)
            self.parse_fmu_dialog.show()


    def set_entities_from_fmu(self, new_bes_id, parsed_entities):
        self.reset_bes(f"urn:ngsi-ld:{new_bes_id}")
        parsed_entities = parsed_entities.split(" ")
        for entity in parsed_entities:
            current_entity_count = self.building_energy_system.get_entity_count(int(entity))
            entity_type_str, entity_def = ontology_strings.get_entity_strings(int(entity))
            entity_type_no_prefix = ontology_strings.strip_prefix(entity_type_str)
            entity_id = f"urn:ngsi-ld:{new_bes_id}:{entity_type_no_prefix}:{str(current_entity_count + 1).zfill(3)}"
            self.building_energy_system.add_entity(int(entity), entity_id)
        self.building_energy_system.set_relationships_automatically()
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
            rel_str = f"{first_entity} {rel_type} {ref_entity}"
            self.ui.list_widget_relationships.addItem(QListWidgetItem(rel_str))


    def show_devices(self):
        selected_entity = self.ui.list_widget_entities.currentRow()
        self.show_devices_dialog = ShowDevicesDialog(self.building_energy_system, selected_entity)
        #self.show_devices_dialog.chosen_entity.connect(self.add_entity_to_bes)
        self.show_devices_dialog.setWindowModality(Qt.ApplicationModal)
        self.show_devices_dialog.show()

    def write_bes_to_file(self, save_file_name):
        save_file_text = "# FiBEM save file"
        entity_count = self.ui.list_widget_entities.count()

        # add entities to save file
        for i in range(entity_count):
            item_strings = self.ui.list_widget_entities.item(i).text().split(" ")
            current_entity_type = item_strings[0]
            current_entity_id = item_strings[-1]
            save_file_text = f"{save_file_text}\n#Entity {current_entity_type} {current_entity_id}"
        # add relationships to save file
        for relationship in self.building_energy_system.relationships:
            first_entity = str(relationship["first_entity"])
            ref_entity = str(relationship["ref_entity"])
            relationship_type = str(relationship["relationship_type"])
            save_file_text = f"{save_file_text}\n#Relationship {first_entity} {ref_entity} {relationship_type}"

        # write save file
        with open(save_file_name, "w") as save_file:
            save_file.write(save_file_text)


    def bes_save(self):
        if self.bes_save_file_name:
            self.write_bes_to_file(self.bes_save_file_name)
        else:
            self.bes_save_as()


    def bes_save_as(self):
        save_file_name, check = QFileDialog.getSaveFileName(self, "Save Building Energy System", "", "Config file (*.cfg)")
        if check:
            self.bes_save_file_name = save_file_name
            self.write_bes_to_file(save_file_name)


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
        if current_entity_index == 0:
            no_item_selected_message_box = QMessageBox()
            no_item_selected_message_box.setIcon(QMessageBox.Information)
            no_item_selected_message_box.setText("Root entity can not be deleted.\n")
            no_item_selected_message_box.setWindowTitle("Can not delete root entity")
            no_item_selected_message_box.setStandardButtons(QMessageBox.Ok)
            answer = no_item_selected_message_box.exec()
            return
        elif current_entity_index < 1:
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


    def clear_all(self):
        self.building_energy_system.reset_bes()
        self.display_bes()


    def add_relationship_to_bes(self, first_entity, ref_entity, relationship_type):
        self.building_energy_system.add_relationship(first_entity, ref_entity, relationship_type)
        self.display_bes()


    def add_relationship(self):
        self.add_relationship_dialog = AddRelationshipDialog(self.building_energy_system)
        self.add_relationship_dialog.new_relationship.connect(self.add_relationship_to_bes)
        self.add_relationship_dialog.setWindowModality(Qt.ApplicationModal)
        self.add_relationship_dialog.show()


    def get_relationships_auto(self):
        get_rel_auto_message_box = QMessageBox()
        get_rel_auto_message_box.setIcon(QMessageBox.Information)
        get_rel_auto_message_box.setText(("This function will try to set the relationships between the\n"
                                          "given entities automatically. Previously set relationships\n"
                                          "will be removed. You can add or delete relationships after this\n"
                                          "operation."))
        get_rel_auto_message_box.setWindowTitle("Get Relationships Automatically")
        get_rel_auto_message_box.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        answer = get_rel_auto_message_box.exec()
        if answer == QMessageBox.Ok:
            self.building_energy_system.set_relationships_automatically()
            self.display_bes()


    def export_json(self):
        json_file_name, check = QFileDialog.getSaveFileName(self, "Export JSON", "", "JSON File (*.json)")
        if check:
            self.building_energy_system.print_json(json_file_name)


    def export_ontology(self):
        ontology_file_name, check = QFileDialog.getSaveFileName(self, "Export Ontology", "", "TTL File (*.ttl)")
        if check:
            self.building_energy_system.print_ontology(ontology_file_name)


    def push_to_fiware(self):
        self.fiware_config_dialog = FiwareConfigDialog(self.building_energy_system)
        self.fiware_config_dialog.setWindowModality(Qt.ApplicationModal)
        self.fiware_config_dialog.show()


    def exit_application(self):
        exit_message_box = QMessageBox()
        exit_message_box.setIcon(QMessageBox.Information)
        exit_message_box.setText("Do you really want to quit?")
        exit_message_box.setWindowTitle("Quit Application")
        exit_message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        answer = exit_message_box.exec()
        if answer == QMessageBox.Ok:
            self.close()
