from .base_entity import BaseEntity
from bes_entities import ontology_strings

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
