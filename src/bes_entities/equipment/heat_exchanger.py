from bes_entities.base_entity import BaseEntity
from bes_entities import ontology_strings
from bes_entities import device_attributes


class HeatExchanger(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.heat_exchanger_definition
        HeatExchanger.entity_count += 1

    @staticmethod
    def get_entity_count():
        return HeatExchanger.entity_count


    def setup_standard_devices(self):
        self.add_device(f"{self.short_id_ontology}_Heat_Out_Water_Flow_Sensor",
                        f"{self.base_attributes['id']}:Heat_Out:Water_Flow_Sensor",
                        "Water_Flow_Sensor",
                        f"{ontology_strings.device_definitions['Water_Flow_Sensor']}",
                        device_attributes.dynamic_device_attributes['volume_flow_attr'])
        self.add_device(f"{self.short_id_ontology}_Heat_Out_Entering_Water_Temperature_Sensor",
                        f"{self.base_attributes['id']}:Heat_Out:Entering_Water_Temperature_Sensor",
                        "Entering_Water_Temperature_Sensor",
                        f"{ontology_strings.device_definitions['Entering_Water_Temperature_Sensor']}",
                        device_attributes.dynamic_device_attributes['temperature_attr'])
        self.add_device(f"{self.short_id_ontology}_Heat_Out_Leaving_Water_Temperature_Sensor",
                        f"{self.base_attributes['id']}:Heat_Out_Leaving_Water_Temperature_Sensor",
                        "Leaving_Water_Temperature_Sensor",
                        f"{ontology_strings.device_definitions['Leaving_Water_Temperature_Sensor']}",
                        device_attributes.dynamic_device_attributes['temperature_attr'])


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Heat_Exchanger;\n'
                         f'    skos:definition "{ontology_strings.heat_exchanger_definition}"')
        return ttl_file_text
