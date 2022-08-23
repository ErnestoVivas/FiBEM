from bes_entities.base_entity import BaseEntity
from bes_entities import ontology_strings
from bes_entities import device_attributes


class Cogeneration(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.cogeneration_plant_definition
        self.base_attributes["ontology"]["value"] = "Brick, extended by EBC"
        Cogeneration.entity_count += 1


    @staticmethod
    def get_entity_count():
        return Cogeneration.entity_count


    def setup_standard_devices(self):
        self.add_device(f"{self.short_id_ontology}_Power_Out_Electrical_Power_Sensor",
                        f"{self.base_attributes['id']}:Power_Out:Electrical_Power_Sensor",
                        "Electrical_Power_Sensor",
                        f"{ontology_strings.device_definitions['Electrical_Power_Sensor']}",
                        device_attributes.dynamic_device_attributes['power_attr'])
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
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a ebc:Cogeneration_Plant;\n'
                         f'    skos:definition "{ontology_strings.cogeneration_plant_definition}"')
        return ttl_file_text
