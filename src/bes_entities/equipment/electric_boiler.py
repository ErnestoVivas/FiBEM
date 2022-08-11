from bes_entities.base_entity import BaseEntity
from bes_entities.device_attributes import power_attr
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
        self.add_device(f"{self.short_id_ontology}_Electrical_Power_Sensor",
                        f"{self.base_attributes['id']}:Electrical_Power_Sensor",
                        "Electrical_Power_Sensor",
                        f"{ontology_strings.device_definitions['Electrical_Power_Sensor']}")
        self.add_device(f"{self.short_id_ontology}_Power_In_Command",
                        f"{self.base_attributes['id']}:Power_In:Command",
                        "Command",
                        f"{ontology_strings.device_definitions['Command']}")
        self.add_device(f"{self.short_id_ontology}_Thermal_Power_Sensor",
                        f"{self.base_attributes['id']}:Thermal_Power_Sensor",
                        "Thermal_Power_Sensor",
                        f"{ontology_strings.device_definitions['Thermal_Power_Sensor']}")
        self.add_device(f"{self.short_id_ontology}_Water_Flow_Sensor",
                        f"{self.base_attributes['id']}:Water_Flow_Sensor",
                        "Water_Flow_Sensor",
                        f"{ontology_strings.device_definitions['Water_Flow_Sensor']}")
        self.add_device(f"{self.short_id_ontology}_conversionEfficiency",
                        f"{self.base_attributes['id']}:conversionEfficiency",
                        "conversionEfficiency",
                        f"{ontology_strings.device_definitions['conversionEfficiency']}")


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Electric_Boiler;\n'
                         f'    skos:definition "{ontology_strings.electric_boiler_definition}"')
        return ttl_file_text
