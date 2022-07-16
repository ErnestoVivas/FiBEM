from gui import add_relationship_dialog_ui

from PyQt5 import QtCore, QtWidgets

from building_energy_system import BuildingEnergySystem
from bes_entities import ontology_strings


class AddRelationshipDialog(QtWidgets.QDialog):

    def __init__(self, curr_bes):
        super().__init__()
        self.ui = add_relationship_dialog_ui.Ui_AddRelationshipDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.current_bes: BuildingEnergySystem = curr_bes
        self.setup_relationships_combo_box()
        self.setup_entities_combo_boxes()

        # connect gui elements to functions
        self.ui.combo_box_relationship_type.currentIndexChanged.connect(self.display_relationship_definition)
        self.ui.button_add_relationship.clicked.connect(self.add_relationship)
        self.ui.button_cancel.clicked.connect(self.cancel_add_relationship)


    def setup_entities_combo_boxes(self):
        for entity in self.current_bes.entities:
            self.ui.combo_box_first_entity.addItem(entity.base_attributes["id"])
            self.ui.combo_box_ref_entity.addItem(entity.base_attributes["id"])


    def setup_relationships_combo_box(self):
        self.ui.combo_box_relationship_type.addItem("feeds")
        self.ui.combo_box_relationship_type.addItem("hasLocation")
        self.ui.combo_box_relationship_type.addItem("hasPart")
        self.ui.combo_box_relationship_type.addItem("isFedBy")
        self.ui.combo_box_relationship_type.addItem("isLocationOf")
        self.ui.combo_box_relationship_type.addItem("isPartOf")
        self.ui.combo_box_relationship_type.addItem("isRegulatedBy")
        self.ui.combo_box_relationship_type.addItem("regulates")
        self.ui.combo_box_relationship_type.setCurrentIndex(0)
        self.display_relationship_definition()


    def display_relationship_definition(self):
        current_relationship = self.ui.combo_box_relationship_type.currentIndex()
        relationship_definition = ontology_strings.relationship_definition_by_value[str(current_relationship)]
        self.ui.text_edit_definition.setText(relationship_definition)

    def add_relationship(self):
        self.close()


    def cancel_add_relationship(self):
        self.close()
