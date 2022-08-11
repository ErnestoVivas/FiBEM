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
        self.add_device(f"{self.short_id_ontology}_Condenser_Thermal_Power_Sensor",
                        f"{self.base_attributes['id']}:Condenser:Thermal_Power_Sensor",
                        "Thermal_Power_Sensor",
                        f"{ontology_strings.device_definitions['Thermal_Power_Sensor']}")
        self.add_device(f"{self.short_id_ontology}_Evaporator_Thermal_Power_Sensor",
                        f"{self.base_attributes['id']}:Evaporator:Thermal_Power_Sensor",
                        "Thermal_Power_Sensor",
                        f"{ontology_strings.device_definitions['Thermal_Power_Sensor']}")
        self.add_device(f"{self.short_id_ontology}_Compressor_Electrical_Power_Sensor",
                        f"{self.base_attributes['id']}:Compressor:Electrical_Power_Sensor",
                        "Electrical_Power_Sensor",
                        f"{ontology_strings.device_definitions['Electrical_Power_Sensor']}")
        self.add_device(f"{self.short_id_ontology}_Compressor_Command",
                        f"{self.base_attributes['id']}:Compressor:Command",
                        "Command",
                        f"{ontology_strings.device_definitions['Command']}")
        self.add_device(f"{self.short_id_ontology}_COP",
                        f"{self.base_attributes['id']}:COP",
                        "COP",
                        f"{ontology_strings.device_definitions['COP']}")


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a ebc:Heat_Pump;\n'
                         f'    skos:definition "{ontology_strings.heat_pump_definition}"')
        return ttl_file_text
