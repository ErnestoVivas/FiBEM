from .base_entity import BaseEntity
from bes_entities import ontology_strings


class NaturalGasBoiler(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.natural_gas_boiler_definition
        NaturalGasBoiler.entity_count += 1


    @staticmethod
    def get_entity_count():
        return NaturalGasBoiler.entity_count


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Natural_Gas_Boiler;\n'
                         f'    skos:definition "{ontology_strings.natural_gas_boiler_definition}"')
        return ttl_file_text
