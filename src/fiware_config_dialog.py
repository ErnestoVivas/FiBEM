import random
import string
import json
from pathlib import Path

from gui import fiware_config_dialog_ui

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from filip.models.ngsi_v2.context import ContextEntity
from filip.models.ngsi_v2.iot import Device
from filip.clients.ngsi_v2.cb import ContextBrokerClient
from filip.clients.ngsi_v2.iota import IoTAClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import ServiceGroup


class FiwareConfigDialog(QtWidgets.QDialog):

    def __init__(self, new_bes):

        # setup window
        super().__init__()
        self.ui = fiware_config_dialog_ui.Ui_FiwareConfigDialog()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # set values in line edits
        bes_short_id = new_bes.id.split(":")[-1]
        random_api_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        home_dir = Path.home()
        default_mqtt_topics_path = Path.joinpath(home_dir, str(bes_short_id + "_mqtt_topics.csv"))
        default_grafana_config_path = Path.joinpath(home_dir, str(bes_short_id + "_grafana.json"))
        self.ui.line_edit_url.setText("http://localhost")
        self.ui.line_edit_fiware_service.setText("openiot")
        self.ui.line_edit_fiware_service_path.setText("/" + bes_short_id)
        self.ui.line_edit_api_key.setText(random_api_key)
        self.ui.line_edit_mqtt_topics_file.setText(str(default_mqtt_topics_path))
        self.ui.line_edit_grafana_config_file.setText(str(default_grafana_config_path))
        self.setup_time_zones()

        # set building energy system
        self.building_energy_system = new_bes

        # connect button functions
        self.ui.button_ok.clicked.connect(self.push_to_fiware)
        self.ui.button_cancel.clicked.connect(self.cancel_push_to_fiware)
        self.ui.button_random_api_key.clicked.connect(self.generate_random_api_key)


    def push_to_fiware(self):

        # right now: testing

        # paramters:
        fw_url = self.ui.line_edit_url.text()
        fw_service = self.ui.line_edit_fiware_service.text()
        fw_service_path = self.ui.line_edit_fiware_service_path.text()
        fw_apikey = self.ui.line_edit_api_key.text()
        fw_header = FiwareHeader(service = fw_service, service_path = fw_service_path)

        # post the entity
        try:

            # post entities
            with ContextBrokerClient(url = fw_url + ":1026", fiware_header = fw_header) as client:
                for entity in self.building_energy_system.entities:
                    print(json.dumps(entity.base_attributes, indent=2))
                    client.post_entity(entity = ContextEntity(**(entity.base_attributes)))

            # post devices (do this later)
            #with IoTAClient(url = fw_url + ":4041", fiware_header = fw_header) as iota_client:
            #    for entity in self.building_energy_system.entities:
            #        for device in entity.devices:
            #            iota_client.post_device(device = Device(**device))

            post_successful_msg = QMessageBox()
            post_successful_msg.setIcon(QMessageBox.Information)
            post_successful_msg.setText("The entities have been posted to FIWARE")
            post_successful_msg.setWindowTitle("Post successul")
            post_successful_msg.exec_()
        except:
            fiware_connection_error_msg = QMessageBox()
            fiware_connection_error_msg.setIcon(QMessageBox.Critical)
            fiware_connection_error_msg.setText("Connection Refused")
            fiware_connection_error_msg.setInformativeText("Could not connect to FIWARE")
            fiware_connection_error_msg.setWindowTitle("Error")
            fiware_connection_error_msg.exec_()

        self.close()


    def generate_random_api_key(self):
        random_api_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.ui.line_edit_api_key.setText(random_api_key)


    def cancel_push_to_fiware(self):
        self.close()


    def setup_time_zones(self):
        self.ui.combo_box_time_zone.addItem("Pacific/Kiritimati")
        self.ui.combo_box_time_zone.addItem("Pacific/Apia")
        self.ui.combo_box_time_zone.addItem("Pacific/Chatham")
        self.ui.combo_box_time_zone.addItem("Pacific/Auckland")
        self.ui.combo_box_time_zone.addItem("Pacific/Bougainville")
        self.ui.combo_box_time_zone.addItem("Australia/Lord_Howe")
        self.ui.combo_box_time_zone.addItem("Australia/Sydney")
        self.ui.combo_box_time_zone.addItem("Australia/Darwin")
        self.ui.combo_box_time_zone.addItem("Asia/Seoul")
        self.ui.combo_box_time_zone.addItem("Australia/Eucla")
        self.ui.combo_box_time_zone.addItem("Asia/Hong_Kong")
        self.ui.combo_box_time_zone.addItem("Asia/Bangkok")
        self.ui.combo_box_time_zone.addItem("Asia/Yangon")
        self.ui.combo_box_time_zone.addItem("Asia/Dhaka")
        self.ui.combo_box_time_zone.addItem("Asia/Kathmandu")
        self.ui.combo_box_time_zone.addItem("Asia/Colombo")
        self.ui.combo_box_time_zone.addItem("Indian/Maldives")
        self.ui.combo_box_time_zone.addItem("Asia/Kabul")
        self.ui.combo_box_time_zone.addItem("Asia/Dubai")
        self.ui.combo_box_time_zone.addItem("Asia/Tehran")
        self.ui.combo_box_time_zone.addItem("Europe/Moscow")
        self.ui.combo_box_time_zone.addItem("Africa/Addis_Ababa")
        self.ui.combo_box_time_zone.addItem("Europe/Athens")
        self.ui.combo_box_time_zone.addItem("Africa/Johannesburg")
        self.ui.combo_box_time_zone.addItem("Europe/Berlin")
        self.ui.combo_box_time_zone.addItem("Europe/Madrid")
        self.ui.combo_box_time_zone.addItem("Africa/Lagos")
        self.ui.combo_box_time_zone.addItem("Europe/London")
        self.ui.combo_box_time_zone.addItem("Africa/Accra")
        self.ui.combo_box_time_zone.addItem("Atlantic/Azores")
        self.ui.combo_box_time_zone.addItem("America/Noronha")
        self.ui.combo_box_time_zone.addItem("America/Sao_Paulo")
        self.ui.combo_box_time_zone.addItem("America/Argentina/Buenos_Aires")
        self.ui.combo_box_time_zone.addItem("America/Caracas")
        self.ui.combo_box_time_zone.addItem("America/New_York")
        self.ui.combo_box_time_zone.addItem("America/Managua")
        self.ui.combo_box_time_zone.addItem("America/Mexico_City")
        self.ui.combo_box_time_zone.addItem("America/Phoenix")
        self.ui.combo_box_time_zone.addItem("America/Los_Angeles")
        self.ui.combo_box_time_zone.addItem("Pacific/Anchorage")
        self.ui.combo_box_time_zone.addItem("Pacific/Marquesas")
        self.ui.combo_box_time_zone.addItem("Pacific/Honolulu")
        self.ui.combo_box_time_zone.addItem("Pacific/Midway")
        self.ui.combo_box_time_zone.setCurrentIndex(24)
