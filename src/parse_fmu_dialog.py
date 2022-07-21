from gui import parse_fmu_dialog_ui

from PyQt5 import QtCore, QtWidgets

from fmpy import *
from fmpy.util import plot_result, fmu_info


class ParseFmuDialog(QtWidgets.QDialog):

    def __init__(self, opened_fmu_file_name, platform):

        # setup window
        super().__init__()
        self.ui = parse_fmu_dialog_ui.Ui_ParseFmuDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        if (platform == "linux") or (platform == "linux2"):
            self.ui.text_edit_fmu_info.setFont(QFont("DejaVu Sans Mono"))
            self.ui.text_edit_entities_and_relationships.setFont(QFont("DejaVu Sans Mono"))
        self.fmu_entities = []
        self.fmu_relationships = []

        # display fmu information
        self.fmu_file_name = opened_fmu_file_name
        self.fmu_file_info = fmu_info(opened_fmu_file_name)
        self.fmu_file_model_description = read_model_description(opened_fmu_file_name)
        self.parse_fmu()
        self.ui.text_edit_fmu_info.setText(self.fmu_file_info)

        # connect buttons to functions
        self.ui.button_cancel.clicked.connect(self.cancel_parse_fmu)
        self.ui.button_ok.clicked.connect(self.import_entities_from_fmu)


    def parse_fmu(self):
        pass


    def cancel_parse_fmu(self):
        self.close()


    def import_entities_from_fmu(self):
        self.close()
