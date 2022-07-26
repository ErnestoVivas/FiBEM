from bes_entities.base_entity import BaseEntity
from bes_entities import ontology_strings


class HeatPump(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["ontology"]["value"] = "Brick, extended by EBC"
        self.base_attributes["definition"]["value"] = ontology_strings.heat_pump_definition
        HeatPump.entity_count += 1


    @staticmethod
    def get_entity_count():
        return HeatPump.entity_count


    def setup_standard_devices(self):
        condenser_thermal_power_sensor = {
                "device_id": f"{self.short_id_ontology}_Condenser_Thermal_Power_Sensor",
                "entity_name": f"{self.base_attributes['id']}:Condenser:Thermal_Power_Sensor",
                "entity_type": "Thermal_Power_Sensor",
                "timezone": "Europe/Berlin",     # default value, can be set by user
                "protocol": "IoTA-JSON",
                "transport": "MQTT"
        }
        self.devices.append(condenser_thermal_power_sensor)


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a ebc:Heat_Pump;\n'
                         f'    skos:definition "{ontology_strings.heat_pump_definition}"')
        return ttl_file_text
