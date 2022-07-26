from bes_entities.base_entity import BaseEntity
from bes_entities import ontology_strings


class Radiator(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.radiator_definition
        Radiator.entity_count += 1


    @staticmethod
    def get_entity_count():
        return Radiator.entity_count


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Radiator;\n'
                         f'    skos:definition "{ontology_strings.radiator_definition}"')
        return ttl_file_text
