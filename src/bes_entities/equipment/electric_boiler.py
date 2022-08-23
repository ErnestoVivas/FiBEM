from bes_entities.base_entity import BaseEntity
from bes_entities import device_attributes
from bes_entities import ontology_strings


class ElectricBoiler(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["ontology"]["value"] = "Brick"
        self.base_attributes["definition"]["value"] = ontology_strings.electric_boiler_definition
        ElectricBoiler.entity_count += 1


    @staticmethod
    def get_entity_count():
        return ElectricBoiler.entity_count


    def setup_standard_devices(self):
        self.add_device(f"{self.short_id_ontology}_Electrical_Power_Command",
                        f"{self.base_attributes['id']}:Electrical_Power:Command",
                        "Command",
                        f"{ontology_strings.device_definitions['Command']}",
                        device_attributes.dynamic_device_attributes['power_attr'])
        self.add_device(f"{self.short_id_ontology}_Electrical_Power_Sensor",
                        f"{self.base_attributes['id']}:Electrical_Power_Sensor",
                        "Electrical_Power_Sensor",
                        f"{ontology_strings.device_definitions['Electrical_Power_Sensor']}",
                        device_attributes.dynamic_device_attributes['power_attr'])
        self.add_device(f"{self.short_id_ontology}_Water_Flow_Sensor",
                        f"{self.base_attributes['id']}:Water_Flow_Sensor",
                        "Water_Flow_Sensor",
                        f"{ontology_strings.device_definitions['Water_Flow_Sensor']}",
                        device_attributes.dynamic_device_attributes['volume_flow_attr'])
        self.add_device(f"{self.short_id_ontology}_Entering_Water_Temperature_Sensor",
                        f"{self.base_attributes['id']}:Entering_Water_Temperature_Sensor",
                        "Entering_Water_Temperature_Sensor",
                        f"{ontology_strings.device_definitions['Entering_Water_Temperature_Sensor']}",
                        device_attributes.dynamic_device_attributes['temperature_attr'])
        self.add_device(f"{self.short_id_ontology}_Leaving_Water_Temperature_Sensor",
                        f"{self.base_attributes['id']}:Leaving_Water_Temperature_Sensor",
                        "Leaving_Water_Temperature_Sensor",
                        f"{ontology_strings.device_definitions['Leaving_Water_Temperature_Sensor']}",
                        device_attributes.dynamic_device_attributes['temperature_attr'])


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Electric_Boiler;\n'
                         f'    skos:definition "{ontology_strings.electric_boiler_definition}"')
        return ttl_file_text
