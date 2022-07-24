from gui import parse_fmu_dialog_ui

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal

from fmpy import *
from fmpy.util import plot_result, fmu_info


class ParseFmuDialog(QtWidgets.QDialog):

    parsed_entities = pyqtSignal(str, str)
    #parsed_entities = pyqtSignal(str, List[int])

    def __init__(self, opened_fmu_file_name, platform):

        # setup window
        super().__init__()
        self.ui = parse_fmu_dialog_ui.Ui_ParseFmuDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        if (platform == "linux") or (platform == "linux2"):
            self.ui.text_edit_fmu_info.setFont(QFont("DejaVu Sans Mono"))
            self.ui.text_edit_entities_and_relationships.setFont(QFont("DejaVu Sans Mono"))
        self.system_type = -1
        self.system_name = ""
        self.fmu_model_variables = {}
        self.fmu_entities = ""

        # possible system types
        self.system_type_key_words = {
            0: ["heat", "pump"],
            1: ["electric", "boiler"],
            2: ["gas", "boiler"],
            3: ["cogeneration"],
            4: ["heat", "exchange"],
            5: ["pvt"],
            6: ["pv"],
            7: ["solar", "thermal"],
            8: ["hydraulic"],
            9: ["hydraulik"]
        }

        # standard entities for corresponding system types
        self.standard_system_entities = {
            0: "14 0 8 12 18 17 19",
            1: "14 16 1 9 18",
            2: "14 2 12 18 17 19",
            3: "14 15 3 8 12 18 17 19",
            4: "14 8 12 18 17 19",
            5: "14 15 6 8 12 18 17 19",
            6: "15 5 13 18 19",
            7: "14 7 8 12 18 17 19",
            8: "18 16 9 9 10 10 11 11",
            9: "18 16 9 9 10 10 11 11"
        }

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
        self.get_system_type(self.fmu_file_model_description.modelName)
        self.add_entities()

        for variable in self.fmu_file_model_description.modelVariables:
            self.fmu_model_variables[variable.name] = variable.valueReference
        #inputs = self.fmu_model_variables["input"]
        #outputs = self.fmu_model_variables['output']
        #for input in inputs:
        #    print(input)
        #for output in outputs:
        #    print(output)


    def get_system_type(self, model_name):
        #print(model_name)
        self.system_name = model_name.split('.')[-1]
        #print(short_model_name)
        for key in self.system_type_key_words:
            if all(x in model_name.lower() for x in self.system_type_key_words[key]):
                self.system_type = key
                break


    def add_entities(self):
        if self.system_type >= 0:
            self.fmu_entities = self.standard_system_entities[self.system_type]


    def cancel_parse_fmu(self):
        self.close()


    def import_entities_from_fmu(self):
        if self.system_type >= 0:
            self.parsed_entities.emit(self.system_name, self.fmu_entities)
        self.close()
