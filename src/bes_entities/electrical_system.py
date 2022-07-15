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
