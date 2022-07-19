from .base_entity import BaseEntity
from bes_entities import ontology_strings


class ElectricalSystem(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.electrical_system_definition
        ElectricalSystem.entity_count += 1


    @staticmethod
    def get_entity_count():
        return ElectricalSystem.entity_count


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Electrical_System;\n'
                         f'    skos:definition "{ontology_strings.electrical_system_definition}"')
        return ttl_file_text
