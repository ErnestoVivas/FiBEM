from .base_entity import BaseEntity
from bes_entities import ontology_strings


class HVACSystem(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.hvac_system_definition
        HVACSystem.entity_count += 1

    @staticmethod
    def get_entity_count():
        return HVACSystem.entity_count
