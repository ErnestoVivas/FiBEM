from .base_entity import BaseEntity
from bes_entities import ontology_strings


class WaterSystem(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.water_system_definition
        WaterSystem.entity_count += 1

    @staticmethod
    def get_entity_count():
        return WaterSystem.entity_count
