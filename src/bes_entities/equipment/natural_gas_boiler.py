from bes_entities.base_entity import BaseEntity
from bes_entities import ontology_strings
from bes_entities import device_attributes


class NaturalGasBoiler(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.natural_gas_boiler_definition
        NaturalGasBoiler.entity_count += 1


    @staticmethod
    def get_entity_count():
        return NaturalGasBoiler.entity_count


    def setup_standard_devices(self):
        self.add_device(f"{self.short_id_ontology}_Natural_Gas_Valve_Command",
                        f"{self.base_attributes['id']}:Natural_Gas:Valve_Command",
                        "Valve_Command",
                        f"{ontology_strings.device_definitions['Valve_Command']}",
                        device_attributes.dynamic_device_attributes['percentage_attr'])
        self.add_device(f"{self.short_id_ontology}_Natural_Gas_Flow_Sensor",
                        f"{self.base_attributes['id']}:Natural_Gas:Flow_Sensor",
                        "Flow_Sensor",
                        f"{ontology_strings.device_definitions['Flow_Sensor']}",
                        device_attributes.dynamic_device_attributes['volume_flow_attr'])
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
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Natural_Gas_Boiler;\n'
                         f'    skos:definition "{ontology_strings.natural_gas_boiler_definition}"')
        return ttl_file_text
